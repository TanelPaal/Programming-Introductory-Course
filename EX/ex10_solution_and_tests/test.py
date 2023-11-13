"""Test cases for solution."""
from solution import students_study, lottery, fruit_order


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    # Night.
    assert students_study(1, False) is False
    assert students_study(1, True) is False
    assert students_study(2, False) is False
    assert students_study(2, True) is False
    assert students_study(4, False) is False
    assert students_study(4, True) is False

    # Day.
    assert students_study(5, False) is False
    assert students_study(5, True) is True
    assert students_study(13, False) is False
    assert students_study(13, True) is True
    assert students_study(17, False) is False
    assert students_study(17, True) is True

    # Evening.
    assert students_study(18, False) is True
    assert students_study(18, True) is True
    assert students_study(20, False) is True
    assert students_study(20, True) is True
    assert students_study(24, False) is True
    assert students_study(24, True) is True


def test_lottery():
    """
    Fill later.

    :return:
    """
    assert lottery(5, 5, 5) == 10
    assert lottery(4, 4, 4) == 5
    assert lottery(5, 4, 3) == 1
    assert lottery(5, 5, 4) == 0
    assert lottery(-1, -1, -1) == 5
    assert lottery(0, 0, 0) == 5
    assert lottery(2, 2, 1) == 0
    assert lottery(2, 3, 3) == 1
    assert lottery(3, 2, 3) == 0
    assert lottery(-2, -2, -2) == 5


def test_fruit_order():
    """
    Fill later.

    :return:
    """
    assert fruit_order(0, 2, 10) == 0
    assert fruit_order(5, 1, 9) == 4
    assert fruit_order(3, 2, 9) == -1
    assert fruit_order(3, 1, 10) == -1
    assert fruit_order(0, 0, 5) == -1
    assert fruit_order(5, 5, 0) == 0
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(0, 5, 0) == 0
    assert fruit_order(5, 0, 0) == 0
    assert fruit_order(0, 2, 15) == -1
    assert fruit_order(0, 2, 5) == 0
    assert fruit_order(5, 0, 5) == 5
    assert fruit_order(0, 5, 20) == 0
    assert fruit_order(5, 0, 2) == 2
    assert fruit_order(10, 0, 4) == 4
    assert fruit_order(2, 0, 11) == -1
    assert fruit_order(55, 55, 330) == 55
    assert fruit_order(0, 2, 9) == -1
    assert fruit_order(0, 200, 200) == 0
    assert fruit_order(1000, 1000, 1000) == 0
    assert fruit_order(6, 98, 0) == 0
    assert fruit_order(0, 0, 19) == -1
    assert fruit_order(1980, 3458, 10003) == 3
    assert fruit_order(3, 300_000, 500_000) == 0
    assert fruit_order(56, 0, 56) == 56
    assert fruit_order(0, 49, 16) == -1