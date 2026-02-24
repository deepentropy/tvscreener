---
status: complete
priority: p1
issue_id: "020"
tags: [cli, config, settings]
dependencies: ["019"]
---

## Problem Statement

New settings scaffolding exists but the CLI never loads or applies it, so YAML/.env configuration has no effect.

## Findings

- `tvscreener/config/loader.py:27-76` defines `load_settings()` and `merge_with_cli_args()`.
- `tvscreener/cli.py` does not import or use either function, and provides no `--config` flag.
- CLI defaults are hard-coded (e.g., `tvscreener/cli.py:169-176` timeframes + contract type), bypassing `ScreenerSettings`.

## Proposed Solutions

### Option A: Wire settings into CLI (Recommended)

- Add `--config` (default `tvscreener.yaml`).
- Call `load_settings(config_path=args.config)` early in `main()`.
- Use settings for defaults (universe/timeframes/contract type) and strategy thresholds.
- Use `merge_with_cli_args()` to produce the config dict passed to `ForexScreenerConfig` and `StrategyConfig`.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] Running with only `tvscreener.yaml` changes behavior (no CLI args required)
- [ ] `.env` overrides YAML
- [ ] CLI args override both
- [ ] `--config` selects an alternate YAML file
