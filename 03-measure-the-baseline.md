# Step 3. Measure the baseline

## Purpose

Record how often AI engines mention, cite and describe the brand today. Every later result is compared with this baseline.

## Inputs

- The frozen prompt set from step 2
- Access to the AI engines you want to track, for example ChatGPT, Google AI Overviews, Gemini, Perplexity and Copilot
- A list of tracked brands (your brand and its main competitors)
- A list of domains that count as your own sources

## Method

1. Fix the test conditions and write them down.
   - Same language and country for every run.
   - A fresh session without personal history where possible.
   - The same day or the same week for all engines.
2. Run each prompt on each engine. Run each prompt three times if time allows, because answers vary.
3. For each answer, log one row in `templates/ai-answer-log.csv`.
   - `brands_mentioned` the tracked brands named in the answer, separated by semicolons.
   - `sources_cited` the domains of the sources the answer cites, separated by semicolons.
   - `sentiment` positive, neutral or negative for how the answer describes your brand, or not_mentioned.
   - `notes` anything unusual, such as an answer that refused to respond.
4. Run the metrics script.

```bash
python scripts/geo_metrics.py --log my-baseline.csv --brand YourBrand --domains yourbrand.com
```

5. Read the results by engine and by topic with `--by engine` and `--by topic`.

## Role of AI

AI engines are the object of the measurement. Do not use an AI tool to judge its own answers without checking them. A person reads each answer and fills the log. Paid tracking tools can automate the runs, and the same log format works with their exports.

## Output

A baseline log, a baseline results table and a list of prompts where competitors appear and your brand does not.

## Quality checks

- At least 30 answers in total, and more is better. The script warns when the sample is small.
- The test conditions are written down.
- Two people can log the same answer and reach the same result.

## Common mistakes

- Running each prompt once and treating the result as fixed.
- Changing the prompts or the engines before the follow-up.
- Counting a mention in a comparison list as positive sentiment.
