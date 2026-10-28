#!/usr/bin/env python3
"""Collapse duplicate <main id="main"> tags introduced by the skip-link script."""
import os

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")

pages = [
    "index.html", "lesson-plans.html", "worksheets.html", "quizzes.html",
    "parent-emails.html", "templates/index.html", "templates/lesson-plan.html",
    "templates/worksheet.html", "templates/quiz.html", "templates/parent-email.html",
]

for name in pages:
    path = os.path.join(SITE, name)
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    tag = '<main id="main">'
    count = content.count(tag)
    if count <= 1:
        print("ok:", name)
        continue

    # Keep only the first occurrence; drop the rest.
    first = content.find(tag)
    rest = content[first + len(tag):]
    # Replace remaining occurrences with plain text (no tag).
    rest = rest.replace(tag, "")
    content = content[:first] + tag + rest

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print("fixed:", name)