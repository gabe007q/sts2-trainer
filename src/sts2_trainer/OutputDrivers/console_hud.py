"""Console HUD showing HP / energy / draw pile every tick."""
from __future__ import annotations

from rich.console import Console
from rich.table import Table

from sts2_trainer.Core.Models.game_state import GameSnapshot
from sts2_trainer.OutputDrivers.base import OutputDriver


class ConsoleHud(OutputDriver):
    def __init__(self) -> None:
        self._console = Console()
        self._first = True

    def render(self, snap: GameSnapshot) -> None:
        table = Table(title=f"STS2 — act {snap.act} floor {snap.floor}", show_header=False)
        table.add_row("HP", f"{snap.player.hp}/{snap.player.max_hp}")
        table.add_row("Energy", f"{snap.player.energy}/{snap.player.max_energy}")
        table.add_row("Draw", str(snap.combat.draw_pile))
        table.add_row("Gold", str(snap.player.gold))
        if self._first:
            self._console.clear()
            self._first = False
        self._console.print(table)