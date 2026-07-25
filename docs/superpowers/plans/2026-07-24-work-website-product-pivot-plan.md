# work-website Product Pivot — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild itsnemo.dev/work to sell one product — a custom internal operations system with an optional AI layer — replacing the three-bucket freelance services menu.

**Architecture:** Four static pages plus one new page. All copy is written and humanized into a copy deck first, then pasted into HTML verbatim. A vanilla-Python checker script enforces the spec's honesty guardrails, internal links, and asset existence; it runs after every page task. No framework, no build step, no dependencies.

**Tech Stack:** Static HTML5, CSS custom properties (existing `style.css`), vanilla JS (existing `main.js`), GSAP 3.12.5 + ScrollTrigger + Lucide icons via CDN, Google Fonts (Bricolage Grotesque + DM Sans), Formspree `mqeykwbq`. Python 3 stdlib for the checker. GitHub Pages deploy from `main`.

**Spec:** `docs/superpowers/specs/2026-07-24-work-website-product-pivot-design.md`

## Global Constraints

- **Branch:** all work on `product-pivot`. **Never push to `main`** — that is a live deploy with no staging.
- **No build step.** No npm, no bundler, no framework. Static files served as-is.
- **No new runtime dependencies.** The checker script is Python 3 stdlib only.
- **Every string of copy runs through `/humanizer` before it lands in HTML.** No exceptions.
- **Product vocabulary:** the product is called an "operations system." Never a brand name, never "CRM software," never "platform."
- **Banned from all copy:** uptime figures, SLA, "24/7", HIPAA, FERPA, SOC 2, "guarantee", "unlimited", "dev team", "affordable", "cheap", "87%".
- **Banned from all pages except `about.html`:** real client, partner, and vendor names — Trailhead, Bluecove, Sawyer, Gusto, rcrtr, Little Bites, Nashville, Western Colorado, and any individual's name. (`about.html` may name Western Colorado University because that is Nemo's own biography, not a client claim.)
- **Only these figures may appear on the site** (spec §9): 5,100+ athlete performances; 600+ programs; 686 coach and AD contacts; 388 with a verified email; 5 states and regions; 4 platforms plus PDFs; attendance ~40 → 70+, up 75%; 3 coaches in parallel; ~60 museum staff, subs, and volunteers.
- **Museum status wording is exactly:** "Built and delivered. Rollout in progress." Never "in production," never "running."
- **AI layer status wording:** "Rolling out with a small first group of organizations." No adoption counts, no testimonials.
- **Published prices:** monthly tiers only ($75 / $150 / from $200), on `system.html` only. Build prices are never published.
- **Case study order is fixed:** children's museum, then college athletics department, then university advising office.
- **No real screenshots, no client logos.** Placeholder visual slots only.

---

## File Structure

| File | Status | Responsibility |
|---|---|---|
| `docs/copy/work-website-copy-deck-2026-07-24.md` | Create | Every final string for every page. The single source of truth for copy; HTML tasks paste from it |
| `scripts/check-site.py` | Create | Guardrail lint + internal link/anchor check + asset existence check. Python 3 stdlib |
| `.gitignore` | Create | `.DS_Store` and friends |
| `CLAUDE.md` | Create | Project context for future sessions + the demo-assets TODO |
| `index.html` | Modify | Home page: hero, before/after, four capabilities, thin-layer, proof, how-it-works, contact |
| `system.html` | Create | Product deep dive: capabilities, AI layer, who this isn't for, engagement, pricing tiers |
| `services.html` | Replace | Redirect stub → `system.html` (canonical + meta refresh) |
| `portfolio.html` | Modify | Three case studies + three one-liners, placeholder visual slots |
| `about.html` | Modify | Retuned bio framing + new CTA + new meta |
| `style.css` | Modify | Add: capability card grid, step list, case-visual placeholder, pricing table, not-for list. Remove: `.card-grid--5` rules if unused |
| `main.js` | Modify | Delete the `fixFiveCardGrid` helper once the 5-card grid is gone |
| `docs/superpowers/specs/worksite-revamp-design-2026-03-06.md` | Move | From `docs/2026-03-06-worksite-revamp-design.md` |
| `docs/superpowers/plans/worksite-revamp-plan-2026-03-06.md` | Move | From `docs/plans/2026-03-06-worksite-revamp-plan.md` |
| `docs/superpowers/specs/seo-expansion-2026-03-06.md` | Move | From `docs/SEO-EXPANSION.md` |

**Existing CSS classes to reuse rather than rewrite** (avoids a 200-line restyle): `.services-hero`, `.services-headline`, `.services-subline`, `.services-anchor-bar`, `.services-anchor-link`, `.services-bucket`, `.bucket-header`, `.service-list`, `.service-entry`, `.service-title`, `.service-plain`, `.service-example`, `.service-why`, `.service-label` all carry over to `system.html` unchanged. The class names keep saying "service" — that is invisible to visitors and not worth the churn.

---

## Task 1: Repo hygiene and project memory

**Files:**
- Create: `.gitignore`, `CLAUDE.md`
- Move: three docs into `docs/superpowers/{specs,plans}/`
- Untrack: `.DS_Store`

- [ ] **Step 1: Confirm the branch**

```bash
cd /Users/ncionelo/Downloads/JOBS/PROJECTS/work-website
git branch --show-current
```

Expected: `product-pivot`. If not, `git checkout product-pivot`.

- [ ] **Step 2: Create `.gitignore`**

```
.DS_Store
**/.DS_Store
Thumbs.db
*.swp
.env
.env.*
```

- [ ] **Step 3: Untrack `.DS_Store` and verify**

```bash
git rm --cached .DS_Store
git ls-files | grep -c DS_Store
```

Expected: `0`. A `.gitignore` entry alone does not untrack an already-tracked file.

- [ ] **Step 4: Move the old docs to the superpowers convention**

```bash
mkdir -p docs/superpowers/specs docs/superpowers/plans
git mv docs/2026-03-06-worksite-revamp-design.md docs/superpowers/specs/worksite-revamp-design-2026-03-06.md
git mv docs/plans/2026-03-06-worksite-revamp-plan.md docs/superpowers/plans/worksite-revamp-plan-2026-03-06.md
git mv docs/SEO-EXPANSION.md docs/superpowers/specs/seo-expansion-2026-03-06.md
rmdir docs/plans
```

- [ ] **Step 5: Create `CLAUDE.md`**

```markdown
# work-website — itsnemo.dev/work

Nemo's developer site. Sells **one product**: a custom internal operations system —
role-based access, records, analytics — with an optional AI layer trained on the
client's own documents. Not a services menu.

## Stack

Static HTML/CSS/vanilla JS. GSAP + Lucide + Google Fonts via CDN. No build step,
no framework, no dependencies. Formspree (`mqeykwbq`) handles the contact form.

## Deploy

GitHub Pages from `main` → itsnemo.dev/work/. **Push to `main` is a production
deploy with no staging.** Work on a branch; the user pushes.

## Pages

| File | Purpose |
|---|---|
| `index.html` | The pitch |
| `system.html` | Product deep dive + published monthly tiers |
| `services.html` | Redirect stub → `system.html` (kept for inbound links) |
| `portfolio.html` | Three anonymized case studies |
| `about.html` | Bio |

## Copy rules

- Source of truth: `docs/copy/work-website-copy-deck-2026-07-24.md`. Edit the deck, then the HTML.
- Every new string runs through `/humanizer` before it ships.
- `python3 scripts/check-site.py` enforces the honesty guardrails. It must pass before any commit.
- Never publish: uptime claims, SLAs, compliance claims, client names, build prices.
- Only the figures in the design spec §9 may appear. They were counted from source
  data — do not "round up" or re-derive them.

## TODO — separate session

**Demo assets for the case studies.** All three case studies currently ship with
empty placeholder slots. The real work: redacted screenshots, or dummy-data demo
instances that can be linked publicly. Requires deciding per system whether to
scrub a real instance or seed a fake one. Scope it on its own — it is not a
copy task.

Related: `assets/og-image.png` is referenced by every page's meta tags and does
not exist. It currently points at `logo-full.png` as a stopgap; a proper
1200×630 share image belongs in the same session.

## Docs

- Design: `docs/superpowers/specs/2026-07-24-work-website-product-pivot-design.md`
- Plan: `docs/superpowers/plans/2026-07-24-work-website-product-pivot-plan.md`
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "chore: untrack .DS_Store, add gitignore and CLAUDE.md, move docs to superpowers convention"
```

---

## Task 2: Write and humanize the copy deck

**Files:**
- Create: `docs/copy/work-website-copy-deck-2026-07-24.md`

**Interfaces:**
- Produces: the deck's section headings (`## index.html`, `## system.html`, `## portfolio.html`, `## about.html`, `## meta`) are referenced verbatim by Tasks 4–8. Every HTML task pastes strings from its matching deck section and adds nothing of its own.

This is the highest-leverage task in the plan. Nothing goes into HTML until the deck is approved.

- [ ] **Step 1: Write the deck with the draft copy below**

Create `docs/copy/work-website-copy-deck-2026-07-24.md` containing exactly these sections.

````markdown
# work-website Copy Deck

**Date:** 2026-07-24 · **Status:** humanized, approved
**Source of truth for every string on the site.** Edit here first, then the HTML.

---

## meta

| Page | `<title>` | `<meta name="description">` |
|---|---|---|
| index.html | Custom Operations Systems for Small Organizations \| Nehemiah Cionelo | One internal system per organization: role-based access, every record in one place, the analytics you run on, and an AI trained on your own files. Built on top of the tools you already pay for. |
| system.html | How It Works — Custom Operations Systems \| itsnemo.dev | Role-based access, records, analytics, and an AI trained on your documents — what each one means in practice, plus what ongoing support costs. |
| portfolio.html | Case Studies — Operations Systems in the Field \| itsnemo.dev | Three builds: a children's museum with ~60 staff, a college athletics department, and a university advising office. |
| about.html | About — Nehemiah Cionelo, Developer in Gunnison, Colorado | Developer in Gunnison, Colorado, building custom internal operations systems for small organizations. Available remotely, everywhere. |

- Canonical: `https://itsnemo.dev/work/<file>` on every page (`index.html` → `https://itsnemo.dev/work`).
- `og:image`: `https://itsnemo.dev/work/assets/logo-full.png` on every page until a real share image exists.
- `og:title` / `og:description` mirror the table above.

---

## index.html

### Hero
- Eyebrow: Custom operations systems · Gunnison, Colorado & remote
- H1 line 1: Your team's work lives in five places.
- H1 accent line: It should live in one.
- Subline: I build one internal system per organization. Who can see what, every record in one place, and the numbers you actually run on. An AI trained on your own files comes with it.
- Primary CTA: Book a walkthrough
- Secondary CTA: See how the system works →
- Note under CTAs: Free walkthrough. I work with a small number of organizations at a time.

### Before / After
- Before eyebrow: Where most teams are
  - Two versions of the schedule, both wrong
  - Coverage for Thursday found by texting people one at a time
  - Records in a folder anyone with the link can open
  - The report that only exists in someone's head
  - A new hire waiting three days for access
- After eyebrow: Where they end up
  - One schedule, correct everywhere
  - Coverage requested, offered, confirmed, tracked
  - People see exactly what their role allows
  - The numbers on a page instead of in a spreadsheet
  - Access on the first day, gone on the last
- Anchor: Most teams wait until something gets exposed or someone quits. You don't have to.

### The system (four cards)
- Eyebrow: The system
- Section title: One system. Four things it does.
- Card 1 — Role-Based Access (icon `shield-check`): Everyone sees exactly what their job requires. Nothing else.
- Card 2 — Records & CRM (icon `database`): People, clients, schedules, history. Edited once, correct everywhere.
- Card 3 — Analytics (icon `bar-chart-3`): The numbers you run on, without opening a spreadsheet.
- Card 4 — AI Trained On Your Files (icon `sparkles`): Ask it about your own documents. It answers, and names the file it came from.

### Built on what you already pay for
- Eyebrow: How it fits
- Title: It sits on top of what you already use.
- Body: Your registration system, your payroll, your file storage — they stay exactly where they are. I don't rebuild software you're already paying for. The system connects to it, links out to it, and owns only the parts nothing else covers. That's the difference between a six-month migration and something live in weeks.

### Proof
- Eyebrow: Recent work
- Line 1: A children's museum — about 60 staff, subs, and volunteers on one schedule, family information locked down.
- Line 2: A college athletics department — 5,100+ records unified, three staff working one list, attendance up 75%.
- Line 3: A university advising office — an assistant that answers from the office's own documents and cites the file.
- Link: Read the case studies →

### How this works
- Eyebrow: How this works
- Step 1 — Walkthrough · Free: You show me where your team's information actually lives. I map it and tell you what to fix first.
- Step 2 — First build · One-time: The smallest thing that removes the worst friction. Live in weeks, not next year.
- Step 3 — Monthly · From $75: Hosting, support, fixes, and small changes. The system keeps growing as you do.
- Link: See what's included →
- Anchor: You're not buying a finished deliverable that starts rotting the day it ships.

### Bridge
- Headline: Not sure where to start?
- Subline: Most people aren't. If you know something's off, that's enough to go on.
- Button: Let's talk →

### Contact
- Headline line 1: Let's find out where
- Headline line 2: your information lives.
- Subline: Free walkthrough. I'll map what you have and tell you what the first build should be — whether or not you hire me.
- Field placeholders: Your name · Your organization · your@email.com
- Textarea placeholder: Where does your team's information actually live right now?
- Submit button: Book a walkthrough
- Success message: Got it. I'll be in touch within 24 hours.

---

## system.html

### Hero
- Eyebrow: The system
- H1: One system, built around how your organization already works.
- Subline: Four capabilities in one place. Here's what each one means in practice, and what it costs to keep running.

### Anchor bar
Access · Records · Analytics · AI · Pricing

### 1. Role-based access
- One-liner: Everyone sees what their job requires. Nothing else.
- What it is: Every person gets a role. The role decides what they can open, what they can change, and what they never see. It's enforced in the database, not hidden in the interface.
- What it looks like: A teacher opens the app and sees their own shifts. An admin sees all sixty. A board member sees the summary and no personal information at all.
- Why it matters: Most exposure isn't a break-in. It's a folder shared with "anyone with the link" three years ago and forgotten.

### 2. Records
- One-liner: One place, edited once.
- What it is: People, clients, families, staff, schedules, history. One record per thing, one place to change it.
- What it looks like: A shift moves. It's correct on the schedule, on the calendar feed, and on the coverage list at the same time. Nobody updates a second document.
- Why it matters: Two documents holding the same information don't drift apart eventually. They drift apart immediately.

### 3. Analytics
- One-liner: The numbers you run on, on a page.
- What it is: The handful of questions you ask every month, answered on screen. Not a BI tool. Not a spreadsheet you rebuild each time.
- What it looks like: Who's under-scheduled. Which programs fill and which don't. Last season next to this one.
- Why it matters: If a number takes twenty minutes to get, you stop asking for it.

### 4. The AI layer
- One-liner: It answers from your files, and tells you which file.
- What it is: An assistant grounded in your own documents — policies, handbooks, procedures, past records. Ask in plain language, get an answer that names its source.
- What makes it different: It says "not in my knowledge base" instead of inventing an answer. It flags anything it hasn't seen verified in over a year. And it never becomes the official record — it points you to the system that is.
- Your documents stay yours: Each organization's material is kept separate. Nothing from your files is used to train anything outside your own system.
- Where it stands: Rolling out with a small first group of organizations. If you're a fit, I'll tell you. If you're not one yet, I'll tell you that too.

### 5. Built on what you already pay for
- One-liner: I don't rebuild what already works.
- Body: Your registration system, your payroll, your file storage stay where they are. The system reads from them, links out to them, and owns only the parts nothing else covers. Replacing working software is how a three-week project becomes a nine-month one.

### 6. Who this isn't for
- Intro: Three kinds of projects I turn down, so neither of us wastes a call:
  - Solo operators. One person with a notebook doesn't need this, and I'd be selling you overhead.
  - Anyone who needs it live next week. A first build takes weeks. There's no version of this that ships on Friday.
  - Anyone who wants a marketing website with nothing behind it. I used to do that work. I don't anymore.

### 7. How engagements work
- Step 1 — Walkthrough · Free: We go through where your team's information actually lives — every spreadsheet, folder, and system. I come back with a map and the one thing worth fixing first.
- Step 2 — First build · One-time, quoted: The smallest system that removes the worst friction. Live in weeks. You use it before you commit to anything bigger.
- Step 3 — Monthly partnership: Hosting, support, fixes, and small changes. The system grows as the organization does, because every organization I've built for needed the second thing about three months after the first.

### 8. What it costs
- Intro: The monthly is published below. The build isn't, because it depends entirely on what you need — that's what the walkthrough is for.

| | Monthly | Who it's for |
|---|---|---|
| Single tool | $75 | One tool, a handful of people, no role-based access |
| Team system | $150 | The full system with role-based access, up to 40 accounts |
| Organization | From $200 | More than 40 accounts |

- Included: hosting, support, fixes, and small changes.
- Quoted separately: new features and expansions.
- Closing line: Every build is quoted after the walkthrough. No hourly surprises, and no monthly bill for work nobody asked for.

### Bottom CTA
- Headline: Want to see where your information actually lives?
- Button: Book a walkthrough

---

## portfolio.html

### Hero
- Eyebrow: Case studies
- H1: Three organizations, one system.
- Subline: Names and details are left out on purpose — these are live operations. The numbers are real and counted, not estimated.

### Case 1 — A children's museum
- Tags: Role-based access · Records
- The situation: About sixty staff, subs, and volunteers across three hiring tracks. The schedule lived in two separate documents that drifted apart within days. Finding a sub meant texting people one at a time and hoping. Staff and family information sat in a folder anyone with the link could open.
- What got built: One schedule everyone reads from. A personal "my shifts" view for every person, plus a calendar feed that syncs straight to their phone. A sub-coverage workflow that tracks requested, offered, and confirmed instead of living in text messages. Role-based access so nobody sees more than their job requires.
- What stayed: Registration, billing, and payroll never moved. They're in systems the museum already pays for, and rebuilding them would have been the fastest way to blow the budget.
- Status: Built and delivered. Rollout in progress.

### Case 2 — A college athletics department
- Tags: Records · Analytics · Role-based access
- The situation: Thousands of performance records spread across four incompatible platforms and a stack of PDFs. No way to connect a result to the person running the program behind it. And three staff who needed to work the same list at the same time without duplicating each other's outreach.
- What got built: One database — 5,100+ athlete performances, 600+ programs, and 686 coaches and athletic directors across five states and regions, 388 of them with a verified email. Contact discovery with confidence scoring, so nobody wastes a morning on a dead address. Outreach written from what each program actually did that season: team wins, podium finishes, standout individual races, athletes by name.
- Three people, one list: All three staff worked the same list simultaneously without stepping on each other. That's the role-based access piece, running on real users.
- The result: Attendance up 75% year over year — about forty to seventy-plus. First-time relationships with rural programs nobody had been contacting. And early contact with athletes who matter two seasons from now.

### Case 3 — A university advising office
- Tags: The AI layer
- The situation: Program requirements, testing rules, transfer agreements, and policy spread across a public website, a shared drive, and institutional memory. New staff asked the same questions for months. A wrong answer had consequences for a student's schedule or their aid.
- What got built: An assistant grounded in the office's own documented knowledge. Every answer names the file it came from. Anything not verified in the last twelve months is flagged as stale. Outside its coverage, it points to the right office instead of guessing.
- Where the line is: It never became the system of record, and it says so in every answer that touches one. An assistant that guesses confidently is worse than no assistant.

### Also built
- A public-health advisory firm — a live data dashboard with an access-controlled editor, replacing a spreadsheet that had to be re-published by hand.
- A college coaching staff — timing data from eight vendor formats in one consistent view.
- A small food business — ordering that writes straight into the sheet the kitchen already uses.

### Bottom CTA
- Headline: Recognize your own operation in any of these?
- Button: Book a walkthrough

---

## about.html

Only these strings change. Everything else on the page stays.

- "Who I am" closing sentence: A computer science degree and a master's in sport management. I've built software, and I've studied how organizations actually run — which is why the system ends up fitting the organization instead of the other way around.
- Closing CTA headline: Let's talk about where your information lives.
- Closing CTA button: Book a walkthrough
````

- [ ] **Step 2: Run the humanizer pass**

Invoke the `humanizer` skill on the deck file. Apply its edits in place. Watch specifically for: em-dash density, rule-of-three sentence rhythm, "not just X but Y" constructions, and promotional adjectives.

Constraint: the humanizer may not change any figure, any status wording ("Built and delivered. Rollout in progress."), or any price. If it proposes a change to one of those, reject it and note the rejection in the deck.

- [ ] **Step 3: Run the copy against the guardrail list by hand**

```bash
grep -inE "24/7|SLA|uptime|HIPAA|FERPA|SOC ?2|guarantee|unlimited|dev team|affordable|cheap|87%" docs/copy/work-website-copy-deck-2026-07-24.md
grep -inE "Trailhead|Bluecove|Sawyer|Gusto|rcrtr|Little Bites|Nashville|Western Colorado" docs/copy/work-website-copy-deck-2026-07-24.md
```

Expected: no output from either. Any hit is a copy bug — fix the copy, not the check.

- [ ] **Step 4: Commit**

```bash
git add docs/copy/work-website-copy-deck-2026-07-24.md
git commit -m "docs: add humanized copy deck for product pivot"
```

- [ ] **Step 5: STOP — user review gate**

Show the deck to Nemo before any HTML changes. This is the last cheap moment to change positioning. Do not proceed to Task 3 without explicit approval.

---

## Task 3: Build the site checker

**Files:**
- Create: `scripts/check-site.py`

**Interfaces:**
- Produces: `python3 scripts/check-site.py` — exits `0` on pass, `1` on any violation, printing `file:line` for each. Tasks 4–8 each end by running it.

The site has no test framework and does not need one. What it needs is a gate that catches the three failure modes that actually matter: a banned claim slipping into copy, a broken internal link after the `services.html` → `system.html` move, and a referenced asset that doesn't exist.

- [ ] **Step 1: Write the checker**

```python
#!/usr/bin/env python3
"""Guardrail, link, and asset checks for itsnemo.dev/work.

Usage: python3 scripts/check-site.py
Exit 0 = clean. Exit 1 = violations printed as file:line: message.

Rules come from docs/superpowers/specs/2026-07-24-work-website-product-pivot-design.md
sections 8 and 9. Adding a rule here is cheaper than catching a bad claim in production.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "system.html", "services.html", "portfolio.html", "about.html"]

# Claims the infrastructure cannot back, plus positioning we deliberately killed.
BANNED_EVERYWHERE = [
    r"24/7",
    r"\bSLA\b",
    r"\buptime\b",
    r"\bHIPAA\b",
    r"\bFERPA\b",
    r"\bSOC ?2\b",
    r"\bguarantee",
    r"\bunlimited\b",
    r"\bdev team\b",
    r"\baffordable\b",
    r"\bcheap\b",
    r"87%",
]

# Client, partner, and vendor names. about.html is exempt: it names Western Colorado
# University as part of Nemo's own biography, which is not a client claim.
CLIENT_NAMES = [
    r"Trailhead",
    r"Bluecove",
    r"Sawyer",
    r"Gusto",
    r"rcrtr",
    r"Little Bites",
    r"Nashville",
    r"Western Colorado",
]
CLIENT_NAME_EXEMPT = {"about.html"}

# Wording the spec pins exactly. If the phrase on the left appears, the phrase on the
# right must appear in the same file.
REQUIRED_PAIRS = [
    ("children's museum", "Built and delivered"),
]

TAG_RE = re.compile(r'(?:href|src)="([^"]+)"')
ID_RE = re.compile(r'id="([^"]+)"')


def strip_comments(text):
    """Blank out HTML comments so TODO notes don't trip the copy rules."""
    return re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), text, flags=re.S)


def check_banned(name, text, problems):
    body = strip_comments(text)
    patterns = list(BANNED_EVERYWHERE)
    if name not in CLIENT_NAME_EXEMPT:
        patterns += CLIENT_NAMES
    for i, line in enumerate(body.splitlines(), 1):
        for pat in patterns:
            if re.search(pat, line, re.I):
                problems.append(f"{name}:{i}: banned phrase /{pat}/ -> {line.strip()[:90]}")


def check_required_pairs(name, text, problems):
    body = strip_comments(text)
    for trigger, required in REQUIRED_PAIRS:
        if trigger.lower() in body.lower() and required.lower() not in body.lower():
            problems.append(f"{name}:0: '{trigger}' present but required wording '{required}' missing")


def check_links(name, text, ids_by_file, problems):
    for i, line in enumerate(text.splitlines(), 1):
        for target in TAG_RE.findall(line):
            if target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            path_part, _, anchor = target.partition("#")
            if path_part:
                resolved = (ROOT / path_part).resolve()
                if not resolved.exists():
                    problems.append(f"{name}:{i}: missing target -> {target}")
                    continue
                target_file = path_part
            else:
                target_file = name
            if anchor and target_file in ids_by_file and anchor not in ids_by_file[target_file]:
                problems.append(f"{name}:{i}: dead anchor -> {target}")


def main():
    problems = []
    texts = {}
    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            problems.append(f"{name}:0: page missing")
            continue
        texts[name] = path.read_text(encoding="utf-8")

    ids_by_file = {n: set(ID_RE.findall(t)) for n, t in texts.items()}

    for name, text in texts.items():
        check_banned(name, text, problems)
        check_required_pairs(name, text, problems)
        check_links(name, text, ids_by_file, problems)

    if problems:
        print(f"FAIL — {len(problems)} problem(s):\n")
        for p in problems:
            print("  " + p)
        return 1
    print(f"PASS — {len(texts)} pages: no banned phrases, no dead links, no missing assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run it against the current site and confirm it fails**

```bash
python3 scripts/check-site.py
```

Expected: `FAIL`, reporting at least these real problems in the pre-pivot site — `system.html:0: page missing`, banned `affordable` in `index.html` and `about.html`, banned `dev team` in `index.html`, and a missing `assets/og-image.png` target. If it prints `PASS`, the checker is broken; fix it before continuing.

- [ ] **Step 3: Confirm it catches a planted violation**

```bash
printf '<p>We guarantee 24/7 uptime.</p>\n' >> about.html
python3 scripts/check-site.py | grep -c "about.html"
git checkout about.html
```

Expected: a count of 3 or more (guarantee, 24/7, uptime), then the file is restored.

- [ ] **Step 4: Commit**

```bash
git add scripts/check-site.py
git commit -m "test: add copy guardrail, link, and asset checker"
```

---

## Task 4: Fix the broken share image and unify meta across all pages

**Files:**
- Modify: `index.html:6-16`, `services.html`, `portfolio.html`, `about.html` (`<head>` blocks)

**Interfaces:**
- Consumes: the `## meta` table from the copy deck (Task 2).
- Produces: every page carries a correct `<title>`, `description`, `canonical`, and an `og:image` that resolves. Task 7 creates `system.html` with the same head pattern.

`assets/og-image.png` is referenced by every page and does not exist — every share link on every platform is currently broken. This is the one live bug in the repo, so it gets fixed before the rewrite rather than after.

- [ ] **Step 1: Confirm the bug**

```bash
grep -l "og-image.png" *.html
ls assets/og-image.png
```

Expected: all four pages listed, then `No such file or directory`.

- [ ] **Step 2: Point `og:image` at an asset that exists, on every page**

In each of the four pages, replace:

```html
  <meta property="og:image" content="https://itsnemo.dev/work/assets/og-image.png">
```

with:

```html
  <!-- TODO: replace with a purpose-built 1200x630 share image (see CLAUDE.md) -->
  <meta property="og:image" content="https://itsnemo.dev/work/assets/logo-full.png">
```

- [ ] **Step 3: Apply the deck's titles, descriptions, and og tags**

For `index.html`, `portfolio.html`, and `about.html`, replace `<title>`, `<meta name="description">`, `<meta property="og:title">`, and `<meta property="og:description">` with the values from the deck's `## meta` table. Leave `canonical` as-is where already correct; add it where missing.

Leave `services.html` alone — Task 7 replaces that file entirely.

- [ ] **Step 4: Verify**

```bash
python3 scripts/check-site.py
grep -c "og-image.png" *.html
```

Expected: the missing-asset problem is gone from the checker output (banned-phrase and missing-page problems remain, since the copy rewrite hasn't happened). Second command: `0` for every page.

- [ ] **Step 5: Commit**

```bash
git add index.html services.html portfolio.html about.html
git commit -m "fix: point og:image at an asset that exists, apply new page meta"
```

---

## Task 5: Update nav and footer across all pages

**Files:**
- Modify: `index.html:47-70`, `portfolio.html`, `about.html`, `services.html` (nav blocks)

**Interfaces:**
- Produces: the exact nav markup block below. Task 7 copies it verbatim into `system.html`.

- [ ] **Step 1: Replace the nav links and CTA in `index.html`**

Desktop links block becomes:

```html
      <div class="nav-links">
        <a href="portfolio.html" class="nav-link">Case Studies</a>
        <a href="system.html" class="nav-link">How It Works</a>
        <a href="about.html" class="nav-link">About</a>
      </div>
      <a href="#contact" class="btn-ghost nav-cta">Book a walkthrough</a>
```

Mobile menu block becomes:

```html
    <div class="nav-mobile-menu" id="navMobileMenu">
      <a href="portfolio.html" class="nav-mobile-link">Case Studies</a>
      <a href="system.html" class="nav-mobile-link">How It Works</a>
      <a href="about.html" class="nav-mobile-link">About</a>
      <a href="#contact" class="btn-primary nav-mobile-cta">Book a walkthrough</a>
    </div>
```

- [ ] **Step 2: Apply the same nav to `portfolio.html` and `about.html`**

Identical markup, with two differences per page: the CTA `href` becomes `index.html#contact` (there is no `#contact` section on those pages), and the current page's own link carries `nav-link--active` / `nav-mobile-link--active`.

- [ ] **Step 3: Verify no page still links to a services menu**

```bash
grep -n 'nav-link">Services\|nav-mobile-link">Services' *.html
python3 scripts/check-site.py
```

Expected: no output from the grep. The checker still reports banned copy and the missing `system.html`; it must not report new dead links.

- [ ] **Step 4: Commit**

```bash
git add index.html portfolio.html about.html
git commit -m "feat: nav points to case studies and how-it-works, CTA becomes walkthrough"
```

---

## Task 6: Rewrite `index.html`

**Files:**
- Modify: `index.html:72-272` (hero through contact)
- Modify: `style.css` (append: `.step-list`, `.proof-list`, `.fit-body`)
- Modify: `main.js:225-255` (delete `fixFiveCardGrid`)

**Interfaces:**
- Consumes: the deck's `## index.html` section (Task 2), the nav from Task 5.
- Produces: `#system`, `#how-it-works`, and `#contact` section ids, linked from `system.html` in Task 7.

- [ ] **Step 1: Rewrite the hero**

Use the deck's Hero strings. Keep every existing class (`.hero-inner`, `.hero-text`, `.eyebrow`, `.hero-headline`, `.headline-accent`, `.hero-subline`, `.hero-actions`, `.btn-primary`, `.btn-text`, `.hero-demo-note`, `.hero-visual`) — GSAP's hero timeline in `main.js:28` animates these by class, so renaming any of them silently kills the entrance animation. Secondary CTA `href` becomes `system.html`.

- [ ] **Step 2: Rewrite the before/after lists**

Replace the ten `<li>` items in `#before-after` with the deck's five-and-five, and the `.arc-anchor` paragraph with the deck's anchor line. Structure and classes unchanged.

- [ ] **Step 3: Replace `#who-i-help` with the four-capability section**

```html
  <section id="system" class="section-bg">
    <div class="container">
      <div class="section-header reveal">
        <p class="eyebrow">The system</p>
        <h2 class="section-title">One system.<br>Four things it does.</h2>
      </div>

      <div class="card-grid" id="system-grid">
        <div class="card reveal" style="transition-delay:0.05s">
          <i data-lucide="shield-check" class="card-icon"></i>
          <h3 class="card-title">Role-Based Access</h3>
          <p class="card-desc">Everyone sees exactly what their job requires. Nothing else.</p>
        </div>
        <div class="card reveal" style="transition-delay:0.10s">
          <i data-lucide="database" class="card-icon"></i>
          <h3 class="card-title">Records &amp; CRM</h3>
          <p class="card-desc">People, clients, schedules, history. Edited once, correct everywhere.</p>
        </div>
        <div class="card reveal" style="transition-delay:0.15s">
          <i data-lucide="bar-chart-3" class="card-icon"></i>
          <h3 class="card-title">Analytics</h3>
          <p class="card-desc">The numbers you run on, without opening a spreadsheet.</p>
        </div>
        <div class="card reveal" style="transition-delay:0.20s">
          <i data-lucide="sparkles" class="card-icon"></i>
          <h3 class="card-title">AI Trained On Your Files</h3>
          <p class="card-desc">Ask it about your own documents. It answers, and names the file it came from.</p>
        </div>
      </div>
    </div>
  </section>
```

- [ ] **Step 4: Replace `#what-i-build` with the thin-layer section and the proof list**

```html
  <section id="how-it-fits" class="section-surface">
    <div class="container container--narrow">
      <div class="section-header reveal">
        <p class="eyebrow">How it fits</p>
        <h2 class="section-title">It sits on top of what you already use.</h2>
      </div>
      <p class="fit-body reveal">Your registration system, your payroll, your file storage — they stay exactly where they are. I don't rebuild software you're already paying for. The system connects to it, links out to it, and owns only the parts nothing else covers. That's the difference between a six-month migration and something live in weeks.</p>

      <div class="section-header reveal" style="margin-top:var(--space-8)">
        <p class="eyebrow">Recent work</p>
      </div>
      <ul class="proof-list reveal">
        <li>A children's museum — about 60 staff, subs, and volunteers on one schedule, family information locked down.</li>
        <li>A college athletics department — 5,100+ records unified, three staff working one list, attendance up 75%.</li>
        <li>A university advising office — an assistant that answers from the office's own documents and cites the file.</li>
      </ul>
      <a href="portfolio.html" class="btn-text reveal">Read the case studies →</a>
    </div>
  </section>
```

- [ ] **Step 5: Add the how-it-works section before `#bridge`**

```html
  <section id="how-it-works" class="section-bg">
    <div class="container container--narrow">
      <div class="section-header reveal">
        <p class="eyebrow">How this works</p>
      </div>
      <ol class="step-list">
        <li class="reveal">
          <span class="step-num">1</span>
          <h3 class="step-title">Walkthrough <span class="step-price">Free</span></h3>
          <p class="step-desc">You show me where your team's information actually lives. I map it and tell you what to fix first.</p>
        </li>
        <li class="reveal" style="transition-delay:0.1s">
          <span class="step-num">2</span>
          <h3 class="step-title">First build <span class="step-price">One-time</span></h3>
          <p class="step-desc">The smallest thing that removes the worst friction. Live in weeks, not next year.</p>
        </li>
        <li class="reveal" style="transition-delay:0.2s">
          <span class="step-num">3</span>
          <h3 class="step-title">Monthly <span class="step-price">From $75</span></h3>
          <p class="step-desc">Hosting, support, fixes, and small changes. The system keeps growing as you do. <a href="system.html#pricing" class="btn-text">See what's included →</a></p>
        </li>
      </ol>
      <p class="section-anchor reveal">You're not buying a finished deliverable that starts rotting the day it ships.</p>
    </div>
  </section>
```

- [ ] **Step 6: Update bridge and contact copy**

Bridge headline, subline, and button from the deck. Contact headline, subline, four field placeholders (`Your organization` replaces `Your business`), textarea placeholder, submit label `Book a walkthrough`, and success message. Leave the `<form action>`, `method`, hidden `_subject`, and all `name` attributes untouched — Formspree keys off them. Update `hero-demo-note` to the deck's note line.

- [ ] **Step 7: Append the new CSS**

```css
/* ═══════════════════════════════════════════════════
   THIN-LAYER + PROOF (index)
   ═══════════════════════════════════════════════════ */
.fit-body {
  font-size: 1.0625rem;
  line-height: 1.75;
  color: var(--text-muted);
  margin-bottom: var(--space-6);
}

.proof-list {
  list-style: none;
  margin: 0 0 var(--space-5);
  padding: 0;
}

.proof-list li {
  position: relative;
  padding-left: var(--space-5);
  margin-bottom: var(--space-3);
  color: var(--text-muted);
  line-height: 1.6;
}

.proof-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.6em;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
}

/* ═══════════════════════════════════════════════════
   STEP LIST (index + system)
   ═══════════════════════════════════════════════════ */
.step-list {
  list-style: none;
  margin: 0 0 var(--space-6);
  padding: 0;
}

.step-list li {
  position: relative;
  padding: var(--space-5) 0 var(--space-5) var(--space-8);
  border-bottom: 1px solid var(--border);
}

.step-list li:last-child { border-bottom: none; }

.step-num {
  position: absolute;
  left: 0;
  top: var(--space-5);
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--accent);
}

.step-title {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 700;
  margin: 0 0 var(--space-2);
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  flex-wrap: wrap;
}

.step-price {
  font-family: var(--font-body);
  font-size: 0.8125rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--accent);
}

.step-desc {
  color: var(--text-muted);
  line-height: 1.65;
  margin: 0;
}
```

Check the variable names against the top of `style.css` first (`--space-*`, `--text-muted`, `--border`, `--accent`, `--font-display`, `--font-body`). If any differs, use the real one — do not introduce a new variable.

- [ ] **Step 7b: Remove the dead 5-card grid helper**

Delete `fixFiveCardGrid`, its call, and its resize listener (`main.js:225-255`). The 5-card grid no longer exists on any page. The function guards with `if (!grid) return`, so leaving it is harmless but dishonest — dead code that looks load-bearing.

Then delete the `.card-grid--5` rules from `style.css` (search for `card-grid--5`).

- [ ] **Step 8: Verify**

```bash
python3 scripts/check-site.py
grep -c "card-grid--5" style.css main.js index.html
python3 -m http.server 8080 &
open http://localhost:8080/index.html
```

Expected: the checker's only remaining problem is `system.html:0: page missing`. The grep returns `0` for all three files. In the browser: hero animates, the four capability cards reveal on scroll, the step list reads cleanly, and at a 375px window width nothing scrolls horizontally.

- [ ] **Step 9: Commit**

```bash
git add index.html style.css main.js
git commit -m "feat: rewrite home page around one product"
```

---

## Task 7: Create `system.html` and turn `services.html` into a redirect

**Files:**
- Create: `system.html`
- Replace: `services.html` (entire file)
- Modify: `style.css` (append: `.pricing-table`, `.not-for-list`, `.ai-status`)

**Interfaces:**
- Consumes: the deck's `## system.html` section, the nav from Task 5, `.services-*` classes already in `style.css`.
- Produces: anchor ids `#access`, `#records`, `#analytics`, `#ai`, `#pricing` — `index.html` links to `#pricing` (Task 6, Step 5).

- [ ] **Step 1: Create `system.html`**

Copy `services.html`'s existing skeleton — `<head>` block, nav, `.services-hero`, `.services-anchor-bar`, footer, and the `main.js` script tag — then replace the body content. Meta values come from the deck's `## meta` table; nav markup from Task 5 with `system.html` marked active and the CTA pointing at `index.html#contact`.

Anchor bar:

```html
  <div class="services-anchor-bar">
    <div class="container">
      <a href="#access" class="services-anchor-link">Access</a>
      <span class="services-anchor-dot" aria-hidden="true">·</span>
      <a href="#records" class="services-anchor-link">Records</a>
      <span class="services-anchor-dot" aria-hidden="true">·</span>
      <a href="#analytics" class="services-anchor-link">Analytics</a>
      <span class="services-anchor-dot" aria-hidden="true">·</span>
      <a href="#ai" class="services-anchor-link">AI</a>
      <span class="services-anchor-dot" aria-hidden="true">·</span>
      <a href="#pricing" class="services-anchor-link">Pricing</a>
    </div>
  </div>
```

Each of sections 1–3 follows this shape, with strings from the deck:

```html
  <section id="access" class="services-bucket section-surface">
    <div class="container">
      <div class="bucket-header reveal">
        <h2 class="section-title">Role-based access</h2>
        <p class="bucket-desc">Everyone sees what their job requires. Nothing else.</p>
      </div>
      <div class="service-list">
        <div class="service-entry reveal">
          <div class="service-entry-inner">
            <p class="service-plain">Every person gets a role. The role decides what they can open, what they can change, and what they never see. It's enforced in the database, not hidden in the interface.</p>
            <p class="service-example"><span class="service-label">What it looks like</span> A teacher opens the app and sees their own shifts. An admin sees all sixty. A board member sees the summary and no personal information at all.</p>
            <p class="service-why"><span class="service-label">Why it matters</span> Most exposure isn't a break-in. It's a folder shared with "anyone with the link" three years ago and forgotten.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
```

Alternate `section-surface` and `section-bg` between sections, matching the existing page rhythm.

Section 4 (`#ai`) adds two extra paragraphs after the same three — the isolation line and the status line:

```html
          <p class="service-why"><span class="service-label">Your documents stay yours</span> Each organization's material is kept separate. Nothing from your files is used to train anything outside your own system.</p>
          <p class="ai-status"><span class="service-label">Where it stands</span> Rolling out with a small first group of organizations. If you're a fit, I'll tell you. If you're not one yet, I'll tell you that too.</p>
```

The isolation sentence is a promise the build has to keep. Per-organization separation must actually hold in the product; if that ever stops being true, this line comes off the page first.

Section 6 (who this isn't for):

```html
  <section id="not-for" class="services-bucket section-bg">
    <div class="container container--narrow">
      <div class="bucket-header reveal">
        <h2 class="section-title">Who this isn't for</h2>
        <p class="bucket-desc">Three kinds of projects I turn down, so neither of us wastes a call:</p>
      </div>
      <ul class="not-for-list reveal">
        <li>Solo operators. One person with a notebook doesn't need this, and I'd be selling you overhead.</li>
        <li>Anyone who needs it live next week. A first build takes weeks. There's no version of this that ships on Friday.</li>
        <li>Anyone who wants a marketing website with nothing behind it. I used to do that work. I don't anymore.</li>
      </ul>
    </div>
  </section>
```

Section 7 reuses the `.step-list` markup from Task 6, Step 5, with the deck's longer `## system.html` step descriptions.

Section 8 (`#pricing`):

```html
  <section id="pricing" class="services-bucket section-bg">
    <div class="container container--narrow">
      <div class="bucket-header reveal">
        <h2 class="section-title">What it costs</h2>
        <p class="bucket-desc">The monthly is published below. The build isn't, because it depends entirely on what you need — that's what the walkthrough is for.</p>
      </div>

      <table class="pricing-table reveal">
        <thead>
          <tr><th scope="col">Tier</th><th scope="col">Monthly</th><th scope="col">Who it's for</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Single tool</th><td class="price">$75</td><td>One tool, a handful of people, no role-based access</td></tr>
          <tr><th scope="row">Team system</th><td class="price">$150</td><td>The full system with role-based access, up to 40 accounts</td></tr>
          <tr><th scope="row">Organization</th><td class="price">From $200</td><td>More than 40 accounts</td></tr>
        </tbody>
      </table>

      <p class="fit-body reveal"><strong>Included:</strong> hosting, support, fixes, and small changes.<br><strong>Quoted separately:</strong> new features and expansions.</p>
      <p class="section-anchor reveal">Every build is quoted after the walkthrough. No hourly surprises, and no monthly bill for work nobody asked for.</p>
    </div>
  </section>
```

Close with the existing bottom-CTA pattern from `services.html`, using the deck's headline and `Book a walkthrough` pointing at `index.html#contact`.

- [ ] **Step 2: Append the new CSS**

```css
/* ═══════════════════════════════════════════════════
   PRICING TABLE + NOT-FOR LIST (system)
   ═══════════════════════════════════════════════════ */
.pricing-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: var(--space-6);
  font-size: 0.9375rem;
}

.pricing-table th,
.pricing-table td {
  text-align: left;
  padding: var(--space-4) var(--space-3);
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}

.pricing-table thead th {
  font-family: var(--font-body);
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
}

.pricing-table tbody th {
  font-family: var(--font-display);
  font-weight: 700;
  white-space: nowrap;
}

.pricing-table .price {
  font-family: var(--font-display);
  font-weight: 700;
  color: var(--accent);
  white-space: nowrap;
}

.pricing-table td:last-child { color: var(--text-muted); }

@media (max-width: 600px) {
  .pricing-table { font-size: 0.875rem; }
  .pricing-table th,
  .pricing-table td { padding: var(--space-3) var(--space-2); }
}

.not-for-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.not-for-list li {
  position: relative;
  padding-left: var(--space-6);
  margin-bottom: var(--space-4);
  color: var(--text-muted);
  line-height: 1.7;
}

.not-for-list li::before {
  content: "—";
  position: absolute;
  left: 0;
  color: var(--accent);
}

.ai-status {
  margin-top: var(--space-4);
  padding: var(--space-4);
  border: 1px solid var(--border-amber, var(--border));
  border-radius: 8px;
  color: var(--text-muted);
  line-height: 1.65;
}
```

- [ ] **Step 3: Replace `services.html` with a redirect stub**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>How It Works — Custom Operations Systems | itsnemo.dev</title>
  <meta name="description" content="This page moved. The services menu is now one product: a custom internal operations system.">
  <link rel="canonical" href="https://itsnemo.dev/work/system.html">
  <meta http-equiv="refresh" content="0; url=system.html">
  <link rel="icon" href="assets/logo-mark.png" type="image/png">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="container container--narrow" style="padding:25vh 0;text-align:center">
    <p class="eyebrow">This page moved</p>
    <h1 class="section-title">One product now, not a menu.</h1>
    <p class="fit-body">If you aren't redirected, <a href="system.html">see how the system works</a>.</p>
  </main>
</body>
</html>
```

No `noindex` — the canonical passes the existing link equity to `system.html`, which is the point of keeping the file at all.

- [ ] **Step 4: Verify**

```bash
python3 scripts/check-site.py
python3 -m http.server 8080 &
open http://localhost:8080/system.html
open http://localhost:8080/services.html
```

Expected: the checker prints `PASS`. This is the first task where it should. In the browser: the anchor bar scrolls to all five sections, the pricing table doesn't overflow at 375px, and `services.html` bounces to `system.html` immediately.

- [ ] **Step 5: Commit**

```bash
git add system.html services.html style.css
git commit -m "feat: add system.html product deep dive, redirect services.html"
```

---

## Task 8: Rewrite `portfolio.html` as case studies

**Files:**
- Modify: `portfolio.html` (hero + card grid)
- Modify: `style.css` (append: `.case-visual`, `.case-block`)

**Interfaces:**
- Consumes: the deck's `## portfolio.html` section, existing `.card--project`, `.card-tags`, `.card-tag` classes.

- [ ] **Step 1: Rewrite the hero**

Deck strings: eyebrow `Case studies`, H1 `Three organizations, one system.`, subline about names being left out on purpose.

- [ ] **Step 2: Replace the three project cards with three case study blocks, in the spec's order**

Museum first, athletics second, advising office third. Each block:

```html
      <article class="case-block reveal">
        <div class="card-tags">
          <span class="card-tag">Role-based access</span>
          <span class="card-tag">Records</span>
        </div>
        <h2 class="section-title">A children's museum</h2>

        <!-- TODO (separate session, see CLAUDE.md): replace with a redacted screenshot
             or a dummy-data demo instance. Do not ship a real client screenshot. -->
        <div class="case-visual" role="img" aria-label="Screenshot pending: staff schedule and coverage interface">
          <span>Demo coming soon</span>
        </div>

        <p class="case-label">The situation</p>
        <p class="fit-body">About sixty staff, subs, and volunteers across three hiring tracks. The schedule lived in two separate documents that drifted apart within days. Finding a sub meant texting people one at a time and hoping. Staff and family information sat in a folder anyone with the link could open.</p>

        <p class="case-label">What got built</p>
        <p class="fit-body">One schedule everyone reads from. A personal "my shifts" view for every person, plus a calendar feed that syncs straight to their phone. A sub-coverage workflow that tracks requested, offered, and confirmed instead of living in text messages. Role-based access so nobody sees more than their job requires.</p>

        <p class="case-label">What stayed</p>
        <p class="fit-body">Registration, billing, and payroll never moved. They're in systems the museum already pays for, and rebuilding them would have been the fastest way to blow the budget.</p>

        <p class="case-status">Built and delivered. Rollout in progress.</p>
      </article>
```

The athletics block adds a `Three people, one list` labelled paragraph and a `The result` paragraph; the advising block adds `Where the line is`. All strings come from the deck — do not paraphrase, and do not add a status line to blocks the deck doesn't give one for.

- [ ] **Step 3: Add the "Also built" list**

```html
      <section class="case-also reveal">
        <p class="eyebrow">Also built</p>
        <ul class="proof-list">
          <li>A public-health advisory firm — a live data dashboard with an access-controlled editor, replacing a spreadsheet that had to be re-published by hand.</li>
          <li>A college coaching staff — timing data from eight vendor formats in one consistent view.</li>
          <li>A small food business — ordering that writes straight into the sheet the kitchen already uses.</li>
        </ul>
      </section>
```

- [ ] **Step 4: Append the new CSS**

```css
/* ═══════════════════════════════════════════════════
   CASE STUDIES (portfolio)
   ═══════════════════════════════════════════════════ */
.case-block {
  padding-bottom: var(--space-8);
  margin-bottom: var(--space-8);
  border-bottom: 1px solid var(--border);
}

.case-block:last-of-type { border-bottom: none; }

.case-block .section-title { margin: var(--space-3) 0 var(--space-5); }

.case-visual {
  display: flex;
  align-items: center;
  justify-content: center;
  aspect-ratio: 16 / 9;
  margin-bottom: var(--space-6);
  border: 1px dashed var(--border);
  border-radius: 10px;
  background: var(--surface-2);
  color: var(--text-muted);
  font-size: 0.8125rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.case-label {
  font-family: var(--font-body);
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent);
  margin: var(--space-5) 0 var(--space-2);
}

.case-status {
  display: inline-block;
  margin-top: var(--space-4);
  padding: var(--space-2) var(--space-4);
  border: 1px solid var(--border-amber, var(--border));
  border-radius: 999px;
  font-size: 0.8125rem;
  color: var(--text-muted);
}

.case-also { margin-top: var(--space-8); }
```

- [ ] **Step 5: Verify**

```bash
python3 scripts/check-site.py
grep -c "Built and delivered" portfolio.html
python3 -m http.server 8080 &
open http://localhost:8080/portfolio.html
```

Expected: checker `PASS` — this is the task most likely to trip the client-name and required-wording rules, so a failure here is the checker doing its job. The grep returns `1`. In the browser: three placeholder slots hold their 16:9 shape with no broken-image icon, and nothing overflows at 375px.

- [ ] **Step 6: Commit**

```bash
git add portfolio.html style.css
git commit -m "feat: rewrite portfolio as three anonymized case studies"
```

---

## Task 9: Retune `about.html` and run final verification

**Files:**
- Modify: `about.html` (bio closing sentence, CTA)

- [ ] **Step 1: Apply the deck's `## about.html` strings**

Three edits only: the "Who I am" closing sentence, the closing CTA headline, and the CTA button label. Everything else on the page — Gunnison, altitude training, remote availability, the headshot — stays exactly as it is. Confirm the CTA still points at `index.html#contact`.

- [ ] **Step 2: Run the full check**

```bash
python3 scripts/check-site.py
```

Expected: `PASS — 5 pages`.

- [ ] **Step 3: Confirm no stale positioning survives anywhere**

```bash
grep -rinE "free estimate|Websites|Automation & Tools|SEO & Content|WordPress|Zapier|Airtable|booking system" *.html
```

Expected: no output. Any hit is old services-menu copy that survived the rewrite. (`about.html` and `system.html` may legitimately mention a client-facing website as a component — read each hit before deleting it.)

- [ ] **Step 4: Manual browser pass, all five pages**

```bash
python3 -m http.server 8080 &
for p in index system services portfolio about; do open "http://localhost:8080/$p.html"; done
```

On each page, confirm: nav links work in both desktop and mobile menus, the hamburger opens and closes, scroll-reveal animations fire, no console errors, and no horizontal scroll at a 375px window width (iPhone SE). Submit the contact form once with real values and confirm the Formspree success state appears.

- [ ] **Step 5: Final commit**

```bash
git add about.html
git commit -m "feat: retune about page for the product positioning"
git log --oneline product-pivot ^main
```

- [ ] **Step 6: STOP — hand off to Nemo**

Do not push. Report the branch name, the commit list, and this checklist of what he needs to decide:

1. Review the live pages locally and approve the copy in place.
2. Confirm the monthly tiers read the way he wants them to before they're public.
3. Merge and push `main` himself — that action is a production deploy.
4. Schedule the demo-assets session (`CLAUDE.md` TODO): three placeholder slots plus a real 1200×630 share image.

---

## Self-Review

**Spec coverage:**

| Spec section | Task |
|---|---|
| §1 one product, no brand name | 2 (deck), 6 (index) |
| §2 buyer | 2 (deck copy targets ops-heavy orgs) |
| §3 voice, humanizer pass | 2 |
| §4 hero | 2, 6 |
| §5 index sections | 6 |
| §5 services.html → system.html + redirect | 7 |
| §5 portfolio, 3 cases + 3 one-liners, fixed order | 8 |
| §5 about retune | 9 |
| §6 placeholder visuals | 8 (slots), 1 (CLAUDE.md TODO) |
| §7 engagement model + published tiers, system.html only | 6 (step 5, "From $75" + link), 7 (table) |
| §8 honesty guardrails | 3 (enforced), 2 (authored) |
| §9 verified numbers | 2 (deck), 8 (case 2) |
| §10 og-image, .DS_Store, doc moves, CLAUDE.md, SEO, branch | 4, 1, 1, 1, 4, global constraints |
| §11 out of scope (architecture doc) | not planned — correct |

**Placeholder scan:** no TBDs. Every code step carries real markup, CSS, or Python. The two `TODO` comments that ship in the HTML are deliberate content decisions recorded in `CLAUDE.md`, not plan gaps.

**Type and name consistency:** `#pricing` is the anchor id created in Task 7 and linked from Task 6 Step 5 — matched. `.step-list`, `.fit-body`, and `.proof-list` are defined in Task 6's CSS and reused in Tasks 7 and 8 — defined before use. `check-site.py`'s exit contract is stated in Task 3 and relied on by Tasks 4–9. `.card-grid--5` removal (Task 6, Step 7b) covers both `style.css` and `main.js`.

**One risk worth naming:** Task 6 keeps every hero class name because `main.js` animates them by class. A subagent that "cleans up" those names will silently break the entrance animation with no error in the console. The step says so explicitly; a reviewer should check it.
