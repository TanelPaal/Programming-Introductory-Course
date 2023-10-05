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
    phones = list_of_phones(all_phones)  # Get list of phones from the input string.
    brand_model_dict = {}  # Create a dictionary to store brands and their models.

    for phone in phones:
        brand, model = phone.split(' ', 1)  # Split the phone into brand and model.
        brand = brand.strip()
        model = model.strip()

        # If brand is not in the dictionary, add it with an empty list as the value.
        if brand not in brand_model_dict:
            brand_model_dict[brand] = []
        # Add the model to the list of models for the brand, but only if it's not already there.
        if model not in brand_model_dict[brand]:
            brand_model_dict[brand].append(model)

    # Create the final output list with structured information about brands and models.
    brand_model_list = [[brand, models] for brand, models in brand_model_dict.items()]
    return brand_model_list


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
    # Create a dictionary from an existing phone list to make it easier to add phones.
    existing_phones_dict = {brand: models for brand, models in phone_list}

    # Use the phone_brand_and_models func to process the input string and create structured information.
    new_phone_list = phone_brand_and_models(all_phones)
    print(new_phone_list)

    # Loop through the new_phone_list and add phones to the existing list.
    for brand, models in new_phone_list:
        if brand in existing_phones_dict:
            # If the brand already exists in the list, add new models to it.
            existing_phones_dict[brand].extend(models)
        else:
            # If the brand is not in the list, add it as a new entry.
            existing_phones_dict[brand] = models

    # Convert the dictionary back to the required format for the output.
    updated_phones_list = [[brand, models] for brand, models in existing_phones_dict.items()]

    return updated_phones_list


def number_of_phones(all_phones: str) -> list:
    """
    Create a list of tuples with brand quantities.

    The result is a list of tuples.
    Each tuple is in the form: (brand_name: str, quantity: int).
    The order of the tuples (brands) is the same as the first appearance in the list.
    """
    phones = list_of_phones(all_phones)  # Get list of phones from the input string.
    brand_quantity_dict = {}

    for phone in phones:
        brand = phone.split(' ', 1)[0]  # Split the phone into brand and model, and get the brand.
        brand = brand.strip()  # Remove whitespace from brand.

        if brand in brand_quantity_dict:
            # If the brand already exists in the dictionary, increase the quantity by 1.
            brand_quantity_dict[brand] += 1
        else:
            # If the brand is not in the dictionary, add it with a quantity of 1.
            brand_quantity_dict[brand] = 1

    # Create the final output list.
    brand_quantity_list = [(brand, quantity) for brand, quantity in brand_quantity_dict.items()]

    return brand_quantity_list


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    [['IPhone', ['11']], ['Google', ['Pixel']]] =>
    "IPhone 11,Google Pixel"
    """
    # Store phone strings in an empty list.
    phone_strings = []

    # Loop through the input list and create phone strings.
    for brand, models in phone_list:
        for model in models:
            phone_strings.append(f"{brand} {model}")

    # Create the final output string by joining the phone strings using commas.
    result = ','.join(phone_strings)

    return result

# Add test cases if needed.
if __name__ == '__main__':

