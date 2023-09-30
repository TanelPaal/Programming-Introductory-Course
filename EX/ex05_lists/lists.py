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
    # Split the input string by commas to separate brands and models.
    phones_list = all_phones.split(',')

    return phones_list


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    # Check if the input string is empty.
    if not all_phones:
        return []
    # An empty list for containing unique phone brands.
    unique_brands = []
    # Split the input string by commas to separate brands and models.
    phones_list = all_phones.split(',')

    for name in phones_list:
        # Extract the brand.
        brand = name.split(' ')[0]
        # Check if the brand is not already in the list.
        if brand not in unique_brands:
            unique_brands.append(brand)

    return unique_brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    # Check if the input string is empty.
    if not all_phones:
        return []
    # An empty list for containing unique phone models.
    unique_models = []
    # Split the input string by commas to separate brands and models.
    phones_list = all_phones.split(',')

    for name in phones_list:
        # Extract the words in the name.
        words = name.split(' ')
        # Extract the model.
        if len(words) >= 2:
            model = ' '.join(words[1:])
            if model not in unique_models:
                unique_models.append(model)

    return unique_models


def search_by_brand(*all_phones: str) -> list:
    # Extract the last string.
    brand = all_phones[-1].lower()

    # Combine all string into one large string, separating phone names with commas.
    combined_phone_list = ', '.join(all_phones[:-1])

    # Split the list of phones by comma and remove whitespace.
    phones = combined_phone_list.split(',')
    phones = [phone.strip() for phone in phones]

    # Filter the list of phones, keeping only those from the searched brand.
    result = [phone for phone in phones if brand in phone.lower()]
    # Remove duplicates.
    result = list(set(result))

    return result


def search_by_model(*all_phones: str) -> list:
    # Extract the last string.
    model = all_phones[-1].lower()

    # Combine all string into one large string, separating phone names with commas.
    combine_phone_list = ', '.join(all_phones[:-1])

    # Split the list of phones by comma and remove whitespace.
    phones = combine_phone_list.split(',')
    phones = [phone.strip() for phone in phones]

    # Filter the list of phones, keeping only those from the searched model.
    result = [phone for phone in phones if model in phone.lower()]
    # Remove duplicates.
    result = list(set(result))

    return result


if __name__ == '__main__':
    print("\nPrint of all phones:")
    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))  # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(list_of_phones(""))  # []

    print("\nSearch for Brand names:")
    print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))  # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))  # ['Google']
    print(phone_brands(''))  # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14,Samsung Galaxy S23,IPhone 14 Pro Max"))  # ['14', 'Pixel', 'Magic5', 'Galaxy S23', '14 Pro Max']

    print("\nSearch by Brand:")
    print(search_by_brand("IPhone 14,iphone 7,IPHONE 11 Pro,IPhone 14,Google Pixel,Honor Magic5,IPhone 14 Pro Max,", "iphone"))
    print(search_by_brand("Honor Magic6,Honor Magic5,Honor Whatever", "Honor"))
    print(search_by_brand("Google Pixel", "Google Pixel", "Google Pixel", "Google Pixel2", "Google Pixel 2022", "Google"))

    print("\nSearch by Model:")
    print(search_by_model("IPhone 14,iphone 7,IPHONE 11 Pro,Google Pixel,IPhone 14 Pro Max,IPhone 14 Pro Max", "Pro"))
    print(search_by_model("IPhone 14,iphone 7,IPHONE 11 Pro,Google Pixel,IPhone 14 Pro Max,IPhone 14 Pro Max", "Pro Max"))
    print(search_by_brand("Google Pixel", "Google Pixel", "Google Pixel", "Google Pixel2", "Google Pixel 2022", "Pixel"))
    print(search_by_brand("Google Pixel", "Google Pixel", "Google Pixel", "Google Pixel2", "Google Pixel 2022", "Pixel2"))
