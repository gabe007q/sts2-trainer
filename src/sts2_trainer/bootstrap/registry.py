"""Default wiring for the pipeline stages."""
from __future__ import annotations

from sts2_trainer.Core.Services.memory_client import MemoryClient
from sts2_trainer.Ingest.base import IngestHandler
from sts2_trainer.Ingest.combat_reader import CombatReader
from sts2_trainer.Processors.base import Processor
from sts2_trainer.Processors.godmode_patch import GodmodePatch
from sts2_trainer.Processors.energy_refill import EnergyRefill
from sts2_trainer.Processors.draw_injector import DrawInjector
from sts2_trainer.OutputDrivers.base import OutputDriver
from sts2_trainer.OutputDrivers.console_hud import ConsoleHud
from sts2_trainer.OutputDrivers.overlay_window import OverlayWindow


def load_defaults(
    mem: MemoryClient, cheats: list[str]
) -> tuple[list[IngestHandler], list[Processor], list[OutputDriver]]:
    handlers: list[IngestHandler] = [CombatReader(mem)]

    procs: list[Processor] = []
    if "godmode" in cheats:
        procs.append(GodmodePatch(mem))
    if "energy" in cheats:
        procs.append(EnergyRefill(mem))
    if "draw" in cheats:
        procs.append(DrawInjector(mem))

    drivers: list[OutputDriver] = [ConsoleHud(), OverlayWindow(enabled=True)]
    return handlers, procs, drivers