"""Inflation."""


def inflation(n: int, goal: int) -> int:
    """
    Increase the given positive number until it reaches the goal (or goes over it).

    NB! The number must be returned the first time it reaches the goal or goes over it (don't increase it more).
    NB! The number is increased only once per cycle iteration:
    if it gains an extra digit within the cycle, it should not be increased again until the next cycle iteration.

    Rules:
    1. If the number is exactly 1/2 of the goal, multiply it by 2. (Most important)
    2. If the number is currently a 1-digit number, multiply it by 5.
    3. If the number is currently a 2-digit number, multiply it by 4.
    4. If the number is currently a 3-digit number, multiply it by 3.
    5. If the number is currently a 4-digit number, multiply it by 2.
    6. In any other case, multiply it by 7.

    :param n: starting number
    :param goal: goal to reach (may go over)
    :return: new number
    """
    while n < goal:
        # Check if n is 1/2 of the goal.
        if n * 2 == goal:
            n *= 2
            # Check if n is a 1-digit number
        elif 0 < n < 10:
            n *= 5
            # Check if n is a 2-digit number
        elif 10 <= n < 100:
            n *= 4
            # Check if n is a 3-digit number
        elif 100 <= n < 1000:
            n *= 3
            # Check if n is a 4-digit number
        elif 1000 <= n < 10000:
            n *= 2
        else:
            n *= 7
    return n


if __name__ == '__main__':
    print(inflation(10, 11))  # 40
    print(inflation(2, 1000))  # 1440
    print(inflation(800, 79400))  # 134400
    print(inflation(2, 5784))  # 11520
    print(inflation(39, 3400))  # 5616
    print(inflation(5, 10))  # 10
