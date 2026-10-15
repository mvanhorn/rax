#!/usr/bin/env python3
"""Discover and run tests under skills/.

    python3 skills/run_tests.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(str(root), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
