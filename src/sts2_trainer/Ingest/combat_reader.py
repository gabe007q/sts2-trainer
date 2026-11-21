"""Reads the current combat state from Slay the Spire 2."""
from __future__ import annotations

from sts2_trainer.Core.Models.game_state import (
    CombatState, GameSnapshot, PlayerState,
)
from sts2_trainer.Core.Models.offsets import OFFSETS, CURRENT_BUILD
from sts2_trainer.Core.Services.memory_client import MemoryClient
from sts2_trainer.Ingest.base import IngestHandler


class CombatReader(IngestHandler):
    def __init__(self, mem: MemoryClient) -> None:
        self.mem = mem

    def read(self) -> GameSnapshot | None:
        hp_addr = self.mem.try_resolve("player_hp", OFFSETS["player_hp"])
        en_addr = self.mem.try_resolve("player_energy", OFFSETS["player_energy"])
        draw_addr = self.mem.try_resolve("draw_pile_count", OFFSETS["draw_pile_count"])
        gold_addr = self.mem.try_resolve("gold", OFFSETS["gold"])
        if not (hp_addr and en_addr):
            return None

        player = PlayerState(
            hp=self.mem.read_int(hp_addr + OFFSETS["player_hp"].extra),
            max_hp=80,
            energy=self.mem.read_int(en_addr + OFFSETS["player_energy"].extra),
            max_energy=3,
            gold=self.mem.read_int(gold_addr + OFFSETS["gold"].extra) if gold_addr else 0,
        )
        combat = CombatState(
            turn=1,
            hand_size=5,
            draw_pile=self.mem.read_int(draw_addr + OFFSETS["draw_pile_count"].extra) if draw_addr else 0,
            discard_pile=0,
        )
        return GameSnapshot(player=player, combat=combat, floor=1, act=1, build_id=CURRENT_BUILD)