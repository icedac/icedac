# Profile design and maintenance

Intent → Give icedac a quiet, recognizable profile grounded in current public work.
Behavior → A monochrome interference study, a short introduction and three project links.
Acceptance → Readable on desktop and mobile, light and dark themes, useful without animation.

## Content research — 29 October 2026, Asia/Seoul

| Public source | Observed fact | Use in the profile |
| --- | --- | --- |
| [GitHub profile](https://github.com/icedac) | Display name zhugehyuk; Seoul; link to 2lab.ai and Threads | Name, location and links |
| [llmux](https://github.com/2lab-ai/llmux) and [28 October commit](https://github.com/2lab-ai/llmux/commit/1734ab000341e274c94b537e5886a3e0ad9d0ea7) | Public local AI proxy; recent commit by icedac | Current work, first project |
| [np_alloc](https://github.com/icedac/np_alloc) | C++ per-thread lock-free allocator; repository pushed 3 April 2026 | Systems project |
| [experiments](https://github.com/icedac/experiments) | WebGL prototypes and visual art; repository pushed 28 March 2026 | Computational art project |
| [2lab.ai](https://2lab.ai) | Public tools and experimental AI research | Home link and context |
| [Pinned paper repository](https://github.com/labforadvancedstudy/paper) | Pinned on the public profile | Research link |

“Systems, agents & experiments”, “A continuous work in progress” and “Still curious” are editorial copy, not quoted biography. No private repository contents, unverified titles, audience counts or benchmarks are included. The recent rea and herdr repositories on the personal account are forks; they are not represented here as original projects.

## Profile-format research

- [GitHub's profile README guide](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) establishes the same-name repository convention.
- [GitHub's formatting quickstart](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github) documents `<picture>`, theme-specific images and alternative text.
- [antfu's current profile repository](https://github.com/antfu/antfu) is a reference for concise identity and direct navigation.
- [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) demonstrates the SVG medium for profile motion. Its hosted service and assets are not used here.

These are inspected references, not a claim that one visual style is a universal 2026 trend. The interference sculpture is original geometry generated for this profile.

## Rebuild

```sh
python3 tools/build.py
```

Python's standard library is enough. Edit copy in `README.md`, `STILL.md` and `tools/preview.template.html`; artwork text and geometry live in `tools/build.py`. The generator writes all SVG variants and the single-file `preview.html`.

Open `preview.html` in a browser, or serve this directory locally. The preview has a light/dark switch and pause/play control. It is a companion presentation; GitHub determines the surrounding README font and link styling.

## Motion and accessibility

- Two groups, 64 ellipses each; 32- and 43-second alternating phase changes.
- CSS transform animation only; no JavaScript, fonts, trackers or external requests in the SVGs.
- `prefers-reduced-motion: reduce` disables animation in the SVG and the companion preview.
- `STILL.md` links to separate SVGs with no animation code. This gives visitors a static option even without a system preference.
- The standalone preview pauses when its document is hidden.
- Responsive `<picture>` sources select tall artwork at widths up to 640px, and choose the appropriate palette.
- Native README text and descriptive alt text preserve the key information if images cannot load.

## Review notes

| Before | After | Why |
| --- | --- | --- |
| Bright badges, counters and remote stats cards | Monochrome artwork and three concise project links | A coherent identity with fewer external failure points |
| Generic greeting | Public name, location and current project | Connect the visual design to the person |
| No dedicated motion control | System preference, static version and preview pause button | Let visitors choose motion |

## Verification

See the pull request for the final check results. Verify GitHub's rendered branch README before merging because GitHub sanitizes Markdown independently of the standalone preview.
