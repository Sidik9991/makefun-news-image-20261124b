/**
 * Entry contract: the program always writes one file, entry.png, a
 * 1024x1024 PNG byte-identical to the copy bundled in this repository.
 * It never draws, fetches, or transforms anything: the bundled bytes are
 * the entry, and a damaged bundle must fail loudly instead of shipping
 * a corrupt image. Runs twice must produce identical bytes. The image
 * itself is a 1024x1024 PNG drawn in code (PIL) from the verified
 * stories listed in SOURCES.md — no photographs, no truncated summaries.
 */
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const here = fileURLToPath(new URL(".", import.meta.url));
const bundled = join(here, "entry.png");

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

const png = readFileSync(bundled);
// PNG files start with a fixed 8-byte signature; refuse anything else
// before a single byte is written.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!png.subarray(0, 8).equals(PNG_SIGNATURE)) {
  throw new Error("bundled entry.png is not a PNG: refusing to write");
}
if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });
writeFileSync(target, png);

const written = readFileSync(target);
const digest = (b: Buffer) => createHash("sha256").update(b).digest("hex");
if (digest(written) !== digest(png)) {
  throw new Error("entry.png mismatch after copy: aborting");
}
console.log(`wrote ${target}: ${written.length} bytes sha256=${digest(written)}`);
