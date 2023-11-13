"""Test cases for solution."""
from solution import students_study, lottery, fruit_order


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    # Check for sleepers.
    assert students_study(1, False) is False
    assert students_study(4, True) is False

    # Check for day time studiers.
    assert students_study(5, False) is False
    assert students_study(17, False) is False
    assert students_study(6, True) is True

    # Check for evening time studiers.
    assert students_study(18, True) is True
    assert students_study(24, False) is True


def test_lottery():
    """
    Fill later.

    :return:
    """
    assert lottery(5, 5, 5) == 10
    assert lottery(4, 4, 4) == 5
    assert lottery(5, 4, 3) == 1
    assert lottery(5, 5, 4) == 0


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
