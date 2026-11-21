"""Make sure we only ever attach to Slay the Spire 2."""
from __future__ import annotations

import psutil

ALLOWED_NAMES = {"SlayTheSpire2.exe", "SlayTheSpire2-Win64-Shipping.exe"}


class ProcessGuardError(RuntimeError):
    pass


def require_slay_the_spire(pid: int | None = None) -> psutil.Process:
    if pid is not None:
        proc = psutil.Process(pid)
    else:
        proc = None
        for p in psutil.process_iter(["name", "pid"]):
            if p.info["name"] in ALLOWED_NAMES:
                proc = p
                break
        if proc is None:
            raise ProcessGuardError("SlayTheSpire2.exe not found — launch the game first")

    if proc.name() not in ALLOWED_NAMES:
        raise ProcessGuardError(f"refusing to attach to {proc.name()!r}")
    return proc