# Architecture

```
bootstrap/         CLI entrypoint + dependency wiring
Ingest/            handlers that read game state from the process
Processors/        mutate game state (cheats live here)
OutputDrivers/     render results (overlay, console, log)
Core/Services/     shared services (memory client, patcher, config)
Core/Models/       offsets, game state dataclasses, cheat config
Infrastructure/    win32 glue, process guard, logging
scripts/           dev tooling (offset dumper, sig scanner)
```

The runtime is a **pipeline**:

`Ingest handler -> Processor -> Output driver`

Each stage registers itself against `bootstrap/pipeline.py`. A tick runs
every `tick_ms` (default 250ms) and feeds live `GameSnapshot`s through the
active processors.