"""Create table from the given string."""
import re


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
    times = []

    time_pattern = r"\[([0-1]?\d|2[0-3])\D([0-5]?\d)\s?UTC([\+\-](?:0?\d|1[0-2]))(?=\b)"
    time_match = re.findall(time_pattern, text)
    for time in time_match:
        hour, minute, offset = time

        time_tuple = (int(hour), int(minute), int(offset))
        times.append(time_tuple)

    return times


def get_hour_and_minute(time: tuple[int, int, int]) -> (int, int):
    """Subtract offset from hour and return the time."""
    hour, minute, offset = time
    new_hour = (hour - offset) % 24

    return (new_hour, minute)


def get_formatted_time(time: tuple[int, int]) -> str:
    """Format 24 hour time to the 12 hour time."""
    hour, minute = time

    am_pm = "AM" if hour // 12 == 0 else "PM"
    am_pm_hour = hour % 12
    if am_pm_hour == 0:
        am_pm_hour = 12

    return f"{am_pm_hour}:{minute:02} {am_pm}"


def get_formatted_times(times: list[tuple[int, int]]) -> list[str]:
    """Take all times and convert to 12-hour time."""
    formatted_times = []

    for time in times:
        formatted_str = get_formatted_time(time)
        formatted_times.append(formatted_str)

    return formatted_times

def get_usernames(text: str) -> list[str]:
    """Get usernames from text."""
    user_pattern = r"usr\:(\w+)"
    user_match = re.findall(user_pattern, text)

    return user_match


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    error_pattern = r"error (\d{1,3}(?=\b))"
    error_match = re.findall(error_pattern, text.lower(), flags=re.IGNORECASE)

    errors = [int(error) for error in error_match] if error_match else []

    return errors


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    ipv4_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ipv4_match = re.findall(ipv4_pattern, text)

    return ipv4_match


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    endpoint_pattern = r"\/[\w\&\/\=\?\-\_\%]*"
    endpoint_match = re.findall(endpoint_pattern, text)

    return endpoint_match


def sorted_unique_list(some_list: list, given_key: None = None) -> list:
    """Take the list, then find the unique items using `set` and finally return sorted list of set items with a given key."""
    unique_items = set(some_list)
    return sorted(unique_items, key=given_key)


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
    times_list = get_times(text)
    times_list_calculated = [get_hour_and_minute(time) for time in times_list]
    sorted_times = sorted_unique_list(times_list_calculated, given_key=lambda tup: (tup[0] * 60 + tup[1]))
    formatted_times = get_formatted_times(sorted_times)

    users_list = get_usernames(text)
    sorted_users = sorted_unique_list(users_list)

    errors_list = get_errors(text)
    sorted_errors = sorted_unique_list(errors_list)

    ipv4_list = get_addresses(text)
    sorted_ipv4s = sorted_unique_list(ipv4_list)

    endpoint_list = get_endpoints(text)
    sorted_endpoints = sorted_unique_list(endpoint_list)

    data = {
        "time": formatted_times,
        "user": sorted_users,
        "error": sorted_errors,
        "ipv4": sorted_ipv4s,
        "endpoint": sorted_endpoints
    }

    keys_with_values = [key for key in data if data[key] != []]
    if not keys_with_values:
        return ""

    longest_key = max([len(key) for key in keys_with_values])

    rows = []
    for key in keys_with_values:
        values = data[key]
        string_array = [str(value) for value in values]
        values_str = ", ".join(string_array)

        row_string = f"{key:<{longest_key}} | {values_str}"
        rows.append(row_string)

    return "\n".join(rows)


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

            [0:60 UTC+0] bad
            [0?0 UTC+0] ok
            [0.0 UTC+0] also ok
            """
    print(create_table_string(logs))
    # time     | 5:36 AM, 2:48 PM
    # user     | kasutaja
    # error    | 418
    # ipv4     | 192.168.0.255
    # endpoint | /tere
