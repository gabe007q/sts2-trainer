"""Output driver protocol — render a GameSnapshot somewhere."""
from __future__ import annotations

from abc import ABC, abstractmethod

from sts2_trainer.Core.Models.game_state import GameSnapshot


class OutputDriver(ABC):
    enabled: bool = True

    @abstractmethod
    def render(self, snap: GameSnapshot) -> None:
        raise NotImplementedError