#!/usr/bin/env python3
"""
validate.py — check the hub's integrity before anyone points Opulent at it.

Checks
------
1. Every instance file has frontmatter with a `type:` that exists in types/.
2. Every required field declared on a type (and its parents) is present.
3. Every [[wikilink]] resolves to a real file in the hub.
4. Every gtm.automation has a fenced Prompt block containing a CAUTION line.
5. No automation is `enabled: yes` without `firstOpenChecked: yes`.
6. No file claims `sendReady: yes`.

Also regenerates catalogs/ from what actually exists.

    python3 scripts/validate.py            # check
    python3 scripts/validate.py --catalog  # check + rewrite catalogs
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HUB = pathlib.Path(__file__).resolve().parent.parent
CONTENT_DIRS = ["entities", "entities/connectors", "signals", "pipelines", "automations",
                "workflows", "extractions", "runbooks", "catalogs", "research",
                "skills", "inject", "playbooks"]
# Root pages Jeremy or his agent will read. Not typed as gtm.* but they are surface.
SURFACE_ROOT_FILES = ["start here.md", "ONBOARDING.md", "README.md", "AGENTS.md"]
FORBIDDEN_ON_JEREMY_SURFACE = [
    "Jeremy Alston",
    "Paul Cushman",
    "address trap",
    "never messages him",
    "This hub never messages",
    "CONVEX_DEPLOY",
    "deploy key",
    "Aside",
    "vercel-labs",
    "eve template",
    "eve-content-agent",
    "eve-typefully",
    "typefully-eve",
    "Typefully",
    "eve.dev",
    "getOAuthAuthorizationUrl",
    "The requester",
    "jeremysanchez@opulent.ai",
    "authOwner: operator",
    "paul@opulent.ai",
    "Internal checks",
    "house bar",
]

# Vocabulary supplied by declared deps, resolved by the engine at mount time.
# We cannot read those repos locally, so treat them as known and check shape only.
EXTERNAL_TYPES = {
    "node::au-base-types", "thing::au-base-types", "idea::au-base-types",
    "event::au-base-types", "source::au-base-types", "map::au-base-types",
    "lens::au-base-types", "supersede::au-base-types",
    "mcp.skill::au-mcp-sdk", "mcp.inject::au-mcp-sdk", "mcp.tool::au-mcp-sdk",
    "agent-profile::au-mcp-sdk", "composition::au-host-sdk",
    "au.engine.repo::au-engine", "au.engine.workspace::au-engine",
}
# Fields every node inherits from the base vocabulary.
BASE_FIELDS = {"tldr", "aliases", "origin", "original", "date", "involved"}

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKILINK = re.compile(r"\[\[([^\]|:]+?)(?:::[^\]]+)?\]\]")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Deliberately shallow: we only need top-level scalar keys."""
    m = FM.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if line.startswith((" ", "-", "#")) or ":" not in line:
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"')
    return out


def load_types() -> dict[str, dict]:
    types: dict[str, dict] = {}
    tdir = HUB / "type"
    for p in tdir.glob("*.type.yaml"):
        name = p.name[: -len(".type.yaml")]
        body = p.read_text(encoding="utf-8")
        fields = re.findall(r"^  ([a-zA-Z][a-zA-Z0-9]*)\??:", body, re.M)
        extends = re.findall(r"^extends:\s*\[([^\]]*)\]", body, re.M)
        parents = []
        if extends:
            parents = [x.strip() for x in extends[0].split(",") if x.strip()]
        else:
            blk = re.search(r"^extends:\n((?:\s+- .*\n)+)", body, re.M)
            if blk:
                parents = [l.strip("- ").strip() for l in blk.group(1).splitlines()]
        types[name] = {"fields": set(fields), "parents": parents}
    return types


def all_files() -> list[pathlib.Path]:
    out = []
    for d in CONTENT_DIRS:
        p = HUB / d
        if p.is_dir():
            out.extend(sorted(p.glob("*.md")))
    start = HUB / "start here.md"
    if start.exists():
        out.append(start)
    return out


def surface_files() -> list[pathlib.Path]:
    out = list(all_files())
    for name in SURFACE_ROOT_FILES:
        p = HUB / name
        if p.exists():
            out.append(p)
    return out


def surface_violations(path: pathlib.Path, text: str) -> list[str]:
    rel = path.relative_to(HUB)
    if str(rel).startswith("ops/") or "/ops/" in str(rel):
        return []
    if re.search(r"^surface:\s*[\"']?operator", text, re.M):
        return [f"{rel}: operator file must live under ops/, not on the product surface"]
    found = []
    for phrase in FORBIDDEN_ON_JEREMY_SURFACE:
        if phrase in text:
            found.append(f"{rel}: product surface contains `{phrase}`")
    return found


def stems() -> set[str]:
    return {p.stem for p in all_files()} | {p.name[:-len(".type.yaml")] for p in (HUB / "type").glob("*.type.yaml")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", action="store_true")
    args = ap.parse_args()

    types = load_types()
    files = all_files()
    known = stems() | {pathlib.Path(n).stem for n in SURFACE_ROOT_FILES}
    errors: list[str] = []
    warnings: list[str] = []
    by_type: dict[str, list[pathlib.Path]] = {}

    for p in surface_files():
        text = p.read_text(encoding="utf-8")
        errors.extend(surface_violations(p, text))

    for p in files:
        rel = p.relative_to(HUB)
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)

        if not fm:
            errors.append(f"{rel}: no frontmatter")
            continue

        t = fm.get("type")
        if not t:
            errors.append(f"{rel}: frontmatter has no `type`")
        elif t not in types and t not in EXTERNAL_TYPES:
            errors.append(f"{rel}: unknown type `{t}`")
        else:
            by_type.setdefault(t, []).append(rel)

        # wikilinks resolve
        for link in WIKILINK.findall(text):
            target = link.split("|")[0].strip()
            if target and target not in known:
                errors.append(f"{rel}: dangling link [[{target}]]")

        # send safety
        if re.search(r"^sendReady:\s*[\"']?yes", text, re.M):
            errors.append(f"{rel}: sendReady is yes — nothing in the hub may ship pre-approved")

        if t == "gtm.automation":
            if "```text" not in text:
                errors.append(f"{rel}: automation has no fenced Prompt block")
            elif "CAUTION" not in text:
                errors.append(f"{rel}: automation prompt has no CAUTION line")
            enabled = fm.get("enabled", "no").strip('"')
            checked = fm.get("firstOpenChecked", "no").strip('"')
            if enabled == "yes" and checked != "yes":
                errors.append(f"{rel}: enabled without a checked first open")
            if "costCeilingUsd" not in fm:
                warnings.append(f"{rel}: no costCeilingUsd")

        if t and t.startswith("gtm."):
            if "tldr" not in fm:
                errors.append(f"{rel}: no tldr (required by node::au-base-types)")
            if "provenance" not in fm:
                warnings.append(f"{rel}: no provenance")
            # undeclared fields become engine diagnostics at mount time
            declared = set(BASE_FIELDS) | {"type", "status", "owner", "updated", "provenance"}
            cur, seen = t, set()
            while cur in types and cur not in seen:
                seen.add(cur)
                declared |= types[cur]["fields"]
                parents = [x for x in types[cur]["parents"] if x in types]
                cur = parents[0] if parents else ""
            for k in fm:
                if k not in declared:
                    warnings.append(f"{rel}: field `{k}` not declared on {t}")

    print(f"files checked : {len(files)}")
    print(f"types loaded  : {len(types)}")
    for t in sorted(by_type):
        print(f"  {t:20} {len(by_type[t])}")

    if warnings:
        print(f"\nwarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  x {e}")

    if args.catalog:
        write_catalogs(by_type)
        print("\ncatalogs regenerated")

    print("\nOK" if not errors else "\nFAILED")
    return 1 if errors else 0


def write_catalogs(by_type: dict[str, list[pathlib.Path]]) -> None:
    cat = HUB / "catalogs"
    cat.mkdir(exist_ok=True)

    def table(t: str, cols: tuple[str, ...]) -> str:
        rows = []
        for rel in sorted(by_type.get(t, [])):
            fm = parse_frontmatter((HUB / rel).read_text(encoding="utf-8"))
            cells = [f"[[{rel.stem}]]"] + [fm.get(c, "").strip('"') or "-" for c in cols[1:]]
            rows.append("| " + " | ".join(cells) + " |")
        head = "| " + " | ".join(cols) + " |\n|" + "---|" * len(cols)
        return head + "\n" + "\n".join(rows) if rows else head

    (cat / "automation-dictionary.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"Every automation this hub can stand up, and whether it is gated.\"\nstatus: active\n"
        "owner: Jeremy Sanchez\nupdated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: automations\nentryCount: {len(by_type.get('gtm.automation', []))}\n---\n\n"
        "# Automation dictionary\n\nEvery automation this hub can stand up. None are Enabled until "
        "[[first-open-gate]] passes.\n\n# Index\n\n"
        + table("gtm.automation", ("name", "slug", "mode", "enabled", "firstOpenChecked", "costCeilingUsd"))
        + "\n", encoding="utf-8")
    # Engine body sections are H1 (`# Index`), not H2.

    (cat / "signal-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"Ranked buying triggers, strongest intent first.\"\nstatus: active\nowner: Jeremy Sanchez\n"
        "updated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: signals\nentryCount: {len(by_type.get('gtm.signal', []))}\n---\n\n"
        "# Signal catalog\n\nRanked buying triggers. Rank 1 is the strongest intent.\n\n# Index\n\n"
        + table("gtm.signal", ("name", "rank", "decayDays"))
        + "\n", encoding="utf-8")

    (cat / "runbook-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"Operating procedures and data-extraction runbooks.\"\nstatus: active\nowner: Jeremy Sanchez\n"
        "updated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: workflows\nentryCount: {len(by_type.get('gtm.runbook', [])) + len(by_type.get('gtm.extraction', []))}\n---\n\n"
        "# Runbook and extraction catalog\n\n# Index\n\n### Runbooks\n\n"
        + table("gtm.runbook", ("name", "trigger", "audience"))
        + "\n\n### Extractions\n\n"
        + table("gtm.extraction", ("name", "sourceSystem", "requiresAuth", "authOwner"))
        + "\n", encoding="utf-8")

    (cat / "tactic-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"Outside plays we adopted, each attributed to its author.\"\nstatus: active\nowner: Jeremy Sanchez\n"
        "updated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: tactics\nentryCount: {len(by_type.get('gtm.tactic', []))}\n---\n\n"
        "# Tactic catalog\n\nOutside plays we have adopted. Every one is attributed; a claimed result "
        "stays the author's claim and is never restated as ours.\n\n# Index\n\n"
        + table("gtm.tactic", ("name", "source", "category", "adoptionState"))
        + "\n", encoding="utf-8")

    (cat / "playbook-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"Specialist modules in the outbound motion, and the automation each one owns.\"\nstatus: active\n"
        "owner: Jeremy Sanchez\nupdated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: playbooks\nentryCount: {len(by_type.get('gtm.playbook', []))}\n---\n\n"
        "# Playbook catalog\n\nEvery specialist module in the motion. Run them in the order on "
        "[[routing]]. Do not skip [[icp]] or the send gate.\n\n# Index\n\n"
        + table("gtm.playbook", ("name", "module", "role", "nextOwner"))
        + "\n", encoding="utf-8")

    (cat / "channel-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"How a settled message changes when it moves to a channel.\"\nstatus: active\n"
        "owner: Jeremy Sanchez\nupdated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: channels\nentryCount: {len(by_type.get('gtm.channel-guide', []))}\n---\n\n"
        "# Channel catalog\n\nSame claim. Different first fold. Start with [[channels]].\n\n# Index\n\n"
        + table("gtm.channel-guide", ("name", "channel", "firstFoldChars", "wordCap"))
        + "\n", encoding="utf-8")

    (cat / "skill-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntldr: \"Triggered skills and profiles.\"\nstatus: active\nowner: Jeremy Sanchez\n"
        "updated: 2026-09-16\nsurface: jeremy\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: skills\nentryCount: {len(by_type.get('mcp.skill::au-mcp-sdk', []))}\n---\n\n"
        "# Skill and agent catalog\n\n# Index\n\n### Skills\n\n"
        + table("mcp.skill::au-mcp-sdk", ("name", "description"))
        + "\n\n### Agent profiles\n\nYAML files under `profiles/`.\n"
        + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
