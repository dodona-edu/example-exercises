# example-exercises

Example exercises for Dodona, one top-level directory per judge, plus `reading-activities/` (content pages) and `public/` (images). Teachers clone or fork this repository as a template for their own exercise repositories.

## No Dodona tokens

- Never add an `internals` block (`token`, `_info`) to a `config.json` here, not a new one and not one taken from the production database. People clone this repository and would copy the tokens with it.
- The Dodona server has read-only access to this repository on purpose, so it can't write internals or tokens back. Never propose granting it write access.
- Without tokens, Dodona matches activities by path. Moving or renaming an exercise directory therefore removes the old activity on Dodona and creates a new one, and series that held the old one lose it.

## Layout

- `dirconfig.json` files set defaults per directory: `tested/dirconfig.json` sets the TESTed handler, `suite.yaml` and Python; `tested/<language>/dirconfig.json` overrides the programming language.
- Exercises come in English and Dutch: `description/description.en.md` and `description.nl.md`, with `description.names` for both in `config.json`. A solution with language-specific names gets a `solution.en.*` next to the Dutch one.
- The docs at docs.dodona.be (dodona-edu/dodona-edu.github.io) link to directories here, for example in the judges reference. Check those links before moving or deleting a directory.

## Verifying

Verify TESTed and SQL exercises with the `verify` skill of the dodona-authoring plugin before opening a PR.
