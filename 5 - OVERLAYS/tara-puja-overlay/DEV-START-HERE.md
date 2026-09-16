# Dev — start here

This is the Tara Puja overlay system: one operator advances the puja on a controller, and the position is broadcast over a WebSocket so text overlays stay in sync across multiple language livestreams. We're extending it — read the three docs below in order.

## 1. What we want you to build

**→ `architecture-and-websocket-handoff.md`**

The full brief. Today the WebSocket runs locally; we want it moved to a **hosted service**, and we want the **WeBuddhist app** to subscribe to it too — so in-person attendees can read the liturgy on their phone and have it **auto-scroll** as the operator advances (lyrics-style, like Spotify / YouTube Music). That doc covers the current design, the target design, the message protocol, and the open questions.

## 2. Run it locally (controller + overlays in a browser)

**→ `README.md`**

Clone, `npm install`, `node server.js`. Then open the **controller** and the **overlay** pages in your browser to see the sync working — advance in the controller, watch the overlays follow. This is the fastest way to understand the current behavior before you change it.

## 3. See it in OBS (how it looks on the YouTube stream)

**→ `obs/README.md`**

Import the ready-made OBS scene collection + profile, and you'll see the overlays composited over video exactly as they appear in the livestream — and watch the controller drive them there, the same way it drives the browser overlays. This shows you the production context the overlays live in.

---

You can ignore `branch-output-setup-guide.md` and `branch-output-background-and-troubleshooting.md` — those are operator runbooks for running the livestream, not needed for the WebSocket/app work.
