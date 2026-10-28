#!/usr/bin/env python3
"""Automated tests for the AI for Teachers manual.

Checks:
1. Every HTML page is well-formed and has a <title>
2. Every internal link resolves to an existing file
3. No secrets, API keys, or student names/grades in the repo
4. LICENSE contains the exact required copyright line
5. README credits Asdale Dynamics, LLC
6. The four core teaching topics exist in docs/ and site/
7. No .github/workflows directory

Run: python3 tests/test_site.py
"""

import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(ROOT, "docs")

passed = 0
failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}  {detail}")


class TagChecker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                     "link", "meta", "param", "source", "track", "wbr"}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if not self.stack:
            self.errors.append(f"unexpected </{tag}>")
            return
        if self.stack[-1] != tag:
            self.errors.append(f"closed </{tag}> but expected </{self.stack[-1]}>")
        else:
            self.stack.pop()


def html_files():
    out = []
    for dirpath, _, files in os.walk(SITE):
        for f in files:
            if f.endswith(".html"):
                out.append(os.path.join(dirpath, f))
    return out


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# 1. HTML well-formedness
for path in html_files():
    content = read_text(path)
    checker = TagChecker()
    checker.feed(content)
    ok = not checker.errors and not checker.stack
    rel = os.path.relpath(path, ROOT)
    check(f"well-formed: {rel}", ok, "; ".join(checker.errors + [f"<{t}> unclosed" for t in checker.stack]))
    if ok:
        check(f"has title: {rel}", bool(re.search(r"<title>.*?</title>", content, re.S)))

# 2. Internal links resolve
broken = []
for path in html_files():
    base = os.path.dirname(path)
    for m in re.finditer(r'(?:href|src)=["\']([^"\']+)["\']', read_text(path)):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, target))):
            broken.append((os.path.relpath(path, ROOT), target))
check("all internal links resolve", not broken, str(broken))

# 3. No secrets / no actual student names or grades
# A real student record looks like "grade: A" or "ID number: 12345".
# The words "student names" in the privacy rule text are fine and expected.
secret_pattern = re.compile(r"(api[_-]?key|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN)")
student_pattern = re.compile(
    r"\b(grade[s]?\s*[:=]\s*[A-Fa-f]\b|ID number[s]?\s*[:=]\s*\d+|"
    r"name\s*[:=]\s*[A-Z][a-z]+ [A-Z][a-z]+)\b"
)
hits = []
for dirpath, _, files in os.walk(ROOT):
    if ".git" in dirpath or os.sep + "tests" in dirpath:
        continue
    for f in files:
        if f.endswith((".html", ".md", ".css", ".py")):
            text = read_text(os.path.join(dirpath, f))
            if secret_pattern.search(text):
                hits.append((f, "secret-like pattern"))
            if student_pattern.search(text):
                hits.append((f, "actual student name/grade reference"))
check("no secrets or actual student names/grades", not hits, str(hits))

# 4. LICENSE exact copyright line
license_text = read_text(os.path.join(ROOT, "LICENSE"))
check("LICENSE copyright line exact", "Copyright (c) 2026 Asdale Dynamics, LLC" in license_text)

# 5. README credits Asdale Dynamics, LLC
readme_text = read_text(os.path.join(ROOT, "README.md"))
check("README credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in readme_text)

# 6. Core topics exist in docs and site
for topic, filename in [("lesson plans", "03-lesson-plans.md"),
                        ("worksheets", "04-worksheets.md"),
                        ("quizzes", "05-quizzes.md"),
                        ("parent emails", "06-parent-emails.md")]:
    check(f"docs topic present: {filename}", os.path.exists(os.path.join(DOCS, filename)))
for topic, filename in [("lesson-plans.html", "lesson-plans.html"),
                        ("worksheets.html", "worksheets.html"),
                        ("quizzes.html", "quizzes.html"),
                        ("parent-emails.html", "parent-emails.html")]:
    check(f"site page present: {filename}", os.path.exists(os.path.join(SITE, filename)))

# 7. No .github/workflows
check("no .github/workflows", not os.path.exists(os.path.join(ROOT, ".github", "workflows")))

# 8. Templates exist
for name in ("lesson-plan.md", "worksheet.md", "quiz.md", "parent-email.md"):
    check(f"docs template: {name}", os.path.exists(os.path.join(DOCS, "templates", name)))
for name in ("lesson-plan.html", "worksheet.html", "quiz.html", "parent-email.html"):
    check(f"site template: {name}", os.path.exists(os.path.join(SITE, "templates", name)))

# 9. Print CSS present
css = read_text(os.path.join(SITE, "css", "style.css"))
check("print CSS present", "@media print" in css)

print()
print(f"{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)