# AI for Teachers: A Beginner's Manual

A plain-English, step-by-step guide to using **free AI** for everyday teaching work: lesson plans, worksheets, quiz questions, and parent emails. Written and published by **Asdale Dynamics, LLC**.

## Why this manual exists

You are a teacher. You are busy. AI can feel like another chore — technical, jargon-heavy, and risky. It does not have to be.

This manual explains AI "like a friend would": plain English, step by step, never condescending. You do not need to be technical, and you do not need to pay. Everything here works with free AI models.

It is part of the Asdale Dynamics, LLC library of beginner-friendly AI education. Dylan Asdale, a registered nurse turned AI author, wrote *The Massive AI Manual* and runs [dylanasdale.github.io](https://dylanasdale.github.io). This manual follows the same warm, tested, local-first style.

## What you can do with it

- **Lesson plans** — draft objectives, activities, and timing in minutes, then edit in your own voice
- **Worksheets** — generate questions and a separate answer key
- **Quizzes** — multiple choice and short answer, with answer keys kept separate
- **Parent emails** — warm, short, plain-English drafts you send from your own account
- **Printable templates** — fill-in-the-blank forms you can print and complete by hand

## What is inside

**docs/ — the manual (Markdown)**
- `01-getting-started.md` — what AI is, picking a free model, and writing your first prompt
- `02-free-ai-models.md` — free models you can use today, no credit card required
- `03-lesson-plans.md` — step-by-step lesson plans, with a copyable example prompt
- `04-worksheets.md` — step-by-step worksheets and answer keys
- `05-quizzes.md` — step-by-step quizzes
- `06-parent-emails.md` — step-by-step parent emails, with tone tips
- `07-privacy-safety.md` — the most important rules: never paste student names or grades
- `08-printable-templates.md` — how to print the templates
- `templates/` — four fill-in-the-blank templates you can print and use

**site/ — the same manual as a static HTML website**
- `index.html` — home and overview
- `lesson-plans.html`, `worksheets.html`, `quizzes.html`, `parent-emails.html` — each guide as a printable page
- `templates/` — printer-ready template pages
- `css/style.css` — clean styles, including a print layout that hides navigation
- No build step, no server, no tracking. Open any `.html` file in your browser.

## The golden rule

**Never paste student names, grades, ID numbers, or any other personal student information into an AI tool.**

Treat an AI chat like a public whiteboard: only share what you would feel comfortable writing on the board for the whole school to see. See `docs/07-privacy-safety.md` for the full rules, including how to turn off training on your conversations.

## How to use this manual

1. Pick one free AI tool (see `docs/02-free-ai-models.md`) and use it for a week before trying another.
2. Copy an example prompt from any guide, adapt it, and send it.
3. Check and edit the output — you are still the teacher.
4. Print the templates with Ctrl+P (Windows) or Command+P (Mac).

## Education only

This manual is for teaching and learning use. It is not medical, legal, or professional advice. If an email or handout touches on a student's health or legal matters, have your school administrator review it first.

## Credit

Written and maintained by **Asdale Dynamics, LLC** (Indiana), founder Dylan Asdale. Asdale Dynamics publishes beginner-friendly AI education, books, and practical tools. More at dylanasdale.github.io.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## Tests

Run the automated checks with: `python3 tests/test_site.py`