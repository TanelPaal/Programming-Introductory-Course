"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    # Check for no input.
    if not all_phones.strip():
        return []

    return [phone.strip() for phone in all_phones.strip().split(',')]


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    brand_list = []  # Create an empty list to store unique phone brands.

    # Iterate through each phone in the list of phones.
    for phone in list_of_phones(all_phones):
        model = phone.split(' ', 1)[0]  # Extract the brand (the part before the first space).
        if model in brand_list:
            continue
        brand_list.append(model)  # Add the brand to the list if it's not already present.

    return brand_list


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    # Check if the input string is empty.
    if not all_phones:
        return []

    model_list = []  # Create an empty list to store unique phone models.

    # Iterate through each phone in the list of phones.
    for phone in list_of_phones(all_phones):
        model = phone.split(' ', 1)[1]  # Extract the model (the part after the first space).
        if model not in model_list:
            model_list.append(model)  # Add the model to the list if it's not already present.
            print(model_list)
    return model_list


def search_by_brand(all_phones: str, brand_to_search: str):
    """
    Search for phones by brand and return a list of matching phones (brand and model).

    :param all_phones:
    :param brand_to_search:
    :return:
    """
    results = []  # Create an empty list to store matching phones.
    search_term = brand_to_search.lower()  # Convert the search term to lowercase for case-insensitive matching.

    # Iterate through each phone in the list of phones.
    for phone in list_of_phones(all_phones):
        brand = phone.split(' ', 1)[0]  # Extract the brand (the part before the first space).
        if brand.lower() == search_term:
            results.append(phone)  # Add the phone to the results list if it matches and is not already present.
    return results  # Return the list of matching phones (brand and model).


def search_by_model(all_phones: str, model_to_search: str) -> list:
    """
    Search for phones by model and return a list of matching phones (brand and model).

    :param all_phones:
    :param model_to_search:
    :return:
    """
    results = []  # Create an empty list to store matching phones.
    search_term = model_to_search.lower()  # Convert the search term to lowercase for case-insensitive matching.

    # Iterate through each phone in the list of phones.
    for phone in list_of_phones(all_phones):
        if search_term in phone.lower().split(' ')[1:]:
            results.append(phone)  # Add the phone to the results list if it matches and is not already present.
    return results  # Return the list of matching phones (brand and model).


def phone_brand_and_models(all_phones: str):
    """
    Create a list of structured information about brands and models.

    For each different phone brand in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the brand (string),
    the second element is a list of models for the given brand (list of strings).

    No duplicate brands or models should be in the output.

    The order of the brands and models should be the same as in the input list (first appearance).

    "Honor Magic5,IPhone 11,IPhone 12,Google Pixel,Samsung Galaxy S22,IPhone 13,IPhone 13,Google Pixel2" =>
    [['Honor', ['Magic5']], ['IPhone', ['11', '12', '13']], ['Google', ['Pixel', 'Pixel2']], ['Samsung', ['Galaxy S22']]]
    """
    phone_names = all_phones.split(',')
    brand_models = {}

    


    result = []  # List in lists
    return result


def add_phones(phone_list, all_phones) -> list:
    """
    Add phones from the list into the existing phone list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated phones (as in all the previous functions).
    The task is to add phones from the string into the list.

    Hint: This and phone_brand_and_models are very similar functions. Try to use one inside another.

    [['IPhone', ['11']], ['Google', ['Pixel']]] and "IPhone 12,Samsung Galaxy S22,IPhone 11"

        =>

    [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]
    """
    return []


def number_of_phones(all_phones: str) -> list:
    """
    Create a list of tuples with brand quantities.

    The result is a list of tuples.
    Each tuple is in the form: (brand_name: str, quantity: int).
    The order of the tuples (brands) is the same as the first appearance in the list.
    """
    return []


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    [['IPhone', ['11']], ['Google', ['Pixel']]] =>
    "IPhone 11,Google Pixel"
    """


if __name__ == '__main__':
    print(phone_brand_and_models("Honor Magic5,Google Pixel2,Google Pixel6,IPhone 7,Google Pixel,Google Pixel,IPhone 14"))
    # [['Honor', ['Magic5']], ['Google', ['Pixel2', 'Pixel6', 'Pixel']], ['IPhone', ['7', '14']]]

    print(phone_brand_and_models("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # [['Google', ['Pixel']]]
    print(phone_brand_and_models(""))  # []

    print(add_phones([['IPhone', ['11']], ['Google', ['Pixel']]], "IPhone 12,Samsung Galaxy S22,IPhone 11"))
    # [['IPhone', ['11', '12']], ['Google', ['Pixel']], ['Samsung', ['Galaxy S22']]]

    print(number_of_phones("IPhone 11,Google Pixel,Honor Magic5,IPhone 12"))  # [('IPhone', 2), ('Google', 1), ('Honor', 1)]

    print(number_of_phones("HTC one,HTC one,HTC one,HTC one"))  # [('HTC', 4)]

    print(number_of_phones(""))  # []

    print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))  # "IPhone 11,Google Pixel"
