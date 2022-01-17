#!/usr/bin/env python3


def diagonalDifference(arr):
    rows = len(arr)
    cols = len(arr[0])

    sum1 = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum1 += arr[i][j]

    arr.reverse()

    sum2 = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum2 += arr[i][j]

    return abs(sum1 - sum2)


def test_diagonalDifference():
    assert (
        diagonalDifference(
            [
                [11, 2, 4],
                [4, 5, 6],
                [10, 8, -12],
            ]
        )
        == 15
    )
