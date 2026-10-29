# Prompt 1. Extract claims from an expert interview

**Used in** step 4, capture expert insight
**Human check** the expert validates every claim before it is used

## Prompt

```text
You are a marketing editor. Below is the transcript of an interview with a subject matter expert.

Task
1. List every factual claim, figure, date and named standard the expert mentioned.
2. For each item, copy the exact words the expert used.
3. Mark each item as "stated as fact", "opinion" or "unclear".
4. List the questions a buyer would ask that the expert answered well.
5. List statements that need a source before publication.

Rules
- Use only what is in the transcript.
- Do not add figures, names or sources that the expert did not mention.
- If something is unclear, write "needs confirmation" and do not guess.

Output format
A table with the columns claim, exact words, type, needs source (yes or no).
Then a bullet list of buyer questions answered.

Transcript
[paste transcript]
```

## After the run

Copy the table into `templates/claims-register.csv` and send it to the expert for confirmation.
