"""Password validation tests."""
import random

import password


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
