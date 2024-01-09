"""KT3."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if len(s) <= 1:
        return s
    return s[-1] + s[:-1]


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    nr_of_pairs = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            nr_of_elements = 0
            if numbers[i] == numbers[j]:
                nr_of_elements += 1
            if nr_of_elements == 1:
                nr_of_pairs += 1
                break
    return nr_of_pairs == 1


def swap_dict_keys_and_value_lists(d: dict) -> dict:
    """
    Swap keys and values in dict.

    Values are lists.
    Every element in this list should be a key,
    and current key will be a value for the new key.
    Values in the result are lists.

    Every list in input dict has at least 1 element.
    The order of the values in the result dict is not important.

    swap_dict_keys_and_value_lists({"a": ["b", "c"]}) => {"b": ["a"], "c": ["a"]}
    swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) => {2: [1, 4], 3: [1], 5: [4]}
    swap_dict_keys_and_value_lists({}) => {}
    swap_dict_keys_and_value_lists({1: [2]}) => {2: [1]}
    """
    if len(d) == 0:
        return d
    result = {}
    for key, val in d.items():
        for v in val:
            if v not in result:
                result[v] = [key]
            else:
                result[v].append(key)
    return result


def substring(s: str, count: int) -> str:
    """
    Return first part of string with length of count.

    Function should be recursive, loops (for/while) are not allowed!
    count <= len(string)

    assert substring("hello", 2) == "he"
    assert substring("hi", 2) == "hi"
    assert substring("house", -1) == ""
    assert substring("house", 0) == ""

    :param s: input string.
    :param count: int, count <= len(string).
    :return: first count symbols from string.
    """
    if s == "" or count < 1:
        return ""
    return s[0] + substring(s[1:], count - 1)


if __name__ == '__main__':
    assert last_to_first("ab") == "ba"
    assert last_to_first("") == ""
    assert last_to_first("hello") == "ohell"

    assert only_one_pair([1, 2, 3]) is False
    assert only_one_pair([1]) is False
    assert only_one_pair([1, 2, 3, 1]) is True
    assert only_one_pair([1, 2, 1, 3, 1]) is False
    assert only_one_pair([1, 2, 1, 3, 1, 2]) is False

    assert swap_dict_keys_and_value_lists({"a": ["b", "c"]}) == {"b": ["a"], "c": ["a"]}
    assert swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) == {2: [1, 4], 3: [1],
                                                                      5: [4]}  # or {2: [4, 1], 3: [1], 5: [4]}
    assert swap_dict_keys_and_value_lists({}) == {}
    assert swap_dict_keys_and_value_lists({1: [2]}) == {2: [1]}

    assert substring("hello", 2) == "he"
    assert substring("hello", -1) == ""
    assert substring("", 0) == ""
    assert substring("world", 5) == "world"
