"""What is this hell."""


def function_a(x: int) -> int:
    """Docstring."""
    result = x / x
    return int(result)


def function_b(x: int) -> int:
    """Docstring."""
    result = x + 11
    return result


def function_c(x: int) -> int:
    """Docstring."""
    result = x * x * x * x * x * x * x * x
    return result


def function_d(x: int) -> int:
    """Docstring."""
    result = (x * x) * (6 * 6)
    return result


def function_e(x: int) -> int:
    """Docstring."""
    result = x * 32
    return result


def function_f(x: int) -> int:
    """Docstring."""
    result = x // 175
    return result

print(function_f(5840)) # 33


def function_g(x: int) -> int:
    """Docstring."""
    result = -x
    return result


def function_h(x: int) -> int:
    """Docstring."""
    result = x * 2538
    return result


def function_i(x: int) -> int:
    """Docstring."""
    return 0


def function_j(x: int) -> int:
    """Docstring."""
    result = x * 10 - 10
    return result
