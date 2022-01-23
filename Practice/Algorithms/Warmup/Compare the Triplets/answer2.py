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


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
