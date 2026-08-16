# Security Policy

This is a **documentation repository** (Markdown guides plus two small, self-contained example scripts). It ships no service, stores no user data, and has no runtime attack surface of its own. Even so, we take a few things seriously.

## What counts as a security issue here

- A problem in the **example code** (`examples/`) that could harm someone who runs it — e.g., an unsafe default, a command-injection risk, or an insecure snippet presented as a recommended pattern.
- **Dangerous or misleading guidance** — advice in the docs that, if followed, would make a real system less secure (this repo is partly *about* agent security, so accuracy is a security property).
- A **malicious or hijacked link** in the docs.

For general link rot or typos, please just open a normal issue or PR.

## Reporting

Prefer GitHub's **private vulnerability reporting** ("Report a vulnerability" under the repo's *Security* tab) so details aren't public before a fix. If that isn't available, open an issue that describes the concern **without** including anything that would help someone exploit it, and note that you have security details to share privately.

Please include:

- what the issue is and where (file and line),
- why it's a problem / the impact, and
- a suggested fix if you have one.

## Scope & expectations

- This is a community, best-effort project — there is no paid support or guaranteed SLA.
- Fixes to example code and corrections to guidance are handled like any other change: with a test or reviewed edit (see [CONTRIBUTING.md](./CONTRIBUTING.md)).
- The playbook's own security guidance lives in [docs/security.md](./docs/security.md); improvements there are especially welcome.
