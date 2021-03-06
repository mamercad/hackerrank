#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true


def plusMinus(arr):
    total, positive, negative, zero = len(arr), 0, 0, 0
    for a in arr:
        if a > 0:
            positive += 1
        elif a == 0:
            zero += 0
        else:
            negative += 1
    return positive / total, negative / total, zero / total


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
