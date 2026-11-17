# DFIR, timelines, geolocation and chronolocation

How investigators reason about device and log forensics, building timelines, and placing media in space and time. This is method, not a tool manual.

## Contents
- Live systems and order of volatility
- Timestamps
- Building a timeline
- Anti-forensics and missing data
- Geolocation
- Chronolocation
- Sources

## Live systems and order of volatility

- **Every action on a live system changes it.** Running a command writes to memory, logs, shell history and access times. A record of each command (time, tool, version, purpose) is what lets you explain its effect later (ACPO principles 2 and 3).
- **Volatile data goes first.** RFC 3227 gives the order of volatility as: registers and cache; routing table, ARP cache, process table and memory; temporary files; disk; remote logs; physical configuration; archival media.
- **Running commands on a live or compromised host is the human's decision**, including memory capture. The agent's useful role is to propose the order of collection and log each command.
- **Images over live looks, where possible.** Analysis on a hashed copy leaves the original intact. Pulling the plug or rebooting loses memory, which may hold encryption keys, running malware and network connections, so that trade-off is a judgment call for the human.
- **A compromised host's own tools can lie.** Rootkits hide from `ps`, `ls` and `netstat`, which is why known-good binaries or offline analysis are preferred.

## Timestamps

- **One reference zone.** Normalising to UTC while keeping each timestamp's original zone and source avoids timelines that are wrong in ways that look right.
- **Each source's clock means something different:**
  - **EXIF** times usually carry no zone; the camera's clock was whatever someone set it to.
  - **Filesystem times** (modified, accessed, changed, born, the "MACB" times) record different events, behave differently per filesystem and OS, and can be edited.
  - **Email `Date:`** is set by the sender's client. `Received:` headers are set by each relay and are more trustworthy toward the recipient's end.
  - **Platform displays** ("3 days ago", local-time rendering) are relative or viewer-localised. The absolute value, or the capture time and viewer's zone, is what can be relied on.
  - **Logs** may be local time, UTC, or a device clock with drift.
- **Clock skew and DST.** Comparing a device's clock against a trusted reference event reveals drift. Daylight-saving transitions duplicate or delete an hour.
- **Timestamps can be altered** (timestomping, edited EXIF, forged headers). A timestamp a conclusion depends on is stronger with independent corroboration.
- **A first-seen date bounds the start; it does not set it.** Activity began no later than the earliest observation and may have begun earlier.

## Building a timeline

- Useful timeline entries carry the normalised time, the original time and zone, the source and locator, the event, and how confident the time is.
- **Observed and inferred events kept distinct** stops inference from hardening into fact.
- **Gaps matter as much as events.** A silent stretch can mean deletion, a device change, travel, log rotation, or nothing; which of those can be shown is worth stating.
- **Sequence is evidence.** An account created before the persona was "born", a domain registered after the post that links to it, or a file modified before it was downloaded are contradictions worth chasing.
- **Overlap claims** (two accounts active at the same time from the same IP) depend on the window and the clock sources for each side.

## Anti-forensics and missing data

Subjects and intruders remove traces. Absence on a device is weak evidence for the same reason absence on a public profile is (see `SKILL.md`). Things worth looking for:
- cleared logs, and gaps in log sequence numbers;
- timestomping, where filesystem times disagree with each other or with internal metadata;
- secure-delete tools and their own artefacts;
- disappearing messages and auto-delete settings;
- encrypted containers and hidden volumes;
- portable or live-boot operating systems;
- wiped browser history while other artefacts (caches, DNS caches, prefetch, jump lists, thumbnails) survive.

The traces of deletion are often more visible than the deleted thing. They are findings about the device, not proof of what was deleted.

## Geolocation

- **One matching feature is a hypothesis, not a location.** Confidence comes from several independent features (skyline, road layout, signage, terrain, vegetation, shadows, street furniture, power lines), ideally shown side by side with the reference imagery.
- Stating the precision (exact spot, street, town, region) and what would falsify it makes the claim checkable.
- Reference imagery (satellite, street-level) is dated. Its capture date, and what may have changed since, affects the match.
- Image metadata GPS can be absent, stripped, spoofed or wrong. It is a lead to check visually, not a location.
- Images that may show a child stay out of third-party services (see `SKILL.md`).

## Chronolocation

- Shadows give a sun angle, and a sun-position calculator turns that into a time window for a known place and date. It gives a window, not a time.
- Weather history (cloud, rain, snow), visible events (construction stages, shop signage, vehicles, posters) and seasonal vegetation narrow the date range.
- Independent clues combine into a window whose assumptions are worth stating (the place, the direction the camera faces, whether the image is mirrored).
- The upload time bounds the capture time from above, provided it's the real upload time. Some platforms allow backdated posts or display an edit or repost time instead. The earliest copy found gives the tightest bound.

## Sources

- RFC 3227, *Guidelines for Evidence Collection and Archiving*: <https://www.rfc-editor.org/rfc/rfc3227>
- ACPO Good Practice Guide for Digital Evidence: <https://www.digital-detective.net/acpo-good-practice-guide-for-digital-evidence/>
- NIST SP 800-86: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf>
- Berkeley Protocol, verification chapter (geolocation and chronolocation as authentication methods): <https://www.ohchr.org/sites/default/files/2024-01/OHCHR_BerkeleyProtocol.pdf>
- The timestamp, anti-forensics and geolocation points are standard practitioner knowledge, summarised here without a single primary source.
