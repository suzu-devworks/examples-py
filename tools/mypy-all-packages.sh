#! /usr/bin/sh
find ./packages/ -name pyproject.toml | xargs -n 1 dirname |  xargs -i uv run --directory {} mypy $@ .
