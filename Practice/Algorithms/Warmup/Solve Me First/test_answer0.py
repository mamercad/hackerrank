#!/usr/bin/env python3

import pytest


def solveMeFirst(a, b):
    return a + b


def test_solveMeFirst():
    assert solveMeFirst(1, 1) == 2
    assert solveMeFirst(1, 2) == 3
    assert solveMeFirst(-1, 2) == 1
    assert solveMeFirst(-1, 0) == -1
    assert solveMeFirst(3, 7) == 10
