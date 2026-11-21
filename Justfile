[private]
default:
    @just --list

install:
    uv sync

lint:
    uv run ruff check .
    uv run ruff format --check .

format:
    uv run ruff check --fix .
    uv run ruff format .

typecheck:
    uv run mypy

check: lint typecheck

check-ci: lint typecheck

pre-commit:
    uv run pre-commit run --all-files
