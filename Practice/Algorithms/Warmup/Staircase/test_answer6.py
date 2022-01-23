#!/usr/bin/env python3

import pytest


def staircase(n):
    rows = []
    for x in range(n):
        rows.append(" " * (n - x - 1) + "#" * (x + 1))
    return "\n".join(rows) + "\n"


def test_staircase():
    assert staircase(4) == "   #\n  ##\n ###\n####\n"
    assert staircase(5) == "    #\n   ##\n  ###\n ####\n#####\n"
    assert staircase(6) == "     #\n    ##\n   ###\n  ####\n #####\n######\n"
