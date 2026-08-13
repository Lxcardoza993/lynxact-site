#!/usr/bin/env python3
"""Pre-deploy link/asset integrity check for the LynxAct static site.

Run before `wrangler pages deploy` to catch broken internal href/src
references (the site deploys with no CI — direct upload — so this is
the only safety net). Exits 1 if any local link/asset is missing.

Usage: python3 scripts/check-links.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def collect_html(root):
    out = []
    for dirpath, _dirs, files in os.walk(root):
        if ".git" in dirpath:
            continue
        for f in files:
            if f.endswith((".html", ".htm")):
                out.append(os.path.join(dirpath, f))
    return out


def check(root):
    broken = []
    for f in collect_html(root):
        with open(f, encoding="utf-8") as fh:
            s = fh.read()
        for m in re.finditer(r'(?:href|src)="([^"]+)"', s):
            u = m.group(1)
            if u.startswith(("http", "mailto:", "//", "tel:", "data:", "#")):
                continue
            path = u.split("?")[0].split("#")[0]
            if not path:
                continue
            target = os.path.join(root, path.lstrip("/")) if path.startswith("/") \
                else os.path.normpath(os.path.join(os.path.dirname(f), path))
            if not os.path.exists(target):
                broken.append((os.path.relpath(f, root), u))
    return broken


if __name__ == "__main__":
    broken = check(ROOT)
    print(f"Scanned {len(collect_html(ROOT))} HTML files.")
    if broken:
        print("BROKEN LINKS:")
        for f, u in broken:
            print(f"  {f} -> {u}")
        sys.exit(1)
    print("OK — 0 broken internal links/assets.")
