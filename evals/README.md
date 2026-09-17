# Cold-start evaluations

These cases test whether a fresh Codex session can discover and apply the skill suite without hidden project knowledge.

Run each case from a clean session against the repository root. Do not preload specialist skills manually unless the case explicitly invokes one.

## Core pass criteria

- routes broad requests through `brand-design` and narrow requests to the correct specialist
- extracts a useful brief without asking low-value questions
- produces materially distinct directions when exploration is requested
- does not fabricate company facts, images, credentials, or production verification
- distinguishes concept/spec/prompt from an actually created artifact
- uses concrete design language rather than vague adjectives
- invokes an independent review mindset after creation
- gives printer/vendor requirements priority in production work

Record failures by category: routing, brief, concept diversity, source truth, artifact claim, design specificity, review quality, production boundary.
