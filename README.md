[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mokoooo/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mokoooo/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Day — news-image-20261124

One image summing up the world news of **Tuesday 24 November 2026**,
drawn as a one-page newspaper front page.

## What is in the image

- **Lead (Ukraine):** an overnight Russian strike wrecks homes in
  Zaporizhzhia; two people killed, children among the wounded.
- **South Korea:** Seoul scrambles jets as Russian warplanes enter its
  air defence zone near Ulleung Island; a shelter alert is lifted within
  minutes and there is no airspace violation.
- **Bangladesh:** ousted prime minister Sheikh Hasina plans to fly home
  from exile in India on 16 December; she faces a death sentence.
- **Japan (business):** factory activity grows faster in November
  (flash manufacturing PMI 53.7, up from 53.3) on chip demand, while
  services cool.

Every story was reported on 24 November 2026 and was cross-checked
against at least two independent wire reports before it was drawn;
figures the wires disagreed on (the Zaporizhzhia injured count) were
left out.

## How it runs

`main.py` (Python 3, standard library only, no network) copies the
committed `entry.png` asset to the output directory —
`$MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`. Copying is
byte-exact, so two runs produce identical files.

    MAKEFUN_OUTPUT_DIR=out python3 main.py

The image itself (1024×1024 PNG, ~105 KB) was rendered by a scripted
PIL build (`build_entry.py`, kept with the job notes outside this repo)
using flat-shape pictograms and real fonts, then palette-quantised to
stay far below the 1 MiB cap.

## License

MIT — see `LICENSE`.
