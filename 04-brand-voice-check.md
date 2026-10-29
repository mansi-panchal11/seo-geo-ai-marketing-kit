# Prompt 4. Brand voice checker

**Used in** step 6, repurpose and check the brand voice
**Human check** a person makes the final approval. The checker only flags problems.

## Prompt

```text
You are a brand editor. Review the draft below against the brand voice rules.

For each rule in the guide, answer pass or fail.
For each fail, quote the exact words, explain the problem in one sentence and give a corrected version.

Also check
- Every figure or claim appears in the validated facts list.
- The call to action is single and clear.
- No competitor is named.
- No superlative is used without proof.

Output format
1. A table with the columns rule, result, quoted text, fix.
2. An overall decision. Write "approve", "approve with changes" or "reject".
3. A list of claims that are not in the validated facts list.

Brand voice rules
[paste]

Validated facts
[paste]

Draft
[paste]
```

## Notes

Keep a count of pass and fail results per draft. This gives the first-time compliance rate described in `docs/measurement-guide.md`.
