# Automation ideas

These are design notes for teams that want to automate parts of the workflow. They are not included as ready-made workflows. Test every automation on a small batch before relying on it.

## Weekly measurement run

1. A scheduler starts the run each week.
2. A tracking tool or an API sends each prompt in the prompt set to each engine.
3. The answers are parsed into the columns of the answer log.
4. The script computes the metrics and stores the results.
5. A person reviews a sample of the parsed answers to confirm the parsing is correct.

## Draft pipeline

1. A new interview transcript is saved in a shared folder.
2. An AI step extracts claims into the claims register.
3. The expert receives the register for confirmation.
4. After confirmation, an AI step drafts the article and sends it to the editor.

## Brand voice gate

1. Every new draft goes through the checker prompt.
2. The result (pass or fix needed) is logged.
3. Drafts marked reject return to the writer. Drafts marked approve go to the content owner.

## Rules for any automation

- A person approves anything that is published or sent outside the company.
- Log every automated step so results can be traced.
- Keep personal and confidential data out of tools that the company has not approved.
