#!/usr/bin/python3
# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true


def timeConversion(s):
    ampm = s[-2:]
    hour = int(s[0:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    if ampm == "PM":
        hour += 12
    return f"{hour:02}:{minute:02}:{second:02}"


def test_timeConversion():
    assert timeConversion("07:05:45AM") == "07:05:45"
    assert timeConversion("07:05:45PM") == "19:05:45"
