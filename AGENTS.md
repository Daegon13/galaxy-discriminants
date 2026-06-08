# AGENTS.md

## Project role

This repository is a scientific computing prototype for galaxy rotation curve analysis and discriminant galaxy selection.

The project compares families of models such as baryonic/Newtonian baselines, MOND/RAR, NFW halos, Burkert halos, and future hybrid models.

The goal is not to solve dark matter or propose a new theory of gravity. The goal is to build a reproducible computational framework for ranking galaxies by their usefulness for discriminating between competing model families.

## Required reading before work

Before making code changes, read these files in this order:

1. `PROJECT_MASTERPLAN.md`
2. `PATCH_ROADMAP.md`
3. `DECISIONS_LOG.md`
4. `CODEX_TASK_PROMPT.md`

Use `CODEX_TASK_PROMPT.md` as the active task for the current patch.

If the active task conflicts with the roadmap, stop and report the conflict instead of guessing.

## Development environment

Use:

- Python 3.12
- `uv`
- `src/` layout
- `pytest`
- `ruff`

Standard commands:

```powershell
uv sync
uv run python --version
uv run pytest
uv run ruff check .
```

Python must remain 3.12.x unless a change is explicitly requested.

Do not replace `uv` with `pip`, Poetry, Conda, npm, pnpm, or another package manager.

## Repository structure expectations

Expected top-level structure:

```text
galaxy-discriminants/
├── AGENTS.md
├── README.md
├── PROJECT_MASTERPLAN.md
├── PATCH_ROADMAP.md
├── CODEX_TASK_PROMPT.md
├── DECISIONS_LOG.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── src/
├── tests/
├── data/
├── outputs/
└── reports/
```

Expected Python package location:

```text
src/galaxy_discriminants/
```

Prefer package modules over loose scripts.

## Scope control

Work only on the requested patch.

Do not advance to the next roadmap version without explicit approval.

For `v0.1`, the active scope is:

- use only mock/synthetic data;
- create a reproducible skeleton;
- create minimal mock data structures;
- create placeholder models only;
- create basic visualization;
- create basic tests;
- update README with executable commands.

For `v0.1`, do not:

- download real datasets;
- implement real MOND/RAR;
- implement real NFW;
- implement real Burkert;
- implement real discriminant ranking;
- implement scientific conclusions;
- add web dashboards;
- add AI/ML;
- add MCMC;
- add N-body simulations;
- add heavy dependencies;
- move to v0.2 without approval.

## Scientific honesty rules

Do not claim that the project:

- solves dark matter;
- proves or disproves MOND;
- proves or disproves dark matter halos;
- produces scientific conclusions from mock data;
- validates a theory using synthetic data only.

Clearly mark:

- facts;
- assumptions;
- pending verification;
- risks;
- future extensions.

SPARC and BIG-SPARC must be treated as pending verification until availability, format, license, and usage constraints are checked.

If a scientific formula, dataset, parameterization, or model choice is not verified, mark it as `Pending verification`.

## Code style

Prefer:

- small modules;
- explicit names;
- typed functions where useful;
- simple data structures;
- reproducible outputs;
- deterministic tests;
- clear error messages;
- documented units;
- pure functions where reasonable.

Avoid:

- hidden global state;
- large scripts;
- unnecessary dependencies;
- premature optimization;
- scientific formulas without documentation;
- undocumented unit assumptions;
- broad refactors unrelated to the active patch.

## Testing rules

Every patch should preserve or improve the test suite.

Run:

```powershell
uv run pytest
uv run ruff check .
```

If a test cannot be run, explain why.

If you change formatting, prefer:

```powershell
uv run ruff format .
```

Do not hide large behavioral changes inside automatic formatting or auto-fix commands.

## Data policy

Do not commit real datasets unless explicitly approved.

Use:

- `data/mock/` for synthetic data;
- `data/raw/` for raw external data;
- `data/processed/` for processed data;
- `outputs/` for generated outputs;
- `reports/` for generated reports.

Do not remove `.gitkeep` files unless replacing them with intentional tracked files.

Do not commit large binary files, generated plots, notebooks with huge outputs, archives, or downloaded datasets unless explicitly approved.

## Documentation rules

Documentation must be sober, technical, and defensible.

Use Spanish for project documentation unless the active task says otherwise.

When updating docs, distinguish:

- Decisión tomada;
- Supuesto;
- Pendiente de verificación;
- Riesgo;
- Extensión futura.

Do not invent citations, papers, links, dataset URLs, APIs, or scientific results.

## Dependency rules

Avoid new dependencies unless strictly necessary.

If adding a dependency, report:

- dependency name;
- reason;
- why existing dependencies were insufficient;
- whether it is runtime or development-only.

Keep the project suitable for a thesis/prototype, not a production SaaS or web app.

## Git and file safety

Do not:

- reinitialize Git;
- delete `.git`;
- rewrite history;
- remove `uv.lock`;
- remove `.python-version`;
- rename the package without approval;
- change the project architecture without approval.

Before large changes, inspect existing files.

Prefer small, reviewable patches.

## Summary required after each task

At the end of every task, report:

1. Files modified.
2. What was implemented.
3. What was intentionally not implemented.
4. Tests executed.
5. Results of tests.
6. Decisions made.
7. Risks or pending items.
8. Suggested next step.

Do not start the next patch unless explicitly instructed.

## Current patch reminder

The initial active task is `v0.1 — Skeleton reproducible con datos mock`.

Use `CODEX_TASK_PROMPT.md` as the exact task prompt.
