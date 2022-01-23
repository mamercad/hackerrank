#!/usr/bin/env python3


def birthdayCakeCandles(candles):
    count = 0
    for candle in candles:
        if candle == max(candles):
            count += 1
    return count


def test_birthdayCakeCandles():
    assert birthdayCakeCandles([4, 4, 1, 3]) == 2
    assert birthdayCakeCandles([5, 4, 4, 1, 3]) == 1
    assert birthdayCakeCandles([6, 5, 4, 4, 1, 3, 6, 6]) == 3
