#!/usr/bin/env python3
"""Regenerate the lesson index, learning-path list, and glossary index from a clone of
rohitg00/ai-engineering-from-scratch. Reads files only; never executes anything from the clone.

Usage: python3 -I scripts/build_index.py <path-to-clone> <commit-sha> [output-references-dir]
"""
import json
import re
import sys
from pathlib import Path

REPO_URL = "https://github.com/rohitg00/ai-engineering-from-scratch"
RAW = "https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch"
HERE = Path(__file__).resolve().parent
FLAGS = json.loads((HERE / "audit_flags.json").read_text())
LEVEL_LABEL = {"ok": "ok", "wrong": "WRONG", "stale": "stale", "weak": "weak", "unverified": "unverified"}


def cell(text, limit):
    text = re.sub(r"\s+", " ", (text or "").strip()).replace("|", "/")
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def meta(doc_text, key):
    m = re.search(rf"\*\*{key}:\*\*\s*(.+)", doc_text)
    return m.group(1).strip() if m else ""


def title_and_motto(doc_text):
    t = re.search(r"^#\s+(.+)$", doc_text, re.M)
    m = re.search(r"^>\s*(.+)$", doc_text, re.M)
    return (t.group(1).strip() if t else ""), (m.group(1).strip().strip("*_") if m else "")


def phase_title(slug):
    return re.sub(r"^\d+-", "", slug).replace("-", " ").title()


def build_lessons(repo, out, commit):
    phases = sorted(p for p in (repo / "phases").iterdir() if p.is_dir())
    summary = []
    for ph in phases:
        pnum = ph.name.split("-")[0]
        lessons = sorted(p for p in ph.iterdir() if p.is_dir())
        rows = []
        for ls in lessons:
            lnum = ls.name.split("-")[0]
            doc = ls / "docs" / "en.md"
            text = doc.read_text(errors="replace") if doc.exists() else ""
            title, motto = title_and_motto(text)
            code_exts = sorted({p.suffix.lstrip(".") for p in (ls / "code").rglob("*") if p.is_file() and p.suffix in {".py", ".ts", ".rs", ".jl", ".go", ".c", ".js"}}) if (ls / "code").exists() else []
            n_out = len([p for p in (ls / "outputs").rglob("*") if p.is_file() and p.name != ".gitkeep"]) if (ls / "outputs").exists() else 0
            flag = FLAGS["flags"].get(f"{pnum}/{lnum}")
            trust = f"{LEVEL_LABEL[flag[0]]}: {flag[1]}" if flag else "-"
            rows.append(
                f"| {lnum} | `{ls.name}` | {cell(title, 60)} | {meta(text, 'Type') or '?'} | "
                f"{cell(meta(text, 'Time'), 14)} | {', '.join(code_exts) or '-'} | "
                f"{'y' if (ls / 'quiz.json').exists() else '-'} | {n_out or '-'} | "
                f"{cell(motto, 130)} | {cell(meta(text, 'Prerequisites'), 70) or '-'} | {cell(trust, 150)} |"
            )
        trust_note = FLAGS["phase_trust"].get(pnum, "Not audited.")
        body = (
            f"# Phase {pnum}: {phase_title(ph.name)}\n\n"
            f"Upstream commit `{commit}`. {len(lessons)} lessons. Path pattern: `phases/{ph.name}/<lesson>/docs/en.md`.\n"
            f"Audit coverage: {trust_note}\n\n"
            "Columns: Type = Build or Learn; Lang = code file types; Quiz = has quiz.json; Out = reusable artifacts in outputs/; "
            "Audit = audit status (a dash means not audited). Fetch a lesson per `repo-guide.md`.\n\n"
            "| # | Folder | Title | Type | Time | Lang | Quiz | Out | Motto | Prerequisites | Audit |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n"
        )
        (out / "lessons" / f"{ph.name}.md").write_text(body)
        summary.append((pnum, ph.name, len(lessons)))
    return summary


def lesson_title(repo, path):
    doc = repo / path / "docs" / "en.md"
    if not doc.exists():
        return "(title not found)"
    t = re.search(r"^#\s+(.+)$", doc.read_text(errors="replace"), re.M)
    return t.group(1).strip() if t else "(title not found)"


def trust_of(path):
    m = re.match(r"phases/(\d+)-[^/]+/(\d+)-", path)
    flag = FLAGS["flags"].get(f"{m.group(1)}/{m.group(2)}") if m else None
    return f"{LEVEL_LABEL[flag[0]]}: {cell(flag[1], 90)}" if flag else "not audited"


def build_paths(repo, out, commit):
    lines = [
        "# Learning paths", "",
        f"Source: `learning-paths/*.json` at commit `{commit}`. Each path is an ordered lesson route with time estimates. "
        "Paths whose JSON lists `invocation` also exist as in-repo tutor skills. Hour estimates in the upstream README for the two longest routes are wrong; use the minutes below. "
        "The bracket after each lesson is its audit status (see trust-guide.md; labels: ok, WRONG, stale, weak, unverified, not audited); optional lessons come last.", "",
        "## Contents", "",
    ]
    files = sorted((repo / "learning-paths").glob("*.json"))
    docs = [json.loads(f.read_text()) for f in files]
    for d in docs:
        lines.append(f"- {d['title']} (`{d['id']}`)")
    lines.append("")
    for d in docs:
        lessons = d.get("lessons", [])
        mins = d.get("estimatedMinutes", 0)
        lines += [f"## {d['title']} (`{d['id']}`)", "", d.get("summary", ""), "",
                  f"Estimated {mins} min (about {mins / 60:.0f} h), {len(lessons)} required lessons"
                  + (f", {len(d['optionalLessons'])} optional" if d.get("optionalLessons") else "") + ".", ""]
        for l in lessons + d.get("optionalLessons", []):
            lines.append(f"{l['order']}. " if l.get('order') else "- (optional) ")
            lines[-1] += (f"`{l['path']}` {cell(l.get('title') or lesson_title(repo, l['path']), 80)} ({l.get('minutes', '?')} min{'' if l.get('required', True) else ', optional'}) [{trust_of(l['path'])}]")
        lines.append("")
    (out / "learning-paths.md").write_text("\n".join(lines))
    return len(docs)


def build_glossary(repo, out, commit):
    text = (repo / "glossary" / "terms.md").read_text()
    entries = []
    for block in re.split(r"^### ", text, flags=re.M)[1:]:
        name, _, rest = block.partition("\n")
        cat = re.search(r"\*\*Category:\*\*\s*(.+)", rest)
        learn = re.search(r"\*\*Learn it:\*\*\s*\[[^\]]*\]\(\.\./([^)]+)\)", rest)
        entries.append((name.strip(), cat.group(1).strip() if cat else "?", learn.group(1).strip("/") if learn else "-"))
    lines = [
        "# Glossary index", "",
        f"Source: `glossary/terms.md` at commit `{commit}` ({len(entries)} terms). This is an index only. "
        f"Read definitions from `{RAW}/{commit}/glossary/terms.md` (search for `### <Term>`). "
        "Each entry has what it means, why it matters, a practical note, a common confusion, related terms, and sources. "
        "The glossary itself says current official documentation wins over its general definitions.", "",
        "## Contents", "",
    ]
    cats = {}
    for _, c, _ in entries:
        cats[c] = cats.get(c, 0) + 1
    lines += [f"- {c} ({n} terms)" for c, n in sorted(cats.items())]
    lines += ["", "## Terms", "", "| Term | Category | Lesson |", "|---|---|---|"]
    for n, c, l in entries:
        lines.append(f"| {cell(n, 60)} | {c} | {('`' + l + '`') if l != '-' else '-'} |")
    (out / "glossary-index.md").write_text("\n".join(lines) + "\n")
    return len(entries)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    repo = Path(sys.argv[1]).resolve()
    commit = sys.argv[2]
    out = Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else HERE.parent / "references"
    (out / "lessons").mkdir(parents=True, exist_ok=True)
    summary = build_lessons(repo, out, commit)
    n_paths = build_paths(repo, out, commit)
    n_terms = build_glossary(repo, out, commit)
    total = sum(n for _, _, n in summary)
    print(f"{len(summary)} phases, {total} lessons, {n_paths} learning paths, {n_terms} glossary terms -> {out}")
    for pnum, slug, n in summary:
        print(f"  {pnum} {slug} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
