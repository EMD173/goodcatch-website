# GoodCatch — company website (4 Black Centuries LLC)

One self-contained file: `index.html`. No build step, no dependencies, no JavaScript required.
Open it in a browser to view; upload it anywhere to publish.

## Two placeholders to make real before publishing

1. **Domain** — the site references `goodcatchapp.com`, which is NOT registered yet.
   Check availability (Namecheap/Cloudflare, ~$10–12/yr) for, in order of preference:
   `goodcatchapp.com` · `getgoodcatch.com` · `goodcatch.app` · plus `4blackcenturies.com`
   for the company itself. Whatever you register, it becomes the URL for the Mercury
   "Company website" field and the D-U-N-S application.
2. **Email** — the contact button points to `hello@goodcatchapp.com`. Set up that mailbox
   (Cloudflare Email Routing forwards it to your Gmail for free) or search/replace it in
   `index.html` with an address that exists.

## Deploying (pick one, all free)

- **Netlify Drop** (fastest, ~2 minutes): go to https://app.netlify.com/drop and drag this
  folder onto the page. You get a live URL immediately; connect your custom domain in
  Site settings → Domain management.
- **Cloudflare Pages**: if you register the domain at Cloudflare anyway, create a Pages
  project and upload this folder — domain wiring is one click.
- **Firebase Hosting** (the stack you already know): `firebase init hosting` in this folder,
  set public dir to `.`, then `firebase deploy`.

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
