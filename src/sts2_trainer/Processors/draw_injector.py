"""Draw injector cheat: bump the draw pile count each tick."""
from __future__ import annotations

from sts2_trainer.Core.Models.game_state import GameSnapshot
from sts2_trainer.Core.Models.offsets import OFFSETS
from sts2_trainer.Core.Services.memory_client import MemoryClient
from sts2_trainer.Processors.base import Processor


class DrawInjector(Processor):
    def __init__(self, mem: MemoryClient, extra: int = 2) -> None:
        self.mem = mem
        self.extra = extra

    def apply(self, snap: GameSnapshot) -> None:
        addr = self.mem.try_resolve("draw_pile_count", OFFSETS["draw_pile_count"])
        if addr is None:
            return
        new_count = snap.combat.draw_pile + self.extra
        self.mem.write_int(addr + OFFSETS["draw_pile_count"].extra, new_count)
        snap.combat.draw_pile = new_count