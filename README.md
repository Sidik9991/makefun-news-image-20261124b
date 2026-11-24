# The World in One Day — Tuesday 24 November 2026

An atlas edition of one day's world news, drawn entirely in code on a
single 1024×1024 page: 36 dated stories from Tuesday 24 November 2026,
grouped into 8 regions — Europe–Ukraine 8, Asia-Pacific 6, Americas 5,
Middle East 5, South Asia 4, Africa 4, Sport 3 and Global 1.

The page leads with the day's biggest stories: Ukraine sinks the Russian
corvette Merkury off Libya, Russia warns Estonia of "open war", 25
seafarers are killed near Hormuz, Iran vows "every means" against the US
blockade, Nvidia reinstates Huang, and Tokyo reopens after the Nikkei's
5.06% plunge.

## What is on the page

- A six-number KPI strip: 25 seafarers killed near Hormuz, 7 naval drones
  sank the Merkury, the Nikkei at −5.06% on Friday, $1.6bn from India to
  Nepal, 24 dead in the Cikande factory fire, and 258 Democrat House
  seats.
- A counted region bar showing how the 36 stories split across the
  8 regions.
- THE DAY IN UTC, a timeline of the day's fixed points, noting that the
  starred times fell on Monday 23 November UTC and rolled into Tuesday
  across Asia-Pacific.
- 15 pictured panels, each drawn in code (no photographs), with a
  headline, a short detail line, the reporting outlet and a certainty
  tag: CONFIRMED, REPORTED or DEVELOPING.
- A 15-pin map, "Where it happened", with the pins numbered to match the
  panels.
- A 21-story digest, "The rest of the day", carrying the stories that did
  not get a panel.
- A DATE CHECK box naming the big stories deliberately left out because
  they belong to other days — the COP31 collapse itself, the Dymer toll,
  the Wellington Test draw, the Alcaraz ATP Finals win and the Nikkei's
  Friday close among them — so that everything on the page is genuinely
  24 November news.

The full numbered source list, with outlets, UTC timings and certainty
tags for all 36 stories plus the exclusions, is in SOURCES.md.

## Reproducing the image

main.ts reproduces and verifies entry.png. It reads the entry.png
bundled beside it, checks the file, creates the output directory if it
is missing, and writes the image to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). It then re-reads the written file and compares its
sha256 against the expected digest
318160d56f1e3707a1be15146c35063a15dbc4936ece786183a09e72f17d203e,
throwing on any mismatch and printing the byte count and sha256 on
success.
