# Multi-language puja livestream — OBS setup guide

How to stream the puja to a separate YouTube (and optionally Facebook) broadcast for each language — Tibetan, English, Chinese (and Hindi if added) — all from **one** copy of OBS. One camera, one overlay controller, one operator.

*Part of the `tara-puja-overlay` project in the `21-taras-rails` repo. Companion docs: `README.md` (overview & operating), `branch-output-background-and-troubleshooting.md` (why the architecture is this way + symptom → fix table), `obs/` (import a ready-made OBS setup), `architecture-and-websocket-handoff.md` (the coming in-app scroll feature). You only need this guide to run an event.*

---

## What you need

- **OBS Studio** (Apple Silicon build) with the **Branch Output** plugin installed.
- The **overlay system** — the `tara-puja-overlay` folder from the repo (Node server + controller + per-language overlays).
- The **camera** (Logitech C920) and your **audio source(s)**.
- A **YouTube channel** with live streaming enabled, and **stream keys** (one per language — see Step 6).
- A **wired internet connection** at the venue.
- The event runs on an **M5 MacBook Air (16 GB)**.

> ⚠️ The MacBook Air is fanless. For a multi-hour event, keep it **plugged into power** and **well-ventilated** (hard surface, cool room), and close other apps. The hardware encoder in Step 5 keeps heat low, but don't run it on a bed/couch or let the room get hot.

**Get the files** (first time on a machine):

```bash
git clone https://github.com/WeBuddhist/21-taras-rails.git
cd "21-taras-rails/5 - OVERLAYS/tara-puja-overlay"
npm install
```

**Before you open OBS:** start the overlay server —

```bash
cd "21-taras-rails/5 - OVERLAYS/tara-puja-overlay"
node server.js
```

Leave it running. The controller is at `http://localhost:8080/controller.html`.

> 💡 **Shortcut:** rather than building the scenes by hand (Steps 2–5), you can **import a ready-made OBS scene collection + profile** from `obs/` — see `obs/README.md` — then jump to Step 6. You'll still re-pick the camera and enter fresh stream keys.

---

## Step 1 — Install Branch Output

1. Download the macOS **Apple Silicon (arm64)** package from the [Branch Output plugin page](https://obsproject.com/forum/resources/branch-output-streaming-recording-filter-for-source-scene.1987/).
2. Quit OBS, run the installer, reopen OBS.
3. Open **Docks → Branch Outputs**. This dock starts, stops, and monitors every output. Keep it visible.

## Step 2 — One scene per language, one shared camera

1. Create three scenes: **Tibetan**, **English**, **Chinese** (add **Hindi** if needed).
2. In the Tibetan scene, add **Video Capture Device** → the C920. Name it `Camera-C920`.
3. Right-click `Camera-C920` → **Copy**. In each other scene, right-click Sources → **Paste (Reference)**.

> ⚠️ Use **Paste (Reference)**, not a new Video Capture Device — the camera can only be opened by one source.

## Step 3 — Add the overlays

1. In each scene, add a **Browser Source** as the top layer:
   - Tibetan → `http://localhost:8080/overlay.html?lang=bo`
   - English → `...?lang=en`
   - Chinese → `...?lang=zh` (Hindi → `...?lang=hi`)
2. Set each to **1920×1080**.
3. In each browser source's **Properties**, **uncheck "Shutdown source when not visible."**

> ⚠️ The "Shutdown source when not visible" box must be **unchecked** on every overlay, or the two scenes you're not currently viewing will go black on their streams.

## Step 4 — Route the audio

Each language stream reads its own **audio track**. Set this up in the mixer's **Advanced Audio Properties** (gear icon → Advanced Audio Properties), where each audio source has checkboxes for Tracks 1–6.

| Track | Stream | Chanting phase | Teaching phase |
|-------|--------|----------------|----------------|
| 1 | Tibetan | Tibetan chant | Rinpoche (Tibetan) |
| 2 | English | Tibetan chant | English translator |
| 3 | Chinese | Tibetan chant | Chinese translator |
| 4 | Hindi *(opt.)* | Tibetan chant | Hindi translator |

- **Chanting:** the Tibetan feed goes to every stream — tick it onto Tracks 1, 2, 3 (and 4). Overlays differ so viewers chant along; the audio is the same everywhere.
- **Teaching:** each translator leads its own stream. Bring up the translator on its track; keep the Tibetan feed as a quiet bed underneath, or drop it from tracks 2–4 so only the translator is heard.

> ⚠️ Every stream's audio must come from a track that actually has a source feeding it. If a track is empty, that stream goes out **silent** (audio bitrate 0 on YouTube). During a single-source test, tick your one source onto Tracks 1, 2, and 3.

## Step 5 — Add a Branch Output filter to each scene

Right-click a scene → **Filters** → **+** → **Branch Output**. Configure:

**Streaming** — check it, then:
- **Stream Count:** `1` for one destination (YouTube). Set `2` to also send Facebook (Step 7).
- **Streaming 1 Server / Stream Key:** this language's YouTube URL + key (Step 6). Leave **"Use authentication" unchecked**.

**Custom Audio Source** — check it and select this language's **Audio Track** (Tibetan → Track 1, English → Track 2, Chinese → Track 3).

**Video Encoder:**
- **Video Source:** `Independent Mix (Default)`
- **Video Encoder:** `Apple VT H264 Hardware`
- **Bitrate:** from the bandwidth formula in Step 8.
- **Keyframe Interval:** `2`
- **Resolution / Frame Rate:** 1080p is fine; 720p and/or 30 fps (Frame Rate Divider 1/2) reduce load and bandwidth, and are plenty for a puja.

**Audio Encoder:** AAC, 160 Kbps.

**Advanced Settings:** leave **"Blank output when source is not in Main Output" unchecked**.

Click **Apply**. Repeat for each scene.

> ⚠️ Set **Keyframe Interval to 2 *after* you've selected the Apple VT encoder** — changing the encoder resets it to 0. If you change any encoder setting on a running output, **stop and restart that output** (Branch Outputs dock) so the change takes effect.

## Step 6 — Create a YouTube broadcast + key for each language

Each simultaneous stream needs its **own broadcast with its own distinct stream key**.

1. In YouTube Studio, go to **Content → Live** → **Schedule stream** (or **+ Create**).
2. Title it clearly ("English Puja"), set visibility, set the time to the event.
3. In its **Stream settings**, use the **Key** dropdown to assign a **new, distinct stream key**.
4. Repeat for each language — a separate scheduled broadcast, each with its own key.
5. Put each broadcast's key into the matching scene's Branch Output (Step 5).

> ⚠️ Don't use the instant **"Go Live"** button for this — it only ever runs one broadcast. Create the broadcasts under **Content → Live**, and give each language its **own** key (a shared key collapses them into one stream).

**Ingest URLs:**
- YouTube: `rtmp://a.rtmp.youtube.com/live2`
- Facebook (Step 7): `rtmps://live-api-s.facebook.com:443/rtmp/`

## Step 7 — (Optional) Also stream to Facebook

To send a language to both YouTube and Facebook, set that scene's Branch Output **Stream Count = 2**: Streaming 1 = YouTube, Streaming 2 = Facebook. Both share one encode.

- Get each Facebook key from **Facebook Live Producer → Streaming software**.
- Facebook usually allows **one live video per Page at a time**, so three simultaneous Facebook streams need three separate Pages or events.

## Step 8 — Set the bitrate for your connection

> **per-stream bitrate ≈ (upload speed × 0.7) ÷ number of streams**

Run a speed test at the venue. Example: 30 Mbps upload, three streams → ~7 Mbps each. Six streams (YouTube + Facebook) → ~3.5 Mbps each. Use a **wired** connection.

> ⚠️ If YouTube reports "not receiving enough video" or buffering, your bitrate is above what the connection can carry — lower it. A message that your bitrate is *below* the recommended 6800 is only an FYI and safe to ignore for this content.

## Step 9 — Go live

1. Start `node server.js`, then open OBS.
2. In the **Branch Outputs dock**, start all outputs.
3. In YouTube, open each broadcast from **Content → Live** and confirm it shows **"Excellent."** Click **Go Live** on each.
4. Advance the **controller** — confirm all overlays move together.

**Pre-flight check per stream:**
- ☐ Correct overlay language on screen
- ☐ Audio present (not silent)
- ☐ Stream health "Excellent," no keyframe warning
- ☐ Overlay advances with the controller

> ⚠️ **Quick fixes if a stream looks wrong:**
> - **Silent** → that scene's audio track has no source feeding it (Step 4).
> - **Keyframe warning** → set Keyframe Interval to 2 *after* the encoder, restart the output (Step 5).
> - **Buffering / "not enough video"** → lower the bitrate (Step 8).
> - **Two YouTube streams look like one** → each needs its own distinct key + broadcast (Step 6).
