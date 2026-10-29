# Measurement guide

This guide defines every metric used in the kit and explains how to read the results.

## Visibility metrics

| Metric | Definition | Formula |
|---|---|---|
| Answer inclusion rate | Share of answers that mention the brand | Answers that mention the brand divided by all answers |
| Share of Voice | The brand's part of all tracked brand mentions | Brand mentions divided by mentions of all tracked brands |
| Share of Citation | The brand's part of all cited sources | Citations of the brand's own domains divided by all citations |
| Positive sentiment | How favourably the brand is described | Positive answers divided by answers that mention the brand |

## Content and process metrics

| Metric | Definition | How to collect |
|---|---|---|
| Pages passing every readiness check | Pages with no failed item in the checklist | Count from `templates/readiness-checklist.md` |
| First-time brand compliance rate | Drafts that pass the brand voice check at the first run | Pass count divided by draft count from the checker log |
| Days from interview to publication | Time between the expert interview and the publication date | Dates in the claims register and the publication log |
| Reach and interactions per post | Audience response to repurposed posts | Platform analytics |
| Visits and leads from AI referrals | Sessions that arrive from AI engines and the leads they produce | Web analytics, filtered by referrer |

## How to read the results

- A change of a few points on a small sample can be noise. The script warns below 30 answers.
- Compare the same prompts, engines and conditions.
- Look at the breakdown by engine and by topic. A flat overall result can hide a gain on one engine and a loss on another.
- Share of Voice depends on the list of tracked brands. Keep the list the same between runs.
- Sentiment is a judgement. Have a second person check a sample of the answers.

## Limits

- AI answers vary between runs and between users.
- Engines change over time, so a movement can come from the engine and not from your work.
- Other activity, such as press coverage or competitor launches, can also move the metrics.
- This kit measures visibility in AI answers. It does not measure sales.
