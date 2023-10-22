import re

def create_table_string(text: str) -> str:
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
        # Convert the time to UTC
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
    time_pattern = r'(\d{1,2})\D+(\d{2}) UTC([-+]\d{1,2})'
    time_matches = re.findall(time_pattern, text)
    times = [(int(hour), int(minute), int(offset)) for hour, minute, offset in time_matches]
    return times

def get_usernames(text: str) -> list[str]:
    username_pattern = r'usr:([a-zA-Z0-9_]+)'
    usernames = re.findall(username_pattern, text)
    return usernames

def get_errors(text: str) -> list[int]:
    error_pattern = r'error (\d{1,3})'
    errors = [int(error) for error in re.findall(error_pattern, text, re.IGNORECASE)]
    return errors

def get_addresses(text: str) -> list[str]:
    address_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    addresses = re.findall(address_pattern, text)
    return addresses

def get_endpoints(text: str) -> list[str]:
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
