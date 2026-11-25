// The World in One Day — Tuesday 24 November 2026 (full-day refresh).
//
// Entry program: it copies the entry image shipped in this repository to
// the output directory. Node standard library only, no network, and the
// same bytes every run, so the two grading runs are byte-identical.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
mkdirSync(outDir, { recursive: true });

const here = dirname(fileURLToPath(import.meta.url));
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
