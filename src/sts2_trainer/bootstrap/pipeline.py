"""Tick loop that wires ingest handlers to processors to output drivers."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Iterable

from sts2_trainer.Core.Models.game_state import GameSnapshot
from sts2_trainer.Core.Services.memory_client import MemoryClient
from sts2_trainer.Ingest.base import IngestHandler
from sts2_trainer.Processors.base import Processor
from sts2_trainer.OutputDrivers.base import OutputDriver


@dataclass
class Pipeline:
    tick_ms: int = 250
    cheats: list[str] = field(default_factory=list)
    handlers: list[IngestHandler] = field(default_factory=list)
    processors: list[Processor] = field(default_factory=list)
    drivers: list[OutputDriver] = field(default_factory=list)

    def __post_init__(self) -> None:
        from sts2_trainer.bootstrap.registry import load_defaults
        mem = MemoryClient.attach_current()
        self.handlers, self.processors, self.drivers = load_defaults(mem, self.cheats)

    def run(self, max_ticks: int | None = None) -> None:
        ticks = 0
        while max_ticks is None or ticks < max_ticks:
            snap: GameSnapshot | None = None
            for h in self.handlers:
                snap = h.read()
                if snap is not None:
                    break
            if snap is None:
                time.sleep(self.tick_ms / 1000)
                continue

            for p in self.processors:
                if p.enabled:
                    p.apply(snap)

            for d in self.drivers:
                d.render(snap)

            ticks += 1
            time.sleep(self.tick_ms / 1000)