#!/usr/bin/python3
# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

import os


def timeConversion(s):
    ampm = s[-2:]
    hour = int(s[0:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    if ampm == "PM":
        hour += 12
    return f"{hour:02}:{minute:02}:{second:02}"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = timeConversion(s)
    fptr.write(result + "\n")
    fptr.close()
