# The World in One Day — Tuesday 24 November 2026 (full-day refresh)

One image summing up the whole of Tuesday 24 November 2026, after the day
had ended in every time zone: **36 dated stories, 8 regions, 15 pictured
panels, date-checked.**

## What is in the image

- Masthead naming the day: Tuesday 24 November 2026.
- KPI strip: 36 stories, 8 regions, 4 tankers hit in Hormuz, the $41bn
  Sanofi–Insmed deal, TAIEX +8.99%, 5,258 UK heat deaths.
- Counted region bar: Europe 6, Middle East 5, East Asia 3, South Asia 5,
  Africa 3, Americas 4, Markets 4, Global + Sport 6.
- "The Day in UTC" timeline with six verified UTC stamps, from the Gaza
  strikes reported at 00:20 to the Falcon 9 launch at 19:08.
- 15 illustrated panels, drawn in code, each with a headline, a complete
  one-line summary and the reporting outlet. No summary is cut off.
- A numbered pin map (pins 1–15 match the panels).
- "The Rest of the Day": the 19 remaining stories in one line each.
- A DATE CHECK box naming seven stories left out because they happened
  on other days, with their real dates (Nvidia's Huang reinstatement and
  the COP31 collapse among them).

## Files

- `entry.png` — the image (1024×1024, under 1 MiB).
- `main.ts` — Node 22 entrypoint (standard library only, no network);
  it copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
- `SOURCES.md` — every story with its date, time and outlet, plus the
  excluded-stories list and the research method.
- `draw_refresh.py` is not shipped; the image in this repository is the
  entry, and `main.ts` reproduces it byte for byte.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Running it twice produces byte-identical output.
