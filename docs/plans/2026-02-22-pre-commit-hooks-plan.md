---
date: 2026-02-22
topic: pre-commit-hooks
status: completed
---

# Pre-commit Hooks Installation Plan

## Overview

Set up pre-commit hooks for Python project with:
- **Ruff**: Linting + formatting (via `uvx`)
- **Ty**: Type checking (via `uvx`)

---

## Phase 1: Create Pre-commit Config

### 1.1 Install pre-commit

```bash
uv add --dev pre-commit
```

### 1.2 Create `.pre-commit-config.yaml`

```yaml
repos:
  # Ruff - linter and formatter
  - repo: local
    hooks:
      - id: ruff-check
        name: ruff (lint)
        entry: uvx ruff check --fix
        language: system
        types: [python]
        pass_filenames: false

      - id: ruff-format
        name: ruff (format)
        entry: uvx ruff format
        language: system
        types: [python]
        pass_filenames: false

      - id: ty-check
        name: ty (typecheck)
        entry: uvx ty check
        language: system
        types: [python]
        pass_filenames: false
```

---

## Phase 2: Configure Ruff

### 2.1 Create/Update `ruff.toml` or `pyproject.toml`

```toml
[tool.ruff]
target-version = "py312"
line-length = 100
src = ["tvscreener"]

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "SIM",    # flake8-simplify
    "TCH",    # flake8-type-checking
]
ignore = [
    "E501",   # line too long (handled by formatter)
]

[tool.ruff.lint.isort]
known-first-party = ["tvscreener"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
```

---

## Phase 3: Configure Ty (Type Checker)

### 3.1 Add pyproject.toml config for ty

```toml
[tool.ty]
python-version = "3.12"

[tool.ty.rules]
# Adjust strictness as needed
```

### 3.2 Alternative: Use pyright

If `ty` is not available, use `pyright`:

```yaml
# In .pre-commit-config.yaml
- id: pyright
  name: pyright (typecheck)
  entry: uvx pyright
  language: system
  types: [python]
  pass_filenames: false
```

```toml
[tool.pyright]
pythonVersion = "3.12"
typeCheckingMode = "standard"
```

---

## Phase 4: Install and Test

### 4.1 Install hooks

```bash
uv run pre-commit install
```

### 4.2 Run on all files (initial check)

```bash
uv run pre-commit run --all-files
```

### 4.3 Test hook triggers

```bash
# Make a small change and try to commit
echo "# test" >> tvscreener/cli.py
git add tvscreener/cli.py
git commit -m "test"
```

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `.pre-commit-config.yaml` | Create |
| `pyproject.toml` | Add ruff/ty config |
| `.gitignore` | Add `.ruff_cache/` if not present |

---

## Success Criteria

- [ ] `.pre-commit-config.yaml` created
- [ ] Ruff linter runs on commit
- [ ] Ruff formatter runs on commit
- [ ] Type checker runs on commit
- [ ] All checks pass on current codebase
- [ ] Hooks auto-run on `git commit`

---

## Estimated Effort

| Phase | Effort |
|-------|--------|
| Phase 1: Pre-commit config | 10 min |
| Phase 2: Ruff config | 10 min |
| Phase 3: Ty config | 5 min |
| Phase 4: Install and test | 10 min |
| **Total** | **35 min** |

---

## Notes

### Why `uvx`?

- `uvx` runs tools in isolated environments without installing them as dependencies
- Always uses latest version of tools
- No version conflicts with project dependencies

### Why `pass_filenames: false`?

- Ruff and ty check the entire project, not individual files
- Faster execution (single process vs multiple)
- Consistent with how these tools are designed to run

### Alternative: Pre-commit Mirrors

If `uvx` is not preferred, use official pre-commit mirrors:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

This pins versions but requires manual updates.
