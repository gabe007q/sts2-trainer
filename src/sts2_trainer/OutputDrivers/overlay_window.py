"""Simple always-on-top overlay rendered with a Win32 layered window.

Kept intentionally minimal — full overlay is behind a feature flag while
DirectX hooking is stabilised.
"""
from __future__ import annotations

import ctypes
from ctypes import wintypes

from sts2_trainer.Core.Models.game_state import GameSnapshot
from sts2_trainer.OutputDrivers.base import OutputDriver

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

WS_EX_TOPMOST = 0x00000008
WS_EX_LAYERED = 0x00080000


class OverlayWindow(OutputDriver):
    def __init__(self, enabled: bool = True) -> None:
        self.enabled = enabled
        self._hwnd: int | None = None

    def _ensure_window(self) -> int:
        if self._hwnd:
            return self._hwnd
        self._hwnd = user32.CreateWindowExW(
            WS_EX_TOPMOST | WS_EX_LAYERED, "STATIC", "sts2-trainer",
            0x80000000, 20, 20, 260, 120, 0, 0, 0, 0,
        )
        user32.ShowWindow(self._hwnd, 4)
        return self._hwnd

    def render(self, snap: GameSnapshot) -> None:
        if not self.enabled:
            return
        hwnd = self._ensure_window()
        text = f"HP {snap.player.hp}  E {snap.player.energy}  Draw {snap.combat.draw_pile}"
        user32.SetWindowTextW(hwnd, text)