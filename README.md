[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/muhrevan72-ux/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/muhrevan72-ux/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

# World News in One Image — Thursday 19 November 2026

A newspaper front page that sums up Thursday 19 November 2026 in one
1024×1024 image, for the make.fun bounty
[Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

## What the image shows

- **Lead story:** GTA VI rolls out worldwide — gamers enter Vice City as
  Grand Theft Auto VI begins its global rollout.
- **Geopolitics:** Trump, Xi and Putin to meet in Shenzhen — trilateral
  talks planned at the APEC summit in China.
- **Middle East:** Israeli troops launch a Gaza ground operation —
  troops advance beyond the ceasefire line; aid access urged.
- **Europe:** Crimean Bridge attacked again — traffic halted after a new
  strike. EU proposes a €45bn Ukraine loan.
- **Tech & economy:** Anthropic in a record $81.3bn IPO — the biggest
  stock-market debut ever.
- **Science:** Voyager 1 reaches one light-day — NASA's probe, nearly
  50 years out, hits a new milestone.
- **Culture:** Van Gogh sells for a record $190.4m.
- **Also today:** Cyclone Akvan nears India, Myanmar genocide verdict,
  France protests.

Headlines are the events reported on 19 November 2026, checked against
BBC, The New York Times, Sky News and AP reporting that day. No event
is invented; nothing is shown as fact that was only speculation.

## How it was built

`render.py` draws the image locally with Pillow and DejaVu fonts
(a local build tool only — it is not run by the grader).
`main.py` is the submission program: Python 3.13 standard library
only, no network, deterministic. It copies `entry.png` to
`/output/entry.png`, exactly as the starter entry does.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024×1024 PNG, well under 1 MiB
```

## Test results (local, 19 Nov 2026)

- `python3 main.py` run twice → byte-identical `entry.png`
  (sha256 checked, both runs).
- Image: 1024×1024 PNG, 112 KB (< 1 MiB limit).
- Visually checked: all headlines and summaries legible, no text
  clipped or garbled.

## Licence

MIT — see `LICENSE`.
