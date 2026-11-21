# Security policy

sts2-trainer reads and writes to the memory of a live game process. That
means the tool itself is a privileged surface. We treat the following as
security-relevant bugs:

- Arbitrary file write outside `%LOCALAPPDATA%\sts2-trainer\`.
- Code execution triggered by a malicious save file or map seed.
- Any way the trainer can be coerced into patching a **non**-`SlayTheSpire2.exe`
  process (see `src/Infrastructure/process_guard.py`).
- Signature/pattern scan that can be hijacked via env vars.

## Reporting
Email `security@sts2-trainer.invalid` (PGP key in `docs/keys/`) or open a
private advisory on GitHub. Do **not** file a public issue for
process-injection bugs.

## Scope
Only the current release line (0.6.x) is supported. Old releases that
still ship hardcoded offsets are out of scope.