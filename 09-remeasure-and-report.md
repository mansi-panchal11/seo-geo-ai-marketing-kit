# Step 9. Re-measure and report

## Purpose

Find out whether visibility changed after the content work, and decide what to do next.

## Inputs

- The baseline log from step 3
- The publication log from step 8
- The same prompt set, engines and test conditions

## Method

1. Wait four to six weeks after publication. AI engines need time to pick up new pages.
2. Run the same prompts on the same engines under the same conditions. Use the same number of runs per prompt.
3. Log the answers in a new file.
4. Compare the two logs with the script.

```bash
python scripts/geo_metrics.py --log baseline.csv --compare followup.csv \
    --brand YourBrand --domains yourbrand.com --by engine
```

5. Run the comparison by topic and by stage as well.
6. Run `prompts/06-summarise-results.md` to draft the written summary. Check every number against the script output.
7. Complete `templates/results-report.md`.
8. Decide the next loop.
   - Prompts where the brand is still absent go back to step 4.
   - Pages that still fail a readiness check go back to step 7.
   - New topics and new prompts go into a new version of the prompt set.

## Role of AI

AI drafts the summary from the numbers provided. It must not add numbers or claim a cause.

## Role of the human

A person checks the numbers, writes the conclusion and chooses the next actions.

## Output

A results report and a plan for the next loop.

## Quality checks

- The report shows the number of answers behind each figure.
- The report names other possible explanations for the change.
- The report says what was not measured.

## Common mistakes

- Reporting a change as proof of cause.
- Comparing runs made under different conditions.
- Stopping after one loop. Visibility moves as engines and competitors change, so the loop should repeat.
