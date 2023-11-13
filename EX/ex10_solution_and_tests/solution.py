"""Solution to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 1 <= time <= 4:
        return False  # Sleep students.
    elif 5 <= time <= 17 and coffee_needed:
        return True
    elif 18 <= time <= 24:
        return True
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c and a != 5:
        return 5
    elif a != b and a != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    big_baskets_used = min(big_baskets, ordered_amount // 5)
    remaining_amount = ordered_amount - (big_baskets_used * 5)

    if remaining_amount <= small_baskets:
        return remaining_amount
    else:
        return -1


if __name__ == '__main__':
    print("Study:")
    print(students_study(6, False))  # False.
    print(students_study(16, True))  # True.
    print(students_study(19, True))  # False.
    print(students_study(24, False))  # True.
    print("\nLottery:")
    print(lottery(5, 5, 5))  # 10.
    print(lottery(4, 4, 4))  # 5.
    print(lottery(5, 4, 3))  # 1.
    print(lottery(5, 5, 4))  # 0.
    print("\nFruit Order:")
    print(fruit_order(0, 2, 10))  # 0.
    print(fruit_order(10, 0, 10))  # 0.
    print(fruit_order(5, 1, 9))  # 4.
    print(fruit_order(3, 2, 9))  # -1.
    print(fruit_order(3, 1, 10))  # -1.
    print(fruit_order(0, 0, 5))  # -1.
    print(fruit_order(5, 5, 0))  # 0.
    print(fruit_order(10, 10, 55))  # 5.
