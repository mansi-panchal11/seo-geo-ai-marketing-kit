# Step 6. Repurpose and check the brand voice

## Purpose

Turn one approved article into the formats an audience actually reads, and keep the brand voice consistent across all of them.

## Inputs

- The approved article from step 5
- The brand voice guide (`templates/brand-voice-guide.md`)
- The list of approved hashtags and key messages

## Formats

| Format | Length | Purpose |
|---|---|---|
| LinkedIn post | 120 to 160 words | Share the main finding |
| Carousel | 6 slides | One idea per slide and one call to action |
| Executive post | 80 to 120 words | First-person voice for a leader |
| Newsletter item | About 60 words | Drive readers to the article |
| Video script | 45 seconds | Spoken text and on-screen text |

## Method

1. Run `prompts/03-repurpose-formats.md` with the approved article and the brand voice rules.
2. Run each output through `prompts/04-brand-voice-check.md`.
3. Fix every item marked as fail, then run the checker again.
4. The content owner reads each format and approves it. The checker only flags problems.
5. Adapt the approved formats for other languages and countries if needed. Have a native speaker review the result.
6. Log the checker result for each draft (pass at first run or fix needed).

## Role of AI

AI adapts the article into formats and flags deviations from the voice rules.

## Role of the human

A person approves every format. A person decides when a voice rule should change.

## Output

Approved content in all formats and a log of checker results.

## Quality checks

- No format contains a fact that is missing from the article.
- Each format has one call to action.
- Translated versions are reviewed by a person who speaks the language.

## Common mistakes

- Publishing the AI output without a person's approval.
- Writing a voice guide that is too vague for a checker to apply.
- Using the checker as a replacement for the expert's review.
