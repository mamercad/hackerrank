#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true


def simpleArraySum(ar):
    sum = 0
    for a in ar:
        sum += a
    return sum


def test_simpleArraySum():
    assert simpleArraySum([1, 2, 3]) == 6
    assert simpleArraySum([0, 2, 3]) == 5
    assert simpleArraySum([0, 2, 3, 5]) == 10
    assert simpleArraySum([0, 2, 3, 5, -1, -2]) == 7
    assert simpleArraySum([0, 2, 3, 5, -1, -2, 0]) == 7
