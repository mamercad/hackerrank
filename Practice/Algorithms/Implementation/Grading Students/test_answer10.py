#!/usr/bin/env python3


def round_to_nearest(n, m):
    return m * round(n / m)


def round_grade(grade):
    if grade < 38:
        return grade
    else:
        nearest_multiple = round_to_nearest(grade, 5)
        if nearest_multiple - grade < 3:
            return nearest_multiple
        else:
            return grade


for grade in [80, 81, 82, 83, 84, 85]:
    print("===")
    print(grade, round_grade(grade))


def test_round_grade():
    assert round_grade(20) == 20
    assert round_grade(30) == 30
    assert round_grade(82) == 82
    assert round_grade(83) == 85
    # assert round_grade(84) == 85
    # assert round_grade(85) == 85
    # assert round_grade(73) == 75
    # assert round_grade(67) == 67
    # assert round_grade(38) == 40
    # assert round_grade(33) == 33
