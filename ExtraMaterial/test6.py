"""KT4."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    result = []
    for i in str(nr):
        result.append(int(i))
    return result


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_elements_around_last_three([1, 3, 7]) -> 8
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_elements_around_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    if 3 not in nums or len(nums) < 3:
        return 0
    all_indexes = [num for num, x in enumerate(nums) if x == 3]
    if len(all_indexes) == 1 and all_indexes[0] == len(nums) - 1:
        return 0
    elif all_indexes[-1] == len(nums) - 1:
        index = all_indexes[-2]
        return nums[index - 1] + nums[index + 1]
    else:
        index = all_indexes[-1]
        return nums[index - 1] + nums[index + 1]


def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    result = {}
    if not pairs:
        return result
    for pair in pairs:
        key = ""
        val = ""
        if ">" in pair:
            key = pair[0]
            val = pair[2]
        elif "<" in pair:
            key = pair[2]
            val = pair[0]
        if key not in result:
            result[key] = [val]
        else:
            if val not in result[key]:
                result[key].append(val)
    return result


def count_the_dumplings(day: int) -> int:
    """
    Count the dumplings.

    You are the production engineer of new dumpling factory.
    Each day the factory has to double its dumpling production.
    Your manager asked you how many dumplings are we making on day X.
    As a lazy software engineer you decided to write a recursive program to count it.
    This function CANNOT contain any while/for loops.
    NB: The factory started working on day one and before that it made 0 dumplings.
    count_the_dumplings(0) => 0
    count_the_dumplings(1) => 1
    count_the_dumplings(2) => 2
    count_the_dumplings(3) => 4
    count_the_dumplings(30) ==> 536870912
    """
    if day == 0:
        return 0
    else:
        return 2 ** (day - 1)


if __name__ == '__main__':
    print(two_digits_into_list(11))  # [1, 1]
    print(two_digits_into_list(71))  # [7, 1]

    print(sum_elements_around_last_three([1, 3, 7]))  # 8
    print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]))  # 5
    print(sum_elements_around_last_three([1, 2, 3]))  # 0

    print(create_dictionary_from_directed_string_pairs(["a>b", "a<b"]))  # {"a": ["b"], "b": ["a"]}
    print(create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]))  # {"1": ["1", "2"]}

    print(count_the_dumplings(3))  # 4
    print(count_the_dumplings(30))  # 536870912
