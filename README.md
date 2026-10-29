# Huddling motion iterations

## Latest

- [Latest MP4: v4 typography revision](out/mission-impact-v4-type.mp4)
- [Editable composition](out/mission-impact-v4/compositions/flow.html)
- [Revision notes and references](out/mission-impact-v4/README.md)
- 1920 × 1080, 30 fps, 18.5 seconds, silent.

The current revision zooms through the submitted button itself, replaces the approval check/confetti with kinetic typography, and connects the ending symbol expansion to the closing copy.

## Earlier versions

| Version | Source | Video |
| --- | --- | --- |
| Flow v1 | [source](out/mission-flow) | [MP4](out/mission-flow-v1.mp4) |
| Studio v2 | [source](out/mission-studio) | [MP4](out/mission-studio-v2.mp4) |
| Studio v3 | [source](out/mission-studio-v3) | [MP4](out/mission-studio-v3.mp4) |
| Impact v4 before typography revision | [archived source files](out/mission-impact-v4/previous-source) | [MP4](out/mission-impact-v4-before-type.mp4) |

The archived v4 files reuse assets from out/mission-impact-v4. To reconstruct that revision, copy the project to a separate folder and replace index.html and compositions/flow.html with the archived versions.

## Preview and render

Use Node.js 24 and FFmpeg installed locally. From the repository root:

```sh
cd out/mission-impact-v4
npx hyperframes@0.8.198 preview
npx hyperframes@0.8.198 check --json
npx hyperframes@0.8.198 render --fps 30 --quality delivery --output ../mission-impact-v4-type.mp4
```

## Project rules

- [Brand and source facts](docs/brand-rules.md)
- [Motion direction and feedback rules](docs/motion-direction.md)
- [Quality checks and mandatory docs updates](docs/quality-review.md)

Runtime caches, temporary screenshots, and bundled executables are not part of this upload.
