#!/usr/bin/env python3
"""
materialize.py — install this hub into Jeremy Sanchez's Opulent account.

What it does
------------
1. Reads every markdown file in the hub's content directories.
2. Creates one Opulent *knowledge* row per file (folder = the hub directory).
   Files under runbooks/ are additionally created as *runbook* rows.
3. Attaches the created ids to the account's workspace so every Opulent session
   on this account sees the hub as context.

It is idempotent: a file whose `name` already exists is skipped, not duplicated.

Dry run (default):
    python3 scripts/materialize.py

Real install:
    CONFIRM=send python3 scripts/materialize.py --apply
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import subprocess
import sys

HUB = pathlib.Path(__file__).resolve().parent.parent
PILOT = HUB / "scripts" / "pilot.sh"
USER_ID = os.environ.get("OPERATOR_ACCOUNT_ID", "")
if not USER_ID:
    raise SystemExit("Set OPERATOR_ACCOUNT_ID in private environment")
WORKSPACE_ID = "ws_6b932257a9014a51a2ec5d42bb"

# Directory -> how it should land in Opulent.
#   knowledge : always-available reference the agent can search
#   runbook   : an operating procedure the agent can execute
CONTENT_DIRS = {
    "entities": "knowledge",
    "entities/connectors": "knowledge",
    "signals": "knowledge",
    "pipelines": "knowledge",
    "automations": "knowledge",
    "workflows": "knowledge",
    "extractions": "runbook",
    "runbooks": "runbook",
    "catalogs": "knowledge",
    "research": "knowledge",
    "skills": "knowledge",
    "inject": "knowledge",
    "playbooks": "knowledge",
}


def is_jeremy_surface(path: pathlib.Path) -> bool:
    """ops/ never installs. Product files with surface: operator never install."""
    rel = path.relative_to(HUB).as_posix()
    if rel.startswith("ops/") or "/ops/" in rel:
        return False
    text = path.read_text(encoding="utf-8")
    if re.search(r"^surface:\s*[\"']?operator", text, re.M):
        return False
    return True


def pilot(mode: str, fn: str, args: dict) -> dict | list | None:
    """Call production through the governed seam."""
    proc = subprocess.run(
        [str(PILOT), mode, fn, json.dumps(args)],
        capture_output=True,
        text=True,
        env={**os.environ},
    )
    if proc.returncode != 0:
        sys.stderr.write(f"  ! {fn} failed: {proc.stderr.strip()[:300]}\n")
        return None
    body = proc.stdout.strip()
    if not body:
        return None
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return body  # some mutations return a bare id string


def existing_names() -> set[str]:
    names: set[str] = set()
    for fn, key in (
        ("knowledgeRunbooks:listKnowledge", "name"),
        ("knowledgeRunbooks:listRunbooks", "title"),
    ):
        res = pilot("read", fn, {"userId": USER_ID, "limit": 500})
        rows = res if isinstance(res, list) else (res or {}).get("items") or []
        if isinstance(res, dict):
            for k in ("knowledge", "runbooks", "results", "items"):
                if isinstance(res.get(k), list):
                    rows = res[k]
                    break
        for r in rows:
            if isinstance(r, dict) and r.get(key):
                names.add(r[key])
    return names


def collect() -> list[tuple[pathlib.Path, str, str]]:
    """Return (path, kind, folder) for every content file."""
    out = []
    for rel, kind in CONTENT_DIRS.items():
        d = HUB / rel
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            if not is_jeremy_surface(p):
                continue
            out.append((p, kind, rel.replace("/", "-")))
    start = HUB / "start here.md"
    if start.exists() and is_jeremy_surface(start):
        out.append((start, "knowledge", "root"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually write to production")
    args = ap.parse_args()

    apply = args.apply
    if apply and os.environ.get("CONFIRM") != "send":
        sys.stderr.write("refusing to install: re-run with CONFIRM=send\n")
        return 2

    files = collect()
    print(f"hub files found : {len(files)}")

    have = existing_names() if apply else set()
    if apply:
        print(f"already installed: {len(have)}")

    created_knowledge: list[str] = []
    created_runbooks: list[str] = []
    skipped = 0

    for path, kind, folder in files:
        name = path.stem
        title = f"merraine/{folder}/{name}"
        if title in have:
            skipped += 1
            continue

        content = path.read_text(encoding="utf-8")
        if not apply:
            print(f"  [dry] {kind:8} {title}  ({len(content)} bytes)")
            continue

        if kind == "runbook":
            res = pilot("write", "knowledgeRunbooks:createRunbook", {
                "userId": USER_ID,
                "title": title,
                "content": content,
                "source": "merraine-context-hub",
            })
            if res:
                created_runbooks.append(res if isinstance(res, str) else str(res))
                print(f"  [ok]  runbook  {title}")
        else:
            res = pilot("write", "knowledgeRunbooks:createKnowledge", {
                "userId": USER_ID,
                "name": title,
                "content": content,
                "folder": f"merraine/{folder}",
                "source": "merraine-context-hub",
                "status": "active",
            })
            if res:
                created_knowledge.append(res if isinstance(res, str) else str(res))
                print(f"  [ok]  knowledge {title}")

    print()
    print(f"created knowledge : {len(created_knowledge)}")
    print(f"created runbooks  : {len(created_runbooks)}")
    print(f"skipped existing  : {skipped}")

    if not apply:
        print("\ndry run only. Re-run with: CONFIRM=send python3 scripts/materialize.py --apply")
        return 0

    if created_knowledge or created_runbooks:
        print("\nattaching to workspace", WORKSPACE_ID)
        pilot("write", "workspaceEntities:attachContextForAgentInternal", {
            "userId": USER_ID,
            "workspaceId": WORKSPACE_ID,
            "attachedKnowledgeIds": created_knowledge,
            "attachedRunbookIds": created_runbooks,
        })
        print("attached. Re-run scripts/audit.sh and confirm mounted_context > 0.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
