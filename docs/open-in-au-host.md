# Opening this hub in Ars Umbris

You have au-host running on the Opulent desktop, sitting on the Welcome screen with
the starter picker up (Blank / Deep research / Weave).

**Do not pick a starter.** Those create a new workspace from a template. This hub
*is* a workspace. Use **Open an existing workspace...**

---

## Paste this into the Opulent thread that has the desktop

```text
Ars Umbris is running on the desktop. Mount the Merraine context hub as a workspace.

1. Clone the hub next to the other arsumbris repos:
     mkdir -p ~/arsumbris
     git clone https://github.com/OpulentiaAI/merraine-context-hub.git ~/arsumbris/merraine-context-hub

2. Confirm its type dependencies are already present in ~/arsumbris/. The hub declares:
     au-base-types, au-mcp-sdk, au-skills, au-writing-style
   If any is missing, clone it at the SAME release tag as the rest of the install
   (see ~/arsumbris/arsumbris/VERSION.md — every part must be on one tag, not branch HEADs):
     git clone --branch "$VERSION" https://github.com/arsumbris/<repo>.git ~/arsumbris/<repo>

3. Start the engine daemon on the hub:
     au daemon start ~/arsumbris/merraine-context-hub

4. In the au-host window, click "Open an existing workspace..." and choose
   ~/arsumbris/merraine-context-hub

5. Report back: the diagnostics count, and the first ten diagnostics in full.
   Do not fix anything yet. I want to see what the engine says before we change it.
```

---

## What the engine will check that our validator cannot

`scripts/validate.py` enforces the shape we control. The engine enforces the rest:

- **Dep resolution.** `au-base-types`, `au-mcp-sdk`, `au-skills`, `au-writing-style`
  must actually mount. A missing dep is a hard failure, not a warning.
- **Cross-repo type references.** Every `extends: thing::au-base-types` resolves for
  real. Our validator treats those as known-external and only checks shape.
- **Field types.** `Date` must parse as a date; `Number{integer}` must be whole;
  `gtm.signal*` must point at a file that really carries that type.
- **Required inherited fields.** `node` requires `tldr` on every instance. We added
  it to all 47, but the engine is the authority.
- **Body sections.** Types declaring `body:` sections require those headings to be
  present. `gtm.automation` demands Overview, Prompt and Forbidden Actions.

Expect diagnostics on the first mount. That is the point — bad data surfaces as a
diagnostic and never blocks a read or a save.

---

## What was ported, and why it changed

The repo was restructured to match the real contract, read out of `au-base-types`,
`au-mcp-sdk` and the `au-defaults` workspace templates rather than guessed from the
README.

| Before | After | Why |
|---|---|---|
| `repo.yaml` with no `type` | `type: au.engine.repo::au-engine` | **Without it the daemon hard-refuses the entry** (`entry-not-a-repo`). This alone would have blocked the mount. |
| `workspace.yaml` with no `type` | `type: au.engine.workspace::au-engine` | Same contract |
| `types/` | `type/` | Engine convention, singular |
| `injects/` | `inject/` | Matches the au-defaults templates |
| `agents/*.md` with a local type | `profiles/*.yaml`, `type: agent-profile::au-mcp-sdk` | Profiles are YAML and bind an adapter, not markdown |
| `hub.skill` | `mcp.skill::au-mcp-sdk` | The real skill type. Frontmatter is `name` + `description` only |
| `hub.inject` | `mcp.inject::au-mcp-sdk` | Same |
| Standalone `gtm.entity` root | `extends: [thing/idea/event/source/map ::au-base-types, gtm.managed]` | Subtype the base vocabulary instead of reinventing it |
| `title:` on every instance | `tldr:` | `node` requires `tldr`; `title` was an undeclared field |
| `evidence.sourceUrl` | `evidence.origin` | `gtm.evidence` now extends `source`, which already owns `origin` |
| — | `workspace-layout.yaml` | `composition::au-host-sdk`, so panes and viewers resolve |
| — | `start here.md` | The entry map, as every au-defaults template ships |

The GTM vocabulary now subtypes the base ontology honestly:

- `gtm.org`, `gtm.person`, `gtm.account`, `gtm.connector` → **thing** (they persist)
- `gtm.observation` → **event** (it happened on a date, with participants)
- `gtm.evidence` → **source** (captured material with an origin)
- `gtm.catalog` → **map** (a slice of the graph presented as a page)
- everything else → **idea**

`gtm.managed` is a local abstract mixin carrying `status`, `owner`, `updated`,
`provenance`, so every maintained node declares where it came from.

---

## Two things still to decide

**1. Should the hub become a starter?** `au-defaults` ships
`au-weave-template`, `au-tree-research-template`, `au-arscontexta-template` — those
are the three buttons on the Welcome screen. A `merraine-gtm-template` could sit
beside them so any future client workspace starts from this ontology instead of
being hand-built. That is the right shape if we do this for a second client.

**2. Host-side deps are not declared yet.** The weave template depends on the host
bundle packages (`editor`, `tabs`, `file-tree`, `force-graph`, `bento`, `column`,
`aup-reader`, `media-viewers`, `placeholder-picker`, `sandwich`, `terminal`,
`intent`, `au-host-sdk`). Our `workspace.yaml` mounts `host-bundle` and `mcp-bundle`
under `discover`, which should be enough to resolve them — but if the first mount
reports unresolved viewers, copy the weave template's `deps` list into
`.arsumbris/repo.yaml`.
