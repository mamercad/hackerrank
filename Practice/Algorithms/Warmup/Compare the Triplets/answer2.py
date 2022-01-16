#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


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


compareTriplets([1, 2, 3], [4, 5, 6])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     a = list(map(int, input().rstrip().split()))
#     b = list(map(int, input().rstrip().split()))
#     result = compareTriplets(a, b)
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#     fptr.close()
