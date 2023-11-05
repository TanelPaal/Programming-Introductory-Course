"""File."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into a string.

    In this exercise, assume that the file exists.

    :param filename: The name of the file to read.
    :return: The contents of the file as a string.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list[str]:
    r"""
    Read file contents into a list of lines.

    In this exercise, assume that the file exists.

    Each line from the file is a separate element in the list,
    and the order of the list matches the order in the file.
    Newline characters ('\n') are removed from each line.

    :param filename: The name of the file to read.
    :return: A list of lines without newline characters.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip('\n') for line in file]


def read_csv_file(filename: str) -> list[list[str]]:
    """
    Read CSV file contents into a list of rows.

    Each row is represented as a list of "columns" or fields.

    Example CSV (Comma-separated values) data:
    name,age
    john,12
    mary,14

    Will return as:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Note: The "csv" module should be used.

    :param filename: The name of the file to read.
    :return: A list of lists, where each inner list represents a row of CSV data.
    """
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.strip().split(',')
            result.append(columns)
    return result


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to a file.

    If the file does not exist, it will be created.
    If the file already exists, its contents will be overwritten.

    :param filename: The name of the file to write to.
    :param contents: The content to write to the file.
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list[str]) -> None:
    """
    Write lines to a file.

    Each string in the 'lines' list represents a separate line in the file.
    The function ensures that there is no extra newline added at the end of the file,
    unless the last element in the 'lines' list itself ends with a newline.

    :param filename: The name of the file to write to.
    :param lines: A list of strings, each representing a line to write to the file.
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        if lines and not lines[-1].endswith('\n'):
            file.write('\n'.join(lines[:-1]))
            file.write('\n' + lines[-1] if lines[:-1] else lines[-1])
        else:
            file.writelines('\n'.join(lines))


def write_csv_file(filename: str, data: list[list[str]]) -> None:
    """
    Write data into a CSV file.

    The data is a list of lists, where each inner list represents a row,
    and the elements within each inner list represent the columns.

    Example data:
    [["name", "age"], ["john", "11"], ["mary", "15"]]

    Will be written in the .csv file as:
    name,age
    john,11
    mary,15

    Note: The "csv" module should be used.

    :rtype: object
    :param filename: The name of the file to write to.
    :param data: A list of lists to write to the file, where each list represents a row.
    :return: None
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two input CSV files into one output CSV file.

    The dates file contains names and dates separated by a colon, and the towns file contains
    names and towns separated by a colon. Both files have no headers.

    Example format of the dates file:
    john:01.01.2001
    mary:06.03.2016

    Example format of the towns file:
    john:london
    mary:new york

    The merging is performed based on the names found in input files.
    The order of the lines in the output file follows the order in the dates input file.
    Names that are missing in the dates input file will follow the order in the towns input file.
    The order of the fields is: name, town, date.

    The resulting CSV file should have the following format:
    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be represented as "-" in the output file.

    Example:
    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Reuse CSV reading and writing functions.
    Note: When reading CSV files, specify the delimiter (improve existing method).

    :param dates_filename: The name of the CSV file with names and dates (name:date).
    :param towns_filename: The name of the CSV file with names and towns (name:town).
    :param csv_output_filename: The name of the CSV file to write to names, towns, and dates.
    :return: None
    """
    # Read dates file and create a dictionary with names as keys and dates as values
    with open(dates_filename, 'r', newline='', encoding='utf-8') as file:
        dates_reader = csv.reader(file, delimiter=':')
        dates_dict = {rows[0]: rows[1] for rows in dates_reader}

    # Read towns file and create a dictionary with names as keys and towns as values
    with open(towns_filename, 'r', newline='', encoding='utf-8') as file:
        towns_reader = csv.reader(file, delimiter=':')
        towns_dict = {rows[0]: rows[1] for rows in towns_reader}

    # Merge the dictionaries into a single dictionary for output
    merged_data = {}
    for name in dates_dict:
        merged_data[name] = {
            'town': towns_dict.get(name, '-'),
            'date': dates_dict[name]
        }

    for name in towns_dict:
        if name not in merged_data:
            merged_data[name] = {
                'town': towns_dict[name],
                'date': '-'
            }

    # Write the merged data to the CSV output file
    with open(csv_output_filename, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        # Write header
        csv_writer.writerow(['name', 'town', 'date'])
        # Write data from the dates file first, followed by any additional data from the towns file
        for name in dates_dict.keys():
            csv_writer.writerow([name, merged_data[name]['town'], merged_data[name]['date']])
        for name in towns_dict.keys():
            if name not in dates_dict:
                csv_writer.writerow([name, merged_data[name]['town'], merged_data[name]['date']])


def read_csv_file_into_list_of_dicts(filename: str) -> list[dict[str, str]]:
    """
    Read a CSV file into a list of dictionaries.

    The header line of the CSV file will be used as keys for the dictionaries.
    If there are only headers or no rows in the CSV file, the result is an empty list.
    Each line after the header line will result in a dictionary inside the result list.
    Every line should contain the same number of fields.
    The order of the elements in the list corresponds to the lines in the file
    (the first line becomes the first element, and so on).

    Given a CSV file like this:
    name,age,sex
    John,12,M
    Mary,13,F

    The result will be:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    :param filename: The name of the CSV file to read.
    :return: A list of dictionaries where keys are taken from the header and values are strings.
    """
    result = []
    with open(filename, 'r', newline='', encoding="utf-8") as file:
        # Use DictReader to directly read the file into a dictionary
        csv_reader = csv.DictReader(file)
        # Convert each row in the reader to a dictionary and append to result list
        for row in csv_reader:
            # Ensure that all values are strings as required
            result.append({key: str(value) for key, value in row.items()})
    return result


def write_list_of_dicts_to_csv_file(filename: str, data: list[dict]) -> None:
    """
    Write a list of dictionaries to a CSV file.

    Each dictionary in the 'data' list represents a row in the CSV file,
    with dictionary keys representing the fields of a header.
    Fields missing in certain rows will be empty in these rows.
    The order of rows in the file matches the order of elements in the list.

    Example data:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]

    This data will be written to the CSV file as:
    name,age,town
    john,12,
    mary,,London

    :param filename: The name of the file to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        # If there's no data, no further action is required
        if not data:
            return

        # Collect all keys from all dictionaries to ensure all fields are captured
        fieldnames = list({key for single_dict in data for key in single_dict.keys()})

        # Create a csv writer object and write the header
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Write the data rows
        for row in data:
            csv_writer.writerow(row)


if __name__ == '__main__':
    #  merge_dates_and_towns_into_csv(dates_filename="dates.csv", towns_filename="towns.csv", csv_output_filename="output.csv")
    #  print(read_csv_file_into_list_of_dicts(filename="input.csv"))
    input_list = [
        {"name": "John"},
        {"name": "Mary", "age": "19", "town": "tallinn"}
    ]
    write_list_of_dicts_to_csv_file(filename="dict_output.csv", data=input_list)
