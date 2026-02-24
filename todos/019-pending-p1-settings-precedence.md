---
status: complete
priority: p1
issue_id: "019"
tags: [config, settings, bug]
dependencies: []
---

## Problem Statement

Layered configuration precedence is incorrect: YAML values can override `.env` values, even though the intended order is YAML -> ENV/.env -> CLI.

## Findings

- `tvscreener/config/loader.py:27-36` writes YAML keys into `os.environ` **before** `ScreenerSettings()` reads `.env`.
- Because `.env` is not loaded into `os.environ` yet, YAML will populate `TVSCREENER_*` and effectively win over `.env`.
- `tvscreener/config/settings.py:9-11` declares `env_file=".env"`, so `.env` is expected to override YAML.

## Proposed Solutions

### Option A: Stop mutating `os.environ` (Recommended)

- Load YAML into a dict and pass it as explicit init kwargs to `ScreenerSettings(**yaml_config)`.
- Let pydantic-settings handle `.env` + real environment variables normally.

### Option B: Load dotenv first

- Call `dotenv.load_dotenv(override=False)` before the YAML -> env injection.
- Keep env injection but ensure `.env` populates `os.environ` first.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] `.env` overrides YAML for the same key
- [ ] real environment variables override both YAML and `.env`
- [ ] no code path writes user config into process-wide `os.environ`
