"""Password validation tests."""
import random
import password


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test__is_correct_length__empty():
    """Test whether password is an empty string or no input."""
    assert password.is_correct_length("") is False


def test__is_correct_length__in_range_random():
    """Test whether the random length of password is correct."""
    for length in range(8, 65):
        assert password.is_correct_length(random.choices(alphabet, k=length)) is True


def test__is_correct_length__too_short():
    """Test whether password of length 7 is not correct."""
    assert password.is_correct_length("passwor") is False
    assert password.is_correct_length("passwo") is False
    assert password.is_correct_length("passw") is False
    assert password.is_correct_length("pass") is False
    assert password.is_correct_length("pas") is False
    assert password.is_correct_length("pa") is False
    assert password.is_correct_length("p") is False


def test__is_correct_length__too_long():
    """Test whether password of length > 64 is incorrect."""
    assert password.is_correct_length("passwor" * 20) is False
    assert password.is_correct_length("passwo" * 25) is False
    assert password.is_correct_length("passw" * 30) is False
    assert password.is_correct_length("pass" * 35) is False
    assert password.is_correct_length("pas" * 40) is False
    assert password.is_correct_length("pa" * 45) is False
    assert password.is_correct_length("p" * 65) is False


def test__includes_uppercase__empty():
    """Test whether password is an empty string or no input."""
    assert password.includes_uppercase("") is False


def test__includes_uppercase__includes_numbers():
    """Test whether password includes numbers."""
    assert password.includes_uppercase("password1") is False
    assert password.includes_uppercase("Password1") is True


def test__includes_uppercase__true_but_not_first():
    """Test whether password includes uppercase letters but not in the beginning."""
    assert password.includes_uppercase("passWord1") is True
    assert password.includes_uppercase("pAssWord1") is True
    assert password.includes_uppercase("paSSWorD1") is True
    assert password.includes_uppercase("paSswoRd1") is True
    assert password.includes_uppercase("PassWOrd1") is True


def test__includes_uppercase__only_uppercase_letters():
    """Test whether password includes only uppercase letters."""
    assert password.includes_uppercase("PASSWORD") is True
    assert password.includes_uppercase("PASSWORD1") is True  # Includes numbers.
    assert password.includes_uppercase("PASSWORD!") is True  # Includes special characters.
    assert password.includes_uppercase("PASSWORD1!") is True  # Includes numbers and special characters.


def test__includes_uppercase__every_uppercase_letters():
    """Test whether password includes every uppercase letter."""
    assert password.includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ") is True
    assert password.includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ1") is True  # Includes numbers.
    assert password.includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ!") is True  # Includes special characters.
    assert password.includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ1!") is True  # Includes numbers and special characters.


def test__includes_lowercase__empty():
    """Test whether password is an empty string or no input."""
    assert password.includes_lowercase("") is False


def test__includes_lowercase__includes_numbers():
    """Test whether password includes numbers."""
    assert password.includes_lowercase("PASSWORD1") is False
    assert password.includes_lowercase("Password1") is True


def test__includes_lowercase__true_but_not_first():
    """Test whether password includes uppercase letters but not in the beginning."""
    assert password.includes_lowercase("PASSWord1") is True
    assert password.includes_lowercase("pASSWord1") is True
    assert password.includes_lowercase("paSSWorD1") is True
    assert password.includes_lowercase("paSswoRd1") is True
    assert password.includes_lowercase("PassWOrd1") is True


def test__includes_lowercase__only_lowercase_letters():
    """Test whether password includes only lowercase letters."""
    assert password.includes_lowercase("password") is True
    assert password.includes_lowercase("password1") is True  # Includes numbers.
    assert password.includes_lowercase("password!") is True  # Includes special characters.
    assert password.includes_lowercase("password1!") is True  # Includes numbers and special characters.


def test__includes_lowercase__every_lowercase_letters():
    """Test whether password includes every lowercase letter."""
    assert password.includes_lowercase("abcdefghijklmnopqrstuvwxyz") is True
    assert password.includes_lowercase("abcdefghijklmnopqrstuvwxyz1") is True  # Includes numbers.
    assert password.includes_lowercase("abcdefghijklmnopqrstuvwxyz!") is True  # Includes special characters.
    assert password.includes_lowercase("abcdefghijklmnopqrstuvwxyz1!") is True  # Includes numbers and special characters.


def test__includes_special__empty():
    """Test whether password is an empty string or no input."""
    assert password.includes_special("") is False


def test__includes_special__includes_whitespace():
    """Test whether password includes whitespace."""
    assert password.includes_special("password ") is True
    assert password.includes_special("password1 ") is True
    assert password.includes_special("password!") is True
    assert password.includes_special("password1!") is True


def test__includes_special__no_special():
    """Test whether password does not include special characters."""
    assert password.includes_special("password") is False
    assert password.includes_special("password1") is False


def test__includes_special__several_different_special():
    """Test whether password includes several different special characters."""
    assert password.includes_special("pa$$ word") is True
    assert password.includes_special("passw$%^ord123") is True
    assert password.includes_special("1!2@3#4$5%6^7&8*9(0)") is True
    assert password.includes_special("pa!!ssw##ord") is True


def test__includes_number__empty():
    """Test whether password is an empty string or no input."""
    assert password.includes_number("") is False


def test__includes_number__every_digit():
    """Test whether password includes every digit."""
    assert password.includes_number("0123456789") is True
    assert password.includes_number("0123456789a") is True  # Includes lowercase letters.
    assert password.includes_number("0123456789A") is True  # Includes uppercase letters.
    assert password.includes_number("0123456789!") is True  # Includes special characters.
    assert password.includes_number("0123456789a!") is True  # Includes lowercase letters and special characters.
    assert password.includes_number("0123456789A!") is True  # Includes uppercase letters and special characters.
    assert password.includes_number("0123456789aA!") is True  # Includes lowercase letters, uppercase letters and special characters.


def test__includes_number_no_digit():
    """Test whether password does not include digits."""
    assert password.includes_number("password") is False
    assert password.includes_number("password!") is False
    assert password.includes_number("passworda") is False
    assert password.includes_number("passworda!") is False
    assert password.includes_number("passwordA") is False
    assert password.includes_number("passwordA!") is False
    assert password.includes_number("passwordaA") is False
    assert password.includes_number("passwordaA!") is False
    assert password.includes_number("password!") is False
    assert password.includes_number("passworda!") is False
    assert password.includes_number("passwordA!") is False
    assert password.includes_number("passwordaA!") is False


def test__includes_number_true_but_not_first():
    """Test whether password includes digits but not in the beginning."""
    assert password.includes_number("passw0rd") is True
    assert password.includes_number("p4ssw0rd") is True
    assert password.includes_number("pa55w0rd") is True
    assert password.includes_number("passw0rd!") is True


def test_is_different__password_with_uppercase():
    """Test whether the function ignores the case for new and old password."""
    assert password.is_different_from_old_password("TeStInG", "tEsTiNg") is False
    assert password.is_different_from_old_password("WhEEEEEEEn?!", "THeeeeeeeN.") is False
    assert password.is_different_from_old_password("Lorem Ipsum dolor sit amet", "Just, Bloody, Work") is True
    assert password.is_different_from_old_password("Lorem Ipsum dolor sit amet", "Lorem Ipsum Dolor Sit Amet") is False


def test__is_different__password_odd_lengths():
    """Test whether the function works with odd length passwords."""
    assert password.is_different_from_old_password("", "") is True  # New Pass odd length but barely different.
    assert password.is_different_from_old_password("abcdefgh", "abcdefghi") is False  # New Pass odd length but barely different.
    assert password.is_different_from_old_password("pass", "password") is True  # New password is longer
    assert password.is_different_from_old_password("password", "pass") is True  # New password is shorter
    assert password.is_different_from_old_password("12345","123456") is False  # Old password odd length, new password one character longer
    assert password.is_different_from_old_password("abcdef","abcdefg") is False  # Old password even length, new password one character longer and odd
