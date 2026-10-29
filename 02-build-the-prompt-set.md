# Step 2. Build the prompt set

## Purpose

Create the fixed list of questions that will be asked to AI engines. The prompt is the unit of measurement. Topics only group prompts.

## Why prompts differ from keywords

Keywords are short and come with public volume data. Prompts are long, conversational and have no volume data. A prompt reads like a real question, for example "Which commercial EV charging providers offer software to manage many chargers?".

## Inputs

- The chosen topics from step 1
- Buyer personas
- Real questions from sales, support and search tools

## Method

1. Define the personas for each topic, for example facility manager, procurement lead, finance director.
2. Define the funnel stages.
   - **Awareness** the buyer learns about the problem.
   - **Consideration** the buyer compares options.
   - **Decision** the buyer chooses a supplier.
3. Source real questions.
   - Question-style queries from Google Search Console (what, why, how, which, where).
   - Auto-suggested questions from search engines and AI tools.
   - Sub-questions an AI engine asks itself when you submit the topic. Some engines show them.
   - Questions collected by sales and customer support.
4. Write 10 to 20 prompts per topic. Balance the three stages. Include a few prompts that name the brand and mostly prompts that do not.
5. Write each prompt as a full sentence, the way a buyer would type it.
6. Record each prompt in `templates/prompt-set.csv` with its topic, persona, stage, intent and priority.
7. Freeze the set and give it a version number. Do not change prompts between the baseline and the follow-up. Add new prompts in a new version.

## Role of AI

AI can generate variations of a question and cluster similar ones. A person removes prompts that no buyer would ask and checks that the wording is natural.

## Output

A versioned prompt set.

## Quality checks

- Every prompt belongs to one topic, one persona and one stage.
- The set is not limited to prompts that name the brand.
- Prompts are written in the language of the target market.

## Common mistakes

- Writing prompts as keyword strings.
- Writing only prompts that favour the brand.
- Editing the prompts after the baseline run.
