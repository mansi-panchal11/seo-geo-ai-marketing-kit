# Prompt 6. Summarise the measurement results

**Used in** step 9, re-measure and report
**Human check** verify every number against the script output

## Prompt

```text
You are a marketing analyst. Below is the output of a before and after comparison of AI search visibility.

Task
1. Describe in plain sentences what changed. Use only the numbers provided.
2. Name the engines and topics where the change was largest and smallest.
3. List two or three possible explanations other than our content, such as competitor activity or engine updates.
4. State how many answers sit behind each figure and say whether the sample is large enough to trust.
5. Suggest three actions for the next loop.

Rules
- Do not claim that our content caused the change.
- Do not round figures upwards.
- If a figure is missing, say so.

Comparison output
[paste the table from scripts/geo_metrics.py]

Content published between the two runs
[paste list]
```
