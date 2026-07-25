# itsnemo.dev/work — Product Pivot Design

**Date:** 2026-07-24
**Status:** Approved. Implementation plan to follow.
**Supersedes:** the positioning in `worksite-revamp-design-2026-03-06.md` (structure and voice, not the stack)

---

## 1. What changes

The site sells 12 services in three buckets. It will sell one thing.

> **A custom internal operations system: role-based access, records in one place, and analytics that answer real questions — built on top of the tools the organization already pays for. An AI trained on their own documents comes with it.**

Four capabilities, one product. The AI is a module inside the system, never a separate offer.

**Why:** a menu reads junior. Depth in one product reads senior, and senior is what gets paid on retainer.

**No brand name for the product.** A name implies a SaaS with an uptime page and a support team. Use the phrase "operations system" consistently instead.

---

## 2. Who it's for

Organizations with 10–100 staff, several systems that don't talk to each other, and records that matter — nonprofits, camps, clinics, advisory firms, university offices, athletic departments. They have no internal IT, which is why they buy retainers.

Out: the restaurants / gyms / retail grid. Those stay as one-line examples at most.

---

## 3. Voice

| Cut | Why |
|---|---|
| "at prices local businesses can actually afford" | Price-led positioning sells one-offs, not retainers |
| "You don't need a dev team" | Frames you as the cheap substitute, not the engineer |
| The six-card ICP grid | Replaced by the shape of the buyer, not a list of industries |

Keep: plain English, no jargon, free walkthrough, the before/after section.

**Every string of copy runs through `/humanizer` before it lands in HTML.** No exceptions.

---

## 4. Hero

- **Eyebrow:** Custom operations systems · Gunnison, Colorado & remote
- **H1:** Your team's work lives in five places. / *It should live in one.*
- **Sub:** One internal system per organization — who can see what, every record in one place, the numbers you actually need, and an AI trained on your own files. Built on top of the tools you already pay for, not instead of them.
- **CTA:** Book a walkthrough · *See how the system works →*

---

## 5. Pages

Four pages stay four pages. Static HTML/CSS/vanilla JS. No framework, no build step.

**Nav:** `[logo] Case Studies · How It Works · About · [Book a walkthrough]`

### index.html

| Section | Change |
|---|---|
| Hero | Rewritten (§4) |
| Before / After | Keep the shape. Rewrite "after" around access, records, analytics |
| The system | Four cards: Role-Based Access · Records & CRM · Analytics · AI Trained On Your Files |
| Built on what you already pay for | New. The thin-layer posture in three sentences — the single strongest trust builder, and the site doesn't say it today |
| Proof | Three one-line results linking to case studies |
| How this works | New. Walkthrough → first build → monthly partnership (§7) |
| Contact | Keep Formspree `mqeykwbq`. New prompt: "Where does your team's information actually live right now?" |

Deleted: "Who I Help" grid, "What I Build" grid.

### services.html → system.html

New file `system.html` holds the deep dive. `services.html` becomes a redirect stub (canonical + meta refresh) so existing links don't 404.

Sections: what it is → role-based access → records → analytics → **the AI layer** → built on what you already pay for → **who this isn't for** → how engagements work → what it costs.

The 12-service menu is deleted. Website work and SEO survive only as a sentence inside "the client-facing surface of your system."

**Who this isn't for:** solo operators, anyone who needs it live next week, anyone wanting a marketing site with nothing behind it. Turning work away in print is the fastest senior signal there is, and it cuts unqualified inquiries.

### portfolio.html

Filename stays; the page is titled "Case Studies." Three studies, one per capability. Anonymized. Each gets a styled empty visual slot with descriptive alt text and a `TODO` comment — never a broken image.

**1. A college athletics department** — *records + analytics + role-based access*
Results scattered across four platforms and PDFs in five states, with no way to tie a performance to the coach behind it. Now: one database of 5,100+ athlete performances, 600+ programs, and 686 coaches and athletic directors — 388 with a verified email. **Three coaches worked the same list in parallel without stepping on each other.** Recruiting outreach names the athlete and the race instead of blasting a form letter.

**Result: camp attendance up 75% year over year** (~40 to 70+), plus first-time relationships with rural programs that never get contacted and early touches on athletes who matter for college recruiting two seasons out.

Lead this case study with the parallel-coaches detail, not a count. It demonstrates role-based access on real users on the same page that claims it — no number does that.

**2. A children's museum with ~60 staff, subs, and volunteers** — *access + records*
Two schedules that drifted apart, subs found by texting one person at a time, family and staff information sitting behind an "anyone with link" URL.
Status wording: **built and delivered; rollout in progress.**

**3. A university advising office** — *the AI layer*
Answers from the office's own documents, cites the file it came from, flags anything unverified in over a year, and says "not in my knowledge base" instead of guessing.

Then one line each, no cards: an advisory firm's data dashboard, a coach analytics dashboard, a food business's ordering layer.

Removed: Nashville Home Improvements — a marketing site with an SEO ask is exactly the generalist read being killed.

### about.html

Light retune. The CS degree plus the Sport Management master's stops being a fun fact and becomes the credential: software built, and organizations studied. That's why the system fits the org instead of the reverse. Gunnison and remote sections stay. CTA becomes "Book a walkthrough."

---

## 6. Visuals

Every case study gets a placeholder slot, not a screenshot. Real demos require redacted screenshots or dummy-data instances — **a separate session**, recorded as a TODO in a new `work-website/CLAUDE.md`.

---

## 7. Engagement model

1. **Walkthrough** — free. You show me where your team's information actually lives. I map it and name the first slice.
2. **First build** — one-time. The smallest thing that removes the worst friction. Live in weeks.
3. **Monthly partnership** — hosting, support, and continued build.

The line that makes it land: *you're not buying a finished deliverable that starts rotting the day it ships.*

Plus a capacity line — *I work with a small number of organizations at a time.* True, filters tire-kickers, creates urgency.

### Published monthly tiers

The monthly is published. The build price is not — it comes from the walkthrough.

| Tier | Price | Who it's for |
|---|---|---|
| Single tool | **$75/mo** | One tool, a handful of people, no role-based access |
| Team system | **$150/mo** | Full system with role-based access, up to 40 accounts |
| Organization | **from $200/mo** | Over 40 accounts |

**Included:** hosting, support, fixes, and small changes.
**Quoted separately:** new features and expansions.

At these numbers, publishing removes fear rather than creating it, and the account ladder qualifies buyers without a sales call. "From $200" on the top tier keeps a 400-person organization from holding the lowest price forever — that client is the highest support load and would otherwise be the worst-paying account.

**Placement:** the full table lives on `system.html` only. The home page says *ongoing support starts at $75/month* and links to it. A $75 figure near the top of the home page would anchor the whole offering low before the reader knows what the system is.

The middle tier matches the museum's signed $150/mo, so the ladder is already consistent with a real contract.

---

## 8. Honesty guardrails

Hard constraints. The infrastructure today is a shared quantized model on a laptop with a 5–10 person beta cohort.

| Never | Instead |
|---|---|
| Uptime %, SLA, "24/7", HIPAA / FERPA / SOC 2 | Say nothing about uptime |
| "Trusted by teams everywhere" | "Rolling out with a small first group of organizations" |
| Museum system "running in production" | "Built and delivered; rollout in progress" |
| Client names, logos, real screenshots | Sector descriptions, placeholder slots |
| "87% email coverage" | "388 of 686" — the 87% counts empty address fields |
| Any hint the monthly includes unlimited development | "Hosting, support, fixes, and small changes" |

---

## 9. Verified numbers

Every figure below was counted from the source data, not quoted from a README. These are the only numbers cleared for the page.

| Claim | Figure |
|---|---|
| Athlete performances | 5,100+ across 7 state and class championship datasets (plus 1,256 at the Southwest regional) |
| High school programs | 600+ |
| Coach and AD contacts | 686, of which 388 have a verified email |
| Roles tracked | Head coaches, assistants, athletic directors, meet directors |
| Regions | Arizona, Colorado (all four classifications), New Mexico, Utah, Southwest regional |
| Sources unified | 4 platforms plus PDF results |
| Camp attendance | ~40 → 70+, up 75% year over year |
| Parallel users | 3 coaches on one list simultaneously |
| Museum headcount | ~60 staff, subs, and volunteers |

Do not publish "87% email coverage." 388 of 686 is 57%; the 87% figure counted contacts whose email field was present but empty.

---

## 10. Housekeeping

- `og-image.png` is referenced in every page's meta tags and doesn't exist. Every share link is broken today.
- Untrack `.DS_Store`, add `.gitignore`.
- Move old docs to `docs/superpowers/{specs,plans}/` with dated filenames.
- Create `work-website/CLAUDE.md` with project context and the demo-assets TODO.
- SEO shifts toward "custom internal operations system", "role-based access for small teams", "AI trained on company documents". Ground on the affordability keywords is lost on purpose.
- All work on the `product-pivot` branch. Nothing pushed to `main` — that's a live deploy with no staging.

---

## 11. Not in scope

The product architecture document (multi-tenancy, data isolation, RAG design, scaling, cost) that the infrastructure notes call for. Sibling deliverable, separate session.
