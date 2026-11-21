"""structlog + rotating file logging for the trainer."""
from __future__ import annotations

import logging
from pathlib import Path

import structlog

LOG_DIR = Path.home() / "AppData" / "Local" / "sts2-trainer" / "logs"


def configure_logging(level: int = logging.INFO) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=[
            logging.FileHandler(LOG_DIR / "trainer.log", encoding="utf-8"),
        ],
    )
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(level),
    )