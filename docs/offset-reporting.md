# Offset reporting

When a game patch breaks a cheat, file an issue with:

- Game build id (from `SlayTheSpire2.exe` version resource)
- Which cheat broke (`godmode`, `energy`, `draw`, `gold`, `map_reveal`)
- The pattern that failed to match (from `logs/scan.log`)
- A short clip if the symptom is visual

Offsets are stored as `(name, pattern, build_id)` tuples in
`src/Core/Models/offsets.py`. Re-dump with:

```
python scripts/dump_offsets.py --pid <pid> --out snapshots/
```