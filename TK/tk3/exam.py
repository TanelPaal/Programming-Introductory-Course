"""TK3."""


def common_end(a: list, b: list) -> bool:
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.

    Both lists will be length 1 or more.

    common_end([1, 2, 3], [7, 3]) → True
    common_end([1, 2, 3], [7, 3, 2]) → False
    common_end([1, 2, 3], [1, 3]) → True
    :param a: List of integers.
    :param b: List of integers.
    :return: The last or the first elements are the same.
    """
    same = False
    if a[0] == b[0] or a[-1] == b[-1]:
        same = True

    return same


def alarm_clock(day: int, vacation: bool) -> str:
    """
    Return what time the alarm clock should be set.

    Given a day of the week encoded as 0=Mon, 1=Tue, ... 5=Sat, 6=Sun
    and a boolean indicating if we are on vacation,
    return a string of the form "08:00" indicating when the alarm clock should ring.

    Weekdays, the alarm should be "08:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

    alarm_clock(1, False) → '08:00'
    alarm_clock(3, False) → '08:00'
    alarm_clock(6, False) → '10:00'
    alarm_clock(6, True) → 'off'

    :param day: Day of week.
    :param vacation: Whether it is vacation.
    :return: String when to set alarm clock.
    """
    if day in range(5):
        return '10:00' if vacation else '08:00'
    else:
        return 'off' if vacation else '10:00'


def sum_of_a_beach(s: str) -> int:
    """
    Count how many beach elements are in the string.

    Beaches are filled with sand, water, fish, and sun.
    Given a string, calculate how many times the words
    “Sand”, “Water”, “Fish”, and “Sun” appear without
    overlapping (regardless of the case).

    sum_of_a_beach("WAtErSlIde")                    ==>  1
    sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
    sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
    sum_of_a_beach("cItYTowNcARShoW")               ==>  0
    """
    count = 0
    for word in ['sand', 'water', 'fish', 'sun']:
        count += s.lower().count(word)
    return count


def min_index_value(nums: list) -> int:
    """
    Take the first and the last element as indices of two elements and return the smaller of those elements.

    If at least one index is out of range, return -1.
    All the values are non-negative integers.

    min_index_value([1, 2, 3]) => -1 (3 is out of range)
    min_index_value([1, 2, 1]) => 2 (both elements point to 2)
    min_index_value([1, 2, 0]) => 1 (have to take minimum of 2 and 1)
    min_index_value([1, 2, 0, 3]) => 2 (have to take minimum of 2 and 3)

    :param nums: List of non-negative integers.
    :return: Minimum value of two elements at positions of the first and the last element value.
    """
    if nums[0] >= len(nums) or nums[-1] >= len(nums):
        return -1
    else:
        return min(nums[nums[0]], nums[nums[-1]])


def mirror_ends(s: str) -> str:
    """
    Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string.

    In other words, zero or more characters at the very beginning of the given string,
    and at the very end of the string in reverse order (possibly overlapping).

    For example, the string "abXYZba" has the mirror end "ab".

    mirror_ends("abXYZba") → "ab"
    mirror_ends("abca") → "a"
    mirror_ends("aba") → "aba"

    :param s: String
    :return: Mirror image string
    """
    mirror = ''
    for i in range(len(s)):
        if s[i] == s[-i-1]:
            mirror += s[i]
        else:
            break
    return mirror


if __name__ == '__main__':
    print(common_end([1, 2, 3], [7, 3]))
    print(common_end([1, 2, 3], [7, 3, 2]))
    print(common_end([1, 2, 3], [1, 3]))

    print(alarm_clock(1, False))
    print(alarm_clock(3, False))
    print(alarm_clock(6, False))
    print(alarm_clock(6, True))

    print(sum_of_a_beach("WAtErSlIde"))
    print(sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN"))
    print(sum_of_a_beach("gOfIshsunesunFiSh"))
    print(sum_of_a_beach("cItYTowNcARShoW"))

    print(min_index_value([1, 2, 3]))
    print(min_index_value([1, 2, 1]))
    print(min_index_value([1, 2, 0]))
    print(min_index_value([1, 2, 0, 3]))

    print(mirror_ends("abXYZba"))
    print(mirror_ends("abca"))
    print(mirror_ends("aba"))
    