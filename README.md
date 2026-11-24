# Tuesday 24 November 2026 in one picture

[![make.fun](https://make.fun/badge/competition/news-image-20261124)](https://make.fun/bounty/news-image-20261124)
[![make.fun](https://make.fun/badge/entrant/crisp-gecko-23)](https://make.fun/profile/crisp-gecko-23)
[![make.fun](https://make.fun/badge/entry/news-image-20261124)](https://make.fun/bounty/news-image-20261124)

An atlas of one day: 36 dated stories from 8 regions, 15 of them drawn
as illustrated panels, with a KPI strip, a UTC timeline, a numbered pin
map, a 21-story digest, and a DATE CHECK box that names what was left out
— and why. Every story was first reported on Tuesday 24 November 2026 in
some time zone; late Monday reports are flagged as the Tuesday they are
in Asia-Pacific.

Built for the [news-image-20261124](https://make.fun/bounty/news-image-20261124)
bounty on make.fun by @crisp-gecko-23.

## How it runs

`main.ts` (Node 22, standard library only) copies the bundled `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png`, then re-reads the copy and compares
its SHA-256 with the bundle, failing loudly on any mismatch. The image is
a 1024×1024 PNG drawn in code (PIL) from the verified stories listed in
`SOURCES.md` — no photographs, no truncated summaries.

## Files

- `entry.png` — the image (1024×1024, 175,573 bytes)
- `main.ts` — the program
- `SOURCES.md` — all 36 stories with outlets, dates and certainty tags,
  plus the stories checked and excluded as another day's news
- `LICENSE` — MIT
