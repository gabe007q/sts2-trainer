"""Ingest handler protocol — read a GameSnapshot from the game process."""
from __future__ import annotations

from abc import ABC, abstractmethod

from sts2_trainer.Core.Models.game_state import GameSnapshot


class IngestHandler(ABC):
    @abstractmethod
    def read(self) -> GameSnapshot | None:
        """Return a snapshot, or None if the game isn't in a valid state."""
        raise NotImplementedError