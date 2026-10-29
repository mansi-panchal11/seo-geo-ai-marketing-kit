# Step 7. Audit AI readiness

## Purpose

Check whether AI engines can reach a page, recognise it as relevant to a question and extract a precise answer from it. A page can be well written and still fail one of these checks.

## The three checks

| Check | Question | Examples |
|---|---|---|
| Access | Can an AI crawler open the page? | robots.txt rules, login walls, content that only appears after scripts run, sitemap, loading speed |
| Relevance | Does the page signal that it answers the question? | Descriptive URL, title that matches the question, headings that match sub-questions, structured data |
| Extraction | Can an engine lift a clear answer? | Answer in the first 100 words, figures instead of adjectives, tables and lists, author and dates |

The full list is in `templates/readiness-checklist.md`.

## Method

1. Audit the new page and the existing pages that already target the same prompts.
2. Run `prompts/05-readiness-audit.md` for the content checks.
3. Ask the web team to verify the technical items (crawler access, speed, sitemap, structured data).
4. Record pass or fail for every item.
5. Fix the failures in this order. Access first, then relevance, then extraction. A page that cannot be reached cannot be cited.
6. Check the page again after the fixes.

## Role of AI

AI reviews the text against the content checks and suggests rewrites. It cannot verify crawler access or speed.

## Role of the human

The web team checks and fixes technical items. A content owner approves text changes.

## Output

A completed checklist per page and a count of pages that pass every item.

## Quality checks

- Technical checks were made on the live page and not on a draft.
- Each failure has an owner and a date.

## Common mistakes

- Optimising wording while the page blocks crawlers.
- Blocking AI crawlers by accident through a general robots.txt rule.
- Adding structured data that does not match the visible text.
