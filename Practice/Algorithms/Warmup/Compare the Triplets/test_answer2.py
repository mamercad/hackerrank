#!/usr/bin/env python3


def compareTriplets(a, b):
    # Write your code here
    score = [0, 0]
    c = zip(a, b)
    for t in c:
        if t[0] > t[1]:
            score[0] += 1
        elif t[0] < t[1]:
            score[1] += 1
    return score


def test_compareTriplets():
    assert compareTriplets([0, 0, 0], [0, 0, 0]) == [0, 0]
    assert compareTriplets([1, 0, 0], [0, 0, 0]) == [1, 0]
    assert compareTriplets([1, 1, 0], [0, 0, 0]) == [2, 0]
    assert compareTriplets([1, 1, 1], [0, 0, 0]) == [3, 0]
    assert compareTriplets([0, 1, 1], [1, 1, 1]) == [0, 1]
