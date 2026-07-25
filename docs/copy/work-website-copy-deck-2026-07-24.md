# work-website Copy Deck

**Date:** 2026-07-24 · **Status:** humanized, approved 2026-07-24 by Nemo
**Source of truth for every string on the site.** Edit here first, then the HTML.

---

## meta

| Page | `<title>` | `<meta name="description">` |
|---|---|---|
| index.html | Custom Operations Systems for Small Organizations \| Nehemiah Cionelo | One internal system per organization: role-based access, every record in one place, the analytics you run on, and an AI trained on your own files, now in early rollout. Built on top of the tools you already pay for. |
| system.html | How It Works — Custom Operations Systems \| itsnemo.dev | Role-based access, records, analytics, and an AI trained on your documents. What each one does in practice, and what ongoing support costs. |
| portfolio.html | Case Studies — Operations Systems in the Field \| itsnemo.dev | Three builds: a children's museum with ~60 staff, a college athletics department, and a university advising office. |
| about.html | About — Nehemiah Cionelo, Developer in Gunnison, Colorado | Developer in Gunnison, Colorado. I build custom internal operations systems for small organizations, and I work remotely with clients anywhere. |

- Canonical: `https://itsnemo.dev/work/<file>` on every page (`index.html` → `https://itsnemo.dev/work`).
- `og:image`: `https://itsnemo.dev/work/assets/logo-full.png` on every page until a real share image exists.
- `og:title` / `og:description` mirror the table above.

---

## index.html

### Hero
- Eyebrow: Custom operations systems · Gunnison, Colorado & remote
- H1 line 1: Your team's work lives in five places.
- H1 accent line: It should live in one.
- Subline: I build one internal system per organization. Who can see what, every record in one place, and the numbers you run on. An AI trained on your own files can come with it.
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
- Card 4 — AI Trained On Your Files (icon `sparkles`): Ask it about your own documents. It answers, and names the file it came from. Rolling out now with a first group of organizations.

### Built on what you already pay for
- Eyebrow: How it fits
- Title: It sits on top of what you already use.
- Body: Your registration system, your payroll, your file storage all stay where they are. I don't rebuild software you're already paying for. The system connects to what's there, links out to it, and owns only the parts nothing else covers. Try to replace all of it at once and you get a migration that takes months instead of something you're using in weeks.

### Proof
- Eyebrow: Recent work
- Line 1: A children's museum. About 60 staff, subs, and volunteers on one schedule, with family information locked down.
- Line 2: A college athletics department. 5,100+ records in one place, three staff working the same list, camp attendance up 75%.
- Line 3: A university advising office. An assistant that answers from the office's own documents and cites the file it used.
- Link: Read the case studies →

### How this works
- Eyebrow: How this works
- Step 1 — Walkthrough · Free: You show me where your team's information actually lives. I map it and tell you what to fix first.
- Step 2 — First build · One-time: The smallest thing that removes the worst friction. You're using it in weeks.
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
- Subline: Free walkthrough. I'll map what you have and tell you what the first build should be, whether or not you hire me.
- Field placeholders: Your name · Your organization · your@email.com
- Textarea placeholder: Where does your team's information actually live right now?
- Submit button: Book a walkthrough
- Success message: Got it. I'll be in touch within 24 hours.

---

## system.html

### Hero
- Eyebrow: The system
- H1: One system, built around how your organization already works.
- Subline: Four parts, one system. Here's what each one does in practice, and what it costs to keep running.

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
- What it is: The handful of questions you ask every month, answered on screen. It isn't a BI tool, and it isn't another spreadsheet you have to rebuild each time.
- What it looks like: Who's under-scheduled this week, and which programs fill while others sit half empty. Last season next to this one on the same screen.
- Why it matters: If a number takes twenty minutes to get, you stop asking for it.

### 4. The AI layer
- One-liner: It answers from your files, and tells you which file.
- What it is: An assistant grounded in your own documents: policies, handbooks, procedures, past records. Ask in plain language and get an answer that names its source.
- How it behaves: It says "not in my knowledge base" instead of inventing an answer. It flags anything it hasn't seen verified in over a year. And it never becomes the official record. It points you to the system that is.
- Your documents stay yours: I keep each organization's material separate from every other client's. Nothing from your files is used to train a model.
- Where it stands: Rolling out with a small first group of organizations. If you're a fit, I'll tell you. If you're not one yet, I'll tell you that too.

### 5. Built on what you already pay for
- One-liner: I don't rebuild what already works.
- Body: Your registration system, your payroll, your file storage stay where they are. The system reads from them, links out to them, and owns only the parts nothing else covers. Replacing software that already works is how a three-week project turns into one that takes many months.

### 6. Who this isn't for
- Intro: Three kinds of projects I turn down, so neither of us wastes a call:
  - Solo operators. One person with a notebook doesn't need this, and I'd be selling you overhead.
  - Anyone who needs it live next week. A first build takes weeks. There's no version of this that ships on Friday.
  - Anyone who wants a marketing website with nothing behind it. I used to do that work. I don't anymore.

### 7. How engagements work
- Step 1 — Walkthrough · Free: We go through where your team's information lives: every spreadsheet, folder, and system. I come back with a map and the one thing worth fixing first.
- Step 2 — First build · One-time, quoted: The smallest system that removes the worst friction. Live in weeks. You use it before you commit to anything bigger.
- Step 3 — Monthly partnership: Hosting, support, fixes, and small changes. The system grows as the organization does, because every organization I've built for needed a second thing about three months after the first.

### 8. What it costs
- Intro: The monthly is published below. The build isn't, because it depends on what you need. That's what the walkthrough is for.

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
- Subline: Names and details are left out on purpose. These are real organizations, and the numbers are counted, not estimated.

### Case 1 — A children's museum
- Tags: Role-based access · Records
- The situation: About sixty staff, subs, and volunteers across three hiring tracks. The schedule lived in two separate documents that drifted apart within days. Finding a sub meant texting people one at a time and hoping. Staff and family information sat in a folder anyone with the link could open.
- What got built: One schedule everyone reads from. A personal "my shifts" view for every person, plus a calendar feed that syncs straight to their phone. A sub-coverage workflow that tracks requested, offered, and confirmed instead of living in text messages. Role-based access so nobody sees more than their job requires.
- What stayed: Registration, billing, and payroll never moved. They're in systems the museum already pays for, and rebuilding them would have been the fastest way to blow the budget.
- Status: Built and delivered. Rollout in progress.

### Case 2 — A college athletics department
- Tags: Records · Analytics · Role-based access
- The situation: Thousands of performance records spread across four incompatible platforms and a stack of PDFs. No way to connect a result to the person running the program behind it. On top of that, three staff needed to work the same list at once without duplicating each other's outreach.
- What got built: One database holding 5,100+ athlete performances, 600+ programs, and 686 coaches and athletic directors across five states and regions, 388 of them with a verified email. Contact discovery with confidence scoring, so nobody wastes a morning on a dead address. Outreach written from what each program did that season: team wins, podium finishes, standout individual races, athletes by name.
- Three people, one list: All three staff worked the same list simultaneously without stepping on each other. That's the role-based access piece, in real daily use.
- The result: Camp attendance up 75% year over year, about forty to seventy-plus. First-time relationships with rural programs nobody had been contacting, and early contact with athletes who matter two seasons from now.

### Case 3 — A university advising office
- Tags: The AI layer
- The situation: Program requirements, testing rules, transfer agreements, and policy spread across a public website, a shared drive, and institutional memory. New staff asked the same questions for months. A wrong answer had consequences for a student's schedule or their aid.
- What got built: An assistant that answers only from the office's own written material. Every answer names the file it came from. Anything not verified in the last twelve months gets flagged as stale. Ask it something outside its coverage and it points you to the right office instead of guessing.
- Where the line is: It never became the system of record, and it says so in every answer that touches one. An assistant that guesses confidently is worse than no assistant.
- Status: Built and delivered as an internal tool. The hosted version is in early rollout.

### Also built
- A public-health advisory firm: a live data dashboard with an access-controlled editor. It replaced a spreadsheet somebody had to re-publish by hand.
- A college coaching staff: timing data from a pile of incompatible vendor formats, in one view.
- A small food business: ordering that writes straight into the sheet the kitchen already uses.

### Bottom CTA
- Headline: Recognize your own operation in any of these?
- Button: Book a walkthrough

---

## about.html

Only these strings change. Everything else on the page stays.

- "Who I am" closing sentence: A computer science degree and a master's in sport management. I've built software, and I've studied how organizations run, which is why the system ends up fitting the organization instead of the other way around.
- Closing CTA headline: Let's talk about where your information lives.
- Closing CTA button: Book a walkthrough
- "How I work with clients" engagement-model sentence: I keep it straightforward. The walkthrough is free and there's nothing to commit to. If you're not sure a system makes sense for your organization, that's the normal place to start, and I'll tell you if the answer is no.

---

## Humanizer pass — rejected changes

Five humanizer suggestions were rejected because they touched protected content. The
copy below stays exactly as written.

- **"about forty to seventy-plus"** (portfolio, Case 2 result). Flagged as a false
  range ("from X to Y"). Rejected — it is a counted figure, not a rhetorical range.
- **"Built and delivered. Rollout in progress."** (portfolio, Case 1 status). Flagged
  as stacked fragments and proposed as one sentence. Rejected — protected status
  wording, verbatim only.
- **"Rolling out with a small first group of organizations."** (system, §4 Where it
  stands). Flagged as vague scope. Rejected — protected status wording, verbatim only.
- **"From $75" / "From $200"** (index Step 3, system pricing table). Flagged as
  hedging. Rejected — published prices, and the tiers are open-ended by design.
- **"Included: … / Quoted separately: …"** (system, §8). Flagged as an inline-header
  vertical list. Rejected — the split is the commercial promise and has to stay
  legible as two lines.

Three further non-changes, for the record:

- The deck's `Label: value` bullet format trips the same inline-header pattern
  throughout. Kept — this is a copy spec, and Tasks 4–9 address strings by these labels.
- "about 60" (index) and "About sixty" (portfolio) refer to the same count. Both
  spellings are approved figures, and the pages are read separately, so the numeral
  stays where the line is scannable and the word stays where it is prose.
- "AI Trained On Your Files" keeps its title-case "On". The design spec fixes this
  card label in three places; changing it here would desync the deck from the spec.

One label change was applied and approved:

- **system.html §4: `What makes it different:` → `How it behaves:`.** The humanizer pass
  renamed it because "what makes it different" is competitive-marketing framing for what
  is plainly a description of behavior. Reviewed and upheld on the merits by Nemo,
  2026-07-24. This is the only sub-label the pass changed. Task 7 pastes it.
