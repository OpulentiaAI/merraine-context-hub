# Running this hub in Ars Umbris on Linux

A verified end-to-end bring-up of the hub as a live au-host workspace on Debian
(bookworm, `linux/amd64`, headless X via Xvfb), performed 2026-09-14 against release
`0.0.1-alpha`. Upstream `docs/upstream/INSTALL.md` is macOS-tested; everything below is
the Linux delta plus the exact commands that worked, and the one repo-side gap that
still blocks a rendered workspace.

## What "the application" is

This repo is not an app. It is an **arsumbris workspace**: a folder-repo
(`.arsumbris/repo.yaml`) that the engine mounts as a typed graph. Two processes make it
visible:

- **au-engine** — the Rust daemon (`au`). One daemon per entry repo, serving over a Unix
  socket in `~/.arsumbris/au-engine/run/`.
- **au-host** — the Electron UI that supervises that daemon and mounts *projections*
  (file tree, reader, editor, graph views) over the graph.

## Verified environment

| Part | Version used |
|---|---|
| OS | Debian bookworm, `python:3.12.10-slim` base, XFCE on Xvfb `:99` |
| Rust | 1.98.1 (rustup, minimal profile) |
| Node | **24.10.0** — au-host pins `engines.node >= 23`; the box's Node 22 is too old |
| pnpm | 11.1.1 via Corepack (pinned by au-host) |
| arsumbris | every part checked out at tag `0.0.1-alpha` |
| built engine | `au 0.0.5` (`au-cli`), wire schema 29 |
| Electron | 42.3.0, mount contract 7 |

## The commands that worked

```sh
# 1. every part as a sibling under one parent, all on one tag
mkdir -p ~/arsumbris && cd ~/arsumbris
VERSION=0.0.1-alpha
for r in arsumbris au-engine au-engine-sdk au-type-system au-host \
         au-mcp au-mcp-sdk au-mcp-core au-mcp-adapter-cc au-mcp-adapter-codex \
         au-type-codegen au-base-types au-weave au-agent-guides au-rules \
         au-writing-style au-skills au-govern au-competency au-ingest \
         au-tree-research au-defaults; do
  git clone --depth 1 --branch "$VERSION" https://github.com/arsumbris/"$r".git "$r"
done
git clone https://github.com/OpulentiaAI/merraine-context-hub.git ~/arsumbris/merraine-context-hub

# 2. engine (no separate `cargo build --release` needed; cargo install builds + installs)
curl -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal
cd ~/arsumbris/au-engine && cargo install --path crates/au-cli --locked   # ~85s, 4 cores
au --version            # au 0.0.5

# 3. JS deps (Node 24 on PATH first)
cd ~/arsumbris
for r in au-engine-sdk au-mcp au-mcp-sdk au-mcp-core au-mcp-adapter-cc \
         au-mcp-adapter-codex au-type-codegen; do (cd $r && pnpm install --frozen-lockfile); done
cd ~/arsumbris/au-host && pnpm install --frozen-lockfile     # builds node-pty natively, ~30s

# 4. host build
pnpm --filter app exec install-electron
pnpm --filter app rebuild:native
pnpm -r build
pnpm --filter app build:shared-deps

# 5. device config (registers every located repo, including this hub)
cd ~/arsumbris/arsumbris && python3 scripts/seed-device-config.py --write
```

`seed-device-config.py` wrote 66 repos into `~/.arsumbris/au-engine/config/repos.yaml`,
including `merraine-context-hub -> ~/arsumbris/merraine-context-hub`, plus
`~/.arsumbris/au-host/config/paths.yaml` (au binary, au-mcp entry, node).

## Linux-specific deltas

These are the things upstream INSTALL.md does not cover, and each one was required:

1. **Node 24 is mandatory.** `engines.node >= 23`; install a tarball build rather than
   relying on a distro Node 22.
2. **Electron needs `--no-sandbox`** (or `ELECTRON_DISABLE_SANDBOX=1`) in a container
   without user namespaces / a setuid chrome-sandbox.
3. **Software WebGL is mandatory.** Under `llvmpipe`, Chromium blocklists WebGL, and the
   launcher's `<LauncherAvatar>` (three.js) throws during mount with no error boundary —
   the whole Welcome screen renders as a black window. Fix with
   `--enable-unsafe-swiftshader --use-gl=angle --use-angle=swiftshader`. With those flags
   the Welcome screen renders correctly.
4. **`pnpm dev` is not needed.** The built app runs directly and avoids the vite dev
   server: `./node_modules/electron/dist/electron .` from `au-host/app`.
5. **The GTK folder picker is unreliable headless.** Typing a path into the `Ctrl+L`
   location bar only drives autocompletion; the selection never reaches the host and the
   gate silently returns to "Your first workspace". Browsing (Home → arsumbris →
   merraine-context-hub) works, but the supported non-interactive route is better — see
   below.
6. **`AU_ENTRY` is the headless open route.** The host's own multi-window code spawns
   instances with `AU_ENTRY=<workspace root>`; setting it boots straight past the gate and
   starts the daemon on that entry.

### The working launch line

```sh
cd ~/arsumbris/au-host/app
DISPLAY=:99 \
ELECTRON_DISABLE_SANDBOX=1 \
AU_ENTRY=$HOME/arsumbris/merraine-context-hub \
./node_modules/electron/dist/electron . \
  --no-sandbox --enable-unsafe-swiftshader --use-gl=angle --use-angle=swiftshader
```

Add `--remote-debugging-port=9333` to inspect the renderer over CDP (9222 is often taken
by the sandbox's own Chromium).

## What is verified working

- `python3 scripts/validate.py` → **OK**, 0 errors, 12 warnings (undeclared `notes`,
  `evidence`, `relatedAutomations` fields), 47 typed instances across 23 types.
- `au daemon start ~/arsumbris/merraine-context-hub` →
  `engine=up, ref=ready, ready=true, version=1`, socket in `~/.arsumbris/au-engine/run/`.
  **The hub's dep closure (`au-base-types`, `au-mcp-sdk`, `au-skills`, `au-writing-style`)
  resolves and mounts — no `entry-not-a-repo`, no unresolved member.**
- au-host boots, the gate validates the entry (`.arsumbris/repo.yaml` present), and with
  `AU_ENTRY` it opens the workspace and brings the engine up itself.

## The remaining gap: the composition has no panes

With the workspace open, the renderer DOM is:

```html
<div class="kernel-root"><div class="kernel-container" data-pane-id=""></div></div>
<div class="boot-curtain lifted"></div>
```

No console errors, no exceptions — an **empty kernel**. The cause is
`workspace-layout.yaml`: it is a valid `composition::au-host-sdk` but it only declares
`slot-defaults` and `viewer-defaults`. A composition also needs a `windows` list and a
`projections` pool; without them there is nothing to mount, so the window paints black.

Compare `au-defaults/minimal/minimal.yaml`, which is the smallest useful shape: a primary
window → a `bento` split → `file-tree` beside `editor-pane`.

### Proposed fix (not yet applied)

```yaml
type: composition::au-host-sdk
windows:
  - "[[^^au-window-primary]]"
viewer-defaults:
  defaults:
    - opens: md
      viewer: "[[aup-reader::aup-reader]]"
    - opens: yaml
      viewer: "[[editor-pane::editor]]"
    - opens: json
      viewer: "[[editor-pane::editor]]"
    - opens: jsonl
      viewer: "[[editor-pane::editor]]"
    - opens: png
      viewer: "[[image-viewer::media-viewers]]"
projections:
  - ^: au-window-primary
    type: window::au-host-sdk
    primary: true
    content: "[[^^grid]]"
  - ^: grid
    type: bento::bento
    root:
      type: bento-node.branch::bento
      direction: row
      ratio: 0.22
      children:
        - "[[^^tree]]"
        - "[[^^doc]]"
  - ^: tree
    type: file-tree::file-tree
  - ^: doc
    type: aup-reader::aup-reader
```

Two open decisions before applying it:

1. **Which panes the hub should open on.** A GTM hub arguably wants
   `force-graph` (the signal/entity graph) or `type-instances` beside the reader, not just
   a tree and a document. `start here.md` is the natural default document.
2. **Host-side deps.** `.arsumbris/repo.yaml` currently declares only
   `au-base-types, au-mcp-sdk, au-skills, au-writing-style`. `workspace.yaml` pulls
   `host-bundle` under `discover`, which resolved the projections on this install, but the
   shipped templates declare the projections they reference directly (`bento`, `file-tree`,
   `editor`/`aup-reader`, `intent`). Declaring them makes the mount self-describing rather
   than relying on the bundle.

## Notes for the next run

- One daemon owns one entry. If `au daemon start` is run by hand first, stop it
  (`au daemon stop <path>`) before letting the host own the workspace, or the host's own
  supervision and the manual daemon compete for the same socket.
- Disk: the full install (22 repos, cargo toolchain, node_modules, Electron runtime) cost
  roughly 9 GB. `cargo install` cleans its own target directory; a plain
  `cargo build --release` would leave several more GB behind.
- The host writes per-machine state to `~/.arsumbris/au-host/config/` — `paths.yaml`,
  `workspace-template-repos.yaml`, and `recents.yaml` (the gate's recent-workspaces list).
  All three are disposable.
