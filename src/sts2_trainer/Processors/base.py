"""Processor protocol — mutate game state to apply a cheat."""
from __future__ import annotations

from abc import ABC, abstractmethod

from sts2_trainer.Core.Models.game_state import GameSnapshot


class Processor(ABC):
    enabled: bool = True

    @abstractmethod
    def apply(self, snap: GameSnapshot) -> None:
        raise NotImplementedError