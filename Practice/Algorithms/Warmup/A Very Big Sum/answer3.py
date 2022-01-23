#!/usr/bin/env python3

import os


def aVeryBigSum(ar):
    sum_ = 0
    for a in ar:
        sum_ += a
    return sum_


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + "\n")
    fptr.close()
