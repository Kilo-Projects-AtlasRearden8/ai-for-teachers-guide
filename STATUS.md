# STATUS

## What was built

A beginner manual on using free AI for teaching, delivered as Markdown docs and a static HTML site, published by **Asdale Dynamics, LLC**.

**Root**
- `README.md` — overview, founder background, contents, golden rule, education-only note, test instructions
- `LICENSE` — MIT License, copyright line exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`
- `STATUS.md` — this file
- `tests/test_site.py` — automated test suite (42 checks)
- `scripts/add_skip_link.py`, `scripts/fix_main_tags.py` — helper scripts (one-time site fixes)

**docs/ — Markdown manual**
- `01-getting-started.md` — what AI is, picking a free model, first prompt
- `02-free-ai-models.md` — free model options, how to choose, safety check before sign-up
- `03-lesson-plans.md` — step-by-step lesson plans with copyable example prompt
- `04-worksheets.md` — step-by-step worksheets and answer keys
- `05-quizzes.md` — step-by-step quiz questions with separate answer key
- `06-parent-emails.md` — step-by-step parent emails with tone tips
- `07-privacy-safety.md` — golden rule: never paste student names or grades; FERPA in plain English; checklist
- `08-printable-templates.md` — how to print the templates
- `templates/` — four fill-in-the-blank Markdown templates (lesson plan, worksheet, quiz, parent email)

**site/ — static HTML website (no build step, no server, no tracking)**
- `index.html` — home and overview
- `lesson-plans.html`, `worksheets.html`, `quizzes.html`, `parent-emails.html` — the four how-to guides
- `templates/index.html` + four template pages — printable forms
- `css/style.css` — clean styles, `@media print` layout that hides navigation, accessibility skip-link
- Every page credits Asdale Dynamics, LLC

## How to run

1. Open `site/index.html` in any web browser. No build step, no server, no internet required.
2. Read the guides, copy the example prompts into any free AI tool (see `docs/02-free-ai-models.md`).
3. Print any page with Ctrl+P (Windows) or Command+P (Mac); navigation hides automatically for a clean printout.
4. Or read the Markdown in `docs/` directly, and print the templates in `docs/templates/`.
5. Run the tests: `python3 tests/test_site.py` (42 checks).

## Verification results

- Test suite: `python3 tests/test_site.py` → **42 passed, 0 failed**
- HTML well-formedness: all 10 HTML files parse cleanly (no unclosed/mismatched tags), each has a `<title>`, each has exactly one `<main id="main">`
- Internal links: zero broken links (verified relative to each file's own directory)
- Secrets/scan: no API keys, secrets, tokens, or actual student name/grade records anywhere in the repo
- No `.github/workflows` directory or files
- `LICENSE` contains the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC and references founder Dylan Asdale
- No student names or grades appear anywhere in the repository
- No personal data, API keys, or secrets committed
- Print CSS present (`@media print` in `site/css/style.css`)

## Critical review findings (round 2)

- **README quality improved** — warmer tone, founder background (registered nurse turned AI author), education-only disclaimer, and test instructions added
- **Added automated test suite** (`tests/test_site.py`) covering HTML well-formedness, link resolution, secret/student-data scanning, LICENSE copyright line, README credit, topic presence, template presence, print CSS, and absence of `.github/workflows`
- **Added accessibility skip-link** (`Skip to main content`) on all 10 pages, with `id="main"` on each `<main>` element
- **Fixed a duplicate `<main>` tag** introduced during the skip-link addition (collapsed to one per page)
- **Refined the secret/student-data scan** to avoid false positives on the privacy rule text itself (the words "student names" in the rule are correct and expected)
- All content remains plain English, step by step, printable, and free-model-focused

## Known gaps

- No automated test suite beyond `tests/test_site.py` (the site is static HTML/Markdown; the suite above is the verification)
- Free AI models and pricing change over time; `docs/02-free-ai-models.md` tells readers to check each tool's website before signing up
- Links from `site/` pages to `docs/` use `../docs/`, which works when opening files directly in a browser or when the repo root is served
- No search function or dark mode; keep the site intentionally simple and printable
- The two helper scripts in `scripts/` are one-time site-fix utilities, not part of the user-facing deliverable