#!/usr/bin/env python3
"""Render Jeremy-facing hub pages to static HTML with resolved wikilinks.

Used to prove the graph reads as pages when au-host is not on this box.
Does not replace the engine compile.

    python3 scripts/render_preview.py --out /tmp/merraine-render
"""
from __future__ import annotations

import argparse
import html
import pathlib
import re

HUB = pathlib.Path(__file__).resolve().parent.parent
WIKILINK = re.compile(r"\[\[([^\]|:]+?)(?:\|([^\]]+))?\]\]")
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

PAGES = [
    "start here.md",
    "README.md",
    "ONBOARDING.md",
    "entities/icp-context.md",
    "entities/intent-score.md",
    "catalogs/playbook-catalog.md",
    "catalogs/automation-dictionary.md",
    "catalogs/skill-catalog.md",
    "catalogs/signal-catalog.md",
    "catalogs/tactic-catalog.md",
    "playbooks/routing.md",
    "playbooks/signals.md",
    "playbooks/icp.md",
    "playbooks/email.md",
    "playbooks/sequencing.md",
    "playbooks/channels.md",
    "entities/email-components.md",
]


def slug(path: pathlib.Path) -> str:
    return path.stem.replace(" ", "-")


def collect_stems() -> dict[str, pathlib.Path]:
    out: dict[str, pathlib.Path] = {}
    for p in HUB.rglob("*.md"):
        if ".git" in p.parts:
            continue
        out[p.stem] = p
    return out


def md_to_html(text: str, stems: dict[str, pathlib.Path]) -> str:
    body = FM.sub("", text)
    def link(m: re.Match[str]) -> str:
        target = m.group(1).strip()
        label = (m.group(2) or target).strip()
        dest = stems.get(target)
        if dest is None:
            return f'<span class="missing">[[{html.escape(target)}]]</span>'
        return f'<a href="{html.escape(slug(dest))}.html">{html.escape(label)}</a>'
    body = WIKILINK.sub(link, body)
    lines = body.splitlines()
    out: list[str] = []
    in_code = False
    in_ul = False
    in_table = False
    for line in lines:
        if line.startswith("```"):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_table:
                out.append("</table>")
                in_table = False
            if not in_code:
                out.append("<pre><code>")
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if re.match(r"^\|.+\|$", line):
            if re.match(r"^\|[\s:-|]+\|$", line):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            tag = "th" if not in_table else "td"
            if not in_table:
                if in_ul:
                    out.append("</ul>")
                    in_ul = False
                out.append("<table>")
                in_table = True
            out.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>")
            in_table = False
        if line.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{line[2:]}</li>")
            continue
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if line.startswith("# "):
            out.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{line[4:]}</h3>")
        elif line.strip() == "":
            out.append("")
        else:
            out.append(f"<p>{line}</p>")
    if in_ul:
        out.append("</ul>")
    if in_table:
        out.append("</table>")
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


CSS = """
:root { color-scheme: light; }
body { font: 16px/1.5 ui-sans-serif, system-ui, sans-serif; max-width: 820px; margin: 2rem auto; padding: 0 1.25rem; color: #1a1a1a; }
nav { font-size: 13px; margin-bottom: 2rem; }
nav a { margin-right: 0.75rem; }
h1 { font-size: 1.6rem; }
h2 { font-size: 1.2rem; margin-top: 1.6rem; }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { border: 1px solid #ddd; padding: 0.35rem 0.5rem; text-align: left; }
pre { background: #f6f6f4; padding: 0.8rem; overflow: auto; }
a { color: #0b4f6c; }
.missing { color: #a11; }
.meta { color: #555; font-size: 13px; }
"""


def wrap(title: str, body: str, nav: str) -> str:
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
        f"<nav>{nav}</nav>{body}</body></html>\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/tmp/merraine-render")
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    stems = collect_stems()
    nav_links = []
    for rel in PAGES:
        p = HUB / rel
        if p.exists():
            nav_links.append(f'<a href="{slug(p)}.html">{html.escape(p.stem)}</a>')
    nav = " ".join(nav_links)
    written = 0
    for rel in PAGES:
        p = HUB / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        (out / f"{slug(p)}.html").write_text(
            wrap(p.stem, md_to_html(text, stems), nav), encoding="utf-8"
        )
        written += 1
    index = (
        "<h1>Merraine context hub</h1>"
        "<p class=\"meta\">Static render of the typed Ars Umbris graph. "
        "Engine compile is the authority.</p><ul>"
        + "".join(f"<li><a href=\"{slug(HUB / rel)}.html\">{html.escape(rel)}</a></li>"
                  for rel in PAGES if (HUB / rel).exists())
        + "</ul>"
    )
    (out / "index.html").write_text(wrap("Merraine context hub", index, nav), encoding="utf-8")
    print(f"wrote {written + 1} pages to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
