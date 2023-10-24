"""Create table from the given string."""
import re


def create_table_string(text: str) -> str:
    """
    Create table string from the given logs.

    Example of logs:

    [10:50 UTC+8] nothing here
    [12:25 UTC-2] error 404

    There are a total of five categories you need to find the items for.
    Here are the rules for finding them:

    1. Time
    - Hour can be one or two characters long (1, 01, and 11)
    - Minute can be one or two characters long (2, 02, 22)
    - UTC offset ranges from -12 to 12
    - Times in the text are formatted in 24 hour time format (https://en.wikipedia.org/wiki/24-hour_clock)
    - Minimum time is 00:00 (0:00 and 0,00 and 00-0 are also valid)
    - Maximum time is 23:59
    - Hour and minute can be separated by any non-numeric character (01:11, 1.2, 6;5 and 1a4 are valid while 12345 is not)
    2. Username starts after "usr:" and contains letters, numbers and underscores ("_")
    3. Error code is a non-negative number up to 3 digits and comes after a case-insensitive form of "error "
    4. IPv4 address is good enough if it's a group of four 1- to 3-digit numbers separated by dots
    5. Endpoint starts with a slash ("/") and contains letters, numbers and "&/=?-_%"

    Each table row consists of a category name and items belonging to that category.
    Categories are named and ordered as follows: "time", "user", "error", "ipv4" and "endpoint".

    Table from the above input example:

    time  | 2.50 AM, 14.25 PM
    error | 404

    The category name and its items are separated by a vertical bar ("|").
    The length between the category name and separator is one whitespace (" ") for the longest category name in the table.
    The length between the separator and items is one whitespace.
    Items for each category are unique and are separated by a comma and a whitespace (", ") and must be sorted in ascending order.
    Times in the table are formatted in 12 hour time format (https://en.wikipedia.org/wiki/12-hour_clock), like "1:12 PM"
    and "12:00 AM".
    Times in the table should be displayed in UTC(https://et.wikipedia.org/wiki/UTC) time.
    """
    dictionary = {}
    dictionary["time"], dictionary["user"] = get_times(text), sorted(list(set(get_usernames(text))))
    dictionary["error"], dictionary["ipv4"] = sorted(list(set(get_errors(text)))), sorted(list(set(get_addresses(text))))
    dictionary["endpoint"] = sorted(list(set(get_endpoints(text))))
    new_dict = dictionary.copy()
    for key in new_dict:
        if dictionary[key] == []:
            del dictionary[key]
        elif key == "time":
            dictionary[key] = get_formatted_time(dictionary[key])
        elif key == "error":
            dictionary[key] = ", ".join([str(error) for error in dictionary[key]])
        else:
            dictionary[key] = ", ".join(dictionary[key])
    del new_dict, key
    longest_header = max([len(key) for key in dictionary])
    result = ""
    for key in dictionary:
        result += f"{key:<{longest_header}} | {dictionary[key]}\n"
    return result.rstrip("\n")


def get_times(text: str) -> list[tuple[int, int, int]]:
    """
    Get times from text using the time pattern.

    The result should be a list of tuples containing the time that's not normalized and UTC offset.

    For example:

    [10:53 UTC+3] -> [(10, 53, 3)]
    [1:43 UTC+0] -> [(1, 43, 0)]
    [14A3 UTC-4] [14:3 UTC-4] -> [(14, 3, -4), (14, 3, -4)]

    :param text: text to search for the times
    :return: list of tuples containing the time and offset
    """
    str_list = re.findall(r"\[([0-1]?[\d]|2[0-3])[^\d]([0-5]?[\d]) UTC([+-]\d(?!\d)|[+-]1?[0-2])", text)
    return [(int(hour), int(minute), int(utc)) for hour, minute, utc in str_list]


def get_formatted_time(time_list: list[tuple[int, int, int]]) -> str:
    """Format 24 hour time to the 12 hour time."""
    def format_time(hour, minute):
        period = "AM" if hour < 12 else "PM"
        if hour == 0:
            return f"12:{minute:02} {period}, "
        elif hour == 12:
            return f"12:{minute:02} {period}, "
        else:
            return f"{hour % 12}:{minute:02} {period}, "

    formatted_times = set()

    for hour, minute, utc in time_list:
        adjusted_hour = (hour - utc) % 24
        formatted_times.add(format_time(adjusted_hour, minute))

    result = ''.join(formatted_times).rstrip(', ')
    return result


def get_usernames(text: str) -> list[str]:
    """Get usernames from text."""
    result = []
    for username in re.findall(r"usr:([\w\d_]+)", text):
        if username not in result:
            result += [username]
    return result


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    return [int(digit) for digit in re.findall(r"error (\d{1,3})", text, flags=re.IGNORECASE)]


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    return re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", text)


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    return re.findall(r"\/[\w\d&\/=?\-_%]+", text)


if __name__ == '__main__':
    logs = """
            [14?36 UTC+9] /tere eRRoR 418 192.168.0.255
            [8B48 UTC-6] usr:kasutaja
            [14?36 UTC+9] 1.1.1.1
            [8B48 UTC-6] 20.234.454.111
            [14?36 UTC+9] 192.1.3.54
            [8B48 UTC-6] 145.34.5.6
            [14?36 UTC+9] 23453.45643.5322
            [8B48 UTC-6] 754.6.5.5
            [14?36 UTC+9] /A-36DUV1 /DZ&jKith
            [23B00 UTC-12] usr:whatever usr:waccaflower
            """
    print(create_table_string(logs))
    # time     | 5:36 AM, 2:48 PM
    # user     | kasutaja
    # error    | 418
    # ipv4     | 192.168.0.255
    # endpoint | /tere
