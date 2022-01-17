#!/usr/bin/env python3


def aVeryBigSum(ar):
    sum_ = 0
    for a in ar:
        sum_ += a
    return sum_


def test_aVeryBigSum():
    assert (
        aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
        == 5000000015
    )
