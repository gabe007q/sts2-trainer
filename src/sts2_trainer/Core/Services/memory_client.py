"""Thin wrapper around pymem with pattern-scan helpers."""
from __future__ import annotations

import struct
from typing import Optional

import pymem
import pymem.process

from sts2_trainer.Core.Models.offsets import Offset


class MemoryClient:
    def __init__(self, pm: "pymem.Pymem") -> None:
        self._pm = pm
        self._cache: dict[str, int] = {}

    @classmethod
    def attach_current(cls) -> "MemoryClient":
        pm = pymem.Pymem("SlayTheSpire2.exe")
        return cls(pm)

    @property
    def pid(self) -> int:
        return self._pm.process_id

    def resolve(self, off: Offset) -> int:
        if off.name in self._cache:
            return self._cache[off.name]
        module = pymem.process.module_from_name(self._pm.process_handle, off.module)
        base = module.lpBaseOfDll
        addr = self._pm.pattern_scan_module(off.pattern, module)
        if not addr:
            raise RuntimeError(f"pattern for {off.name} not found on build {off.build_id}")
        self._cache[off.name] = addr
        return addr

    def read_int(self, addr: int) -> int:
        return struct.unpack("<i", self._pm.read_bytes(addr, 4))[0]

    def write_int(self, addr: int, value: int) -> None:
        self._pm.write_bytes(addr, struct.pack("<i", value), 4)

    def try_resolve(self, name: str, off: Offset) -> Optional[int]:
        try:
            return self.resolve(off)
        except Exception:
            return None