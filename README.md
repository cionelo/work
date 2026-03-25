# itsnemo.dev/work — Handoff README

Freelance services site. Lives at `itsnemo.dev/work/` via GitHub Pages on `cionelo/work` (standalone repo, main branch).

Local path: `/Users/ncionelo/Downloads/JOBS/PROJECTS/work-website/`

---

## Deploy

Push to `main` — Pages builds in ~1 min.

```bash
git add . && git commit -m "..." && git push
```

Remote: `https://github.com/cionelo/work.git`

---

## File structure

```
work-website/
├── index.html        # Homepage: hero, before/after, services, bridge, contact form
├── portfolio.html    # Project cards (Option A — see upgrade notes below)
├── services.html     # Services: websites, automation, SEO
├── about.html        # About: side-by-side headshot + bio
├── style.css         # All styles, single file, ASCII-sectioned
├── main.js           # GSAP anims, mobile nav, contact form, smooth scroll
└── assets/
    ├── Cionelo.jpg                  # Headshot (used on about.html)
    ├── logo-mark.png
    ├── logo-full.png
    └── logo-full-transparent-bg.png
```

---

## Design tokens (`style.css` `:root`)

| Token | Value | Use |
|-------|-------|-----|
| `--bg` | `#1C1917` | Page background |
| `--surface` | `#292524` | Section/card surface |
| `--accent` | `#F59E0B` | Amber — CTAs, icons, tags |
| `--text` | `#F5F0EB` | Primary text |
| `--text-muted` | `#A8A29E` | Secondary text |
| `--font-display` | Bricolage Grotesque | Headings, buttons |
| `--font-body` | DM Sans | Body, nav, labels |

Icons: Lucide via CDN. No build step, no package.json.

---

## Nav pattern

Every page shares the same nav block. To set the active link, add `nav-link--active` (desktop) and `nav-mobile-link--active` (mobile) to the matching anchors. Nav is sticky on all screen sizes.

---

## Adding a page

1. Copy nav block from any existing page, update active classes
2. Add the new link to `nav-links` and `nav-mobile-menu` in **all other pages**
3. Use `.services-hero` + `.services-headline` for the page header
4. Include `style.css` and `main.js`; set unique `<title>`, `<meta name="description">`, `<link rel="canonical">`

---

## Key components

**Card:**
```html
<div class="card card--project reveal">
  <i data-lucide="[icon]" class="card-icon"></i>
  <h3 class="card-title">...</h3>
  <p class="card-desc">...</p>
  <div class="card-tags"><span class="card-tag">Tag</span></div>
  <a href="..." class="card-link" target="_blank" rel="noopener">View project →</a>
</div>
```

Add `class="reveal"` to any element for scroll-triggered fade-up (GSAP, IO fallback).

**Contact form:** Formspree endpoint in `index.html` `<form action="...">`. Success state: `#form-success`.

---

## Portfolio upgrade path

`portfolio.html` uses Option A (icon cards). Option B (screenshot rows) is documented in a comment at the top of that file. Needs real screenshots in `assets/images/`.

---

## Not yet built

- Testimonials section (homepage, below bridge)
- Portfolio screenshots → enables Option B case study layout
- OG image (`assets/og-image.png` — not yet created)
