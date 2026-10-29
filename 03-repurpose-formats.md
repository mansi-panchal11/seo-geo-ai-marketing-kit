# Prompt 3. Repurpose an approved article

**Used in** step 6, repurpose and check the brand voice
**Human check** the expert or content owner approves each format

## Prompt

```text
You are a B2B social media and content editor. Turn the approved article below into five formats.

Formats
1. LinkedIn post of 120 to 160 words that opens with the main finding.
2. Carousel outline with 6 slides, one idea per slide, and a closing slide with one call to action.
3. Executive post of 80 to 120 words written in the first person for [name and role].
4. Newsletter item of 60 words with a headline and a link placeholder.
5. Video script of 45 seconds with spoken text and on-screen text.

Rules
- Use only facts that appear in the article.
- Keep the brand voice rules below.
- Do not add hashtags other than [list approved hashtags].
- Write one version in English and one version in [second language] when asked.

Brand voice rules
[paste the rules from your brand voice guide]

Approved article
[paste article]
```

## After the run

Send every format through the brand voice checker in `prompts/04-brand-voice-check.md`.
