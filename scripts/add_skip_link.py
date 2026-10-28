#!/usr/bin/env python3
"""Add a skip-to-main link and id="main" to every HTML page."""
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

    if "skip-link" in content:
        print("already updated:", name)
        continue

    # Add skip link after <body>
    content = content.replace(
        "<body>\n<div class=\"container\">",
        "<body>\n<a class=\"skip-link\" href=\"#main\">Skip to main content</a>\n"
        "<div class=\"container\">\n<main id=\"main\">",
    )
    # Ensure the <main> element has id="main"
    content = content.replace("<main>", "<main id=\"main\">")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print("updated:", name)