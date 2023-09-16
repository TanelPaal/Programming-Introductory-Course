"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """
    lowercase_count = 0
    uppercase_count = 0
    digit_sum = 0

    # Check each character in the letter
    for char in letter:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_sum += int(char)

    # Check the rules
    if uppercase_count > lowercase_count and digit_sum <= uppercase_count and digit_sum >= lowercase_count:
        return True
    else:
        return False


if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True
