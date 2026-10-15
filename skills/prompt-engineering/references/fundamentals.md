# Prompt Engineering Fundamentals

Source: dair-ai/Prompt-Engineering-Guide, `pages/introduction.en.mdx`, `pages/introduction/{basics,elements,settings,tips,examples}.en.mdx`.
Items tagged "(not in repo)" are added from general knowledge, not from the guide.

## Contents
1. What prompt engineering is
2. Basic prompting and prompt formats
3. Elements of a prompt
4. LLM settings (temperature, top-p, max length, stop, penalties)
5. General design tips
6. Task examples (summarization, extraction, QA, classification, conversation, code, reasoning)
7. Quick checklist
8. Audit notes

---

## 1. What prompt engineering is
- Discipline of developing and optimizing prompts to apply and build with LLMs across many tasks.
- Researchers use it to probe capabilities, limits and safety; developers use it to build robust prompting techniques that interface with LLMs and tools.
- Guide's test setup: examples run on `gpt-3.5-turbo` in OpenAI Playground with defaults `temperature=1`, `top_p=1`. Outputs vary by model and version, so treat sample outputs as illustrative.

## 2. Basic prompting and formats

Principle: the model continues a token sequence. `The sky is` yields `blue.`; add an instruction and the output improves (`Complete the sentence:\n\nThe sky is` -> `blue during the day and dark at night.`). Quality depends on how much information the prompt gives and how well it is crafted.

Chat roles (OpenAI-style, repo p. basics): `system` (optional; sets overall behavior), `user` (the prompt), `assistant` (model reply; can also be pre-filled to pass examples of desired behavior). Most guide examples use only `user`.

Standard formats:
```
<Question>?
```
```
<Instruction>
```
QA format (zero-shot):
```
Q: <Question>?
A:
```
Newer models infer QA, so `Q:` can be dropped.

Few-shot format (exemplars; enables in-context learning):
```
Q: <Question>?
A: <Answer>

Q: <Question>?
A: <Answer>

Q: <Question>?
A:
```
Format is not tied to QA; task-appropriate exemplars work:
```
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
```
-> `Negative`.

Zero-shot = no examples; few-shot = demonstrations in the prompt. See `techniques.md`.

## 3. Elements of a prompt
A prompt may contain any of (not all required):
- **Instruction**: the specific task to perform.
- **Context**: external info or extra context that steers the model (can be additional examples).
- **Input data**: the input/question to answer.
- **Output indicator**: type or format of output (e.g. the trailing `Sentiment:`).

Example mapping:
```
Classify the text into neutral, negative, or positive      <- instruction

Text: I think the food was okay.                           <- input data

Sentiment:                                                 <- output indicator
```
No context in that example; the format depends on the task.

## 4. LLM settings
Set via API/playground. Experiment per use case; results vary by model version.

| Setting | Effect | Guidance (repo) |
|---|---|---|
| Temperature | Lower = more deterministic (highest-probability token), higher = more random/diverse. | Low for fact-based QA; higher for poems/creative tasks. |
| Top P (nucleus sampling) | Only tokens within the top_p probability mass are considered. Low = confident/exact, high = more diverse. | Low for factual; high for diverse. |
| Max length | Caps generated tokens. | Prevents long/irrelevant output; controls cost. |
| Stop sequences | String that halts generation. | Control length/structure, e.g. stop at "11" to cap a list at 10 items. |
| Frequency penalty | Penalty on next token proportional to how many times it already appeared (prompt + response). | Reduces word repetition. |
| Presence penalty | Flat penalty on any token that has appeared, regardless of count. | Higher for diverse/creative text; lower to stay focused. |

Rules of thumb from repo: alter temperature OR top_p, not both; alter frequency OR presence penalty, not both.

(not in repo) Also: `top_k` on some providers (e.g. Gemini, Claude API); seed for reproducibility where supported. Reasoning/"thinking" models often fix or ignore temperature and top_p; check provider docs. For self-consistency, temperature must be >0 so samples differ. Temperature 0 is not strictly deterministic on all APIs.

## 5. General design tips

**Start simple, iterate.** Prompt design is experimental. Start with a simple prompt, add elements and context as needed. Split big tasks into subtasks and build up (precursor to prompt chaining).

**Instruction.** Use imperative verbs: Write, Classify, Summarize, Translate, Order. Vary keywords/context/data and test. Put instructions at the start and separate from context with a clear delimiter such as `###`:
```
### Instruction ###
Translate the text below to Spanish:

Text: "hello!"
```

**Specificity.** Be descriptive about task, format and style; examples are very effective for forcing an output format. There are no magic keywords. Too many irrelevant details dilute the prompt and prompt length is limited. Example with explicit output format:
```
Extract the name of places in the following text.

Desired format:
Place: <comma_separated_list_of_places>

Input: "<text>"
```

**Avoid imprecision.** Replace vague limits with concrete ones:
- Weak: `Explain the concept prompt engineering. Keep the explanation short, only a few sentences, and don't be too descriptive.`
- Better: `Use 2-3 sentences to explain the concept of prompt engineering to a high school student.`

**Say what to do, not what not to do.** Negative-only instructions (`DO NOT ASK FOR INTERESTS...`) failed in the movie-agent example (model asked for interests anyway). Fix: state the responsibility positively, give a fallback response:
```
The following is an agent that recommends movies to a customer. The agent is responsible to recommend a movie from the top global trending movies. It should refrain from asking users for their preferences and avoid asking for personal information. If the agent doesn't have a movie to recommend, it should respond "Sorry, couldn't find a movie to recommend today.".

Customer: Please recommend a movie based on my interests.
Agent:
```
(Tips adapted by the guide from OpenAI's "Best practices for prompt engineering with the OpenAI API".)

## 6. Task examples (verbatim prompts, trimmed)

### Summarization
```
Explain antibiotics

A:
```
Then compress by appending an instruction after the pasted text: `Explain the above in one sentence:`. Verify summary accuracy yourself.

### Information extraction
```
<paragraph about AI use disclosure in papers>

Mention the large language model based product mentioned in the paragraph above:
```
-> `ChatGPT`.

### Question answering (structured prompt: instruction + context + question + output indicator)
```
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.

Context: <passage>

Question: What was OKT3 originally sourced from?

Answer:
```
The "Unsure about answer" fallback is the anti-hallucination hook.

### Text classification
Zero-shot:
```
Classify the text into neutral, negative or positive.

Text: I think the food was okay.
Sentiment:
```
-> `Neutral`. To force lowercase label, add one example:
```
Classify the text into neutral, negative or positive.

Text: I think the vacation is okay.
Sentiment: neutral

Text: I think the food was okay.
Sentiment:
```
-> `neutral`. Failure case: with a made-up label ("nutral") in the instruction and no examples, the model ignores it and outputs `Neutral` (bias toward known labels). Fixes: add label descriptions or examples that show the unusual label.

### Conversation / role prompting
```
The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.

Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of blackholes?
AI:
```
Swap the tone line to `The assistant answers should be easy to understand even by primary school students.` to change register. More examples improve consistency.

### Code generation
Comment-style prompts, language inferred:
```
/*
Ask the user for their name and say "Hello"
*/
```
Schema-grounded SQL:
```
"""
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
"""
```

### Reasoning
Plain prompt on `The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.` fails (model said sum 119, odd/even confused). Prompt that decomposes works more often:
```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.

Solve by breaking the problem into steps. First, identify the odd numbers, add them, and indicate whether the result is odd or even.
```
Guide notes it still fails sometimes. Escalate to few-shot and CoT (see `techniques.md`).

## 7. Quick checklist
1. State the task as a verb-first instruction; put it first.
2. Delimit context/input (`###`, quotes, XML-ish tags).
3. Specify output format and give an output indicator or example.
4. Quantify constraints (2-3 sentences, N items, audience).
5. Positive instructions plus an explicit fallback for "don't know".
6. Add 1-3 examples if format or label space is unusual.
7. Hard reasoning: ask for steps or use CoT/PAL/etc.
8. Low temperature for facts and extraction; higher for creativity.
9. Iterate and test on several inputs; outputs are stochastic.

## 8. Audit notes
- **Stale model era**: all examples were run on `gpt-3.5-turbo`/`text-davinci-003`-class models. Behaviors like "model fails at 9,000 x 9,000" are not guaranteed on current models; many example failures (odd-numbers sum, "nutral" label) may now pass. Re-test rather than trust.
- **Contradiction**: intro says examples use `temperature=1`; settings page recommends low temperature for factual tasks. The guide's own factual examples (extraction, QA) therefore ran at the creative default.
- **Missing from settings page**: top_k, seed, reasoning-model behavior (many ignore temperature), structured-output/JSON modes, system-prompt best practice, prompt caching.
- **Missing topics**: no coverage of XML/markdown structuring, prefilling the assistant turn, long-context placement, evals/testing of prompts, prompt-injection defense (exists elsewhere in repo, `pages/risks/`).
- "Others recommend that you place instructions at the beginning": hedged, no evidence; for long documents, putting the question after the document is often recommended by providers (not in repo).
- Tip "avoid saying what not to do": the demo's failure is plausible but anecdotal; modern models handle negatives better, and brief prohibitions are fine when paired with the positive instruction.
- Text-classification section says "Neutral" vs "neutral" is a bias issue; it is really a format-specification issue. Fix with an output-format instruction ("Respond with exactly one lowercase word").
- `basics`: playground screenshot/video content not recoverable from text. Page includes marketing components (CoursePromo, promo code) irrelevant to content.
- The stop-sequence example ("11") works only if the list is numbered.
- Summarization example prompt `Explain antibiotics\n\nA:` is QA-style, not summarization; it is an explanation task.
