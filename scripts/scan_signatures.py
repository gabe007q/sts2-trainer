"""Standalone signature scanner used while re-dumping offsets."""
from __future__ import annotations

import sys

import pymem
import pymem.process


def scan_module(pid: int, module_name: str, pattern: bytes) -> list[int]:
    pm = pymem.Pymem()
    pm.open_process_from_id(pid)
    module = pymem.process.module_from_name(pm.process_handle, module_name)
    hits: list[int] = []
    addr = module.lpBaseOfDll
    end = addr + module.SizeOfImage
    while addr < end:
        found = pm.pattern_scan_module(pattern, module)
        if not found:
            break
        hits.append(found)
        addr = found + 1
    return hits


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: scan_signatures.py <pid> <hexpattern>")
        raise SystemExit(1)
    pat = bytes.fromhex(sys.argv[2].replace("?", "00"))
    for hit in scan_module(int(sys.argv[1]), "SlayTheSpire2.exe", pat):
        print(hex(hit))