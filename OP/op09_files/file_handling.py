"""Files."""
import csv
from datetime import datetime


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list[dict]:
    """
    Read data from a CSV file and cast values into different data types based on their content.

    Fields containing only numbers are cast into integers.
    Fields containing dates (in the format dd.mm.yyyy) are cast into date.
    Otherwise, the data type remains string (default by csv reader).
    The order of elements in the list matches the lines in the file.
    None values don't affect the data type (the column will have the type based on the existing values).

    Hint: For date parsing, you can use the strptime method. See examples here:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date

    If a field contains only numbers, it's cast to int:
    name,age
    john,11
    mary,14

    Will become ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    If a field contains text or mixed content, it remains as a string:
    name,age
    john,11
    mary,14
    ago,unknown

    Will become ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    If a field contains only dates, it's cast to date:
    name,date
    john,01.01.2022
    mary,07.09.2023

    Will become:
    [
      {'name': 'john', 'date': datetime.date(2022, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2023, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2022
    mary,late 2023

    Will become:
    [
      {'name': 'john', 'date': "01.01.2022"},
      {'name': 'mary', 'date': "late 2023"},
    ]

    A missing value "-" is interpreted as None (data type is not affected):
    name,date
    john,-
    mary,07.09.2023

    Will become:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2023, 9, 7)},
    ]

    :param filename: The name of the CSV file to read.
    :return: A list of dictionaries containing processed field values.
    """
    data = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        # Determine the data type for each column
        types = {column: 'int' for column in reader.fieldnames}
        for row in rows:
            for column, value in row.items():
                if value != '-':
                    if types[column] == 'int':
                        if not value.isdigit():
                            types[column] = 'date'
                    if types[column] == 'date':
                        try:
                            datetime.strptime(value, '%d.%m.%Y')
                        except ValueError:
                            types[column] = 'str'

        # Convert the data
        for row in rows:
            new_row = {}
            for column, value in row.items():
                if value == '-':
                    new_row[column] = None
                elif types[column] == 'int':
                    new_row[column] = int(value)
                elif types[column] == 'date':
                    new_row[column] = datetime.strptime(value, '%d.%m.%Y').date()
                else:
                    new_row[column] = value
            data.append(new_row)

    return data


if __name__ == '__main__':
    print(read_csv_file_into_list_of_dicts_using_datatypes(filename="input.csv"))
