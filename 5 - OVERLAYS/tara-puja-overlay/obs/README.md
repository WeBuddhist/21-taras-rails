# OBS scene collection & profile — import / export

This folder holds a ready-made OBS setup so a new operator can import working scenes and encoder settings instead of building them by hand.

## What's here

- **`tara-puja.scene-collection.json`** — the OBS **scene collection**: all scenes (Tibetan / English / Chinese), their sources (camera + overlay browser sources), and the Branch Output filters. Stream keys have been **blanked** — you re-enter fresh ones per event.
- **`Profile/`** — the OBS **profile**: encoder, output, bitrate, and audio settings (`basic.ini`, `service.json`, `streamEncoder.json`). Contains no keys.

> ⚠️ **Never commit real stream keys.** The keys in this scene collection were removed before committing. If you re-export after an event, scrub them again — an OBS scene collection stores the Branch Output keys, and a profile's `service.json` can store the main-output key. Each event uses fresh keys anyway (setup guide, Step 6).

## Import (new operator)

1. **Scene collection:** OBS menu → **Scene Collection → Import** → choose `tara-puja.scene-collection.json` → then **Scene Collection** and select it.
2. **Profile:** OBS menu → **Profile → Import** → choose the `Profile/` folder here → then **Profile** and select it.
3. Fix the machine-specific bits the export can't carry:
   - Re-select the **camera** in the `Camera-C920` source (device IDs differ per machine).
   - Re-enter each **stream key** in the Branch Output filters, and create the YouTube broadcasts (setup guide, Steps 5–6).
   - Confirm the overlay Browser Sources point at `http://localhost:8080/overlay.html?lang=…` and that "Shutdown source when not visible" is unchecked.
   - Confirm each Branch Output's Video Encoder is **Apple VT H264 Hardware** with **Keyframe Interval 2** (setup guide, Step 5).
4. Follow `../branch-output-setup-guide.md` from Step 6 to go live.

## Export (after you tune a working setup)

1. **Scene collection:** OBS menu → **Scene Collection → Export** → save the `.json` into this folder (overwrite `tara-puja.scene-collection.json`).
2. **Profile:** OBS menu → **Profile → Export** → pick the **active** profile → save the folder here.
3. **Scrub keys** (see the warning above), then commit.

Keeping these current means the next person clones the repo and imports a known-good setup in a couple of minutes.
