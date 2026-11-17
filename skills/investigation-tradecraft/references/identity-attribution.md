# Identity and attribution

What shared identifiers tend to show and not show, and how investigators merge or split identities without losing leads.

## Contents
- Weighing selectors
- Weak source classes
- Merging and splitting clusters
- Shared and rotating identifiers
- Usernames
- Breach and broker data
- IP addresses and geolocation
- Infrastructure signals
- Pivoting
- Sources

## Weighing selectors

No single selector settles identity. Strength comes from several independent signals agreeing. Signals that share an origin don't add up, because they are one signal seen twice. Rough starting points from practice:

| Signal | What it tends to show | Watch for |
| --- | --- | --- |
| Same email on two accounts | The same account holder at the time of use | Services that accept unverified addresses; providers recycling addresses; expired domains re-registered; shared family inboxes |
| Different emails, same unique and complex password | Very probably the same person | A password from a public leak reused by someone else; shared credentials in a household or group |
| Password variants on one base word | A strong hint when the base word is uncommon | Common words and patterns that thousands of people choose independently |
| Different emails, common password | Little | — |
| Same recovery email or phone | A strong link | Placeholder values; a family or shared contact |
| A signature by the same key or wallet over a challenge or dated message | Control of that key at that time | It says nothing about the legal identity behind the key |
| The same public key or wallet address displayed on two profiles | A lead | Anyone can copy a public key or address |
| Self-identification or a cross-link from the account itself | A strong lead | Quoted or borrowed text (see `references/source-reading.md`); trolling and persona-building |
| Same full name | Little on its own | Name collisions are common |
| Same username on another platform | Little on its own | Collisions, squatting, impersonation |
| Writing style | At most a pointer toward a possible sock puppet | Shared community idioms; deliberate imitation |
| Same residential IP with overlapping activity | Probably the same household or network | CGNAT, VPNs, shared Wi-Fi; one household still holds several people |
| Same IP on CGNAT, mobile or VPN ranges, or at different times | Weak | Recycling and shared egress |
| Photo or face match | A lead | Stolen or stock photos. A reverse search for the original source helps, within the image limits in `SKILL.md` |

## Weak source classes

Some sources weaken any signal they carry:

| Source | Why it's weak |
| --- | --- |
| Marketing databases and data brokers | Known to merge different people into one record |
| Combo lists and credential compilations | Unattributed and cross-contaminated |
| Dating and adult sites | Fake profiles are common, sometimes created by the platform |
| Gaming-platform and social media birthdates | Often invented |
| Forum self-statements | Persona-building and trolling are common |
| AI or agent output, including your own | Only as good as the source it can be traced back to |
| Vigilante or "hunter" group dossiers, anonymous tips | Framing, malicious accusation and mistaken identity are common |

## Merging and splitting clusters

Tidy identities are where leads tend to get lost.

- **Shared secrets group accounts.** Reused passwords, recovery addresses, phones and devices all do this. Mapping the whole graph before merging shows where the seams are.
- **Links are pairwise.** Two addresses sharing a password are linked to each other. That doesn't fold them into a third cluster that uses a different password.
- **Neutral names help.** Threat-intel teams keep unattributed activity in uncategorised clusters ("cluster A", Mandiant's UNC groups) and merge only on evidence, because an early merge is hard to undo once reports cite it.
- **Assigning the stray record is a claim.** "Two people account for all of it" holds only if each record is placed on evidence.
- **Merges are decisions.** Noting what joined two clusters, and what would split them, makes it possible to revisit them later.

## Shared and rotating identifiers

IPs, phone numbers, devices and handles change hands. That they *can* change hands doesn't show they *did* by the date that matters. Dismissing a link on reassignment needs evidence of the handover at that time.

A shared identifier works in both directions. If it ties the target to a place or account, it also ties whoever else shares it. Leaning on it one way while waving it off the other is a common inconsistency.

## Usernames

Enumeration tools (sherlock, maigret, WhatsMyName and similar) show that an account with that name exists, not who owns it. Hits are also worth opening by hand: these tools judge by HTTP response, so soft-404 pages, reserved names and login walls produce false positives, and site rules go stale.

Attribution usually comes from something more:
- registration data;
- self-identification;
- an explicit cross-link from a known account;
- a cryptographic proof;
- independent community confirmation.

Short and common handles collide all the time. Distinctive handles still get squatted and impersonated.

## Breach and broker data

- **Know where each row came from.** Recording the provider, the breach and the fields returned keeps that clear.
- **A dump hit is a lead.** It becomes evidence once the specific rows are preserved and checked.
- **One provider's empty result says little.** Another provider or index may have it. A hit you can't reproduce elsewhere is weaker, but still a lead.
- **A breach row describes its dump date.** It may hold junk, typos or someone else's details.

## IP addresses and geolocation

- **Geolocation is approximate.** It is city level at best and occasionally wrong about the country. Vendors publish accuracy radii from a few kilometres to hundreds, and can't see past proxies or VPNs. Default or centroid coordinates have sent harassment to the wrong household.
- **The address type matters.** Residential ranges, datacenters, mobile carriers, universities and corporate NAT all imply different things about who sits behind an address. The ASN usually tells you which you have.
- **An IP points to a subscriber, through legal process, not to a person.** Behind CGNAT even the provider needs the source port and an exact timestamp to identify the subscriber.

## Infrastructure signals

| Signal | Shows | Doesn't show |
| --- | --- | --- |
| Two domains resolve to the same IP | They were hosted on the same address at that time | Same operator. Shared hosting, CDNs and reverse proxies put thousands of unrelated sites on one IP |
| Passive DNS record | That resolution was observed at that time | That it resolves now, or that every resolution was seen |
| Passive DNS absence | Little; sensor coverage is partial | That the domain was never used |
| Same WHOIS registrant details | A strong link if the details are specific and unredacted | Anything when privacy-proxied, a reseller default, or a placeholder |
| Same registrar, same registration day | Weak co-occurrence | Same operator; bulk and promotional registrations cluster by day |
| Same TLS certificate on two hosts | The same certificate holder or platform | Same operator, if it's a shared CDN or multi-domain hosting cert |
| Same analytics, ad or tracking id | Someone with that account installed it | Current control; ids are copied with templates |
| Same SSH host key | The same key material, from one operator or one cloned image | Same operator, if it comes from a provider's base image |
| Same JARM or JA4 fingerprint | The same server software and configuration | Same operator; common stacks share fingerprints, so it narrows rather than links |
| Same favicon hash, template or error page | The same software or kit | Same operator; kits are sold and reused |
| Same self-hosted mail server | A link worth chasing | Same person (resellers run mail for clients) |
| Sinkholed domain | Someone, often a researcher or LE, took it over | Anything about the operator after that date |
| Parked domain | A parking service controls the content | Operator activity |
| Code overlap or similar malware routines | Possible shared lineage | Same actor; code leaks, is sold, shared, or planted |
| Build metadata match (e.g. Rich header) | Same build environment, if consistent with the binary | Same actor; it can be copied, as in Olympic Destroyer |
| Compile times, language strings, working hours | Weak behavioural hints | Origin; all are easy to fake |
| Tool or TTP overlap | Shared tradecraft; stronger than IPs or hashes | Identity; affiliates and tools move between groups |
| Victim or targeting overlap | Consistent interests | Same actor |
| Claimed responsibility or a persona | Someone wants credit | Who did it (the TV5Monde "CyberCaliphate" claim was later attributed to a state group) |

Some ways of reading these signals:

- **Shared IPs.** The neighbour count and the ratio usually say more than the number of bad neighbours. A handful of related names on a small VPS is a lead; thousands of names with three flagged is an ordinary shared host. Pivots through CDN, load-balancer, parking and sinkhole addresses rarely go anywhere. Nameservers, certificates, or DNS history from before a domain moved behind shared infrastructure tend to work better.
- **Cost to change (Bianco's Pyramid of Pain).** Hashes, IPs and domains are cheap for an adversary to change, which makes them useful for scoping but weak for identity. Host and network artefacts, tools and TTPs cost more to change and cluster better.
- **Layers of attribution (Rid & Buchanan).** How it was done, what the operation was, and who did it and why are separate questions. Uncertainty usually grows from the first to the last, and more technical detail doesn't by itself bring more certainty about who.

## Pivoting

- **Start from strong selectors.** Unique emails, keys, wallets, unique passwords and analytics ids generally lead somewhere more reliable than names, common handles or shared IPs.
- **A chain is as strong as its weakest hop.** A pivot through a shared resource (a CDN IP, a bulk registrar, a common password) weakens everything downstream of it. Recording each hop makes that visible.
- **Count independent chains by origin.** Three findings that trace back to one breach row are one chain.
- **Time windows matter.** Domains expire and are re-registered; IPs are reallocated. A passive-DNS first-seen date means activity began no later than that date. It may have begun earlier, and it isn't a registration date.
- **Accounts and people are different things.** Account age, activity hours and creation patterns help spot sock puppets and impersonators before an account's words are attributed to a person.

## Sources

- Rid & Buchanan, "Attributing Cyber Attacks" (2015): <https://ridt.co/d/rid-buchanan-attributing-cyber-attacks.pdf>
- Caltagirone, Pendergast, Betz, *The Diamond Model of Intrusion Analysis* (2013): <https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf>
- Mandiant on uncategorised clusters and merging: <https://cloud.google.com/blog/topics/threat-intelligence/how-mandiant-tracks-uncategorized-threat-actors>, <https://cloud.google.com/blog/topics/threat-intelligence/evolution-of-fin7>
- Bianco, The Pyramid of Pain: <http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
- Unit 42 on passive DNS pivoting: <https://unit42.paloaltonetworks.com/connecting-the-dots-in-cyber-threat-campaigns-part-2-passive-dns/>
- Europol on CGNAT: <https://www.europol.europa.eu/media-press/newsroom/news/are-you-sharing-same-ip-address-criminal-law-enforcement-call-for-end-of-carrier-grade-nat-cgn-to-increase-accountability-online>
- MaxMind on geolocation accuracy: <https://support.maxmind.com/knowledge-base/articles/ip-geolocation-risk-data-maxmind>
- Kaspersky on the Olympic Destroyer false flag: <https://securelist.com/the-devils-in-the-rich-header/84348/>
- The selector table and weak-source table come from working practice, not a published standard. The WHOIS-privacy, bulk-registrar and shared-certificate rows rest on general practice.
