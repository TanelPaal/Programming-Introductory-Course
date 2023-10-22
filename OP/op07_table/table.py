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
    def convert_to_12_hour_format(hour, minute):
        if hour == 0:
            return f'12:{minute:02d} AM'
        elif hour < 12:
            return f'{hour}:{minute:02d} AM'
        elif hour == 12:
            return f'12:{minute:02d} PM'
        else:
            return f'{hour - 12}:{minute:02d} PM'

    def normalize_time(hour, minute, offset):
        # Convert the time to UTC.
        hour = (hour - offset) % 24
        return convert_to_12_hour_format(hour, minute)

    times = get_times(text)
    usernames = get_usernames(text)
    errors = get_errors(text)
    addresses = get_addresses(text)
    endpoints = get_endpoints(text)

    # Format the data into a table.
    table = [
        f'time     | {", ".join(normalize_time(hour, minute, offset) for hour, minute, offset in times)}',
        f'user     | {", ".join(usernames)}',
        f'error    | {", ".join(map(str, errors))}',
        f'ipv4     | {", ".join(addresses)}',
        f'endpoint | {", ".join(endpoints)}',
    ]

    return '\n'.join(table)


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
    time_pattern = r'(\d{1,2})\D+(\d{2}) UTC([-+]\d{1,2})'
    time_matches = re.findall(time_pattern, text)
    times = [(int(hour), int(minute), int(offset)) for hour, minute, offset in time_matches]
    return times


def get_usernames(text: str) -> list[str]:
    """Get usernames from text."""
    username_pattern = r'usr:([a-zA-Z0-9_]+)'
    usernames = re.findall(username_pattern, text)
    return usernames


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    error_pattern = r'error (\d{1,3})'
    errors = [int(error) for error in re.findall(error_pattern, text, re.IGNORECASE)]
    return errors


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    address_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    addresses = re.findall(address_pattern, text)
    return addresses


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    endpoint_pattern = r'\/[a-zA-Z0-9&\/=?\-_%]+'
    endpoints = re.findall(endpoint_pattern, text)
    return endpoints


if __name__ == '__main__':
    logs = """
            [-1b35 UTC-4] errOR 741
            [24a48 UTC+0] 776.330.579.818
            [02:53 UTC+5] usr:96NC9yqb /aA?Y4pK
            [5b05 UTC+5] ERrOr 700 268.495.856.225
            [24-09 UTC+10] usr:uJV5sf82_ eRrOR 844 715.545.485.989
            [04=54 UTC+3] eRROR 452
            [11=57 UTC-6] 15.822.272.473 error 9
            [15=53 UTC+7] /NBYFaC0 468.793.214.681
            [23-7 UTC+12] /1slr8I
            [07.46 UTC+4] usr:B3HIyLm 119.892.677.533
            """
    print(create_table_string(logs))
