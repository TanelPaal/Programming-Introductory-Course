import re
from datetime import time


def get_times(text: str) -> list[tuple[int, int, int]]:
    time_pattern = r"\[([0-2]?\d)[^\d]([0-5]?\d) UTC([+-]\d{1,2})\]"
    matches = re.findall(time_pattern, text)
    valid_times = [(int(h), int(m), int(offset)) for h, m, offset in matches if 0 <= int(h) < 24 and 0 <= int(m) < 60]
    return valid_times


def get_usernames(text: str) -> list[str]:
    return re.findall(r"usr:([a-zA-Z0-9_]+)", text)


def get_errors(text: str) -> list[int]:
    return [int(match) for match in re.findall(r"error (\d{1,3})", text, re.IGNORECASE)]


def get_addresses(text: str) -> list[str]:
    return re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)


def get_endpoints(text: str) -> list[str]:
    return re.findall(r"/[a-zA-Z0-9&/=?\-_%]+", text)


def create_table_string(text: str) -> str:
    times = get_times(text)

    # Normalize and convert times to UTC and 12-hour format
    normalized_times = []
    for h, m, offset in times:
        total_minutes = h * 60 + m - offset * 60
        total_minutes %= 24 * 60  # wrap around to ensure it's within a day
        h, m = divmod(total_minutes, 60)
        t = time(h, m)
        normalized_times.append(t.strftime('%I:%M %p'))

    usernames = sorted(set(get_usernames(text)))
    errors = sorted(set(get_errors(text)))
    addresses = sorted(set(get_addresses(text)))
    endpoints = sorted(set(get_endpoints(text)))

    # Create table
    table = []
    if normalized_times:
        table.append(f"time     | {', '.join(normalized_times)}")
    if usernames:
        table.append(f"user    | {', '.join(usernames)}")
    if errors:
        table.append(f"error   | {', '.join(map(str, errors))}")
    if addresses:
        table.append(f"ipv4    | {', '.join(addresses)}")
    if endpoints:
        table.append(f"endpoint | {', '.join(endpoints)}")

    return '\n'.join(table) if table else ''

# Example usage
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
