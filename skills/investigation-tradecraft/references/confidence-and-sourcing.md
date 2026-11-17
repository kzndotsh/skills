# Confidence, likelihood and source grading

How analysts express how sure they are, how likely something is, and how far a source can be trusted. The value comes from consistency: readers can compare judgments only when the same words mean the same thing across a product.

## Contents
- Likelihood and confidence
- Likelihood vocabularies
- Confidence levels
- Grading identity claims
- Grading sources and information separately
- What a well-formed judgment contains
- Sources

## Likelihood and confidence

They answer different questions:

- **Likelihood**: how probable is the thing? ("very likely the same operator")
- **Confidence**: how good is the basis for that estimate? This covers source quality and quantity, agreement between sources, gaps, and how well the topic is understood.

A claim can be "likely, low confidence", where the evidence is thin but consistent. It can also be "roughly even chance, high confidence", where there is a lot of good evidence that genuinely points both ways. ICD 203 keeps the two in separate sentences, which avoids readers blending them into one vague impression.

## Likelihood vocabularies

ICD 203, the US intelligence community standard:

| Range | Term | Alternate |
| --- | --- | --- |
| 1–5% | almost no chance | remote |
| 5–20% | very unlikely | highly improbable |
| 20–45% | unlikely | improbable |
| 45–55% | roughly even chance | roughly even odds |
| 55–80% | likely | probable |
| 80–95% | very likely | highly probable |
| 95–99% | almost certain | nearly certain |

The UK PHIA yardstick runs: remote, highly unlikely, unlikely, realistic possibility, likely, highly likely, almost certain.

Points that hold whichever scale you use:
- Readers interpret probability words very differently, which is why Kent proposed fixed meanings in the 1960s. A number next to the word ("likely, ~70%") removes the ambiguity where precision matters.
- Mixing term sets in one product invites misreading.
- "May", "might", "could" and "possibly" carry no probability. In a judgment they tend to read as hedging.

## Confidence levels

A common three-level description:

| Level | Typically means |
| --- | --- |
| High | Several independent, good-quality sources agree; few gaps; counter-hypotheses tested and ruled out with evidence. Still not certainty |
| Moderate | Credible sources and plausible reasoning, but limited corroboration or a live alternative |
| Low | Fragmentary, single-source, poorly corroborated, or from sources of doubtful reliability |

A confidence statement is most useful when it says what would raise it ("a registration record for the account would move this to high").

## Grading identity claims

Words alone ("strong link", "likely the same") drift in meaning over a long investigation. A tier scheme with stated requirements keeps identity claims comparable. One workable scheme from practice:

| Tier | Typical basis |
| --- | --- |
| confirmed | Cryptographic proof such as a signed challenge; an official record (registry, court or company filing); a unique-identifier match on the platform itself; or several independent chains that each hold up alone |
| probable | A shared unique secret (password, recovery address) plus corroborating metadata, or two independent chains; in either case with no live counter-hypothesis |
| possible | One strong chain, with counter-hypotheses considered but not eliminated |
| unverified | Circumstantial evidence, a single data point, a common-name match, or AI output nobody has checked |

Whatever scheme you use, some points carry over:
- **Tier names are labels, not probabilities.** "Probable" as a tier and "probable" as an ICD term mean different things; keeping them visibly distinct avoids confusion.
- **Independence is about origin.** Three chains that all start from one breach row are one chain.
- **An official record proves a filing, not control.** Nominee directors and borrowed identities exist.
- **Linking two accounts is not identifying a person.** Grading account-to-account and account-to-person claims separately avoids conflating them. A signature can settle the first. The second needs a record tying the identifier itself to the person, or a verified self-identification; a filing that merely names someone isn't that.

## Grading sources and information separately

The NATO / Admiralty system grades the source and the information on two axes:

| Source reliability | Information credibility |
| --- | --- |
| A Completely reliable | 1 Confirmed by other sources |
| B Usually reliable | 2 Probably true |
| C Fairly reliable | 3 Possibly true |
| D Not usually reliable | 4 Doubtful |
| E Unreliable | 5 Improbable |
| F Reliability cannot be judged | 6 Truth cannot be judged |

The ideas behind it are worth keeping even without the codes:

- **Separate the two.** A reliable source can pass along wrong information, and an unreliable one can be right.
- **Grade the source on track record and access.** Could it actually know this?
- **Grade the information on corroboration and consistency.** Does it fit known facts?
- **"Cannot be judged" is a legitimate grade.** It is more honest than a guess.
- **A good source doesn't make the information corroborated.** Corroboration means an independent source.
- **Grades change.** Re-grade as new corroboration or contradiction arrives.

UK policing uses 3x5x2. Source grades are reliable, untested or not reliable. Information grades are:
- known directly;
- known indirectly but corroborated;
- known indirectly;
- not known;
- suspected false.

Handling codes are added on top. It labels sources and information the opposite way round from Admiralty, so mixing the two systems in one log causes errors. The College of Policing publishes the current wording.

## What a well-formed judgment contains

Analytic standards (ICD 203 in particular) converge on the same elements:

- the claim, in a sentence;
- its likelihood, and a number where useful;
- the confidence, and why;
- the evidence it rests on, with locators;
- the key assumption, especially if the judgment collapses without it;
- the strongest alternative, and why it ranks lower;
- what would change it;
- whether it differs from an earlier assessment, and why.

Not every note needs all of these. Anything a reader will act on usually does.

## Sources

- ICD 203: <https://archive.dni.gov/files/documents/ICD/ICD-203.pdf>
- Kent, "Words of Estimative Probability": <https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf>
- UK PHIA yardstick: <https://www.gov.uk/government/publications/explaining-uncertainty-in-uk-intelligence-assessment/explaining-uncertainty-in-uk-intelligence-assessment>
- Admiralty code as reproduced in the MISP taxonomy: <https://github.com/MISP/misp-taxonomies/tree/main/admiralty-scale> (AJP-2.1 itself is not public)
- The identity tier scheme comes from working practice, not a published standard.
