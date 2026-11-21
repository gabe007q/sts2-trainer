"""Energy refill cheat: top up energy each tick."""
from __future__ import annotations

from sts2_trainer.Core.Models.game_state import GameSnapshot
from sts2_trainer.Core.Models.offsets import OFFSETS
from sts2_trainer.Core.Services.memory_client import MemoryClient
from sts2_trainer.Processors.base import Processor


class EnergyRefill(Processor):
    def __init__(self, mem: MemoryClient, target: int = 99) -> None:
        self.mem = mem
        self.target = target

    def apply(self, snap: GameSnapshot) -> None:
        if snap.player.energy >= self.target:
            return
        addr = self.mem.try_resolve("player_energy", OFFSETS["player_energy"])
        if addr is None:
            return
        self.mem.write_int(addr + OFFSETS["player_energy"].extra, self.target)
        snap.player.energy = self.target