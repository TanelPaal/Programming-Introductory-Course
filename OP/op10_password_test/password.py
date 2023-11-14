"""Password validation."""
import math


def is_correct_length(password: str) -> bool:
    """
    Check if the password's length is within the valid range.

    The password should have a length between 8 and 64 symbols.
    :param password: Password to be checked
    :return: True if the password's length is within the valid range, False otherwise
    """
    return 8 <= len(password) <= 64


def includes_uppercase(password: str) -> bool:
    """
    Check if the password contains at least one uppercase letter.

    :param password: Password to be checked
    :return: True if the password contains at least one uppercase letter, False otherwise
    """
    for char in password:
        if char.isupper():
            return True
    return False


def includes_lowercase(password: str) -> bool:
    """
    Check if the password contains at least one lowercase letter.

    :param password: Password to be checked
    :return: True if the password contains at least one lowercase letter, False otherwise
    """
    for char in password:
        if char.islower():
            return True
    return False


def includes_special(password: str) -> bool:
    """
    Check if the password contains at least one special character (whitespace is also considered a special character).

    :param password: Password to be checked
    :return: True if the password contains at least one special character, False otherwise
    """
    for char in password:
        if not char.isalnum():
            return True
    return False


def includes_number(password: str) -> bool:
    """
    Check if the password contains at least one numeric digit.

    :param password: Password to be checked
    :return: True if the password contains at least one numeric digit, False otherwise
    """
    for char in password:
        if char.isdigit():
            return True
    return False


def is_different_from_old_password(old_password: str, new_password: str) -> bool:
    """
    Check if the new password is different enough from the old password.

    The overlap between the new password and old password should be less than 50%.
    The check for overlap is case-insensitive.
    The overlap is also checked for the reversed version of the new password.

    :param old_password: The old password
    :param new_password: The new password
    :return: True if the new password is different enough, False otherwise
    """
    old_pass = old_password.lower()
    new_pass = new_password.lower()
    overlap = math.ceil(len(new_pass) / 2)
    x = 0
    while overlap <= len(new_pass):
        if new_pass[x:overlap] in old_pass or new_pass[x:overlap] in old_pass[::-1]:
            return False
        else:
            x += 1
            overlap += 1
    return True


def is_name_in_password(password: str, name: str) -> bool:
    """
    Check if the password contains the name of the account owner.

    The name received as input may contain whitespace to separate the first and last name, neither of which should be
    present in the password.
    If the name contains a hyphen (such as Mari-Liis), neither part of the name should be present in the password.
    The name should not be in the password even if the casing of it is different in the password.
    Reversed format of the name is also not allowed in the password

    :param password: The password to be validated
    :param name: The full name of the account owner
    :return: True if the name is present in the password, False otherwise
    """
    # Convert the password to lowercase for case-insensitive comparison.
    password_lower = password.lower()

    # Split the name into parts using whitespace as a separator.
    name_parts = name.split()

    # Create a list to store the individual name parts.
    individual_name_parts = []

    # Iterate over the name parts
    for part in name_parts:
        # Split hyphenated parts further if needed.
        hyphen_parts = part.split("-")
        individual_name_parts.extend(hyphen_parts)

    # Iterate over the individual name parts and check if any of them are present in the password.
    for name_part in individual_name_parts:
        name_part_lower = name_part.lower()

        if name_part_lower in password_lower or name_part_lower[::-1] in password_lower:
            return True
    return False


def is_birthday_in_password(password: str, birthdate: str) -> bool:
    """
    Check if the password contains the birthday of the account owner.

    The day, month or year in the birthdate cannot be present in the password. For the birth year, the last two digits
    of the birth year separately is also not allowed.

    For the day, month or last 2 digits of the year, the reversed number is allowed but for the full 4-digit year is
    not allowed in the reverse format.

    The date is always in the format "dd.mm.yyyy", where
    dd is 2-digit day (01, 02, .. 31)
    mm is 2-digit month (01, 02, .. 12)
    yyyy is 4-digit year (0001, 0002, ..., 2022, 2023, ..., 3000, ...)

    You don't have to validate the date.

    :param password: The password to be validated
    :param birthdate: Birthday of the account owner, format is dd.mm.yyyy
    :return: True if the birthday is present in the password, False otherwise
    """
    day, month, year = birthdate.split(".")

    # Check if the day, month, or year (in various formats) are in the password.
    if day in password or month in password:
        return True

    # Check the year and its last two digits.
    if year in password or year[-2:] in password or year[::-1] in password:
        return True

    return False


def is_password_valid(new_password: str, old_password: str, name: str, birthdate: str) -> bool:
    """
    Check whether the given password is valid.

    This function combines several checks to determine if the provided password is valid.
    It checks the length, presence of uppercase and lowercase letters, inclusion of at least one number,
    inclusion of at least one special character, absence of the user's name and birthdate in the password.
    Call the functions you wrote before within this one to complete the validation.

    :param new_password: The password to be checked
    :param old_password: the previous password of this account
    :param name: The user's full name
    :param birthdate: The user's birthdate
    :return: True if the password is valid, False otherwise.
    """
    if not is_correct_length(new_password):
        return False

    if not includes_uppercase(new_password):
        return False

    if not includes_lowercase(new_password):
        return False

    if not includes_special(new_password):
        return False

    if not includes_number(new_password):
        return False

    if not is_different_from_old_password(old_password, new_password):
        return False

    if is_name_in_password(new_password, name):
        return False

    if is_birthday_in_password(new_password, birthdate):
        return False

    # If all checks passed, the password is valid
    return True


if __name__ == '__main__':
    print("Password length validation:")
    print(is_correct_length("kascnewi3r34t"))  # -> True
    print(is_correct_length("%df#S1"))  # -> False
    print(is_correct_length("kascn¤e%wi3r34tkj*bö ihvlc&?¤kfxyzsr<eq 3454566FGHJOI*UYUF& %¤##&TTRq6"))  # -> False

    print("\nPassword has at least one uppercase letter validation:")
    print(includes_uppercase("Defwefwevwe"))  # -> True
    print(includes_uppercase("e/¤!fwe64fwevw"))  # -> False

    print("\nPassword has at least one lowercase letter validation:")
    print(includes_lowercase("dJOWE821%&/"))  # -> True
    print(includes_lowercase("ÖJOWE821%&/"))  # -> False

    print("\nPassword has at least one special character validation:")
    print(includes_special("&smqwdp24DS"))  # -> True
    print(includes_special("ksmqwd p24DS"))  # -> True
    print(includes_special("ksmqwdp24DS"))  # -> False
    print(includes_special(""))  # -> False

    print("\nPassword has at least one number validation:")
    print(includes_number("dJOWE8%&/"))  # -> True
    print(includes_number("ÖJOWE%&/"))  # -> False

    print("\nNew password is different from the old one validation:")
    print(is_different_from_old_password("õunamoos", "maasikamoos"))  # -> True
    print(is_different_from_old_password("olevsulev67", "ämblikmees18"))  # -> True
    print(is_different_from_old_password("seinav2rv", "seinakapp"))  # -> False
    print(is_different_from_old_password("merineitsi99", "mereneitsi11"))  # -> False
    print(is_different_from_old_password("eva1970", "0791ave"))  # -> False
    print(is_different_from_old_password("abxyab", "abcxy"))  # -> True
    print(is_different_from_old_password("lammas987", "lammas789"))  # -> False

    print("\nPassword has your name:")
    print(is_name_in_password("ddccwemelani", "Melani Mets"))  # -> True
    print(is_name_in_password("ddccwinalemw", "Melani Mets"))  # -> True
    print(is_name_in_password("ddccwsSTEMq", "Melani Mets"))  # -> True
    print(is_name_in_password("ddccwinagregorq", "Karl-Gregor Mustikas"))  # -> True
    print(is_name_in_password("ddccwinamustikas", "Karl-Gregor Mustikas"))  # -> True
    print(is_name_in_password("ddccws23%q", "Melani Mets"))  # -> False

    print("\nPassword has your birthdate:")
    print(is_birthday_in_password("dd&&ccwe30", "30.04.2023"))  # -> True
    print(is_birthday_in_password("dd&&ccwe03", "30.04.2023"))  # -> False
    print(is_birthday_in_password("ddccw%2023", "30.04.2023"))  # -> True
    print(is_birthday_in_password("ddccw%3202", "30.04.2023"))  # -> True
    print(is_birthday_in_password("04ddccw%&1", "30.04.2023"))  # -> True
    print(is_birthday_in_password("40ddccw%&1", "30.04.2023"))  # -> False
    print(is_birthday_in_password("56ddccw%&1", "30.04.2023"))  # -> False
    print(is_birthday_in_password("23ddccw%&1", "30.04.2023"))  # -> True

    print("\nPassword is completely validated:")
    print(is_password_valid("k45aLK%1", "SunsetBeach2022!", "Marek Põõsas", "26.06.2003"))  # -> True
    print(is_password_valid("keramRTYUY2003RDSCF.", "PurpleDragon42*", "Marek Põõsas", "12.04.2003"))  # -> False
