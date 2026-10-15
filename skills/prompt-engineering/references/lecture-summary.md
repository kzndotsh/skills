# Lecture summary: "Prompt Engineering" by Elvis Saravia / DAIR.AI

Source: lecture/Prompt-Engineering-Lecture-Elvis.pdf (50 slides; text extracted with pypdf since the Read tool's PDF renderer (poppler) was unavailable; diagrams/images on slides 29, 31, 43-46 are not captured). Video: https://youtu.be/dOxUroR57xs (about 1 hour). Companion notebook: `notebooks/pe-lecture.ipynb` (see `notebooks-and-code-recipes.md`). Slides are from early 2023 (model on slide 7: `text-davinci-003`, temperature 0.7, top-p 1).

## Contents
1. Structure and prerequisites
2. Part 1: Intro slides (4-17)
3. Part 2: Advanced techniques (18-32)
4. Part 3: Tools and applications (33-38)
5. Part 4: Safety and future (39-48)
6. Cheat sheet distilled from the slides
7. Audit notes

## 1. Structure
Prereqs: Python, knowledge of language models, basic DL/ML. Objectives: intro to prompt engineering, overview of latest techniques, demos and exercises. Agenda: Intro / Advanced Techniques / Applications and Tools / Conclusion and Future Directions. Demo slides (17, 32, 38) point to the notebook.

## 2. Part 1: Introduction
- **Definition:** prompts = instructions + context passed to an LM; prompt engineering = developing and optimizing prompts to use LMs efficiently. Slide 5 intentionally shows the model "defining" prompt engineering as UX design, illustrating that unguided model answers can miss the intended meaning. Why learn it: research/discovery, testing LLM limits, enabling applications.
- **Elements of a prompt:** Instructions, Context, Input data, Output indicator. Example: "Classify the text into neutral, negative or positive / Text: I think the food was okay. / Sentiment:" (instruction + input + output indicator).
- **Settings:** temperature and top_p control determinism; low for exact answers, high for diverse output.
- **Tasks with example prompts (all verbatim in the notebook):**
  - Summarization: paste text + "Explain the above in one sentence:".
  - QA: "Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer." + Context + Question + "Answer:" (Teplizumab/OKT3 passage, answer "Mice").
  - Classification: "Classify the text into neutral, negative or positive." -> Neutral.
  - Role playing: conversation prefix "The following is a conversation with an AI research assistant. The assistant tone is technical and scientific." with Human/AI turns.
  - Code generation: triple-quoted schema + "Create a MySQL query for all students in the Computer Science Department" -> a subquery SELECT.
  - Reasoning: "The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. Solve by breaking the problem into steps. First, identify the odd numbers, add them, and indicate whether the result is odd or even." -> odd numbers 15,5,13,7,1; sum 41; odd.

## 3. Part 2: Advanced techniques
Listed: few-shot, CoT, self-consistency, knowledge generation, PAL (slides), ReAct.
- **Few-shot:** 4 exemplars of "The odd numbers in this group add up to an even number: ... A: The answer is True/False." then the test group; the slide shows the model answering True (WRONG: the real answer is False since the odd numbers sum to 41). Teaches that few-shot alone fails on arithmetic reasoning.
- **CoT (Wei et al.):** add reasoning in exemplar answers ("Adding all the odd numbers (9, 15, 1) gives 25. The answer is False."). Combine with few-shot; can also be zero-shot.
- **Zero-shot CoT (Kojima et al.):** append "Let's think step by step." Apples example (10 bought, 2+2 given away, 5 bought, 1 eaten = 10): plain prompt answers "11 apples" (wrong), with CoT it reasons to 10 apples (but its trace says "you had 6 apples left... 11 ... 10"). 
- **Self-consistency (Wang et al.):** sample several diverse reasoning paths with few-shot CoT and pick the most common answer; improves arithmetic/commonsense reasoning over greedy decoding. Slide 23 example: "When I was 6 my sister was half my age. Now I'm 70 how old is my sister?" naive answer 35 (wrong); sampled paths converge on 67 (correct). Slide 24 shows the grove-trees/parking-lot/bagels exemplars and three sampled outputs.
- **Generate knowledge prompting (Liu et al.):** step 1 generate knowledge statements from few-shot "Input: ... Knowledge: ..." exemplars (Greece vs Mexico, pebble vs rock; query "Part of golf is trying to get a higher point total than others."); step 2 answer the question with each knowledge piece ("Question: ... Yes or No? Knowledge: ... Explain and Answer:") and pick the highest-confidence prediction. Slide 27 shows Knowledge 1 giving "No" (high confidence, correct) and Knowledge 2 giving "Yes" (low confidence, wrong).
- **PAL (Gao et al.):** LLM reads the problem and writes a program as reasoning; Python interpreter does the computation. Motivation: CoT depends only on generated text.
- **ReAct (Yao et al.):** interleave reasoning traces and task-specific actions; reasoning updates plans and handles exceptions; actions query external sources, giving more reliable factual answers.

## 4. Part 3: Tools and applications
- Tools: platforms/libraries for developing, evaluating, versioning and deploying prompts (pointer to repo tools list; see `resources-catalog.md`).
- Applications: LLMs plus external tools/APIs; data-augmented generation; QA with sources; summarization using sources.
- **LLM + tools** needs: an LLM-powered agent that decides actions, tools to interact with the world (search API, Wolfram, Python REPL, database lookup), and the LLM powering the agent.
- **Data-augmented generation (RAG):** fetch relevant data, augment prompt with it as context; sources: document stores, APIs, databases, user-provided data.

## 5. Part 4: Safety, RLHF, future
- Prompt engineering improves reliability and safety as well as performance; red-teaming finds risky behaviour.
- Prompt injection (hijack output by injecting an untrusted instruction; easy when naively concatenating prompt + user text), prompt leaking (force the model to reveal its own prompt/confidential info), jailbreaking (bypass safety/moderation; models are served static and can have vulnerabilities from training data etc.). Slides 43, 44, 46 are image examples.
- RLHF: collect high-quality prompt datasets, train LLMs to fit human preference; examples Claude, ChatGPT (source "ChatGPT: Optimizing Language Models for Dialogue").
- Future: augmented LMs, emergent abilities, acting/planning with RL, multimodal prompting, graph prompting.
- Closing: first lecture in a series; follow @dair_ai and @omarsar0.

## 6. Cheat sheet distilled from slides
| Need | Do |
|---|---|
| Deterministic/exact answer | low temperature/top_p |
| Format/classification | give instruction + input + output indicator, label set |
| Grounded QA | supply context + "Unsure about answer" abstain option |
| Arithmetic/multi-step | CoT (few-shot with reasoning or "Let's think step by step."), self-consistency, or PAL |
| Commonsense with gaps | generated knowledge |
| Need fresh facts / tools | ReAct, tool use, RAG |
| User text in prompt | assume injection risk |

## 7. Audit notes
- Slide 20 shows a wrong model answer (True) for the few-shot odd-numbers example without flagging it as wrong; the notebook cell has no output saved. Slide 21 then shows the CoT version with the correct "41 ... False".
- Slide 22 shows zero-shot CoT output that is internally inconsistent ("you had 6 apples left... now you had 11 apples... remain with 10") but arrives at the right final answer; the plain answer "11 apples" is wrong.
- Slide 26 Knowledge 2 and slide 27 "low-confidence" label rely on a hand-picked confidence; no explanation of how confidence is scored (paper uses model probabilities).
- Everything is GPT-3 (`text-davinci-003`)-era; modern chat/reasoning models often do CoT by default, and "Let's think step by step" can be redundant or harmful with built-in reasoning models (not in repo).
- Slide 5's first example (model defines prompt engineering as UX/interaction design) is a funny demo of ambiguity, not a recommended definition.
- Slide 6 cites an Anthropic job posting (prompt-engineer role; now dated). PDF text extraction missed images (PAL and ReAct diagrams, injection examples).
