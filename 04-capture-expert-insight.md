# Step 4. Capture expert insight

## Purpose

Collect real knowledge from a subject matter expert so the content contains facts that generic content does not have.

## Inputs

- The gaps found in step 3, meaning prompts where the brand is missing
- An available expert
- The interview guide in `templates/expert-interview-guide.md`

## Method

1. Choose one gap prompt and one expert who can answer it.
2. Share the target question and ask the expert to bring one example, one figure and one common mistake.
3. Hold a 20 to 30 minute interview. Record it only with consent.
4. Transcribe the recording. Any transcription tool works.
5. Run `prompts/01-extract-claims.md` to list every claim, figure and opinion with the exact words used.
6. Copy the result into `templates/claims-register.csv`.
7. Send the register to the expert. The expert marks each claim as confirmed, to correct or to remove.
8. Only confirmed claims move to step 5.

## Role of AI

AI transcribes the interview and extracts claims. It does not add facts. The prompt forbids figures that the expert did not mention.

## Role of the human

The expert confirms every claim. The marketer decides which claims are usable and which sources to attach.

## Output

A claims register with confirmed claims.

## Quality checks

- Every figure in the register has a source or an expert confirmation.
- Opinions are labelled as opinions.
- Confidential or unapproved statements are removed.

## Common mistakes

- Letting AI fill gaps with plausible figures.
- Publishing a claim the expert has not seen.
- Interviewing the expert without a target question.
