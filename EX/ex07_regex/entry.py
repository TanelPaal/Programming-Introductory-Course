"""Entry."""
import re


def parse(row: str) -> tuple:
    """
    Parse string row into a tuple.

    The row has a first forename, last forename, ID code, phone number, date of birth and address.
    Only ID code is mandatory, other values may not be included.

    They can be found by the following rules:
    - Both the first forename and last forename begin with a capital letter and are followed by a lowercase letter
    - ID code is an 11-digit number
    - Phone number has the same rules applied as in the previous task
    - Date of birth is in the form of dd-MM-YYYY
    - Address is everything else that's left

    :param row: given string to find values from
    :return: tuple of values found in given string
    """
    pattern = r'([A-ZÕÄÖÜ][a-zõäöü]+)?([A-ZÕÄÖÜ][a-zõöäü]+)?([0-9]{11})((\+\d{3}\s*)?([0-9]{7,8}))?(\d{2}\-\d{2}\-\d{4})?(.+)?'
    parsed_data = re.search(pattern, row)

    forename = parsed_data.group(1)
    surname = parsed_data.group(2)
    id_code = parsed_data.group(3)
    phone_number = parsed_data.group(4)
    date_of_birth = parsed_data.group(7)
    address = parsed_data.group(8)

    return (forename, surname, id_code, phone_number, date_of_birth, address)


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # (None, None, '39712047623', None, None, None)
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', None, '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', None, 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623'))
    # (None, None, '39712047623', None, None, None)
