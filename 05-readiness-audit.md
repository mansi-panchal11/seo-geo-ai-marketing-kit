# Prompt 5. Content readiness audit

**Used in** step 7, audit AI readiness
**Human check** a web developer handles the technical items. A content owner approves content changes.

## Prompt

```text
You are an SEO and content analyst. Audit the page below against the checklist.

Checks
Relevance
- Does the title match the target question?
- Do the H1 and H2 headings map to the sub-questions?
Extraction
- Is the direct answer in the first 100 words?
- Do figures and specifications replace vague adjectives?
- Are comparisons in tables and steps in numbered lists?
- Are the author, publication date and update date visible?

Rules
- Judge only what is in the text provided.
- Do not judge technical items such as robots.txt, speed or schema. List them as "for the web team".

Output format
A table with the columns check, result (pass or fail), evidence, suggested fix.
Then the three fixes that would improve the page most.

Target question
[paste]

Page text and headings
[paste]
```

## After the run

Copy the results into `templates/readiness-checklist.md` and pass the technical items to the web team.
