"""Memory offsets for Slay the Spire 2.

Every entry is tagged with the game build id it was dumped against. If the
game ships a patch, re-dump with `scripts/dump_offsets.py` and bump
`CURRENT_BUILD` below.
"""
from __future__ import annotations

from dataclasses import dataclass

CURRENT_BUILD = "sts2-1.0.4.1187"


@dataclass(frozen=True)
class Offset:
    name: str
    module: str
    pattern: bytes
    build_id: str
    extra: int = 0


OFFSETS: dict[str, Offset] = {
    "player_hp": Offset(
        "player_hp", "SlayTheSpire2.exe",
        b"\x48\x8B\x05????\x48\x85\xC0\x74", CURRENT_BUILD, extra=0x10,
    ),
    "player_energy": Offset(
        "player_energy", "SlayTheSpire2.exe",
        b"\x89\x87????\x48\x8B\x5C\x24", CURRENT_BUILD, extra=0x28,
    ),
    "draw_pile_count": Offset(
        "draw_pile_count", "SlayTheSpire2.exe",
        b"\x8B\x87????\xC3\xCC\xCC\x48", CURRENT_BUILD, extra=0x34,
    ),
    "gold": Offset(
        "gold", "SlayTheSpire2.exe",
        b"\x8B\x87????\x48\x8D\x54\x24", CURRENT_BUILD, extra=0x44,
    ),
}