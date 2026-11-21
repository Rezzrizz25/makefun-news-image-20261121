# SUBMIT STATUS — news-image-20261121

**Status: PREPARED — awaiting Rija's review. DO NOT SUBMIT yet.**
(Rija's 2026-11-21 rule: she reviews every finished entry before submit.)

- **Competition:** news-image-20261121 — "Sum up 21 November's world news in one image"
- **Prize:** $100 total in USDC on Solana (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)
- **Deadline:** Mon 23 Nov 2026 08:00 +08 (2026-11-23T00:00:00Z)
- **Result due:** within ~1 day of the deadline (last similar contest published results ~3.5h after deadline)
- **Entry fee:** none (free)
- **Repo:** https://github.com/Rezzrizz25/makefun-news-image-20261121 (public)
- **Code commit (kit-checked):** `18738b6e47cb112bf599649ca62adf4c32814989`
- **Submit candidate:** the latest HEAD (this status file is committed on top of the code commit; submit the latest HEAD)
- **Entrypoint:** `main.py` (Python 3.13, stdlib only) — copies `entry.png` to `/output/entry.png`
- **Claim file:** `.makefun/owner.json` → wallet `87cXnmH3V6zZPosrtrFVKB7qZyPDw2nAr8teDrbjuP3M` (agent wallet)
- **License:** MIT, first line `SPDX-License-Identifier: MIT`

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

## Bundle — MADE centrally by the parent (2026-11-21 ~15:44 +08)

The builder's own `bundle` call was refused (run record not whole: the
builder session opens with a hand-off brief, not Rija's words). The parent
bundled centrally with `--prompt-file` (the watch schedule's configured
prompt) + `--prompt-origin scheduled` + `--prompt-via "makefun-new-bounty-watch cron, every 2h"`
+ `--muse-usage` (usage rows exported from muse.db after the sessions
completed) + `--no-discover --no-family`, using ONLY the builder's and the
LICENSE-fixer's own session files. The parent session was NOT bundled
(it contains live API keys).

- **Bundle:** `transcripts.tar.gz` in this directory — 178,105 bytes,
  sha256 `62322f47995dab7351e0e1741a4d19fe69cef86ae83a8c07a27447e0c41d1c8f`
  (2 sessions: builder 78d13ef4 + LICENSE fixer d5e4aded; 2 usage rows)
- **Leak check:** clean — no `sk-`/`v1-`/token strings (only hit is the
  literal phrase "sk-or-v1-" inside the task-prompt text in the manifest)

## Kit check — 14 passed, 0 failed, 5 skipped (at commit 18738b6)

Run 2026-11-21 ~15:44 +08 with the bundle above. All local checks pass,
including `license_osi`, `thinking_in_window` (all 127 timestamps inside
the 00:00Z opening → deadline window), `thinking_priced` (2 usage rows),
`thinking_reproduces` (88.0% authored), `transcripts_run_record`.
The 5 "at submission" items (repo_public, repo_owner, repo_created_after_open,
commit_in_repo, duplicate_snapshot) are verified by the site at submit time;
the repo is public, was created 07:34Z (after the 00:00Z opening), carries
`.makefun/owner.json` with the agent wallet, and the commit is pushed.

## What Rija needs to do to submit

1. Review the image: [entry.png](entry.png) in the repo.
2. If approved, the parent agent submits via the kit CLI with the
   agent-wallet keypair (`~/.solana/agent-wallet.json`) before
   Mon 23 Nov 2026 08:00 +08. No submit/sign command has been run yet.
