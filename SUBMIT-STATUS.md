# SUBMIT STATUS — news-image-20261121

**Status: PREPARED — awaiting Rija's review. DO NOT SUBMIT yet.**
(Rija's 2026-11-21 rule: she reviews every finished entry before submit.)

- **Competition:** news-image-20261121 — "Sum up 21 November's world news in one image"
- **Prize:** $100 total in USDC on Solana (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)
- **Deadline:** Mon 23 Nov 2026 08:00 +08 (2026-11-23T00:00:00Z)
- **Result due:** within ~1 day of the deadline (last similar contest published results ~3.5h after deadline)
- **Entry fee:** none (free)
- **Repo:** https://github.com/Rezzrizz25/makefun-news-image-20261121 (public)
- **Commit:** `c3bd1d477bf5c02231524cff4b081b9caf23b7fb`
- **Entrypoint:** `main.py` (Python 3.13, stdlib only) — copies `entry.png` to `/output/entry.png`
- **Claim file:** `.makefun/owner.json` → wallet `87cXnmH3V6zZPosrtrFVKB7qZyPDw2nAr8teDrbjuP3M` (agent wallet)
- **License:** MIT (first line "MIT License")

## The image

A newspaper front page, "SATURDAY, 21 NOVEMBER 2026", 1024×1024 PNG,
124,113 bytes (cap 1 MiB). Lead story with a night-skyline illustration:
**Russia's massive strike on Ukraine — missiles land in Poland**
(400+ drones, 110 missiles; 8 killed in Kyiv; two missiles + a drone in
Poland; PM Tusk: deliberate provocation). Six more stories: S&P 500 falls
into correction (Nasdaq erases 2026 gains), ICJ Myanmar genocide ruling,
COP31 overtime in Antalya, GTA VI $3.8bn first day, cancer-pill
breakthrough (tumours cleared in 1 in 12 pancreatic patients), Trump's
AI-centre tax threat. Footer: Gen Z protests in 25 European countries,
UK–EU post-Brexit deal, FBI crime-database hack, Bitcoin toward $62,000.

## Local verification (2026-11-21 ~15:39 +08)

- `main.py` run twice (MAKEFUN_OUTPUT_DIR=/tmp/out1 and /tmp/out2):
  byte-identical outputs, sha256
  `be6e0c25715289d19f747564224846f629828db764494229b611affc28bd164c`
- Dimensions 1024×1024, 124,113 bytes ≤ 1,048,576. Stdlib imports only
  (hashlib, os, shutil, struct, sys) — no network at run time.
- Image inspected visually: masthead, lead headline/body, all six cards
  and the footer ticker render cleanly with no clipped or overlapping text.

## Bundle — NOT YET MADE (parent to bundle centrally)

The kit's `bundle` refused to write a bundle from this builder session
alone. Exact refusal:

> makefun bundle: the run record is not whole, so no bundle was written
> (bundle --dry-run prints the record as it stands):
> the prompt: the earliest session,
> sessions/muse-app/78d13ef4-e888-459a-b929-79db800b374c.jsonl, opens with
> no message of the person's in words

This builder session opens with a coordinator hand-off brief, not Rija's
own words, so the run record cannot be completed from this session alone.
The parent session was NOT bundled (it contains live API keys). The parent
agent will attempt bundling centrally after this session completes, when
this session's usage rows exist (Muse writes a subagent's usage row only
once its run completes). Kit check could not run without a bundle.

## What Rija needs to do to submit

1. Review the image: [entry.png](entry.png) in the repo.
2. If approved, the parent agent bundles the transcripts centrally and
   submits via the kit CLI with the agent-wallet keypair
   (`~/.solana/agent-wallet.json`) before Mon 23 Nov 2026 08:00 +08.
   No submit/sign command has been run from this session.
