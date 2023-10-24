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
        time_pattern = r"\[([0-1]?\d|2[0-3])[^\d]([0-5]?\d) UTC([+-]\d(?!\d)|[+-]1?[0-2])"
        matches = re.findall(time_pattern, text)
        return [(int(hour), int(minute), int(utc)) for hour, minute, utc in matches]

    def get_formatted_time(time_list):
        def convert_to_12_hour_format(hour, minute, utc_offset):
            hour = (hour - utc_offset) % 24
            period = "AM" if 0 <= hour < 12 else "PM"
            hour = 12 if hour == 0 or hour == 12 else hour % 12
            return f"{hour}:{minute:02} {period}"

        unique_times = sorted(set(time_list))
        formatted_times = [convert_to_12_hour_format(hour, minute, utc) for hour, minute, utc in unique_times]
        return ', '.join(formatted_times)


    def get_usernames(text: str) -> list[str]:
        """Get usernames from text."""
        return list(set(re.findall(r"usr:([\w\d_]+)", text)))


    def get_errors(text: str) -> list[int]:
        """Get errors from text."""
        return sorted(set(int(match) for match in re.findall(r"error (\d{1,3})", text, flags=re.IGNORECASE)))


    def get_addresses(text: str) -> list[str]:
        """Get IPv4 addresses from text."""
        return list(set(re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", text)))


    def get_endpoints(text: str) -> list[str]:
        """Get endpoints from text."""
        return list(set(re.findall(r"\/[\w\d&/?=_%-]+", text)))

    categories = {
        "time": get_times(text),
        "user": get_usernames(text),
        "error": get_errors(text),
        "ipv4": get_addresses(text),
        "endpoint": get_endpoints(text)
    }

    # Remove empty categories
    categories = {key: value for key, value in categories.items() if value}

    longest_header = max(map(len, categories))
    result = ""
    for key, value in categories.items():
        if key == "time":
            formatted_time = get_formatted_time(value)
            result += f"{key:<{longest_header}} | {formatted_time}\n"
        else:
            result += f"{key:<{longest_header}} | {', '.join(map(str, sorted(value)))}\n"

    return result.rstrip("\n")


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
