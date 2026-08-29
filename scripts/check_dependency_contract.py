"""Verify the installed libraries match the pins in pyproject.toml.

This repository contains no Python source. The pinned versions exist because
`platforms/chatgpt/knowledge/data-analysis-guide.md` teaches Agent 21 to write pandas,
matplotlib and numpy code, and that guide's examples are written against these specific
majors. Importing the packages proves only that *something* installed; this asserts the
resolved environment is the one the guide documents.
"""

from __future__ import annotations

import re
import sys
import tomllib
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = re.compile(r"^(?P<name>[A-Za-z0-9_.-]+)==(?P<version>.+)$")


def main() -> int:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    dependencies = pyproject.get("project", {}).get("dependencies", [])
    if not dependencies:
        print("pyproject.toml declares no dependencies to verify", file=sys.stderr)
        return 1

    problems: list[str] = []
    for entry in dependencies:
        match = PIN.match(entry.strip())
        if match is None:
            problems.append(f"{entry!r} is not an exact `name==version` pin")
            continue

        name, expected = match["name"], match["version"]
        try:
            installed = version(name)
        except PackageNotFoundError:
            problems.append(f"{name} is pinned to {expected} but is not installed")
            continue

        if installed != expected:
            problems.append(f"{name} is pinned to {expected} but {installed} is installed")
        else:
            print(f"  {name} {installed}")

    if problems:
        print("\nDependency contract violated:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    print(f"Dependency contract holds for {len(dependencies)} pinned libraries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
