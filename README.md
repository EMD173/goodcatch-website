# GoodCatch — company website (4 Black Centuries LLC)

One self-contained file: `index.html`. No build step, no dependencies, no JavaScript required.

## Live infrastructure (as of June 10, 2026)

- **Site:** https://goodcatchapp.com — hosted free on GitHub Pages from
  https://github.com/EMD173/goodcatch-website (push to `main` = deploy, ~1 min).
- **Domains:** `goodcatchapp.com` + `4blackcenturies.com`, both registered at Porkbun
  (account: 4BCLLC), ~$11.08/yr each, auto-renew on, WHOIS privacy on.
  `4blackcenturies.com` 302-redirects (wildcard) to the GoodCatch site via Porkbun URL forwarding.
- **DNS** (`goodcatchapp.com`, managed at Porkbun): four A records → GitHub Pages
  (185.199.108–111.153), `www` CNAME → `emd173.github.io`, MX `fwd1`/`fwd2.porkbun.com`
  (free email forwarding) + SPF TXT.
- **Email:** `hello@goodcatchapp.com` forwards to Eli's Gmail via Porkbun's free forwarding.
  Up to 20 aliases free — add more in Porkbun → Email.
- **To edit the site:** change `index.html`, then `git add -A && git commit && git push`.
- **CNAME file** in this repo must stay — it tells GitHub Pages the custom domain.

## What was deliberately left OFF the site (keep it that way)

- The EIN (lives only in the IRS letter — never on the web).
- The street address (it's the home address; the footer says only "Leeds, Alabama").
- Personal phone number.
- The school's name ("Putnam") and the district's name ("Birmingham City Schools") — the
  pilot isn't district-approved yet, so the site says only "a Birmingham, Alabama middle
  school." Name the school only after the district relationship is signed.
- Any claim that 5:1 is a validated threshold — the research section uses the
  "research-aligned nudging" framing per the market-research doc.

## Naming note

The public/product name is **GoodCatch** (matches the Mercury/D-U-N-S filings).
"Panther TRIBE Tracker" is the Putnam-branded pilot skin and stays out of public marketing.
