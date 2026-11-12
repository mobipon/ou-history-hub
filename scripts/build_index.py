#!/usr/bin/env python3
"""Validate every posts/<slug>.json and write index.json (what the site reads).

Usage: python3 scripts/build_index.py          # validate + write index.json
       python3 scripts/build_index.py --check  # validate only (non-zero exit on errors)
"""
import hashlib, json, re, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = {"legends", "moments", "records", "after-football"}
REQUIRED = ["slug", "category", "title", "question", "answer", "summary", "body", "people", "year", "sources", "publish_at"]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def problems(p, path):
    out = []
    for k in REQUIRED:
        if k == "people":   # may be empty (traditions, rivalries), but must be a list
            if not isinstance(p.get(k), list): out.append("people must be a list")
            continue
        if k not in p or p[k] in ("", [], None):
            out.append(f"missing {k}")
    if out:
        return out
    if p["slug"] != path.stem: out.append("slug must match file name")
    if not SLUG.match(p["slug"]) or len(p["slug"]) > 120: out.append("bad slug")
    if p["category"] not in CATEGORIES: out.append(f"category must be one of {sorted(CATEGORIES)}")
    if len(p["title"]) > 80: out.append("title over 80 chars")
    if not (100 <= len(p["summary"]) <= 170): out.append("summary should be 100-170 chars")
    if not isinstance(p["body"], list) or not all(isinstance(x, str) and x.strip() for x in p["body"]): out.append("body must be a list of paragraphs")
    if not isinstance(p["year"], int) or not (1850 <= p["year"] <= 2100): out.append("bad year")
    src = p["sources"]
    if not isinstance(src, list) or len(src) < 2: out.append("need at least 2 sources")
    elif not all(isinstance(s, dict) and str(s.get("url", "")).startswith("https://") and s.get("title") for s in src):
        out.append("each source needs a title and an https url")
    elif all("wikipedia.org" in s["url"] for s in src): out.append("need at least one non-Wikipedia source")
    try: datetime.fromisoformat(p["publish_at"])
    except Exception: out.append("publish_at must be ISO 8601 with offset, e.g. 2026-11-13T08:00:00-06:00")
    return out

def main():
    check_only = "--check" in sys.argv
    posts, errors, seen = [], [], set()
    for path in sorted((ROOT / "posts").glob("*.json")):
        try:
            p = json.loads(path.read_text())
        except Exception as e:
            errors.append(f"{path.name}: invalid JSON ({e})"); continue
        errs = problems(p, path)
        if p.get("slug") in seen: errs.append("duplicate slug")
        seen.add(p.get("slug"))
        if errs:
            errors.extend(f"{path.name}: {e}" for e in errs); continue
        raw = path.read_bytes()
        posts.append({
            "slug": p["slug"], "category": p["category"], "title": p["title"], "question": p["question"],
            "answer": p["answer"], "summary": p["summary"], "year": p["year"], "people": p["people"],
            "publish_at": p["publish_at"], "updated_at": p.get("updated_at", p["publish_at"]),
            "hash": hashlib.sha256(raw).hexdigest()[:16],
        })
    if errors:
        print("\n".join(errors)); sys.exit(1)
    posts.sort(key=lambda x: datetime.fromisoformat(x["publish_at"]), reverse=True)
    print(f"{len(posts)} posts OK")
    if not check_only:
        (ROOT / "index.json").write_text(json.dumps({"count": len(posts), "posts": posts}, ensure_ascii=False, indent=1) + "\n")

if __name__ == "__main__":
    main()
