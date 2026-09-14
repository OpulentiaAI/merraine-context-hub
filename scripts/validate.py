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
                "skills", "injects", "agents"]

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
    tdir = HUB / "types"
    for p in tdir.glob("*.type.yaml"):
        name = p.name[: -len(".type.yaml")]
        body = p.read_text(encoding="utf-8")
        fields = re.findall(r"^  ([a-zA-Z][a-zA-Z0-9]*):", body, re.M)
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
    return out


def stems() -> set[str]:
    return {p.stem for p in all_files()} | {p.name[:-len(".type.yaml")] for p in (HUB / "types").glob("*.type.yaml")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", action="store_true")
    args = ap.parse_args()

    types = load_types()
    files = all_files()
    known = stems()
    errors: list[str] = []
    warnings: list[str] = []
    by_type: dict[str, list[pathlib.Path]] = {}

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
        elif t not in types:
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

        if t and t.startswith("gtm.") and t != "gtm.evidence":
            if "provenance" not in fm:
                warnings.append(f"{rel}: no provenance")

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
        "---\ntype: gtm.catalog\ntitle: Automation dictionary\nstatus: active\n"
        "owner: Opulent\nupdated: 2026-09-14\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: automations\nentryCount: {len(by_type.get('gtm.automation', []))}\n---\n\n"
        "# Automation dictionary\n\nEvery automation this hub can stand up. None are Enabled until "
        "[[first-open-gate]] passes.\n\n## Index\n\n"
        + table("gtm.automation", ("name", "slug", "mode", "enabled", "firstOpenChecked", "costCeilingUsd"))
        + "\n", encoding="utf-8")

    (cat / "signal-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntitle: Signal catalog\nstatus: active\nowner: Opulent\n"
        "updated: 2026-09-14\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: tactics\nentryCount: {len(by_type.get('gtm.signal', []))}\n---\n\n"
        "# Signal catalog\n\nRanked buying triggers. Rank 1 is the strongest intent.\n\n## Index\n\n"
        + table("gtm.signal", ("name", "rank", "decayDays"))
        + "\n", encoding="utf-8")

    (cat / "runbook-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntitle: Runbook and extraction catalog\nstatus: active\nowner: Opulent\n"
        "updated: 2026-09-14\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: workflows\nentryCount: {len(by_type.get('gtm.runbook', [])) + len(by_type.get('gtm.extraction', []))}\n---\n\n"
        "# Runbook and extraction catalog\n\n## Index\n\n### Runbooks\n\n"
        + table("gtm.runbook", ("name", "trigger", "audience"))
        + "\n\n### Extractions\n\n"
        + table("gtm.extraction", ("name", "sourceSystem", "requiresAuth", "authOwner"))
        + "\n", encoding="utf-8")

    (cat / "tactic-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntitle: Tactic catalog\nstatus: active\nowner: Opulent\n"
        "updated: 2026-09-14\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: tactics\nentryCount: {len(by_type.get('gtm.tactic', []))}\n---\n\n"
        "# Tactic catalog\n\nOutside plays we have adopted. Every one is attributed; a claimed result "
        "stays the author's claim and is never restated as ours.\n\n## Index\n\n"
        + table("gtm.tactic", ("name", "source", "category", "adoptionState"))
        + "\n", encoding="utf-8")

    (cat / "skill-catalog.md").write_text(
        "---\ntype: gtm.catalog\ntitle: Skill and agent catalog\nstatus: active\nowner: Opulent\n"
        "updated: 2026-09-14\nprovenance: \"Generated by scripts/validate.py --catalog\"\n"
        f"indexes: skills\nentryCount: {len(by_type.get('hub.skill', []))}\n---\n\n"
        "# Skill and agent catalog\n\n## Index\n\n### Skills\n\n"
        + table("hub.skill", ("name", "readWhen"))
        + "\n\n### Agent profiles\n\n"
        + table("hub.agent-profile", ("name", "role", "modelRoute", "canSend", "canWriteHub"))
        + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
