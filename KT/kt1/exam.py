"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string.

    The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if s:
        return s[0].upper() + s[1:]
    else:
        return ""


def has_seven(nums):
    """
    Whether the list has three 7s and no repeated consecutive elements.

    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    sevens_count = 0

    for i in range(len(nums)):
        if nums[i] == 7:
            sevens_count += 1

        if i > 0 and nums[i] == nums[i - 1]:
            return False

    return sevens_count == 3


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    call_dict = {}
    call_chains = call_log.split(',') if call_log else []

    for chain in call_chains:
        people = chain.split(':')

        for i in range(len(people) - 1):
            caller = people[i]
            callee = people[i + 1]

            if caller not in call_dict:
                call_dict[caller] = []
            if callee not in call_dict[caller]:
                call_dict[caller].append(callee)

    return call_dict




def mirror_ends(s: str) -> str:
    """
    Return the first non-matching symbol pair from both ends.

    The function has to be recursive. No loops allowed!

    Starting from the beginning and end, find the first symbol pair which does not match.
    If the input string is a palindrome (the same in reverse) then return "" (empty string).

    mirror_ends("abc") => "ac"
    mirror_ends("aba") => ""
    mirror_ends("abca") => "bc"
    mirror_ends("abAAca") => "bc"
    mirror_ends("") => ""
    """
    if len(s) <= 1:
        return ""

    if s[0] != s[-1]:
        return s[0] + s[-1]

    return mirror_ends(s[1:-1])


if __name__ == '__main__':
    print("\nCall Log:")
    #print(parse_call_log(""))  # Output: {}
    #print(parse_call_log("ago:kati,mati:malle"))  # {"ago": ["kati"], "mati": ["malle"]}
    #print(parse_call_log("ago:kati,ago:mati,ago:kati"))  # {"ago": ["kati", "mati"]}
    #print(parse_call_log("ago:kati:mati"))  # {"ago": ["kati"], "kati": ["mati"]}
    print(parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati"))  # {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}
