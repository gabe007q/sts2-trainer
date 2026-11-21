"""Dump candidate offsets from a live SlayTheSpire2.exe for a given build."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pymem
import pymem.process


def scan(pid: int, patterns: dict[str, bytes]) -> dict[str, int]:
    pm = pymem.Pymem()
    pm.open_process_from_id(pid)
    module = pymem.process.module_from_name(pm.process_handle, "SlayTheSpire2.exe")
    out: dict[str, int] = {}
    for name, pat in patterns.items():
        addr = pm.pattern_scan_module(pat, module)
        if addr:
            out[name] = addr - module.lpBaseOfDll
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pid", type=int, required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    from sts2_trainer.Core.Models.offsets import OFFSETS
    pats = {name: off.pattern for name, off in OFFSETS.items()}
    results = scan(args.pid, pats)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "offsets.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"wrote {len(results)} offsets to {out / 'offsets.json'}")


if __name__ == "__main__":
    main()