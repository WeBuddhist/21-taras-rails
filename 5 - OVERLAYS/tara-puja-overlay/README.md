# 21 Taras Puja — Overlay System

One operator drives synchronized text overlays for multiple language livestreams. Built for OBS Browser Sources feeding a separate YouTube (and optionally Facebook) stream per language — Tibetan, English, Chinese (Hindi optional).

**Where this lives:** `5 - OVERLAYS/tara-puja-overlay/` in the [`WeBuddhist/21-taras-rails`](https://github.com/WeBuddhist/21-taras-rails) repo.

## Documentation

- **`branch-output-setup-guide.md`** — the full happy-path setup: OBS, Branch Output, YouTube/Facebook broadcasts, going live. Start here to run an event.
- **`branch-output-background-and-troubleshooting.md`** — why the architecture is what it is, approaches ruled out, and a symptom → fix table.
- **`obs/`** — a ready-made OBS setup you can import instead of building scenes by hand: `tara-puja.scene-collection.json` (all scenes + Branch Output filters, keys scrubbed) and a `Profile/` (encoder/output/audio settings). See `obs/README.md`.
- **`architecture-and-websocket-handoff.md`** — the current design and the planned hosted-WebSocket + in-app lyric-scroll feature, for the developer taking it over.

## Get the files

```bash
git clone https://github.com/WeBuddhist/21-taras-rails.git
cd "21-taras-rails/5 - OVERLAYS/tara-puja-overlay"
```

## Run it

```bash
npm install
node server.js
```

Then:

- **Controller** (operator's screen): `http://localhost:8080/controller.html`
- **OBS Browser Sources**, one per stream:
  - `http://localhost:8080/overlay.html?lang=en`
  - `http://localhost:8080/overlay.html?lang=zh`
  - `http://localhost:8080/overlay.html?lang=hi`
  - `http://localhost:8080/overlay.html?lang=bo`

Set each OBS Browser Source to **1920×1080**. The background is transparent, so it sits over the video. Add it as the top layer in each language's scene.

If OBS runs on a different machine than the server, replace `localhost` with the server machine's IP (e.g. `http://192.168.1.20:8080/overlay.html?lang=zh`). For a public/production setup, run this behind the app's infrastructure over `https`/`wss` and the pages connect automatically — see `architecture-and-websocket-handoff.md`.

## What's here

- `server.js` — tiny Node server. Serves the pages and holds the single shared "current position" that the controller sets and every overlay follows.
- `public/content.json` — the puja text. **This is the file you edit.**
- `public/controller.html` — the operator's screen.
- `public/overlay.html` — the OBS browser source (one per language).
- `public/sequence.js` — shared logic (no need to touch).
- `build_content.py` — helper that builds `content.json` from the source.

## Operating during the puja

- **Next / Previous:** buttons, or **→ / Space** and **←** on the keyboard.
- **Round counter:** while in the 21 Taras, the overlay shows "Round N".
- **Repeat the 21:** at the end of Tara 21, click **"↻ Repeat the 21"** in the sidebar (or press **R**). This jumps back to Tara 1 and bumps the round number. Do this as many times as the puja calls for, then hit Next from Tara 21 to move to the Dedication.
- **Jump anywhere:** click any line in the sidebar.

Every language overlay follows the controller instantly — advance once, all streams move together.

## Filling in the content

Open `public/content.json`. The English meaning, the romanized name of each Tara, and the Sanskrit/English names are filled from the source. You may add:

1. **`translit`** — currently the short romanized *name* (e.g. `DROLMA NYURMA PAMO`). Replace with the full 4-line romanized chant to show it.
2. **`uchen`** — Tibetan script. Left blank where it didn't extract cleanly; paste correct Uchen to show script (the overlay hides the line if empty).
3. **`meaning.zh` / `meaning.hi` / `meaning.bo`** — each an empty array `[]`. Fill with translated lines, e.g. `"zh": ["第一行", "第二行", ...]`.
4. **Section titles** — `Refuge`, `Bodhichitta`, `Dedication of Merit`, and the loop title have empty `zh`/`hi`/`bo` — add translations.

Leave any field empty and the overlay omits that line — safe to fill incrementally.

### Adding or removing a language

Overlays render whatever language key you pass in `?lang=`. To add Nepali: add `"ne"` to a verse's `meaning`, then open `overlay.html?lang=ne`. To drop a language, just don't open its overlay.

## Branding

In `public/overlay.html`, top of the file:

- The `:root` CSS variables set colors, panel width, position, and fonts.
- `LOGO_URL` (in the script near the bottom) — point at a logo file dropped in `public/`.

Chinese / Hindi / Tibetan render through Google Noto webfonts loaded in `overlay.html` — the main reason to use a browser source over OBS native text. If the event has its own brand fonts for these scripts, swap the `--cjk` / `--deva` / `--tibetan` variables and load the font files. Always sanity-check stacked Tibetan and conjunct Devanagari on screen before going live.
