# work-website product pivot — session handoff prompt

> Written 2026-07-24. This is a **handoff prompt**, not a plan — the plan is what the
> receiving session produces. Paste the fenced block below into a fresh session.

**Recommended model: Opus 4.8** (`claude-opus-4-8`) — this is positioning and narrative
judgment (what the one product *is*, who it's for, what to stop selling), where a wrong
call causes silent rework across every page. Not schema-driven authoring.

---

```
cd /Users/ncionelo/Downloads/JOBS/PROJECTS/work-website

# Reposition itsnemo.dev/work around one primary product

## Read this first, don't take my summary on faith

Repo: `work-website/` — standalone git repo, remote `github.com/cionelo/work`,
deploys to itsnemo.dev/work/ via GitHub Pages on `main`. Push to `main` = production.
Static HTML/CSS/vanilla JS + GSAP. No build step. Four pages: index, services,
portfolio, about. Existing docs/ has `2026-03-06-worksite-revamp-design.md` and
`docs/plans/2026-03-06-worksite-revamp-plan.md` from the last revamp — read both,
they establish the voice and structure you're changing.

## The problem

The site currently sells three buckets of freelance labor:
  - Websites (custom dev, WordPress, hosting/domains/deploy)
  - Automation & Tools (booking, dashboards, Sheets/Zapier, inventory)
  - SEO & Content (on-page SEO, GBP setup, blog writing)

Hero copy: "You don't need a dev team."

That is no longer what Nemo sells. It reads as a generalist-for-hire menu, and it's
stale (last touched 2026-03).

## What he actually sells now

**One primary product: an all-in-one CRM with a custom LLM/AI trained on the
company's own assets.**

Recent client work is already this product in disguise — treat these as evidence of
the real offering, and mine them for proof points and case studies:
  - `/PROJECTS/bluecove/` — advisory firm site + a Supabase-backed data dashboard
    as the firm's showcase data product
  - `/PROJECTS/trailhead/` — ops tool replacing Drive/spreadsheet chaos for a camp;
    read its CLAUDE.md "systems of record — do NOT rebuild these" section, that
    thin-layer-over-existing-systems posture is a real positioning asset
  - RAS-AI — Nemo will point you at this one

## The architecture reality (constrains what you can promise)

Notion → Nemo Cal → "MBP Setup-VPS" (page id 35b87ba5-08e9-80fc-9d64-c727dafcb330).
Fetch it; the substance:
  - Shared quantized LLM (Ollama / llama.cpp, Qwen-class), NOT per-client models —
    RAM is the binding constraint
  - RAG pipeline over client assets (Drive connect or file upload), pgvector/Qdrant
  - Everything containerized from day one so Mac → VPS is `git pull && docker compose up -d`
  - Rollout: Phase 1 build on the MacBook → Phase 2 5–10 beta testers → Phase 3 VPS
    when there are paying customers
  - Explicitly NOT trusted today for enterprise clients, schools, 24/7 uptime, or
    FERPA-sensitive production data

That last line matters for copy. Do not let the site promise uptime or compliance the
infrastructure can't currently back. The Notion page also asks for a proper
architecture design doc (vision, multi-tenancy, data isolation, RAG design, scaling,
cost) — that's a *sibling* deliverable, not this site. Note it, don't build it here.

## Your job this session — plan only, do not build

1. Invoke `superpowers:brainstorming` and work through it properly. The real
   questions are positioning, not implementation:
   - Does the freelance services menu die, shrink to a footer line, or become the
     on-ramp that feeds the product?
   - Who's the buyer for an AI-native CRM, and is it the same small-business reader
     the current site is written for? If not, the whole voice shifts.
   - How much do you say about the AI before it reads as vaporware? Nemo has shipped
     adjacent things but this product's beta cohort is 5–10 people.
   - Pricing posture: named price, "let's talk", or pilot-first (trailhead's
     $500–$2,000 pilot pattern is a live precedent).
   - What proof exists TODAY that can go on the page, versus what's aspirational.
2. Land a design doc at `docs/superpowers/specs/YYYY-MM-DD-work-website-product-pivot-design.md`
   (note: existing docs sit at `docs/` and `docs/plans/`; move to the
   `docs/superpowers/{specs,plans}/` convention used across /PROJECTS).
3. Then `superpowers:writing-plans` for the implementation plan. Stop there.

## Constraints

- Static HTML/CSS/vanilla JS, no framework, no build step. Keep it.
- Don't push to `main` — that's a live deploy with no staging.
- `.DS_Store` is tracked and dirty in this repo; same untrack cleanup that
  cionelo.github.io-master just got is worth doing.
- File naming: `{description}-{YYYY-MM-DD}.{ext}`
```
