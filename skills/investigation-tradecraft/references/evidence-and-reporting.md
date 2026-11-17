# Evidence, logging, OpSec and reporting

How investigators collect material so it survives scrutiny, keep notes another person can follow, avoid being seen, and write findings a reader can check.

## Contents
- Capturing material
- Integrity and chain of custody
- Keeping a log
- OpSec and collection posture
- Harmful and illegal content
- Leaked and hacked data
- Data minimisation
- Writing findings
- Referrals, reports and takedowns
- Corrections
- Sources

## Capturing material

The Berkeley Protocol (para 155) describes what a capture of online material ideally records. The first three items are its stated minimum for court use:

1. the target URL;
2. the HTML source;
3. a full-page capture with the date and time visible;
4. embedded media, extracted separately (subject to the harmful-content limits below);
5. embedded metadata, such as uploader id, post or media id, upload time, geotag, hashtags and comments;
6. context, such as surrounding comments and the uploader's name and bio, where relevant;
7. collection data: who collected it, from what network route, under which account if any, and when, from a synced clock;
8. a hash taken at the moment of collection.

Native formats preserve the most, and documenting any conversion avoids later questions. How much of this is worth doing depends on use. A quick screenshot is fine for working notes; material that may be relied on later benefits from the fuller record.

## Integrity and chain of custody

The principles behind ACPO and NIST SP 800-86:

- **Originals stay untouched.** Analysis happens on copies, and additions or corrections go in new files rather than edits to the original.
- **Hashes protect from the moment they're made.** Hashing at collection and re-checking before material leaves the team shows nothing changed in between.
- **Processes are repeatable.** Recording each step (tool, version, parameters) lets an independent party reproduce the result.
- **Custody is documented.** That covers who held the material, when, what was done to it, and where it went.
- **Filenames stay neutral.** Predictable names that describe the content without stating conclusions keep evidence easy to find and hard to attack.

## Keeping a log

A running, timestamped log is what makes an investigation reproducible and its negatives credible. Useful entries capture:
- what was looked at;
- what was done, with which tool and route;
- what came back;
- what was concluded.

Keeping the observation apart from the interpretation helps later readers, including you.

Dead ends deserve as much space as hits:
- queries that returned nothing, with the sanity check that showed they could have found something;
- hypotheses that were dropped, and why;
- things that weren't checked.

Without them, "no evidence of X" can't be said honestly.

Writing down the objective, the questions, and what is known versus assumed before starting a search makes later drift visible.

Logs and drafts may be read by opposing counsel or the subject in litigation, so neutral wording (observations, then labelled inferences, no speculation about people) protects both the case and the people named. See `references/legal-and-ethics.md`.

## OpSec and collection posture

- **Passive collection leaves the least trace.** Contact, follows, friend requests, likes, read and view receipts, profile-visitor lists, and link previews fetched from a target-controlled server can all notify the subject. So can port scans, vulnerability probes, registration flows and password-reset flows. These active steps are decisions for the human.
- **A block aimed at you is a decision point, not a routing problem.** Getting around a login wall, IP ban, geoblock or cease notice can be unauthorised access.
- **Deconfliction.** Another agency or team may already be working the target. That is worth checking before any active step or report.
- **Know how your traffic leaves.** Unless verified, traffic may come from an attributable address. Recon that touches the target's own servers (DNS, WHOIS, page fetches) is usually routed through infrastructure that doesn't point back to the investigator. An agent that can't see or choose its egress is better off saying so, and leaving those requests to the human.
- **Separate identities.** Investigation browsing kept apart from personal accounts, password managers and email avoids cross-contamination. Recording any research account used makes captures interpretable later.
- **Third-party services see what you ask them.** Searches, reverse-image lookups, URL scanners and archive requests reveal your interest, and some services publish submissions. A narrower route is often available for sensitive names and private URLs.
- **Terms of service and law.** Breaching a site's terms carries legal risk. That decision sits with the human.

## Harmful and illegal content

- **Suspected child sexual abuse material is not downloaded, opened, rendered, screenshotted, saved or forwarded.** Rendering a page caches its images, which in some jurisdictions counts as making a copy, so suspected sites call for text-only fetching with media and scripts off. The URL, the time and the surrounding text are what the human needs to report it. Reporting routes include the NCMEC CyberTipline in the US, the IWF in the UK, the hotline in the hosting country, and the platform itself. When it's unclear whether something qualifies, asking is better than opening.
- **Images that may show a child stay out of reverse-image and face-search services, and image searches on offender terms are off the table.**
- **Offender vocabulary is best sourced from the human or vetted LE and NGO references.** Building it by browsing offender spaces is not appropriate.
- **In cases that may involve children or illegal content, media stays unfetched.** Record the URL or filename. The human decides on any specific item, except suspected CSAM, which stays unfetched whoever names it.
- **Graphic material.** A warning and a text description usually serve better than surfacing it directly.

## Leaked and hacked data

- **Authenticity first.** Look for internal consistency, plausible id sequences and timestamps, and sample rows that match known accounts. Recycled combo lists relabelled as new breaches are common.
- **Unknown content.** A dump can hold illegal media even in a case unrelated to children. Attachments and media are best left unopened until the human has decided on legality.
- **Legality varies.** Possessing or using some leaked or hacked data is unlawful in some jurisdictions; that is the human's call.
- **Custody.** A note of how the data arrived (purchased, downloaded from a forum, an unsolicited contribution, a provider lookup) belongs with it.
- **Weight.** Material with custody problems works best as a lead until it is authenticated or independently confirmed. Telling a recipient where a lead originally came from is generally better than hiding it, since they may need to know.

## Data minimisation

Collecting what is relevant to a clear question, and keeping bystanders' personal data out of notes and work product, reduces exposure and disclosure burdens. Minimisation concerns what is stored and shared. It is not a reason to drop a lawful lead on someone whose involvement is the open question. Nor is that principle a licence for bulk collection on everyone who matches a filter. A bulk query is better preceded by a stated purpose, and its output kept to what that purpose needs.

## Writing findings

Habits that make a write-up checkable:

- **Bottom line first**, then the support.
- **Facts, assumptions and judgments kept distinct**, with judgments linked to the assumptions they rest on.
- **A locator for each claim** that a reader can open in one step.
- **Likelihood and confidence in a consistent vocabulary** (`references/confidence-and-sourcing.md`) rather than emotive or hedging words.
- **The strongest alternative**, and why it ranks lower.
- **What would change the judgment.**
- **What wasn't checked**: sources not searched, routes that failed.
- **"First copy found online"** rather than "the first copy". Closed channels may predate it.
- **Authentication and attribution stated separately.** "This capture is genuine" and "this person posted it" are different claims.

## Referrals, reports and takedowns

- **Safeguarding doesn't wait for certainty.** If anything suggests someone is in immediate danger, the human needs to know straight away. Hotline and CyberTipline reports run on reasonable suspicion, and safeguarding facts (what was seen, where, when) can be reported with their uncertainty stated.
- **Order usually matters: preserve, refer, then take down.**
  - An abuse report to a host or registrar can destroy evidence and alert the subject.
  - A preservation step may need to come first. In the US, law enforcement can use 18 U.S.C. §2703(f); private parties usually rely on a litigation-hold or preservation letter, or ask law enforcement.
  - The exceptions are imminent risk and CSAM, where the report goes first. Hotline and CyberTipline reports trigger preservation themselves.
- **Attribution claims in referrals and publications** are usually limited to the best-supported ones, each checkable from the cited evidence. IPs serve as leads for legal process rather than location proof.
- **Claims that can't be traced to an openable source** belong in a clearly marked unverified section of a referral, or are left out. This applies especially to claims inherited from someone else's dossier.
- **Material with custody problems.** It is better to rest claims on the independent source, while disclosing where the lead started.
- **Credentials** (passwords, tokens, hashes) are kept to a minimum in anything that leaves the team.
- **Re-check before sending.** Hashes and live state are worth verifying close to sending.
- **Jurisdiction.** Reports tend to work best where the recipient can act: the hosting country's hotline or regulator as well as the international ones.
- **Keep a record.** Logging each report (date, recipient, URLs, ticket, response) builds the case for escalation. An ignored report supports the next step up, such as host to upstream provider, or registrar to registry.

## Corrections

When a shared finding turns out wrong, a visible correction (the amendment, its date, and the old claim kept as disproved rather than deleted) stops the error circulating in copies. So does telling the people who received the original.

## Sources

- Berkeley Protocol on Digital Open Source Investigations (OHCHR/HRC, 2022): <https://www.ohchr.org/sites/default/files/2024-01/OHCHR_BerkeleyProtocol.pdf>
- ACPO Good Practice Guide for Digital Evidence (four principles; ACPO is now NPCC): <https://www.digital-detective.net/acpo-good-practice-guide-for-digital-evidence/>
- NIST SP 800-86: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf>
- SWGDE position on hash algorithms: <https://www.swgde.org/documents/published-complete-listing/swgde-position-on-the-use-of-md5-and-sha1-hash-algorithms-in-digital-and-multimedia-forensics/>
- Bellingcat/GLAN/JA investigation manual: <https://www.bellingcat.com/app/uploads/2022/12/JA-Manual-for-PUBLICATION.pdf>
- Verification Handbook (EJC): <https://datajournalism.com/read/handbook/verification-1/verifying-user-generated-content/3-verifying-user-generated-content>
- CSAM handling guidance (CEOP): <https://www.ceopeducation.co.uk/professionals/blogs/what-to-do-if-you-come-across-child-sexual-abuse-material/>
- Contemporaneous notes, SANS: <https://www.sans.org/white-papers/39185>
- ISO/IEC 27037 is paywalled and was not read; it is cited only as the standard for identification, collection, acquisition and preservation.
