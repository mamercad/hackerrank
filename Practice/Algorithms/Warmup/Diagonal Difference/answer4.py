#!/usr/bin/env python3

import math
import os
import random
import re
import sys


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


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + "\n")
    fptr.close()
