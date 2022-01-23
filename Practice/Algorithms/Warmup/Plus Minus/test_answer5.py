#!/usr/bin/env python3

import pytest

def plusMinus(arr):
    total, positive, negative, zero = len(arr), 0, 0, 0
    for a in arr:
        if a > 0:
            positive += 1
        elif a == 0:
            zero += 1
        else:
            negative += 1
    return f"{positive/total:0.6f}\n{negative/total:0.6f}\n{zero/total:0.6f}\n"

def test_plusMinus():
    assert plusMinus([-4, 3, -9, 0, 4, 1]) == "0.500000\n0.333333\n0.166667\n"
