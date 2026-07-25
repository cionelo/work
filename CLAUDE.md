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
