"""Console entrypoint for sts2-trainer."""
from __future__ import annotations

import argparse
import sys

from rich.console import Console

from sts2_trainer.bootstrap.pipeline import Pipeline
from sts2_trainer.Infrastructure.logging_setup import configure_logging
from sts2_trainer.Infrastructure.process_guard import require_slay_the_spire

log = Console()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sts2-trainer")
    p.add_argument("--pid", type=int, help="Attach to a specific pid")
    p.add_argument("--tick-ms", type=int, default=250)
    p.add_argument("--cheats", nargs="*", default=["godmode", "energy", "draw"])
    p.add_argument("--no-overlay", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    configure_logging()

    proc = require_slay_the_spire(args.pid)
    log.print(f"[bold green]attached[/] pid={proc.pid} name={proc.name}")

    pipe = Pipeline(tick_ms=args.tick_ms, cheats=args.cheats)
    try:
        pipe.run()
    except KeyboardInterrupt:
        log.print("[yellow]detaching...[/]")
    return 0


if __name__ == "__main__":
    sys.exit(main())