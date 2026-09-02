# The Bot Layer: Programmatic Article Creation & Update on Tibetan Wikipedia (bo.wikipedia.org)

Research date: 2026-07-27. All API behaviour below was **verified empirically against the live bo.wikipedia API**, not just read from docs. Working probe script: `/private/tmp/claude-501/-Users-tashitsering-Desktop-work-Obsidian/73add4a1-148e-4256-9607-eeb709eeb75a/scratchpad/probe.py` (runs clean against `requests` 2.34.2).

---

## 0. Bottom line up front

| Decision | Recommendation |
|---|---|
| Auth | **OAuth 2.0 owner-only consumer** (Bearer token) registered at meta. Fall back to bot password only if you must use pywikibot. |
| Library | **Thin `requests` client you own (~250 LOC)**. mwclient 0.11.0 as a second choice. pywikibot is a poor fit for a self-contained repo *and* cannot do OAuth 2. |
| Bot flag | **Do not need one to start.** bo.wikipedia's "automatic approval" path only covers double-redirect bots. Run unflagged at <1 edit/min, seek consensus at bo Village pump, then meta Steward requests. |
| Biggest hidden risk | Not technical — it's the **March 2026 en.wikipedia LLM content ban** and Tibetan title normalization (tsheg/shad variants create duplicate articles). See §8 and §9. |

---

## 1. Authentication

### 1.1 Current status of `action=login` (confirmed 2026-07)

[API:Login](https://www.mediawiki.org/wiki/API:Login) states verbatim that this action *"should only be used in combination with `Special:BotPasswords`; use for main-account login is **deprecated and may fail without warning**."* Main-account interactive login must use `action=clientlogin`.

Priority order per the official docs:
1. **OAuth owner-only consumer** — "Bots and other non-interactive applications should use owner-only OAuth consumers if available as it is more secure."
2. `action=clientlogin` — interactive apps only.
3. `action=login` + bot password — acceptable fallback.

### 1.2 OAuth 2.0 owner-only consumer (RECOMMENDED)

Source: [OAuth/Owner-only consumers](https://www.mediawiki.org/wiki/OAuth/Owner-only_consumers) — I pulled the raw wikitext; it says *"If you aren't sure which one to use, use OAuth 2."*

**Exact steps:**
1. Log into the bot account (a **separate account** from Tashi's — required by [meta:Bot policy](https://meta.wikimedia.org/wiki/Bot_policy): *"A bot must be run using a separate account from the operator"*).
2. Go to **`https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose/oauth2?wpownerOnly=1`** (on a wiki farm the special page only exists on the central wiki — for Wikimedia that's meta).
3. Tick the owner-only box ("This consumer is for use only by *user*").
4. Select grants (see below).
5. **Record the access token shown on submit** — it starts with `ey…` (a JWT). It is shown once.

Owner-only consumers **do not need to be reviewed or authorised** — no community approval step, no waiting.

**Grants to request** (identifiers from [Special:ListGrants](https://www.mediawiki.org/wiki/Special:ListGrants)):
- `basic` — read, autologin, CAPTCHA-free actions
- `highvolume` — **this is the one that carries the `bot`, `apihighlimits` and `noratelimit` rights**
- `editpage` — edit existing pages (the UPDATE path)
- `createeditmovepage` — create pages (the CREATE path)

> Critical gotcha, straight from the pywikibot source docstring: *"Setting up OAuth or BotPassword login, you have to grant `High-volume (bot) access` to get `bot` right **even if the account is member of the bots group granted by bureaucrats**. Otherwise edits cannot be marked with bot flag."* ([`_basepage.py:1367`](https://raw.githubusercontent.com/wikimedia/pywikibot/master/pywikibot/page/_basepage.py))

**Usage** — add header `Authorization: Bearer <token>`. The docs carry a mandatory warning:

> *"To avoid strict rate limits being imposed by the API gateway or CDN layer, clients that use owner-only tokens to authenticate **must implement support for returning cookies to the server**."*

So: one `requests.Session()` for the whole process lifetime. Never a bare `requests.post()`.

### 1.3 OAuth 1.0a owner-only (only if you use pywikibot)

Register at `Special:OAuthConsumerRegistration/propose` (no `/oauth2`). You get **four** strings: consumer key, consumer secret, access token, access secret. The docs carry a warning box: *"Use of the OAuth 2 version of this protocol might be preferred since it is easier to implement."*

**Pywikibot cannot do OAuth 2.** The owner-only page states flatly: *"As of April 2025, Pywikibot does not implement support for this form of authentication. To use Pywikibot, use OAuth1.0a."* Confirmed by [Manual:Pywikibot/OAuth](https://www.mediawiki.org/wiki/Manual:Pywikibot/OAuth): *"MediaWiki supports OAuth v1.0a and v2.0 as methods of authentication, but Pywikibot only supports v1.0a."*

### 1.4 Bot passwords (fallback)

Created at `https://bo.wikipedia.org/wiki/Special:BotPasswords`. Per [Manual:Bot passwords](https://www.mediawiki.org/wiki/Manual:Bot_passwords):
- Login name becomes `Username@botname`, e.g. `OpenPechaBot@wiki-pipeline`.
- Grants are checkboxes — tick **High-volume (bot) access**, **Edit existing pages**, **Create, edit, and move pages**.
- *"Clients using bot passwords can only access the API, not the normal web interface."*
- *"When the user's real password changes, bot passwords will not work until they're reset."*
- There is an "Allowed IP ranges" field — useful if you pin to a known host.

**Login flow** (two requests, cookies carried by the session):

```python
r = S.get(API, params={"action":"query","meta":"tokens","type":"login","format":"json"})
login_token = r.json()["query"]["tokens"]["logintoken"]
r = S.post(API, data={"action":"login","lgname":"OpenPechaBot@wiki-pipeline",
                      "lgpassword":BOT_PASSWORD,"lgtoken":login_token,"format":"json"})
assert r.json()["login"]["result"] == "Success"
```

---

## 2. Libraries — versions and minimal working examples

### 2.1 Version landscape (verified against PyPI JSON API, 2026-07-27)

| Package | Version | Released | Python | Notes |
|---|---|---|---|---|
| `pywikibot` | **11.6.0** | 2026-07-22 | `>=3.9.0` | deps: `mwparserfromhell>=0.7.2`, `packaging>=25.0`, `requests>=2.32.3`. Console script `pwb`. |
| `mwclient` | **0.11.0** | 2024-08-12 | 3.5–3.12 | Only dep: `requests-oauthlib`. Nearly 2 years without release; Snyk flags it as low-maintenance. |
| `mwparserfromhell` | **0.7.2** | — | `>=3.9` | Needed for the UPDATE path regardless of client choice. |

### 2.2 Option A — raw `requests` (RECOMMENDED for this repo)

A complete, self-contained client. This is the shape I'd ship.

```python
"""bowiki.py — minimal, dependency-light bo.wikipedia client."""
import time
import requests

API = "https://bo.wikipedia.org/w/api.php"

# Required format per https://foundation.wikimedia.org/wiki/Policy:User-Agent_policy
UA = ("OpenPechaWikiBot/0.1 "
      "(https://github.com/OpenPecha/<repo>; openpecha@gmail.com) "
      "python-requests/2.34")


class BoWiki:
    def __init__(self, oauth2_token=None, bot_login=None, bot_password=None):
        self.s = requests.Session()          # cookies MUST persist (CDN rate limiting)
        self.s.headers["User-Agent"] = UA
        if oauth2_token:
            self.s.headers["Authorization"] = f"Bearer {oauth2_token}"
        elif bot_login:
            self._login(bot_login, bot_password)
        self._csrf = None

    # ---------- low level ----------
    def _call(self, method="GET", **params):
        params.setdefault("format", "json")
        params.setdefault("formatversion", "2")
        params.setdefault("errorformat", "plaintext")
        for attempt in range(6):
            if method == "GET":
                r = self.s.get(API, params=params, timeout=30)
            else:
                r = self.s.post(API, data=params, timeout=30)
            r.raise_for_status()
            d = r.json()
            err = d.get("error") or (d.get("errors") or [None])[0]
            if err and err.get("code") == "maxlag":
                # HTTP 200 + Retry-After header. Verified live.
                time.sleep(int(r.headers.get("Retry-After", 5)) + attempt * 5)
                continue
            if err and err.get("code") == "ratelimited":
                time.sleep(60)
                continue
            if err:
                raise RuntimeError(err)
            return d
        raise RuntimeError("maxlag/ratelimit retries exhausted")

    def get(self, **p):
        p.setdefault("maxlag", 5)          # read: maxlag optional but harmless
        return self._call("GET", **p)

    def post(self, **p):
        p.setdefault("maxlag", 5)          # write: ALWAYS maxlag=5
        p.setdefault("assert", "user")     # abort rather than edit as an IP
        return self._call("POST", **p)

    def _login(self, name, password):
        tok = self.get(action="query", meta="tokens",
                       type="login")["query"]["tokens"]["logintoken"]
        d = self._call("POST", action="login", lgname=name,
                       lgpassword=password, lgtoken=tok)
        if d["login"]["result"] != "Success":
            raise RuntimeError(d["login"])

    def csrf(self, force=False):
        if self._csrf is None or force:
            self._csrf = self.get(action="query", meta="tokens",
                                  type="csrf")["query"]["tokens"]["csrftoken"]
        return self._csrf

    # ---------- reads ----------
    def page_state(self, title):
        """Existence + current wikitext + baseline for conflict detection, 1 call."""
        d = self.get(action="query", prop="info|revisions", inprop="url",
                     rvslots="main", rvprop="content|timestamp|ids", rvlimit=1,
                     titles=title, redirects=1)
        q = d["query"]
        page = q["pages"][0]
        if page.get("missing"):
            return {"exists": False, "title": page["title"],
                    "redirected_from": q.get("redirects")}
        rev = page["revisions"][0]
        return {"exists": True, "title": page["title"], "pageid": page["pageid"],
                "revid": rev["revid"], "basetimestamp": rev["timestamp"],
                "wikitext": rev["slots"]["main"]["content"],
                "redirected_from": q.get("redirects"), "url": page["fullurl"]}

    # ---------- writes ----------
    def create(self, title, text, summary, bot=True):
        return self._edit(title=title, text=text, summary=summary,
                          createonly=1, bot=bot)

    def update(self, title, text, summary, basetimestamp, starttimestamp,
               bot=True, minor=False):
        return self._edit(title=title, text=text, summary=summary, nocreate=1,
                          basetimestamp=basetimestamp,
                          starttimestamp=starttimestamp,
                          bot=bot, minor=minor)

    def _edit(self, **kw):
        kw = {k: v for k, v in kw.items() if v not in (False, None)}
        kw["bot"] = 1 if kw.get("bot") else None
        kw = {k: v for k, v in kw.items() if v is not None}
        try:
            return self.post(action="edit", token=self.csrf(), **kw)
        except RuntimeError as e:
            if isinstance(e.args[0], dict) and e.args[0].get("code") == "badtoken":
                return self.post(action="edit", token=self.csrf(force=True), **kw)
            raise
```

Usage:

```python
w = BoWiki(oauth2_token=os.environ["BOWIKI_OAUTH2_TOKEN"])

st = w.page_state("སངས་རྒྱས།")
if not st["exists"]:
    w.create("སངས་རྒྱས།", wikitext,
             "OpenPechaBot: ཐ་སྙད་ཀྱི་རྩོམ་གསར་བཟོ། (Gemini-drafted, human-reviewed)")
else:
    start_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    merged = merge_sections(st["wikitext"], new_material)   # mwparserfromhell
    w.update(st["title"], merged, "OpenPechaBot: འགྲེལ་བཤད་ཀྱི་ལུང་འདྲེན་སྣོན་པ།",
             basetimestamp=st["basetimestamp"], starttimestamp=start_ts)
```

### 2.3 Option B — mwclient 0.11.0

```python
import mwclient

site = mwclient.Site(
    "bo.wikipedia.org",
    path="/w/",
    clients_useragent="OpenPechaWikiBot/0.1 (https://openpecha.org; openpecha@gmail.com)",
    max_lag=5,               # library DEFAULT IS 3 — override it
    force_login=True,        # sends assert=user on every edit
)
site.login("OpenPechaBot@wiki-pipeline", BOT_PASSWORD)
# OAuth 1.0a alternative:
# site = mwclient.Site("bo.wikipedia.org", consumer_token=..., consumer_secret=...,
#                      access_token=..., access_secret=...)
# OAuth 2.0 (not natively supported) — bolt it on via headers:
# site = mwclient.Site("bo.wikipedia.org", custom_headers={"Authorization": f"Bearer {TOK}"})

page = site.pages["སངས་རྒྱས།"]
print(page.exists)                    # bool
text = page.text()                    # '' if missing; slot='main' by default
page.edit(new_text, "summary here", minor=False, bot=True)   # save() is an alias
page.append("\n== new ==\n...", "summary", bot=True)         # -> appendtext
```

Verified from source ([`mwclient/page.py`](https://github.com/mwclient/mwclient/blob/master/mwclient/page.py)):
- `edit(text, summary='', minor=False, bot=True, section=None, **kwargs)` — **`bot=True` is the default**.
- `_edit()` **automatically sets `basetimestamp` and `starttimestamp`** from `self.last_rev_time` / `self.edit_time`. You get edit-conflict protection for free — provided you loaded the page through the same object.
- It retries **once** on `badtoken`.
- `Site.__init__` default `max_lag=3`; `USER_AGENT = 'mwclient/0.11.0 (https://github.com/mwclient/mwclient)'` and `clients_useragent` is prepended to it.
- `pool=<requests.Session>` **silently ignores** `clients_useragent`, `custom_headers`, and all OAuth params. Don't pass both.
- **Not usable for OAuth 2 out of the box** — `consumer_token` maps to `requests_oauthlib.OAuth1`.

### 2.4 Option C — pywikibot 11.6.0

```bash
pip install pywikibot==11.6.0
```

`user-config.py` for bo.wikipedia (repo-local — set `PYWIKIBOT_DIR=$(pwd)/pwb` so nothing lands in `$HOME`):

```python
# pwb/user-config.py
mylang = 'bo'
family = 'wikipedia'                          # 'bo' IS in wikipedia_family.py (verified)
usernames['wikipedia']['bo'] = 'OpenPechaBot'
console_encoding = 'utf-8'
password_file = 'user-password.py'
user_agent_description = 'OpenPechaWikiBot (https://openpecha.org; openpecha@gmail.com)'

put_throttle = 60      # DEFAULT IS 10 — raise to 60 while unflagged (meta bot policy)
maxlag = 5             # already the default
minthrottle = 0.1      # default
maxthrottle = 60       # default
max_retries = 15       # default
```

`pwb/user-password.py`, `chmod 600`:

```python
# bot password
('OpenPechaBot', BotPassword('wiki-pipeline', 'the-generated-secret'))
# or OAuth 1.0a — put this in user-config.py instead:
# authenticate['bo.wikipedia.org'] = (consumer_key, consumer_secret, access_key, access_secret)
```

Script:

```python
import pywikibot

site = pywikibot.Site('bo', 'wikipedia')
site.login()

page = pywikibot.Page(site, 'སངས་རྒྱས།')
print(page.exists())          # True even for redirects
old = page.text               # '' if page does not exist
page.text = new_wikitext
page.save(summary='OpenPechaBot: ...', minor=False, bot=True, watch='nochange')
```

Signature (verified against master, `pywikibot/page/_basepage.py:1343`):
```python
save(summary=None, watch=None, minor=True, bot=True, force=False,
     asynchronous=False, callback=None, apply_cosmetic_changes=None,
     quiet=False, **kwargs)
```
- **`minor=True` is the default.** New encyclopedia articles must pass `minor=False` — a minor-flagged article creation looks like vandalism-evasion to patrollers.
- `botflag` was renamed `bot` in **v9.3**; `bot=None` dropped in **v9.4**.
- Boolean `watch` deprecated v7.0, **desupported v10.0** — pass the string `'nochange'`.
- Global CLI args: `-simulate` (blocks all writes), `-putthrottle:n` / `-pt:n`, `-dir:PATH`, `-config:xyz`, `-lang:bo`, `-family:wikipedia`.
- Env vars: `PYWIKIBOT_DIR` (config dir), `PYWIKIBOT_NO_USER_CONFIG=1|2` (run library-only without a config file; `=2` also suppresses warnings).

**Honest assessment for this project:** pywikibot brings a global config-file model, a 128-module script ecosystem, and an OAuth 2 gap, in exchange for `page.text` and throttling you can write in 20 lines. For a self-contained IATS-deliverable repo, it is net negative. Use it only if you specifically want `pagefromfile.py` (§7).

---

## 3. Existence checks, search, and Wikidata reconciliation

All examples below were executed live against bo.wikipedia; outputs are real.

### 3.1 (a) Does a title exist?

```
GET https://bo.wikipedia.org/w/api.php
  ?action=query&format=json&formatversion=2
  &prop=info&inprop=url|protection
  &titles=སངས་རྒྱས།|ThisPageDoesNotExist12345
  &redirects=1
```

Actual response shape (formatversion=2 → `pages` is a **list**, not a pageid-keyed dict):

```json
{"batchcomplete": true, "query": {"pages": [
  {"ns":0,"title":"ThisPageDoesNotExist12345","missing":true,
   "contentmodel":"wikitext","pagelanguage":"bo","restrictiontypes":["create"],
   "fullurl":"https://bo.wikipedia.org/wiki/ThisPageDoesNotExist12345"},
  {"pageid":7061,"ns":0,"title":"སངས་རྒྱས།","contentmodel":"wikitext",
   "touched":"2026-07-13T20:25:28Z","lastrevid":160074,"length":10414,
   "restrictiontypes":["edit","move"]}
]}}
```

Test is `page.get("missing") is True`. Batch up to 50 titles per call (500 with `apihighlimits`). Add `redirects=1` and read `query.redirects` — a term may already exist behind a redirect.

### 3.2 (b) Full-text search — [API:Search](https://www.mediawiki.org/wiki/API:Search)

```
&action=query&list=search&srsearch=སངས་རྒྱས&srlimit=10
&srprop=size|wordcount|snippet|timestamp&srinfo=totalhits|suggestion&srnamespace=0
```
Live: `totalhits: 2843`. `srwhat` accepts `text` (default), `title`, `nearmatch`. `srlimit` max 500.

`srwhat=nearmatch` is the highest-precision existence probe — returns at most one page:
```json
{"query":{"search":[{"ns":0,"title":"སངས་རྒྱས","pageid":7062,"size":83}]}}
```

**CirrusSearch is installed on bo** (confirmed in `siprop=extensions`), so the full operator set works. Verified live:
- `intitle:སངས་རྒྱས` → 78 hits
- `insource:"Cite book"` → **19 hits across the entire wiki**
- `incategory:ཆ་མི་ཚང་བ` (stub category) → 2023 hits

`action=opensearch&search=<prefix>&limit=10` also works for prefix completion.

### 3.3 (c) Wikidata reconciliation — find the bo article under a different name

Two directions, both verified:

**Concept → bo title:**
```
GET https://www.wikidata.org/w/api.php
  ?action=wbsearchentities&search=སངས་རྒྱས&language=bo&uselang=bo
  &type=item&limit=5&format=json&formatversion=2
```
Live result: `["Q9441","Q7055","Q155656","Q25259","Q2280431"]`. Params: `search`, `language` (both required), `strictlanguage`, `type` (item/property/lexeme/form/sense/entity-schema), `limit` (0–50, default 7), `continue`, `props`.

Then resolve the sitelink:
```
?action=wbgetentities&ids=Q9441&props=sitelinks|labels
&sitefilter=bowiki|enwiki&languages=bo|en&format=json&formatversion=2
```
Live:
```json
{"entities":{"Q9441":{
  "labels":{"en":{"value":"The Buddha"},"bo":{"value":"སྟོན་པ་ཤཱཀྱ་ཐུབ་པ།"}},
  "sitelinks":{"bowiki":{"site":"bowiki","title":"སྟོན་པ་ཤཱཀྱ་ཐུབ་པ་"},
               "enwiki":{"site":"enwiki","title":"The Buddha"}}}}}
```

> **Note the mismatch**: the bo *label* is `སྟོན་པ་ཤཱཀྱ་ཐུབ་པ།` (shad-final) but the bo *article title* is `སྟོན་པ་ཤཱཀྱ་ཐུབ་པ་` (tsheg-final). Never use a Wikidata label as a page title. Always use `sitelinks.bowiki.title`.

**bo title → Q-id** (reverse lookup, for the UPDATE path):
```
?action=wbgetentities&sites=bowiki&titles=སངས་རྒྱས།&props=sitelinks|labels
```
Live: resolves to `Q7055` ("Buddha"), with `sitelinks.enwiki.title = "Buddha (title)"`.

Also worth having: `wbgetentities` with `sites=enwiki&titles=<en article>` to bridge from English scholarship into the bo namespace.

### 3.4 (d) Get current wikitext

Three options, in order of usefulness:

**Best — `prop=revisions` (one call gives you content + the conflict baseline):**
```
&action=query&prop=revisions&titles=སངས་རྒྱས།
&rvslots=main&rvprop=content|timestamp|ids&rvlimit=1&formatversion=2
```
→ `pages[0].revisions[0].slots.main.content`, plus `.revid` and `.timestamp` (the exact value you feed back as `basetimestamp`). **Use this one.**

**`action=parse&prop=wikitext`** works but returns no revision id/timestamp:
```
&action=parse&page=Wikipedia:Bot policy&prop=wikitext&formatversion=2
```

**REST API v1** — cleanest single call, verified live on bo:
```
GET https://bo.wikipedia.org/w/rest.php/v1/page/སངས་རྒྱས།
```
```json
{"id":7061,"key":"སངས་རྒྱས།","title":"སངས་རྒྱས།",
 "latest":{"id":160074,"timestamp":"2026-03-23T10:08:49Z"},
 "content_model":"wikitext",
 "license":{"url":"https://creativecommons.org/licenses/by-sa/4.0/deed.bo", ...},
 "source":"{{Databox}}\n\n'''སངས་རྒྱས'''…"}
```
The matching writes are `POST /w/rest.php/v1/page` (body: `title`, `source`, `comment`, `content_model`, `token`) and `PUT /w/rest.php/v1/page/{title}` (body: `source`, `comment`, `latest.id` for conflict detection, `token`). REST uses **revision-id** conflict detection instead of timestamps, which is cleaner. However REST has **no `bot` flag, no `minor`, no `createonly`/`nocreate`** — so the action API remains the right choice for a bot.

---

## 4. Editing safely — every guard rail, empirically verified

### 4.1 Edit-conflict detection

`basetimestamp` = timestamp of the revision your edit is based on. `starttimestamp` = when you began (guards against the page being *deleted and recreated* under you).

Verified live — sending a stale `basetimestamp`:
```json
{"errors":[{"code":"editconflict","text":"Edit conflict: སངས་རྒྱས།","module":"edit"}]}
```

**Always send both on the UPDATE path.** Without them, a concurrent human edit is silently clobbered. mwclient does this automatically; raw `requests` and pywikibot-with-manual-text do not.

### 4.2 `createonly` / `nocreate`

Verified live:

| Param | Situation | Error code returned |
|---|---|---|
| `createonly=1` | page already exists | `articleexists` — *"The page you tried to create has been created already."* |
| `nocreate=1` | page does not exist | `missingtitle` — *"The page you specified doesn't exist."* |

Use `createonly=1` on the CREATE path and `nocreate=1` on the UPDATE path — **always**, even after an existence check. This closes the TOCTOU window between your check and your write, and it makes an accidental mass-creation bug impossible.

### 4.3 `bot` and `minor` flags

- `bot=1` — hides the edit from default Recent Changes. **Silently ignored** if the account lacks the `bot` right; no error is raised. Verify with `action=query&meta=userinfo&uiprop=groups|rights` before assuming.
- `minor=1` — never for article creation or substantive content addition. Reserve for typo/format-only follow-ups.

### 4.4 `maxlag` — use 5

[Manual:Maxlag parameter](https://www.mediawiki.org/wiki/Manual:Maxlag_parameter): maxlag=5 *"is an appropriate non-aggressive value, set as default value on Pywikibot."*

Verified live (`maxlag=-1` to force it):
```
HTTP/2 200
retry-after: 5
x-database-lag: 0

{"error":{"code":"maxlag","info":"Waiting for 10.192.16.41: 0.10323 seconds lagged.",
          "host":"10.192.16.41","lag":0.10323,"type":"db"}}
```
Note it is **HTTP 200 with an error body**, not a 5xx. `raise_for_status()` will not catch it. Read `Retry-After`, sleep at least that long, back off; never busy-loop.

### 4.5 `assert` / `assertuser` — [API:Assert](https://www.mediawiki.org/wiki/API:Assert)

Send `assert=user` on every write (`assert=bot` once flagged), and `assertuser=OpenPechaBot`. Failure codes: `assertuserfailed`, `assertbotfailed`, `assertnameduserfailed`, `assertanonfailed`. This is what stops a session expiry from turning your run into a burst of IP-attributed edits.

### 4.6 Rate limits on bo.wikipedia

Queried the live wiki (`meta=siteinfo&siprop=usergroups`):

```
*              -> ['edit', 'createpage']
user           -> ['edit', 'createpage']
autoconfirmed  -> ['autoconfirmed']
bot            -> ['noratelimit', 'bot', 'autoconfirmed', 'apihighlimits']
sysop          -> ['noratelimit', 'autoconfirmed', 'apihighlimits']
```

Anonymous `uiprop=ratelimits` returns `{"edit": {"ip": {"hits": 8, "seconds": 60}}}`. WMF defaults per [Manual:$wgRateLimits](https://www.mediawiki.org/wiki/Manual:$wgRateLimits): `ip` 8/60, `newbie` 8/60, `user` 90/60. So an unflagged registered bot account is hard-capped at **90 edits/minute** technically — but see the policy limit below, which is 60× stricter.

The `bot` group carries `noratelimit`. Per [Manual:Rate limits](https://www.mediawiki.org/wiki/Manual:Rate_limits): *"To bypass configured rate limits using the noratelimit right, a bot that uses OAuth must ensure that its OAuth client includes the highvolume grant."*

Hitting a limit yields error code `ratelimited`; back off and retry with increasing delay.

### 4.7 Policy edit throttle (this is the binding constraint, not the technical limit)

[meta:Bot policy § Edit throttle and peak hours](https://meta.wikimedia.org/wiki/Bot_policy), verbatim:

> *"Bots running without a bot flag should edit at intervals of over 1 minute between edits (= less than 1 edit per minute). Once they have been authorised and appropriately flagged, they should operate at an absolute minimum interval of 5 seconds (12 edits per minute). Bots should try to avoid running during the busiest hours… During these hours, they should operate at intervals of 20 seconds (3 edits per minute)."*

So: **unflagged → 60 s between edits. Flagged → 5 s (20 s at peak).** Make this a single config constant.

### 4.8 User-Agent — exact required format

[Wikimedia Foundation User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:User-Agent_policy) template:

```
<client name>/<version> (<contact information>) <library/framework name>/<version> [<library name>/<version> ...]
```

Official example: `CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0`

Contact must be an email address, a website URL, or a wiki username as `(<project>; User:<name>)`. Including the word "bot" helps WMF classify traffic. **Do not** send a browser UA, `curl`, `Python-urllib`, or an empty string — the consequence is *"blocked without notice"*, an HTTP 403, or a generic technical error.

Concrete value for this project:
```
OpenPechaWikiBot/0.1 (https://github.com/OpenPecha/<repo>; openpecha@gmail.com; bo.wikipedia; User:OpenPechaBot) python-requests/2.34
```

### 4.9 API etiquette

[API:Etiquette](https://www.mediawiki.org/wiki/API:Etiquette): *"Making your requests in series rather than in parallel… should result in a safe request rate."* No parallel workers against api.php. Batch with pipes (`titles=A|B|C`, up to 50 / 500 with `apihighlimits`).

### 4.10 Change tags — unavailable on bo

Queried `list=tags&tgprop=name|defined|source|active` on bo: **zero manually-appliable tags** exist (100 tags total, all software-defined). So `tags=llm-assisted` or similar is not possible until a sysop creates one at `Special:Tags`. Given the AI-content climate (§9), **asking bo's two admins to create a local tag like `openpecha-bot` is a cheap, high-value transparency gesture** and would let the community filter/review your edits.

---

## 5. Sandbox and testing

### 5.1 The best tool: `action=parse` as a dry-run renderer (no save, live templates)

This is the single most useful finding for this pipeline. You can render arbitrary generated wikitext against bo.wikipedia's **live** template + Scribunto module set without touching the wiki:

```
POST https://bo.wikipedia.org/w/api.php
  action=parse
  title=ཚོད་ལྟ།                # affects {{PAGENAME}} etc.
  text=<your generated wikitext>
  contentmodel=wikitext
  prop=text|templates|categories|parsewarnings|links|externallinks
  pst=1                        # apply pre-save transform (~~~~, subst:)
  formatversion=2
```

Verified live with `x<ref>{{Cite book|title=…}}</ref>{{Reflist}}{{Stub}}`:
```
templates used: ['དཔེ་པང་།:Reflist', 'དཔེ་པང་།:Cite book', 'དཔེ་པང་།:Stub',
                 'དཔེ་པང་།:ཆ་མི་ཚང་བ', 'Module:Citation/CS1',
                 'Module:Citation/CS1/Configuration', 'Module:Citation/CS1/Whitelist',
                 'Module:Citation/CS1/Utilities', 'Module:Citation/CS1/Date validation',
                 'Module:Citation/CS1/Identifiers', 'Module:Citation/CS1/COinS']
categories: ['ཆ་མི་ཚང་བ']
parsewarnings: []
cite error present: False
```

**Answer to "can bo-specific templates be tested anywhere?" — yes, right here, against the real wiki, with zero edits.** Make this a mandatory CI gate: every Gemini-drafted article must round-trip through `action=parse` and be rejected if `parsewarnings` is non-empty, if the rendered HTML contains `mw-ext-cite-error` / `cs1-visible-error`, or if any element of `templates` is `missing`.

### 5.2 User sandbox

`User:OpenPechaBot/sandbox`, or better, one subpage per term: `User:OpenPechaBot/draft/<term>`. Namespace 2 is fully editable by the bot and is the natural human-review staging area for the semi-automatic workflow. bo's User namespace localizes to `སྤྱོད་མཁན།` but `User:` works as the canonical alias (title normalization is automatic — verified: `Template:Reflist` → `དཔེ་པང་།:Reflist`).

### 5.3 Special:ApiSandbox

Live on bo at `https://bo.wikipedia.org/wiki/Special:ApiSandbox` (301-redirects to the localized `དམིགས་བསལ།:ApiSandbox`). Good for hand-checking a parameter set once; not scriptable.

### 5.4 test.wikipedia.org

Verified: `Template:Reflist`, `Template:Cite book` and `Sandbox` all exist there. Useful for rehearsing the **auth + edit + conflict-handling mechanics** (bot passwords / OAuth work there; you'd register a separate consumer or use the same account). **Not** useful for template fidelity — test.wikipedia has none of bo's localized template names (`དཔེ་པང་།:Databox`) or the bo CS1 configuration. Use `action=parse` on bo for content fidelity, test.wikipedia for plumbing.

### 5.5 Other

- **TemplateSandbox** extension is installed on bo — lets you preview a page with modified template versions.
- pywikibot `-simulate` blocks all writes globally.
- mwclient has no simulate mode — you'd gate it yourself.

---

## 6. Bot approval on bo.wikipedia

### 6.1 What bo has (verified)

- bo.wikipedia adopted the **standard bot policy on 2011-06-17**, with **automatic approval = allowed** and **global bots = allowed** ([meta:Bot policy/Implementation](https://meta.wikimedia.org/wiki/Bot_policy/Implementation)).
- `bo:Wikipedia:Bot policy` exists but its **entire content is `#redirect[[Wikipedia:Community Portal]]`** — there is no local bot request page and no local bot-approval process.
- bo's whole Project namespace is **60 pages**. It includes `Wikipedia:Village pump`, `Wikipedia:Village pump (policy)`, `Wikipedia:Village pump (idea lab)`, `Wikipedia:Village pump (miscellaneous)`, `Wikipedia:Requests for adminship`.
- Wiki scale: **8,072 articles, 22,734 pages, 161,834 edits, 31 active users, 2 admins**, MediaWiki 1.47.0-wmf.12.
- 27 accounts hold `bot` or `sysop`; the bot accounts are legacy interwiki bots (AlleborgoBot, Escarbot, JAnDbot, BodhisattvaBot…). No bureaucrats surfaced — flag grants go through stewards.

### 6.2 The three authorisation routes and which applies

Per [meta:Bot policy](https://meta.wikimedia.org/wiki/Bot_policy):

1. **Global bots** — restricted remit (interwiki, double redirects). Requires a 2-week discussion at Steward requests/Bot status and demonstrated acceptance on 5+ wikis. **Does not cover content creation.**
2. **Automatic approval** — *"the bot must edit regularly without a bot flag for at least a week **or** make 100 edits… **and the bot must only fix double-redirects**."* **Does not apply to this project.**
3. **Community consensus** — *"bots must obtain community approval on the most relevant local discussion page before editing without a bot flag at high speeds or without human supervision. Once there is consensus, a local bureaucrat will add the flag, or a steward may be requested to do so."* ← **This is your route.**

The fallback clause matters: *"If there is no local community and the above does not apply, the bot must operate without a bot flag or not at all."* bo does have an (extremely small) active community, so route 3 is live.

### 6.3 Concrete path

1. Register `User:OpenPechaBot` (or similar), separate from Tashi's account. Create a bot userpage stating: it is a bot, who operates it, what it does, that content is Gemini-drafted and human-reviewed, and how to stop it. Policy: *"operators must be available to answer any comments themselves."*
2. Post a proposal at **`bo:Wikipedia:Village pump (policy)`** — in Tibetan — describing the task, the source corpus (Kangyur/Tengyur + commentaries), the citation model, the human review step, and the edit rate. Wait ≥1 week.
3. Run unflagged at **<1 edit/minute** meanwhile — that's your demonstration corpus.
4. If consensus, request the flag at **[meta:Steward requests/Bot status](https://meta.wikimedia.org/wiki/Steward_requests/Bot_status)**. Instructions: *"DO NOT post your request here without having fulfilled the local policies first, and having waited for at least a week to gauge community opinion."* Template:
```
=== OpenPechaBot@bo.wikipedia ===
{{sr-request
| status  = <!--don't change this line-->
| domain  = bo.wikipedia
| user name = OpenPechaBot
| discussion = <link to the Village pump thread>
}}
(remarks) ~~~~
```

### 6.4 What happens if you never get a flag

Editing without a bot flag is **not** in itself a policy violation for human-paced, human-supervised edits. Concretely:
- Rate limited to 90 edits/60 s technically; policy asks for <1 edit/min.
- No `apihighlimits` (50-title batches instead of 500).
- `bot=1` is silently ignored — every edit appears in Recent Changes and on watchlists.
- On a wiki with 31 active users and 2 admins, that visibility is arguably a **feature**: it means humans see and can revert. Given the AI-content sensitivity (§9), running visibly and slowly is the lower-risk posture regardless of the flag.

---

## 7. Reusable pywikibot built-in scripts

From the [scripts index](https://doc.wikimedia.org/pywikibot/stable/scripts/index.html):

| Script | Relevance |
|---|---|
| **`pagefromfile.py`** | The only real candidate. Batch-creates pages from a delimited text file. |
| `add_text.py` | Append/prepend a fixed block to pages. Too blunt for section-level merges. |
| `replace.py` | Regex find/replace across pages. Could apply category or template fixes post-hoc. |
| `touch.py` | Null edits to refresh cached template output. Occasionally useful after template changes. |
| `category.py` | Bulk add/change/remove category tags. Plausible for maintenance categories. |
| `template.py` | Template A → template B migration. Not needed. |
| `harvest_template.py` / `claimit.py` | Populate **Wikidata** claims from article templates / categories. Interesting *later* if you want the terms to gain Wikidata items — out of scope for v1. |
| `weblinkchecker.py` | Dead-link checking. Not applicable (citations are to texts, not URLs). |

**`pagefromfile.py` format** ([manual](https://www.mediawiki.org/wiki/Manual:Pywikibot/pagefromfile.py)):
```
{{-start-}}
'''Page Title'''
…wikitext…
{{-stop-}}
```
Options: `-file:xxx` (default `dict.txt`), `-notitle`, `-title:xxx`, `-titlestart:` / `-titleend:`, `-force` (overwrite existing), `-appendtop` / `-appendbottom`, `-summary:xxx`, `-minor`, `-autosummary`, `-showdiff` (diff + confirm per page), `-nocontent:xxx` (skip pages containing text), `-noredirect`, `-include`, `-textonly`.

**Verdict:** `pagefromfile.py -showdiff -summary:… -pt:60` is a legitimate, low-effort MVP for the CREATE path — the `{{-start-}}` format is trivially emitted from your pipeline and `-showdiff` gives per-page human approval. But it has **no `createonly`**, no per-page edit summaries, no Wikidata reconciliation, and `-appendbottom` is a crude approximation of the UPDATE path. Fine for a demo; not the architecture.

---

## 8. bo.wikipedia field notes (empirical — these will bite you)

### 8.1 Tibetan title normalization is a real duplicate-generator

There are **three distinct pages** for the term *sangs rgyas* on bo.wikipedia right now:

| pageid | title | codepoints | type | length |
|---|---|---|---|---|
| 7060 | `སངས་རྒྱས་` | ends U+0F0B **tsheg** | article | 3,981 |
| 7061 | `སངས་རྒྱས།` | ends U+0F0D **shad** | article | 10,414 |
| 7062 | `སངས་རྒྱས` | bare | redirect → `སངས་རྒྱས། (གོ་ལོག་སེལ་བ།)` | 83 |

And the redirect target **does not exist** (`missing: true` — a broken redirect). MediaWiki treats these as three unrelated titles. If your pipeline checks only one form, it will create a fourth.

Minimum viable normalization: strip trailing `U+0F0B` (tsheg), `U+0F0D` (shad), `U+0F0E` (double shad), and whitespace; probe all variants in a single batched `prop=info` call with `redirects=1`; treat *any* hit as "exists"; and follow broken redirects manually.

### 8.2 Namespace localization

| ns | local name | canonical |
|---|---|---|
| 2 | `སྤྱོད་མཁན།` | `User` |
| 3 | `སྤྱོད་མཁན་གྱི་ བགྲོ་གླེང་།` | `User talk` |
| 4 | `Wikipedia` | `Project` |
| 10 | `དཔེ་པང་།` | `Template` |
| 14 | `རིགས་དབྱེ།` | `Category` |
| 828 | `Module` | `Module` |

Canonical English prefixes work as input (the API normalizes `Template:Reflist` → `དཔེ་པང་།:Reflist`), but **responses come back localized** — string-compare on the returned title, not on what you sent.

### 8.3 Citation infrastructure that actually exists on bo

Verified present: `Template:Reflist` (3080), `Template:Cite web` (21165), `Template:Cite book` (24090), `Template:Cite journal` (25566), `Template:Databox` (27273), `Template:Infobox` (22525), `Template:Stub` (2827), and the full `Module:Citation/CS1` Lua suite. **`Template:Citation` does NOT exist.** Extensions include `Cite`, `Scribunto`, `CirrusSearch`, `TemplateStyles`, `TemplateData`, `TemplateWizard`, `VisualEditor`, `WikibaseClient`.

But: **`insource:"Cite book"` returns only 19 articles wiki-wide.** Structured citation is essentially unpracticed on bo.wikipedia. A pipeline that emits well-formed `{{Cite book}}` for every statement will be, by a wide margin, the most heavily cited content on the wiki. That's the project's strongest selling point in the Village pump proposal — and also means you should not assume any local citation convention exists to conform to. Consider proposing a purpose-built `{{Cite Kangyur}}` / `{{Cite Tengyur}}` template with Derge/Toh numbers rather than forcing Kangyur folios into CS1's book fields.

Reference markers render in **Tibetan numerals** (`[༡]`) — expected, but worth knowing when diffing rendered output.

---

## 9. Governance risk you must plan around

On **20 March 2026**, English Wikipedia closed an RfC adopting [WP:LLM](https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models) as a **content guideline**. Its wikitext reads: *"the use of LLMs to generate or rewrite article content is prohibited,"* with narrow exceptions for copyediting one's own writing and first-pass translation. A companion guideline, "Presumptive removal of AI-generated content," was last updated 22 July 2026 and includes an `LLMPROD` deletion process (5-day tag → admin deletion) for pages where the AI-using editor is the sole significant contributor. Coverage: [TechCrunch, 26 Mar 2026](https://techcrunch.com/2026/03/26/wikipedia-cracks-down-on-the-use-of-ai-in-article-writing/).

**This is English Wikipedia policy and is not binding on bo.wikipedia.** I searched bo's Project namespace (all 60 pages) — there is no AI/LLM content policy there, and no equivalent global policy on meta. But small wikis routinely import en's norms, and a visible, unannounced LLM-drafting bot is exactly the trigger for that import.

Mitigations that are cheap now and expensive later:
- Lead the Village pump proposal with the LLM disclosure, in Tibetan, before anyone discovers it.
- Human sign-off recorded per article, with the reviewer's wiki username in the edit summary.
- Every statement carries a citation to a specific Kangyur/Tengyur/commentary locus — which is precisely the gap WP:LLM exists to close (unverifiable AI text). Lean on this.
- Bot userpage states the model, the prompt regime, and the review process.
- Ask for a local change tag so the community can audit the corpus in one click.

---

## Implementation implications

- **Auth: register an OAuth 2.0 owner-only consumer at `meta:Special:OAuthConsumerRegistration/propose/oauth2?wpownerOnly=1` with grants `basic`, `highvolume`, `editpage`, `createeditmovepage`.** Store the `ey…` token in `BOWIKI_OAUTH2_TOKEN` (env / `.env`, gitignored). This choice forecloses pywikibot — accept that consciously.
- **Do not use pywikibot.** It cannot do OAuth 2, its config lives outside the repo by default, its `save()` defaults to `minor=True`, and it buys ~20 lines of throttling. If a reviewer insists on it, the repo needs `PYWIKIBOT_DIR=./pwb`, OAuth 1.0a credentials, `put_throttle=60`, and every `save()` must pass `minor=False, bot=True, watch='nochange'`.
- **Ship a single `bowiki.py` module wrapping one `requests.Session`.** Session reuse is mandatory (CDN cookie requirement for owner-only tokens), not stylistic. Same session for reads and writes.
- **Hardcode the User-Agent as a module constant** in the exact WMF format, including a repo URL and `openpecha@gmail.com`. Never allow it to be unset.
- **Every write carries `maxlag=5`, `assert=user`, `assertuser=<botname>`, and a CSRF token with one `badtoken` refresh-and-retry.** Handle `maxlag` as HTTP 200 + error body + `Retry-After` — `raise_for_status()` will not catch it.
- **CREATE always sends `createonly=1`; UPDATE always sends `nocreate=1` + `basetimestamp` + `starttimestamp`.** Treat `articleexists` as "switch to update path", `missingtitle` as "switch to create path", `editconflict` as "re-fetch, re-merge, retry once, then queue for human".
- **Make the edit interval a single config constant defaulting to 60 seconds**, with a `--flagged` switch dropping it to 5 s (20 s during UTC peak). This is the meta bot policy limit, and it is 60× stricter than the technical rate limit — design the run loop around it (a 200-term batch is a 3.5-hour run, not a 3-minute one).
- **Title resolution is a first-class pipeline stage, not a helper.** Given a Tibetan term, generate {bare, +tsheg U+0F0B, +shad U+0F0D} variants, batch-probe them with `prop=info&redirects=1`, *and* reconcile via Wikidata (`wbsearchentities` → `wbgetentities` → `sitelinks.bowiki.title`). Use `sitelinks.bowiki.title`, never the bo *label*. Persist the resolved `(term → Q-id, bo title, pageid)` mapping to a ledger so runs are idempotent.
- **Also probe `srwhat=nearmatch` and `intitle:` search** before deciding "no article exists" — bo has near-duplicate titles that exact-title lookup misses entirely.
- **Fetch page state with one `prop=info|revisions&rvslots=main&rvprop=content|timestamp|ids` call** so content and the conflict baseline arrive together. Do not use `action=parse&prop=wikitext` (no revid/timestamp).
- **Add a mandatory pre-publish validation gate using `action=parse` with `text=` + `pst=1` against live bo.** Reject the draft if `parsewarnings` is non-empty, if rendered HTML contains `mw-ext-cite-error` or `cs1-visible-error`, or if any returned template is missing. This is the only way to catch bo-specific template breakage without editing.
- **Design the citation layer around `{{Cite book}}` / `{{Cite journal}}` + `<ref>` + `{{Reflist}}` — `{{Citation}}` does not exist on bo.** Since only 19 articles wiki-wide use structured citations, seriously consider proposing a dedicated `{{Cite Kangyur}}` / `{{Cite Tengyur}}` template (Toh/Derge number, volume, folio, line) rather than mangling CS1 fields.
- **Build a `User:OpenPechaBot/draft/<term>` staging namespace into the workflow** as the human-review checkpoint, with promotion to mainspace as a separate, explicitly-approved step. This is what makes "semi-automatic" real rather than nominal.
- **Plan for no bot flag at launch.** bo's automatic-approval route only covers double-redirect bots and its local bot policy page is a redirect. Budget for: a Tibetan-language proposal at `bo:Wikipedia:Village pump (policy)`, ≥1 week of unflagged demonstration edits at <1/min, then a `{{sr-request}}` at meta Steward requests/Bot status. Encode this timeline against the Aug 2026 IATS date — the flag is not on the critical path, but community goodwill is.
- **Front-load the LLM disclosure.** en.wikipedia banned LLM-generated article content in March 2026; bo has no such policy yet. Disclose the model, the review process, and the citation guarantee on the bot userpage and in the Village pump proposal, and request a local change tag from bo's two admins so the community can audit every edit the pipeline makes.

---

**Sources:** [API:Login](https://www.mediawiki.org/wiki/API:Login) · [API:Edit](https://www.mediawiki.org/wiki/API:Edit) · [API:Search](https://www.mediawiki.org/wiki/API:Search) · [API:Info](https://www.mediawiki.org/wiki/API:Info) · [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens) · [API:Assert](https://www.mediawiki.org/wiki/API:Assert) · [API:Etiquette](https://www.mediawiki.org/wiki/API:Etiquette) · [API:REST_API/Reference](https://www.mediawiki.org/wiki/API:REST_API/Reference) · [OAuth/Owner-only consumers](https://www.mediawiki.org/wiki/OAuth/Owner-only_consumers) · [OAuth/For Developers](https://www.mediawiki.org/wiki/OAuth/For_Developers) · [Special:ListGrants](https://www.mediawiki.org/wiki/Special:ListGrants) · [Manual:Bot passwords](https://www.mediawiki.org/wiki/Manual:Bot_passwords) · [Manual:Maxlag parameter](https://www.mediawiki.org/wiki/Manual:Maxlag_parameter) · [Manual:Rate limits](https://www.mediawiki.org/wiki/Manual:Rate_limits) · [Manual:$wgRateLimits](https://www.mediawiki.org/wiki/Manual:$wgRateLimits) · [Manual:Pywikibot/user-config.py](https://www.mediawiki.org/wiki/Manual:Pywikibot/user-config.py) · [Manual:Pywikibot/OAuth](https://www.mediawiki.org/wiki/Manual:Pywikibot/OAuth) · [Manual:Pywikibot/BotPasswords](https://www.mediawiki.org/wiki/Manual:Pywikibot/BotPasswords) · [Manual:Pywikibot/pagefromfile.py](https://www.mediawiki.org/wiki/Manual:Pywikibot/pagefromfile.py) · [Pywikibot config reference](https://doc.wikimedia.org/pywikibot/stable/api_ref/pywikibot.config.html) · [Pywikibot page API](https://doc.wikimedia.org/pywikibot/stable/api_ref/pywikibot.page.html) · [Pywikibot scripts index](https://doc.wikimedia.org/pywikibot/stable/scripts/index.html) · [pywikibot on PyPI](https://pypi.org/project/pywikibot/) · [pywikibot source](https://github.com/wikimedia/pywikibot) · [mwclient on PyPI](https://pypi.org/project/mwclient/) · [mwclient source](https://github.com/mwclient/mwclient) · [mwclient page ops](https://mwclient.readthedocs.io/en/latest/user/page-ops.html) · [WMF User-Agent policy](https://foundation.wikimedia.org/wiki/Policy:User-Agent_policy) · [meta:Bot policy](https://meta.wikimedia.org/wiki/Bot_policy) · [meta:Bot policy/Implementation](https://meta.wikimedia.org/wiki/Bot_policy/Implementation) · [meta:Steward requests/Bot status](https://meta.wikimedia.org/wiki/Steward_requests/Bot_status) · [bo:Wikipedia:Bot policy](https://bo.wikipedia.org/wiki/Wikipedia:Bot_policy) · [en:WP:LLM](https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models) · [TechCrunch on the March 2026 RfC](https://techcrunch.com/2026/03/26/wikipedia-cracks-down-on-the-use-of-ai-in-article-writing/)