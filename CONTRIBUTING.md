# Contributing to sts2-trainer

Thanks for considering a patch. This is a hobbyist cheat trainer for
**Slay the Spire 2** — memory patchers, overlay widgets, and a console
that talks to the game process.

## Ground rules
- Everything is **for educational / single-player use only**. Do not use
  any of this in multiplayer or against other players.
- All offsets live in `src/Core/Models/offsets.py` and must be tagged with
  the game build id they were dumped against. Bump the build id when you
  re-dump.
- New cheat features go through the pipeline: an **ingest handler**
  (`src/Ingest/`) that reads game state, a **processor**
  (`src/Processors/`) that mutates it, and optionally an **output driver**
  (`src/OutputDrivers/`) that renders or logs the result.

## Workflow
1. Fork, branch, `pip install -e ".[dev]"`.
2. Add tests under `tests/` — mock the `pymem` handle, do not require the
   game to be running.
3. Run `pytest` and `ruff check .`.
4. Open a PR describing the build id you tested against.

## Reporting offset breakage
Use the `docs/offset-reporting.md` template and include the game's
`build_id.txt` hash.