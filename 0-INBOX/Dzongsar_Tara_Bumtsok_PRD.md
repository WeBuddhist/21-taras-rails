# Product Requirements Document (PRD): Dzongsar Tara Bumtsok (2026) Digital Platform

**Project:** རྫོང་སར་སྒྲོལ་མ་འབུམ་ཚོགས། (2026) | Dzongsar Tara Bumtsok
**Event Duration:** 21 Days
**Core Objective:** Deliver a unified digital platform for a 21-day global event featuring daily Tara initiations (Jenang) by Dzongsar Khyentse Rinpoche, live broadcasts, and synchronized global practice accumulations.

## 1. Global Dashboard (Frontend User Interface)
The homepage serves as the primary hub for practitioners, prioritizing ease of access to the live broadcast and daily progress tracking.

*   **Live Broadcast & Translation Matrix:** The central video player must support a seamless audio-track selector (སྐད་སྒྱུར།), allowing users to toggle between Tibetan, English, Chinese, and other languages without reloading the video feed.
*   **21-Day Interactive Tracker (ཉིན་ཟ།):** A visual grid representing the 21 days.
    *   Future days remain locked/disabled.
    *   The current day is highlighted and routes to the active practice module.
    *   Completed days display a checkmark and remain accessible for archive viewing.
*   **Accumulation Counters (སྒྲོལ་བསྟོད་གྲངས་གསོག།):**
    *   *Global Target Counter:* A real-time aggregate counter tracking the collective goal of 100,000+ recitations.
    *   *Automated Recitation Counter (རང་འགུལ་གྲངས་གསོག):* An automated counter mechanism embedded in the live practice session/viewer that automatically calculates and logs recitations based on continuous session duration and chant loops, requiring minimal to no manual entry by practitioners.

## 2. Daily Practice Modules (Dynamic Content)
Each day requires a dynamically updated page specific to the Tara empowerment being granted.

*   **Daily Introduction:** Displays the name, historical context (ལོ་རྒྱུས་སམ་ངོ་སྤྲོད།), and a high-resolution image (སྐུ་པར།) of the day's specific Tara.
*   **Jenang Context:** Specific empowerment details and source texts, primarily drawn from the *Drubtab Kuntu* (སྒྲུབ་ཐབས་ཀུན་བཏུས).
*   **Commentary Integration:** Embedded 21 Tara Root Text (རྩ་བ) with selected commentary (འགྲེལ་བ) focusing on the specific stanza of the day.

## 3. Resource & Background Library (Static Content)
A permanent reference section for practitioners to access overarching teachings and iconography.

*   **Dharma Cycle Overview:** Foundational information explaining the origins of Tara practices (སྒྲོལ་མའི་ཆོས་སྐོར་སྤྱིའི་ངོ་སྤྲོད།).
*   **Zabtik Drolchok History:** Details on Chokgyur Lingpa's profound essence sadhana and its lineage (ཟབ་ཏིག་སྒྲོལ་ཆོག་གི་བྱུང་རབས་ངོ་སྤྲོད།).
*   **Iconography Gallery:** Comparative visuals featuring the standard Atisha tradition (ཇོ་ལུགས་ཞལ་ཕྱག་གཅིག་པ།) alongside Dzongsar Khyentse Rinpoche’s Indian aesthetic guidelines (རིན་པོ་ཆེའི་རྒྱ་གར་ལུགས།).

## 4. Live Synchronized Text Viewer (The "Karaoke" Feature)
A critical feature to prevent tab-switching or PDF reliance during the live practice. The text viewer will be managed via an Admin-Push architecture.

**User-Facing UI:**
*   **Layout:** Side-by-side on desktop (60% video / 40% text) and stacked on mobile.
*   **Language Toggles:** Checkboxes allowing users to stack Tibetan script, Phonetics/Pinyin, and their chosen translated language.
*   **Display Logic:** The currently chanted stanza is highlighted; surrounding text is dimmed.
*   **Automated Counter Sync (རང་འགུལ་གྲངས་གསོག):** Integrates directly with the text viewer logic, automatically incrementing a user's logged recitations every time the live admin completes a full cycle loop of the 21 Praises text.
*   **Failsafe:** If a user scrolls manually, a "Sync to Live" button appears to snap them back to the Admin's active stanza.

**Required Database Structure (JSON/Document DB):**
All practice texts must be pre-mapped into discrete, stanza-by-stanza objects.

| ID | Tibetan (Pecha) | Phonetics | Translation (Target) |
| :--- | :--- | :--- | :--- |
| `praise_01` | ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། | chak tsal drol ma... | Homage to Tara, the swift... |
| `praise_02` | སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། | chen ni ke chik... | Whose eyes are like a flash... |

## 5. Backend Admin Control Dashboard
The interface used by the event moderator to push live text updates to the global audience. This must be designed for ultra-low latency and minimal cognitive load.

*   **Dual-Panel Layout:**
    *   *Monitor Panel:* Low-latency embedded video/audio feed of the broadcast to ensure the admin hears exactly what the audience hears, plus WebSocket connection health indicators.
    *   *Queue Panel:* A vertical list of the day's stanzas displaying only Tibetan and Phonetics. The active stanza is boxed in green; the upcoming stanza is highlighted in yellow.
*   **Interaction Mechanics:**
    *   *Primary Advance:* Triggered by the Spacebar, Down Arrow, or a large "NEXT STANZA" button.
    *   *Manual Jump:* The admin can click any stanza in the queue to instantly jump the global audience to that point if the chant leader skips a section.
    *   *Quick Revert:* Up Arrow allows the admin to step back one stanza in case of an accidental double-click.
    *   *Loop Completion Trigger:* Admin triggers a "Loop Completed" flag upon finishing a full text iteration, sending an automated count (+1) to all connected clients.
*   **Pre-Broadcast Configuration:** A "Day Selector" dropdown to load the specific Jenang text for that day, and a "Go Live" master toggle to initiate the WebSocket broadcast to the audience.

## 6. Execution Milestones for Department Heads

**Content & Translation Team:**
*   Extract and translate the 21 specific Jenang texts from the *Drubtab Kuntu*.
*   Format all practice materials (Root Text, Zabtik Drolchok, daily Jenangs) into the required stanza-by-stanza database matrix.

**Design & Art Team:**
*   Finalize UI/UX mockups for the split-screen viewer and mobile layouts.
*   Complete the 21 specific Tara digital art assets adhering to the Rinpoche's Indian aesthetic guidelines.

**Engineering Team:**
*   Establish WebSocket (e.g., Socket.io) infrastructure capable of handling high concurrent global connections for the live text sync and automated count events.
*   Implement the automated counter logic (རང་འགུལ་གྲངས་གསོག) synced to live continuous stream duration/admin text loop events.
*   Develop the user-facing customizable text matrix (toggling languages dynamically).
*   Build the Admin Control Dashboard with latency optimization.


# Meeting Notes

**The 11 client requirements provided in the note:**
  
1. **Practice Plan Title (སྒྲུབ་འཆར་མིང):** Dzongsar Tara Bumtsok (2026)
	
2. **Calendar / Schedule (ཉིན་ཟ):** (Separate by day. Archive and store the days that have already passed.)
	
3. **Livestream (ཐད་གཏོང):** + Recitation Texts
	
4. **Tara Praise Recitation Counter (སྒྲོལ་བསྟོད་གྲངས་གསོག):** Automatic Recitation Counter
	
5. **Daily Tara Empowerment / Initiation (ཉིན་རེར་སྒྲོལ་མ་རེའི་རྗེས་གནང):** (The empowerment texts may be located in the _Drubtab Kuntu_.)
	
6. **Translation (སྐད་སྒྱུར):** (Single video stream with audio/language selection options) (Tibetan, English, Chinese, etc.)
	
7. **The Root Text of the 21 Taras (སྒྲོལ་མ་ཉེར་གཅིག་གི་རྩ་བ):** + Commentary
	
8. **History / Introduction for Each Tara (སྒྲོལ་མ་རེ་རེའི་ལོ་རྒྱུས་སམ་ངོ་སྤྲོད):** + Image / Artwork
	
9. **General Introduction to the Tara Dharma Cycle (སྒྲོལ་མའི་ཆོས་སྐོར་སྤྱིའི་ངོ་སྤྲོད)**
    
10. **History / Introduction to the Zabtik Drolchok (ཟབ་ཏིག་སྒྲོལ་ཆོག་གི་བྱུང་རབས་ངོ་སྤྲོད)**
    
11. **Images / Artwork (སྐུ་པར):** Single Face Two Arms Atisha Tradition + Rinpoche’s Indian Tradition