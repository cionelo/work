# SDD ledger — plan: docs/superpowers/plans/2026-07-24-work-website-product-pivot-plan.md
Task 1: complete (commits 0cdea60..48caf78, review clean)
Task 2: review findings 2 important (status line "approved" is plan-mandated text — needs human ruling; sub-label rename "What makes it different" -> "How it behaves" deviates from brief), 1 minor deferred ("every place I have built for" register regression); commits 48caf78..f0bfb63
Task 2: paused at plan-mandated human review gate (Step 5)
Task 2: fix round 1/5 (2 addressed, 0 open; commits f0bfb63..aae0559)
Task 2: minor (deferred): deck status line attributes approval to Nemo by name — he delegated judgment, did not state he read the deck; reword to non-attributive
Task 2: minor (deferred): heading "Humanizer pass — rejected changes" now also holds one approved change; rename to "rulings and rejected changes"
Task 2: complete (commits 48caf78..aae0559, review clean after 1 fix round)
Task 3: implemented (commit aae0559..c36959d) — implementer concern: checker cannot see og:image because TAG_RE matches only href/src and the og value is an absolute URL. Plan Task 4 Step 4 verification assumed the checker gates this. Controller ruling: real gap, enters Task 3 fix loop as an og:image resolution check.
Task 3: minor (deferred): TAG_RE matches only double-quoted attributes; single-quoted href/src invisible. Latent, no live instances.
Task 3: fix round 1 dispatched — strip_comments newline collapse (line numbers off by 31 after multi-line comments) + narrow og:image local resolution for https://itsnemo.dev/work/ prefixed content values.
Task 3: fix round 1/5 (2 addressed, 0 open; commits c36959d..882d130)
Task 3: complete (commits aae0559..882d130, review clean after 1 fix round)
Task 3: minor (deferred): og:url values are also resolved as local targets, broader than specified; harmless today since those pages exist.
Task 4: complete (commits 882d130..980dd89, review clean)
Task 4: minor (deferred): og:image stopgap logo-full.png is 3.8MB — heavy for a share image; fold into the demo-assets session that makes the real 1200x630.
Task 5: complete (commits 980dd89..ebf7ded, review clean). Checker 9 -> 15; all 6 new problems are missing target -> system.html, resolved by Task 7.
Task 6: complete (commits ebf7ded..d06241d, review clean)
Checker fix (out-of-band, commit f227376): REQUIRED_PAIRS scoped to portfolio.html — index.html proof line was an unclearable false positive. Rule verified still firing on portfolio.html.
Task 6: minor (deferred): browser-only verification not possible for any subagent — hero GSAP entrance, scroll reveals, console errors, 375px horizontal scroll, and 4-card grid at >=1024px all need a human spot-check.
Task 7: implemented (commits f227376..0df07dc) — checker 16 -> 6; cleared page-missing, 8 nav dead links, and the retired services.html Nashville hit.
Task 7: complete (commits f227376..0df07dc, review clean, no findings)
Task 8: implemented (commits 0df07dc..52e6ea5) — gate reaches PASS for the first time. Implementer flagged stale portfolio bottom CTA ("Free estimates always") — folded into Task 9, which greps for it.
Task 8: fix round 1 dispatched — bottom CTA still carried old free-estimate framing while the same page nav said Book a walkthrough.
Task 8: fix round 1/5 (1 addressed, 0 open; commits 52e6ea5..5e81f89)
Task 8: complete (commits 0df07dc..5e81f89, review clean after 1 fix round)
Task 9: implemented (commits 5e81f89..da8f5e5) — gate PASS; 4th edit (stale free-estimate prose) applied and back-written to the deck.
Task 9: complete (commits 5e81f89..da8f5e5, review clean)
Task 9: minor (deferred): <br> placement in about.html CTA headline was an unspecified formatting choice mirroring index.html.
FINAL REVIEW (opus, commits 5a46b2d..da8f5e5): 5 Critical, 7 Important, 6 Minor. Verdict: do not merge until Criticals fixed.
Parked ruling: Important 7 (about.html bio names WCU running program; anonymized athletics case is XC/track — adjacent pages de-anonymize by inference). Ruling: the linkage is to Nemo own institution and his own outreach work; disclosure risk is his to accept. Surfaced to him rather than silently softening the proof.
Parked ruling: Important 9 (2.2MB hero logo + 360KB nav logo = ~2.6MB above fold). Real, pre-existing, not introduced by this branch. Ruling: fix in the demo-assets session alongside the 1200x630 share image; recorded in CLAUDE.md TODO.
Ruling: Important 12 (three hiring tracks) — verified in the client ops audit (Museum Floor, Events, Programs). Stays; added to the cleared-figures list.
Final fix wave: complete (commits da8f5e5..5395493) — all 9 findings ADDRESSED, scoped re-review clean, no regressions.
Residual: index.html proof line "attendance up 75%" -> "camp attendance up 75%" dispatched as a one-line consistency fix.
Residual fix: complete (commit 2a9265c). Branch clean, gate PASS, 19 commits, nothing pushed.
STATUS: ready for human browser verification and owner merge decision.
