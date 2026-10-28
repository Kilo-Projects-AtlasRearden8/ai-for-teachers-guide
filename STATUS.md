# STATUS

## What was built

A beginner manual on using free AI for teaching, delivered as Markdown docs and a static HTML site, published by **Asdale Dynamics, LLC**.

**Root**
- `README.md` — overview, contents, golden rule, credit to Asdale Dynamics, LLC, MIT license pointer
- `LICENSE` — MIT License, copyright line exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`
- `STATUS.md` — this file

**docs/ — Markdown manual**
- `01-getting-started.md` — what AI is, picking a free model, first prompt
- `02-free-ai-models.md` — free model options, how to choose, safety check before sign-up
- `03-lesson-plans.md` — step-by-step lesson plans with copyable example prompt
- `04-worksheets.md` — step-by-step worksheets and answer keys
- `05-quizzes.md` — step-by-step quiz questions with separate answer key
- `06-parent-emails.md` — step-by-step parent emails with tone tips
- `07-privacy-safety.md` — golden rule: never paste student names or grades; FERPA in plain English; checklist
- `08-printable-templates.md` — how to print templates
- `templates/` — four fill-in-the-blank Markdown templates (lesson plan, worksheet, quiz, parent email)

**site/ — static HTML website (no build step, no server, no tracking)**
- `index.html` — home and overview
- `lesson-plans.html`, `worksheets.html`, `quizzes.html`, `parent-emails.html` — the four how-to guides
- `templates/index.html` + four template pages — printable forms
- `css/style.css` — clean styles, including `@media print` layout that hides navigation
- Every page credits Asdale Dynamics, LLC

## How to run

1. Open `site/index.html` in any web browser. No build step, no server, no internet required.
2. Read the guides, copy the example prompts into any free AI tool (see `docs/02-free-ai-models.md`).
3. Print any page with Ctrl+P (Windows) or Command+P (Mac); navigation hides automatically for a clean printout.
4. Or read the Markdown in `docs/` directly, and print the templates in `docs/templates/`.

## Verification results

- HTML well-formedness: all 10 HTML files parse cleanly (no unclosed/mismatched tags), each has a `<title>`
- Internal links: zero broken links
- Secrets/scan: grep for API keys, secrets, tokens, passwords found nothing but the word "password" used in general advice (no actual credentials)
- No `.github/workflows` directory or files
- `LICENSE` contains the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC
- No student names or grades appear anywhere in the repository
- No personal data, API keys, or secrets committed

## Known gaps

- No automated test suite (the site is static HTML/Markdown; verification above is the test)
- Free AI models and pricing change over time; `docs/02-free-ai-models.md` tells readers to check each tool's website before signing up
- Links from `site/` pages to `docs/` use `../docs/`, which works when opening files directly in a browser or when the repo root is served
- No search function or dark mode; keep the site intentionally simple and printable
