# Structured analytic techniques

Techniques from intelligence analysis and forensic science that do the disconfirming work intuition tends to skip. They help choose between hypotheses, test a conclusion before it's relied on, and weigh a single piece of evidence.

## Contents
- Which technique fits
- Analysis of Competing Hypotheses (ACH)
- Key Assumptions Check
- Quality of Information Check
- Indicators and signposts
- Challenge techniques
- Weighing a single item: likelihood ratios and base rates
- Sequencing what you look at (Linear Sequential Unmasking)
- Sources

## Which technique fits

| Situation | Often useful |
| --- | --- |
| Starting a case, or picking up someone else's | Key Assumptions Check; several hypotheses including "someone else / nobody we know of" |
| More than one explanation fits the evidence | ACH |
| A conclusion is about to be relied on | Premortem; the adversarial checklist in `SKILL.md` |
| Everyone, including you or the user, is very sure | Devil's advocacy |
| Two people hold opposing views | Team A/Team B |
| The evidence base is mostly scraped or third-party | Quality of Information Check |
| A subject or infrastructure will be watched over time | Indicators and signposts |
| Reasoning about what the subject "would" do | Red hat |
| One striking match (a face, a handle, a rare string) drives the case | Likelihood ratio and base rate |

## Analysis of Competing Hypotheses (ACH)

Heuer's eight steps:

1. **Identify the plausible hypotheses**, including innocent explanations, deception and "a different actor". Generating them before evaluating any keeps the list from being shaped by the favourite.
2. **List the significant evidence and arguments**, including assumptions and the absence of things you'd expect to see.
3. **Build a matrix**, with hypotheses across and evidence down, marking each cell consistent, inconsistent, or not applicable.
4. **Refine it.** Reword or merge hypotheses, and set aside evidence consistent with every hypothesis, since it can't help choose between them.
5. **Draw tentative conclusions by trying to disprove hypotheses rather than prove them.** The strongest hypothesis is the one with the least evidence against it, not the most evidence for it.
6. **Test sensitivity.** Ask which few items the conclusion depends on, and what changes if one of them is wrong, misleading or planted.
7. **Report all the hypotheses** with their relative likelihood, not just the leader.
8. **Identify signposts**: observations that would shift the ranking later.

What makes it work:

- **Reading across rows.** Comparing one item against all hypotheses at once, rather than one hypothesis against all evidence, shows which evidence actually discriminates between them.
- **Evidence consistent with everything carries little weight.** A shared hosting IP, a common password or a popular forum fits the guilty and the innocent hypothesis alike.
- **A single solid inconsistency can outweigh many consistencies.**
- **Unproven is not disproved.** That applies especially to deception, since an absence of signs of deception is what good deception looks like.

## Key Assumptions Check

Most useful at the start of a case and again before finalising:

1. State the current working conclusion in a sentence.
2. List the premises it depends on, especially the ones that seem too obvious to say. Examples: "the account has one owner", "these timestamps are UTC", "this breach row belongs to this person", "the dump is authentic".
3. For each premise, ask why it's believed, what would make it wrong, whether it has held before, and whether it's supported or just assumed.
4. Treat any unsupported premise the conclusion depends on as an open question or a collection task.

## Quality of Information Check

A source log records what each source is, how and when it was obtained, and its strengths, weaknesses and caveats. Reviewing it from time to time catches what tends to happen over a long case: caveats get forgotten and judgments settle on the weakest item. It also shows when several items repeat one origin and so count once.

## Indicators and signposts

For each live hypothesis, list observable events that would make it more or less likely. Written in advance, they make it harder to reinterpret each new fact to fit the current story.

## Challenge techniques

- **Devil's advocacy.** Build the strongest case against the prevailing view. It is most valuable for conclusions that are costly to get wrong, such as naming a person or making a referral, or for ones that have gone unchallenged for a long time.
- **Team A/Team B.** When two genuine views exist, each side argues from the same evidence and the differences are recorded.
- **Premortem.** Imagine the conclusion was published and proved wrong, then list the likeliest reasons. Each reason is something to check now.
- **What if.** Assume an unlikely event already happened (the account was shared, the dump was fabricated) and work out how. That turns "whether" into "how" and produces specific things to look for.
- **High-impact, low-probability.** For an outcome everyone dismisses but that would matter a lot, sketch how it could happen and what would show it starting.
- **Red hat.** Reason from the subject's position, with their constraints and knowledge rather than yours. Mirror imaging, filling gaps with what you'd do yourself, is a well-documented failure.

## Weighing a single item: likelihood ratios and base rates

Each piece of evidence raises two questions:

- How probable is this finding if the hypothesis is true?
- How probable is it if the alternative is true?

The ratio between the two is its weight. A finding that is nearly as likely under the alternative barely moves anything, however striking it feels. The ratio only means something once the alternative is named.

Related points:

- **Absence counts only where presence was expected.** If a careful guilty subject would also never mention X on their blog, the blog's silence about X has a ratio near 1.
- **Base rates come first.** How common is this kind of match across everyone who could have produced it? Starting from that outside view and then adjusting avoids being anchored by the vivid case.
- **The conditional can't be flipped.** "Only 1 in 10,000 accounts share this trait" is not "a 1 in 10,000 chance it's someone else". In a pool of ten million accounts, about a thousand share it.
- **Searching a large pool for the best match always finds a close one.** A face, handle or fingerprint picked as the closest of millions is expected to look similar by chance. The Mayfield misidentification began with exactly this kind of database search.
- **Updates are usually incremental.** One item rarely justifies a jump from "unlikely" to "confirmed". An inconvenient item still deserves its weight.

## Sequencing what you look at (Linear Sequential Unmasking)

Context changes what examiners see. Forensic science's response:

1. **Examine the raw artefact first.** Look at the log, header, image metadata or breach row and note what it shows before reading the case narrative, the suspect's identity, or anyone's conclusion.
2. **Weigh context before using it.** Ask how biasing, how objective and how relevant it is. Context that is highly biasing and not relevant can be held back.
3. **Bring context in deliberately, and note when.** If a conclusion changes after new context, that change and its cause are worth recording.
4. **Verify blind.** A second examiner who has seen the first conclusion tends to agree with it, so that agreement isn't independent. A verifier given the evidence and the question, without the answer, gives a real second opinion.

The same applies to delegating to a subagent. Selectors and a question produce an independent check; the expected answer produces a confirmation.

## Sources

- Heuer, *Psychology of Intelligence Analysis*, ch. 8 (ACH) and ch. 5, 10 (more information, anchoring): <https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf>
- CIA, *A Tradecraft Primer: Structured Analytic Techniques* (2009): <https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf>
- Dror & Kukucka, Linear Sequential Unmasking–Expanded (2021): <https://pmc.ncbi.nlm.nih.gov/articles/PMC8866671/>
- ENFSI Guideline for Evaluative Reporting (likelihood ratios; written for forensic evaluation, not investigative work): <https://www.forensicinstitute.nl/news/news/2015/05/19/european-guideline-for-evaluative-reporting-in-forensic-science>
- DOJ OIG, review of the FBI's handling of the Mayfield case: <https://oig.justice.gov/reports/review-fbis-handling-brandon-mayfield-case-unclassified-and-redacted>
- Premortem and red hat are described from Heuer & Pherson, *Structured Analytic Techniques*, and Klein; not checked against the book here.
