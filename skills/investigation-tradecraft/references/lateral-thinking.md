# Lateral thinking and creative pivots

Ways investigators find the lead nobody else found: generating more hypotheses, getting unstuck, and pivoting through side channels. Creative work produces leads; verification (the adversarial checklist in `SKILL.md`) decides which of them become findings.

## Contents
- Divergence: generate before you judge
- Insight: where new ideas come from
- Reasoning moves
- Getting unstuck
- Side-channel pivots
- Pitfalls of creativity
- Sources

## Divergence: generate before you judge

Generating and judging work better as separate phases. Judging while generating tends to kill the far-fetched idea that turns out to be right.

- **Structured brainstorming.**
  1. Note the current working theory and set it aside; the CIA Primer identifies a long-held line as the main block to new thinking.
  2. Generate candidate explanations or leads without filtering. "That couldn't happen" is held back until later.
  3. Ask what prompted any odd idea; the answer sometimes exposes a hidden assumption.
  4. Then cluster, merge and rank.

  The obvious ideas tend to come first and the novel ones late, so the useful material is often past the point where the list feels finished.
- **What if.**
  1. State the conventional view.
  2. Assume the unlikely thing already happened.
  3. Pick plausible triggers.
  4. Work backwards: what had to occur at each step?
  5. Find several pathways.
  6. List what would be observable on each, and look for it.

  Example: "Assume the alias belongs to the site's own admin. What traces would exist, and where?"
- **Outside-in.** Describe the problem generically. Then list the outside forces that shape the actor's footprint: platforms and their policies, payment rails, legal regimes, hosting markets, time zones and holidays, language communities. Each force suggests a category of data, and thinking about this early saves recoding later.
- **Starbursting.** Before looking for answers, generate only questions: who, what, where, when, why, how, about every element of the case.
- **Morphological analysis.** Break the problem into independent dimensions and list the possible values of each. For attribution that might be actor type × motive × infrastructure source × timing. Then walk the combinations you had not considered.
- **Red hat.** Reason from the subject's position, with their tools, skills, constraints and fears. Which traces would a competent actor avoid leaving, and which couldn't they avoid? The unavoidable ones are usually where to look.

## Insight: where new ideas come from

Klein's study of 120 insight cases found three paths:

- **Contradiction.** Something does not fit the current story: a timestamp, a language quirk, an account created too early. Each misfit is a candidate for rebuilding the theory rather than noise.
- **Connection or coincidence.** An odd overlap, such as the same typo, the same hosting hour, or the same face in two photos. It's a hypothesis to test rather than a discovery.
- **Creative desperation.** When truly stuck, reversing the assumption you've been unable to drop can open things up.

A running "doesn't fit" list kept alongside the findings is where the next breakthrough often comes from.

## Reasoning moves

- **Abduction with a prediction.** Several explanations usually fit the observed facts. For each, "if X, what else must be true?" points to a second trace worth looking for. A theory is worth the traces it predicts, not the facts it was built to explain.
- **Invert.** Alongside "who did this?", it helps to ask:
  - What would make this impossible for candidate A?
  - What would an unconnected person look like here?
  - How would I fail to find this if it were true?
- **First principles.** An online action leaves an actor, a device, a network location, a time, and an account or payment link. Each can be examined separately, and the least protected is usually the way in.
- **Follow the money, the infrastructure, the time.**
  - Money: payment rails, merchant ids, wallets, donation pages.
  - Infrastructure: registrar, host, certificates, nameservers, analytics ids.
  - Time: posting hours, gaps around holidays, clock skew in logs, first and last appearance.

## Getting unstuck

- **Change the question.** "Who is X?" can become "who benefits?", "who had access?", or "what had to exist before this?"
- **Work backwards from what must exist.** A payment needs a recipient, a domain a registrar, a photo a place, an account a sign-up address.
- **Move to the environment.** Associates, followers, family, employers and other users of the same small platform often have weaker OpSec than the target. Looking at them carries a privacy cost for people who aren't subjects, so collection is best kept to what the question needs.
- **Look at the gaps in the timeline.** Silent periods, the last activity before a deletion, the first appearance of a persona, and the persona that predates the one you know.
- **Who else would know?** Communities, former colleagues, mailing lists, local news, court records, trade registries.
- **Switch modality.**
  - Image to text: OCR, signs, shop names, plug types, licence plates.
  - Time to place: posting hours to time zone.
  - Username to image: reverse-search the avatar, unless it may show a child (that is the human's call).
  - Text to time: archive captures.
- **Change the unit of analysis.** Move from person to account to device to infrastructure to organisation, and back. A dead end at one level is often open at another.
- **Change the source class.** When the open web runs dry, other classes include:
  - Archives
  - Certificate transparency
  - Passive DNS
  - Breach indexes
  - Code hosting
  - Academic, court or company records
  - The platform's own export or API

## Side-channel pivots

Pivots generate leads rather than proof. Those marked **active** can notify the subject or breach terms of service, which makes them decisions for the human.

| Pivot | What it can yield | Caveat |
| --- | --- | --- |
| Fitness and activity apps (Strava and similar) | Routines, frequent locations, movement patterns, linked real names | Default privacy zones hide route ends. GPS and times can be wrong. Kudos and comments alert the user (**active**). Settings change, so archive what you see. Location data has helped people locate and harm others, so proportionality matters |
| Git commit metadata | Author name and email, time zone offset, other identities the person committed under | Noreply addresses are common, and author fields are trivially spoofed |
| Certificate transparency logs | Hostnames, subdomains and sometimes emails tied to a domain, without touching the target | Hostnames are leads, not proof of who operates them |
| Analytics, ad and tag-manager ids, favicon hashes | Other sites run by the same account or built from the same kit | Ids are copied with templates, shared by agencies, and sometimes reused after a sale |
| Posting-time distribution | Likely time zone, work or school pattern, holidays observed | Scheduling tools, shift work, automation and deliberate decoys distort it |
| Image backgrounds and document metadata | Place, device, software, author name, internal paths | Metadata is easily stripped or edited. Media that may be illegal stays unfetched (see `SKILL.md`) |
| Old usernames and cached avatars via archives | Earlier identities, real-name periods before a rename | Archive captures are dated, and a reused handle may belong to someone else |
| Public reviews, wishlists, payment-app feeds, PGP keyservers | Interests, approximate location, contacts, linked emails | Practitioner lore not checked against a primary guide here; platform behaviour changes |
| Registration and password-reset flows | Partial emails or phone numbers on file | **Active.** Can trigger notifications, alerts or account locks, and may breach terms or law |

## Pitfalls of creativity

- **Apophenia.** People see patterns in noise. How many comparable pairs were scanned matters: a match among thousands of candidates is expected by chance (see base rates in `references/analytic-techniques.md`).
- **Overfitting.** A clever theory that explains everything and predicts nothing is suspect. A prediction that could embarrass it, and a test of that prediction, separate insight from storytelling.
- **Elegance is not evidence.** The satisfying story is no more likely than the dull one, and deserves the same testing.
- **Leads, not findings.** Brainstorm output is most useful recorded as leads with the reasoning that produced them, until independent evidence and the adversarial checklist say otherwise.

## Sources

- CIA, *A Tradecraft Primer* (2009): brainstorming, what-if and outside-in steps. <https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf>
- Klein, insight's three paths: <https://www.gary-klein.com/insight>. Secondary summary: <https://fs.blog/2013/09/the-remarkable-ways-we-gain-insights/>
- Bellingcat OSINT toolkit, Strava page: <https://bellingcat.gitbook.io/toolkit/more/all-tools/strava>
- Starbursting, morphological analysis and red hat come from Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis*, described from memory and not checked against the book here. The inversion, first-principles and pivot rows other than Strava are practitioner knowledge without a primary citation.
