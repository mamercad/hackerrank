#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true


def staircase(n):
    rows = []
    for x in range(n):
        rows.append(" " * (n - x - 1) + " " + "#" * (x + 1))
    return "\n".join(rows)


if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
