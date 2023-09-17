"""Prime number identifier."""


def is_prime_number(number: int) -> bool:
    """
    Check if the number is a prime number.

    Prime number is a natural number which is only divisible by 1 and itself. 0 and 1 are not prime numbers.

    Conditions:
    1. If number is a prime number then return boolean True
    2. If number is not a prime number then return boolean False

    :param number: the number to check.
    :return: boolean True if number is a prime number or False if number is not a prime number.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    # Check for divisibility by 2 or 3.
    # If the number is divisible by either 2 or 3, it cannot be a prime number.
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Check the divisibility by numbers of the form 6k ± 1, where k is an integer


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(89))  # -> True
    print(is_prime_number(23))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False
    print(is_prime_number(5))
    print(is_prime_number(6))
