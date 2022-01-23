#!/usr/bin/env python3


def miniMaxSum(arr):
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    return [min_sum, max_sum]


def test_miniMaxSum():
    assert miniMaxSum([1, 3, 5, 7, 9]) == [16, 24]
