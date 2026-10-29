# Step 5. Draft answer-first content

## Purpose

Write a page that gives the direct answer immediately and supports it with facts, so that both readers and AI engines can extract a precise answer.

## Inputs

- The target prompt
- The confirmed claims from step 4
- The brand voice guide

## Structure of the page

| Part | Rule |
|---|---|
| Title | Matches the question. Does not start with the brand name. |
| Direct answer | 60 to 100 words at the top. |
| H2 sections | Each section answers one sub-question a buyer would ask next. |
| Facts | Figures and specifications replace vague adjectives. |
| Comparison | A table when the topic has options. |
| Checklist | What to ask a supplier or check before deciding. |
| FAQ | Three short questions. |
| Page details | Author, publication date and update date. |

## Method

1. Run `prompts/02-draft-answer-first-article.md` with the target prompt and only the confirmed claims.
2. Read the draft against the claims register. Mark any sentence without a source.
3. Replace each marker "[fact needed]" with a confirmed fact or delete the sentence.
4. Check the opening. A reader should have the answer after 100 words.
5. Send the draft to the expert for a final read.
6. Save the approved text.

## Role of AI

AI writes a first draft from the facts provided. It structures the page and shortens sentences.

## Role of the human

An editor checks facts, tone and structure. The expert approves the final text.

## Output

An approved article.

## Quality checks

- The answer appears in the first 100 words.
- Every figure appears in the claims register.
- No competitor is named in the article.

## Common mistakes

- Starting with company history instead of the answer.
- Keeping AI-written statistics that nobody confirmed.
- Writing for search engines only and forgetting the reader.
