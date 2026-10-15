#!/usr/bin/env python3
"""Lint every skill under skills/ against the Agent Skills spec and Claude's authoring limits.

Usage: python3 scripts/lint.py [skills_dir]
Exits 1 if any error is found. No dependencies.
"""
import re
import sys
from pathlib import Path

RESERVED = ("anthropic", "claude")
NAME_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
TAG_RE = re.compile(r"</?[A-Za-z][^>]*>")
MD_LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
REF_PATH_RE = re.compile(r"`((?:references|scripts|assets)/[^`\s]+)`")
MAX_BODY_LINES = 500
TOC_AFTER_LINES = 100


def parse_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        return None, text
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"([A-Za-z_-]+):\s*(.*)", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return fields, m.group(2)


def lint_skill(skill, repo):
    root = skill.parent.parent
    errors = []
    err = lambda msg: errors.append(f"{skill.relative_to(root)}: {msg}")
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        err("missing SKILL.md")
        return errors
    text = skill_md.read_text()
    fm, body = parse_frontmatter(text)
    fm_raw = {}
    if fm is not None:
        for line in re.match(r"---\n(.*?)\n---\n", text, re.S).group(1).splitlines():
            kv = re.match(r"([A-Za-z_-]+):\s*(.*)", line)
            if kv:
                fm_raw[kv.group(1)] = kv.group(2).strip()
    if fm is None:
        err("SKILL.md has no frontmatter")
        return errors

    for key, raw in fm_raw.items():
        if raw[:1] not in "\"'|>[{" and (": " in raw or " #" in raw or raw.endswith(":")):
            err(f"frontmatter {key}: unquoted value contains ': ' or ' #' (invalid YAML; reword or quote it)")

    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        err("frontmatter: missing name")
    else:
        if len(name) > 64 or not NAME_RE.fullmatch(name):
            err(f"name {name!r}: need 1-64 chars of a-z 0-9 and single hyphens, none leading or trailing")
        if name != skill.name:
            err(f"name {name!r} must match folder {skill.name!r}")
        if any(w in name for w in RESERVED):
            err(f"name {name!r} contains a reserved word {RESERVED}")
        if TAG_RE.search(name):
            err("name contains XML tags")
    if not desc:
        err("frontmatter: missing or empty description")
    else:
        if len(desc) > 1024:
            err(f"description is {len(desc)} chars (max 1024)")
        if TAG_RE.search(desc):
            err("description contains XML tags")
    if len(fm.get("compatibility", "")) > 500:
        err("compatibility over 500 chars")
    if "license" in fm and not (repo / "LICENSE").is_file():
        err("declares a license but repo has no LICENSE file")

    n_body = len(body.strip().splitlines())
    if n_body > MAX_BODY_LINES:
        err(f"SKILL.md body is {n_body} lines (max {MAX_BODY_LINES}); move detail to references/")

    for target in set(MD_LINK_RE.findall(body)) | set(REF_PATH_RE.findall(body)):
        if re.match(r"[a-z]+:", target):
            continue
        if not (skill / target).exists():
            err(f"SKILL.md references missing path {target}")

    refs = skill / "references"
    if refs.is_dir():
        for f in sorted(refs.glob("*.md")):
            rel = f.relative_to(skill).as_posix()
            if rel not in body and f.name not in body:
                err(f"{rel} is not linked from SKILL.md")
            lines = f.read_text().splitlines()
            if len(lines) > TOC_AFTER_LINES and not any(
                re.match(r"#+\s*(table of )?contents\b|-\s*contents\b", l, re.I) for l in lines[:40]
            ):
                err(f"{rel} is {len(lines)} lines with no contents list near the top")
            for target in set(MD_LINK_RE.findall(f.read_text())):
                if not re.match(r"[a-z]+:", target) and not (f.parent / target).exists():
                    err(f"{rel} links to missing path {target}")
    return errors


LINK_RE = re.compile(r"^- \[[^\]]+\]\((https?://[^)\s]+)\)(: .+)?$")
OUR_RAW = "https://raw.githubusercontent.com/kzndotsh/skills/main/"


def lint_llms(repo):
    """Check llmstxt.org structure, that links into this repo resolve, and that generated llms files are fresh."""
    errors = []
    files = [f for f in [repo / "llms.txt", *sorted((repo / "skills").glob("*/llms.txt")), *sorted((repo / "skills").glob("*/llms/*.txt"))] if f.is_file()]
    for f in files:
        rel = f.relative_to(repo)
        lines = f.read_text().lstrip("\ufeff").splitlines()
        if not lines or not lines[0].startswith("# "):
            errors.append(f"{rel}: first line must be an H1 ('# Title')")
        if len([l for l in lines[:6] if l.startswith("> ")]) == 0:
            errors.append(f"{rel}: missing the blockquote summary near the top")
        in_list = False
        for n, l in enumerate(lines, 1):
            if l.startswith("## "):
                in_list = True
            elif in_list and l.startswith("- "):
                m = LINK_RE.match(l)
                if not m:
                    errors.append(f"{rel}:{n}: list item is not '- [name](url): note'")
                    continue
                url = m.group(1)
                if url.startswith(OUR_RAW) and not (repo / url[len(OUR_RAW):]).exists():
                    errors.append(f"{rel}:{n}: link target not in this repo: {url[len(OUR_RAW):]}")
    gen = repo / "scripts" / "gen_llms.py"
    if gen.is_file():
        ns = {"__file__": str(gen), "__name__": "gen_llms"}
        exec(compile(gen.read_text(), str(gen), "exec"), ns)
        for rel, text in ns["build_all"]().items():
            if not (repo / rel).is_file() or (repo / rel).read_text() != text:
                errors.append(f"{rel} is missing or out of date: run python3 scripts/gen_llms.py")
    return errors, len(files)


def main():
    repo = Path(__file__).resolve().parent.parent
    skills_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else repo / "skills"
    skills = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not skills:
        print(f"no skills found in {skills_dir}")
        return 1
    errors = [e for s in skills for e in lint_skill(s, repo)]
    llms_errors, n_llms = ([], 0)
    if len(sys.argv) == 1:  # only for the real repo, not an ad hoc skills dir
        llms_errors, n_llms = lint_llms(repo)
    errors += llms_errors
    for e in errors:
        print("ERROR", e)
    print(f"{len(skills)} skill(s) and {n_llms} llms file(s) checked, {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
