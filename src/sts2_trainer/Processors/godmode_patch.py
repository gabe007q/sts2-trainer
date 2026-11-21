"""Godmode cheat: hold HP at a floor by rewriting the HP field each tick."""
from __future__ import annotations

from sts2_trainer.Core.Models.game_state import GameSnapshot
from sts2_trainer.Core.Models.offsets import OFFSETS
from sts2_trainer.Core.Services.memory_client import MemoryClient
from sts2_trainer.Processors.base import Processor


class GodmodePatch(Processor):
    def __init__(self, mem: MemoryClient, hp_floor: int = 1) -> None:
        self.mem = mem
        self.hp_floor = hp_floor

    def apply(self, snap: GameSnapshot) -> None:
        if snap.player.hp >= self.hp_floor:
            return
        addr = self.mem.try_resolve("player_hp", OFFSETS["player_hp"])
        if addr is None:
            return
        self.mem.write_int(addr + OFFSETS["player_hp"].extra, self.hp_floor)
        snap.player.hp = self.hp_floor