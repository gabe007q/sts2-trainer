"""Dataclasses describing the state we care about in Slay the Spire 2."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PlayerState:
    hp: int
    max_hp: int
    energy: int
    max_energy: int
    gold: int
    block: int = 0


@dataclass
class CombatState:
    turn: int
    hand_size: int
    draw_pile: int
    discard_pile: int
    enemies: list[str] = field(default_factory=list)


@dataclass
class GameSnapshot:
    player: PlayerState
    combat: CombatState
    floor: int
    act: int
    build_id: str = "unknown"