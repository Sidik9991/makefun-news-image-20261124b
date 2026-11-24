// Entry contract for news-image-20261124, "The World in One Day".
//
// This program reproduces the entry image: it reads the entry.png bundled
// beside this file, verifies it, and writes it unchanged to
// $MAKEFUN_OUTPUT_DIR/entry.png (default /output), creating the output
// directory when it is missing. The written file is then re-read and its
// sha256 is compared against the expected digest; the program throws on
// any mismatch and prints the byte count and sha256 on success.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const EXPECTED_SHA256 =
  "318160d56f1e3707a1be15146c35063a15dbc4936ece786183a09e72f17d203e";

function sha256(data: Buffer): string {
  return createHash("sha256").update(data).digest("hex");
}

function main(): void {
  const here = dirname(fileURLToPath(import.meta.url));
  const source = readFileSync(join(here, "entry.png"));

  const PNG_SIGNATURE = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
  const hasSignature =
    source.length >= PNG_SIGNATURE.length &&
    PNG_SIGNATURE.every((byte, i) => source[i] === byte);
  if (!hasSignature) {
    throw new Error("bundled entry.png does not start with the PNG signature");
  }

  const sourceHash = sha256(source);
  if (sourceHash !== EXPECTED_SHA256) {
    throw new Error(
      `bundled entry.png failed verification: sha256 ${sourceHash} ` +
        `does not match expected ${EXPECTED_SHA256}`,
    );
  }

  const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  mkdirSync(outputDir, { recursive: true });
  const target = join(outputDir, "entry.png");
  writeFileSync(target, source);

  const written = readFileSync(target);
  const writtenHash = sha256(written);
  if (writtenHash !== EXPECTED_SHA256) {
    throw new Error(
      `written entry.png failed verification: sha256 ${writtenHash} ` +
        `does not match expected ${EXPECTED_SHA256}`,
    );
  }

  console.log(`entry.png: ${written.length} bytes sha256=${writtenHash}`);
}

main();
