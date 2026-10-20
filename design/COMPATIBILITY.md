# Compatibility and validation

Validated on 20 October 2026 against the actual GitHub branch README, not a website mockup.

| Check | Result |
| --- | --- |
| GitHub Markdown/HTML | Rendered natively; headings, links and expandable sections present |
| Images | All nine README image references loaded, with non-zero intrinsic sizes |
| Light theme | Inspected in the in-app browser, including opening and project sections |
| Dark theme | Inspected in signed-in Chrome; body background rgb(13,17,23) |
| Mobile | Actual GitHub viewport 390 × 844; article width 309px; document scroll width 375px; no horizontal overflow |
| Desktop | Actual GitHub viewport 1280 × 900; no horizontal document overflow; additional native Chrome dark preview |
| Motion file | Native GIF, 31 encoded frames from 32 authored frames; infinite loop; 3850ms decoded duration |
| Motion delivery | GIF loads and becomes visible when the native details section opens |
| Motion playback limitation | Browser screenshots did not establish frame advancement: paired captures were identical. File decoding verifies changing frames, but continuous playback in the live page is not independently certified by these captures |
| Reduced motion | Still artwork is the default; animation is behind an explicitly labeled optional expansion. No claim that Markdown automatically responds to prefers-reduced-motion |
| Theme isolation | Artwork includes its own dark backgrounds and contrasting lavender lines; body text follows GitHub's theme |
| Links | Nine unique external URLs returned HTTP 200; LinkedIn returned its access-restriction status 999, so its signed-out content was not verified |
| Local files | All referenced assets exist; all SVGs parse; the GIF contains distinct decoded frames |
| Data accuracy | Product limitations preserved; Sabli backend/integration PRs remain open, frontend on main. No product application code changed |
| Sabli visibility | Found public, explicitly confirmed by the user to remain public; README now links to it |
| NINA | Private status confirmed; no code or internal documentation copied |
| History | Baseline retained in Git; separate design branch and PR, no force push |
| Merge | Awaiting visual approval as requested in the new mission |

## Asset budget

All ten local assets together: 298,600 bytes (about 292 KiB). The hero is 235,964 bytes, the GIF 54,745 bytes and each vector less than 2.4 KB. The unused standalone PNG is the sprite reference; it is not an extra request in the README. No third-party badge, stats or animation service is required.

No full performance benchmark or physical-device test was run. Mobile inspection used browser viewport emulation. Screen-reader access was assessed through native text, heading structure, alternative text and the browser accessibility tree, not a complete assistive-technology audit.

## Deliberate adaptations

The main banner is static by default to keep a quiet opening and respect the brief's accessible alternative to automatic animation. The optional start-screen motion uses an original small companion concept; it does not impersonate Nina. Project cards are light vertical text blocks with small original emblems, rather than a wide table or oversized graphic panels. Skill names are duplicated in selectable Markdown. No scripts, external stylesheets, SVG animation or fake interactive controls are embedded.

Before merge, the remaining visual review includes whether the provisional companion should be replaced by the original Nina reference. After approval and merge, verify the profile page itself again, because this validation was performed on the branch README.

