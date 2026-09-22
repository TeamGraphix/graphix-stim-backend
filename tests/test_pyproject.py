"""Tests for project configuration."""

from pathlib import Path


def test_uv_graphix_source_uses_rev_for_pull_ref() -> None:
    """Ensure uv uses `rev` for the Graphix pull-request reference."""
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    assert (
        'graphix = { git = "https://github.com/TeamGraphix/graphix.git", rev = "refs/pull/607/head" }'
        in pyproject.read_text(encoding="utf-8")
    )
