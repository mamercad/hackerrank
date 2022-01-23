#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true


def miniMaxSum(arr):
    min_sum = sum(arr) - min(arr)
    max_sum = sum(arr) - max(arr)
    return min_sum, max_sum


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
