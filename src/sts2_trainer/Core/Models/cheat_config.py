"""User-facing cheat configuration, loaded from YAML."""
from __future__ import annotations

from pydantic import BaseModel, Field


class CheatConfig(BaseModel):
    godmode: bool = False
    godmode_hp_floor: int = 1
    energy_refill: bool = False
    energy_target: int = Field(default=99, ge=3, le=999)
    draw_inject: bool = False
    draw_extra: int = Field(default=2, ge=0, le=10)
    map_reveal: bool = False
    gold_floor: int = 0
    tick_ms: int = Field(default=250, ge=50, le=2000)

    @classmethod
    def from_yaml(cls, path: str) -> "CheatConfig":
        import yaml
        with open(path, "r", encoding="utf-8") as fh:
            return cls(**yaml.safe_load(fh) or {})