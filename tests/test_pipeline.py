from dataclasses import dataclass

from sts2_trainer.Core.Models.game_state import CombatState, GameSnapshot, PlayerState
from sts2_trainer.Processors.base import Processor


@dataclass
class _RecordingProcessor(Processor):
    seen: list[int] = None

    def __post_init__(self):
        self.seen = []

    def apply(self, snap: GameSnapshot) -> None:
        self.seen.append(snap.player.hp)


def _snap(hp: int = 50) -> GameSnapshot:
    return GameSnapshot(
        player=PlayerState(hp=hp, max_hp=80, energy=3, max_energy=3, gold=0),
        combat=CombatState(turn=1, hand_size=5, draw_pile=10, discard_pile=0),
        floor=1, act=1,
    )


def test_processor_receives_snapshot():
    proc = _RecordingProcessor()
    proc.apply(_snap(hp=42))
    assert proc.seen == [42]
</｜｜DSML｜｜ parameter>