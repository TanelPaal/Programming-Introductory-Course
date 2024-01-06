"""Exam 1 (2024-01-05). Practice exam."""


def replace_occurrences(text: str) -> str:
    """
    Replace all occurrences of the first character in the given text with '@', except for the first character itself.

    Examples:
    replace_occurrences("Banana")  -> Banana
    replace_occurrences("rear")  -> Rea@
    replace_occurrences("11a")  -> 1@a
    replace_occurrences("Aardvark")  -> A@rdv@rk

    :param text: The input text in which replacements will be made.
    :return string of the input text in which replacements will be made. Please note that the result always starts with
    capital letter and the rest are small letters.
    """
    if not text:
        return ''
    first_letter = text[0].lower()
    rest_of_text = text[1:].lower()
    replaced_text = rest_of_text.replace(first_letter, "@")
    return first_letter.title() + replaced_text


def swap_case_string(text: str) -> str:
    """
    Take a string and swap its uppercase and lowercase letters.

    Other symbols remain the same.

    :param text: Input text that you want to process.
    :return: Text where uppercase and lowercase letters are swapped.
    """
    swapped_text = ''
    for letter in text:
        if letter.isupper():
            swapped_text += letter.lower()
        else:
            swapped_text += letter.upper()
    return swapped_text


def sum_of_multipliers(first_num: int, second_num: int, limit: int) -> int:
    """
    Sum all unique multipliers for two numbers.

    The task is to find all the multipliers of two given numbers within the limit.
    Then, find the sum of those multipliers where duplicates are removed.

    All the numbers are positive integers.

    sum_of_multipliers(3, 5, 20) => 98
    We get: [3, 6, 9, 12, 15, 18] (21 is over the limit)
    and [5, 10, 15, 20]
    15 is in both lists, we only use it once, sum is 98

    sum_of_multipliers(3, 3, 20) => 63
    sum_of_multipliers(3, 1, 20) => 210

    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    first_multi = set(range(first_num, limit + 1, first_num))
    second_multi = set(range(second_num, limit + 1, second_num))

    return sum(first_multi | second_multi)


def analyze_products(product_data: dict) -> dict:
    """
    Analyze product data and calculate statistics for each category.

    The function receives the input of the dictionary, where the keys are category names (strings),
    and the values are lists of dictionaries representing products.
    Each product dictionary have keys 'name' (string) and 'price' (float).
    Product prices are always greater than zero.

    Return:
        dict: A dictionary containing analysis results for each category.
        Each category is represented by a key, and the corresponding value is a dictionary
        with the following keys:
        - 'average price': The average price of products in the category, rounded to two decimal places.
        - 'products above average': A list of product names with prices above the category average.
        - 'products below average': A list of product names with prices below or equal to the category average.

    Example:
        product_data = {
            "Electronics": [
                {"name": "Laptop", "price": 1200},
                {"name": "Smartphone", "price": 800},
            ],
            "Clothing": [
                {"name": "T-shirt", "price": 20},
                {"name": "Jeans", "price": 50},
            ],
        }
        Output:
            {
                "Electronics": {
                    "average price": 1000.0,
                    "products above average": ["Laptop"],
                    "products below average": ["Smartphone"],
                },
                "Clothing": {
                    "average price": 35.0,
                    "products above average": ["Jeans"],
                    "products below average": ["T-shirt"],
                },
            }
    """
    result = {}

    for category, products in product_data.items():
        # Calculate avg price.
        total_price = sum(product['price'] for product in products)
        avg_price = round(total_price / len(products), 2)

        # Calculate products above and below avg price.
        above_avg = [product['name'] for product in products if product['price'] > avg_price]
        below_avg = [product['name'] for product in products if product['price'] <= avg_price]

        # Result.
        result[category] = {
            'average price': avg_price,
            'products above average': above_avg,
            'products below average': below_avg
        }

        return result


def revert_factorial(factorial: int, n=1) -> int:
    """
    Find the reverted factorial of a number.

    Input is a factorial result, find the original number.
    If the given number is not a factorial of any number return -1.
    Must be recursive!

    revert_factorial(0) => -1
    revert_factorial(120) => 5
    revert_factorial(121) => -1
    revert_factorial(39916800) => 11
    revert_factorial(51090942171709440000) => 21
    """
    if factorial < 1:
        return -1
    if factorial == 1:
        return n - 1 if n != 1 else -1
    if factorial % n == 0:
        return revert_factorial(factorial // n, n + 1)
    else:
        return -1


def matrix_transpose(matrix: list) -> list:
    """
    Transpose the given matrix.

    If matrix is squared, then you can transpose this given matrix.
    Non-squared matrix should be modified to a square one.
    You can add column or row to the matrix by adding all values in the corresponding row or column.

    In this exercise you will need to add maximum one row or one column to matrix to make it squared.

    Examples:
    1)
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    matrix_transpose(matrix) => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    2)
    matrix_non-squared = [[1, 2, 3],
                          [4, 5, 0]]
    you need to make from this matrix squared matrix
    add one more row to matrix:
    1  2  3
    +  +  +
    4  5  0
    5  7  3 => new row
    matrix after adding row:
    [[1, 2, 3],
     [4, 5, 0],
     [5, 7, 3]]

     matrix_transpose(matrix_non-squared) => [[1, 4, 5], [2, 5, 7], [3, 0, 3]]

     3)
     matrix_non-squared2 = [[1, 1],
                            [4, 6],
                            [3, 2]]

    to make new columns add all values in corresponding row:
    matrix after adding third column:
    1 + 1 = 2, 4 + 6 = 10, 3 + 2 = 5
    [[1, 1, 2],
     [4, 6, 10],
     [3, 2, 5]]

    matrix_transpose(matrix_non-squared2) => [[1, 4, 3], [1, 6, 2], [2, 10, 5]]

    4)
    matrix_empty = []
    matrix_transpose(matrix_empty) => []

    :param matrix:  The input matrix.
    :return: list of lists: The transposed matrix.
    """
    pass


# Simple OOP


class Book:
    """Book class."""

    def __init__(self, title: str, author: str, isbn: str, pages: int):
        """
        Initialize Book.

        :param title: title of the book, use title case.
        :param author: author of the book, use title case.
        :param isbn: ISBN code of the book
        :param pages: number of pages in the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages

    def __repr__(self):
        """Represent Book."""
        return f'{self.title} by {self.author}'


class Library:
    """Library class."""

    def __init__(self):
        """Initialize Library."""
        self.books = []

    def get_books(self) -> list[Book]:
        """Return all books in the Library."""
        return self.books

    def add_book(self, book: Book):
        """
        Add a book to the Library.

        :param book: Book object to add
        """
        if isinstance(book, Book):
            self.books.append(book)

    def remove_book(self, book: Book):
        """
        Remove a book if it exists in the Library.

        :param book: Book object to remove.
        """
        if isinstance(book, Book):
            self.books.remove(book)

    def find_books_by_title(self, title: str) -> list[Book]:
        """
        Find all books by a given title.

        The search is case-insensitive.

        :param title: title of the book
        :return: books with the given title
        """
        books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                books.append(book)
        return books

    def find_books_by_author(self, author: str) -> list[Book]:
        """
        Find all books by a given author.

        The search is case-insensitive.

        :param author: author of the books
        :return: books by the given author
        """
        books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                books.append(book)
        return books

    def get_number_of_books(self) -> int:
        """Get the total number of books in the Library."""
        total = 0
        for book in self.books:
            total += 1
        return total

    def get_number_of_unique_books(self) -> int:
        """Get the number of unique books in the Library, determined by ISBN."""
        unique = 0
        for book in self.books:
            if book.isbn not in self.books:
                unique += 1
        return unique

    def sort_books_alphabetically(self) -> list[Book]:
        """
        Sort the Library books alphabetically by title.

        :return: sorted books
        """
        return sorted(self.books, key=lambda book: book.title)

    def get_book_with_most_pages(self) -> Book:
        """
        Get the book from the Library that has the most pages.

        If multiple books have the same maximum number of pages, return the first book.
        """
        most_pages = self.books[0]
        for book in self.books:
            if book.pages > most_pages.pages:
                most_pages = book
        return most_pages

    def get_unique_books(self) -> list[Book]:
        """
        Return all unique books in the Library, determined by ISBN.

        If multiple books are with the same ISBN, first book must be included.
        """
        unique_books = []
        unique_books_by_isbn = []
        for book in self.books:
            if book.isbn not in unique_books_by_isbn:
                unique_books_by_isbn.append(book.isbn)
                unique_books.append(book)
        return unique_books


# Complex OOP

class Topping:
    """Ice cream Topping."""

    def __init__(self, name: str, price: int):
        """Initialize topping."""
        self.name = name
        self.price = price


class IceCream:
    """Ice Cream."""

    def __init__(self, flavour: str, price: int):
        """Initialize ice cream."""
        self.flavour = flavour
        self.price = price

    def add_topping(self, topping: Topping):
        """Add a topping to ice cream."""
        pass

    def get_toppings(self) -> list[Topping]:
        """Return a list of toppings."""
        pass

    def __eq__(self, other):
        """Two IceCreams are equals, if they have the same flavour and the same toppings."""
        pass


class Customer:
    """Customer."""

    def __init__(self, name: str, money: int):
        """Initialize customer."""
        self.name = name
        self.money = money


class Kiosk:
    """Kiosk."""

    def __init__(self):
        """Initialize kiosk."""
        pass

    def change_default_ice_cream_price(self, new_price: int):
        """Change the default price for ice cream (the price without any toppings)."""
        pass

    def add_ice_cream_flavour_to_kiosk(self, flavour: str):
        """Add new ice cream flavour to kiosk, 'chocolate' is the same as 'CHOCOLATE'. No duplicates."""
        pass

    def add_topping_to_kiosk(self, topping: Topping):
        """Add new topping to the kiosk, if kiosk didn't already have that topping."""
        pass

    def get_all_ice_cream_flavours(self) -> list[str]:
        """Return all available ice cream flavours as lowercase strings, in the same order they were added."""
        pass

    def get_all_toppings(self) -> list[Topping]:
        """Return all available toppings in this kiosk, in the same order they were added."""
        pass

    def get_all_topping_names_sorted(self) -> list:
        """Return a list of toppings names, sorted by topping prices in decreasing order."""
        pass

    def start_new_order(self, customer: Customer):
        """
        Open order for this customer.

        Can now start adding ice creams and toppings to order.
        """
        pass

    def add_to_order_ice_cream(self, flavour: str):
        """Add ice cream to order, but only, if there is an order started."""
        pass

    def add_to_order_topping(self, topping: Topping):
        """Check if there is an order started and an ice cream ordered, then add topping to this ice cream."""
        pass

    def pay_for_order(self):
        """Finish order."""
        pass

    def get_all_orders(self) -> list:
        """Return all orders, in the same order they were ordered from the kiosk."""
        pass

    def __discount_ice_cream(self, ice_cream: IceCream):
        """Ice cream is in the third order, add discount (cheapest topping for free)."""
        pass

    def __get_order_price(self) -> int:
        """Calculate the price for the whole order."""
        pass

    def get_all_orders_sorted(self) -> list:
        """
        Return all the orders sorted by the following criteria.

        Get all orders, but sorted by the amount of ice creams. (More ice creams per order, first).
        If multiple orders have the same amount of ice creams, sort those by price (more expensive order first).
        If multiple orders have the same amount of ice creams and same price, leave them in the order they were added.
        """
        pass

    def get_all_ordered_flavours(self) -> list:
        """Get a list of all the flavours of ice creams that were ordered, sorted alphabetically."""
        pass


if __name__ == '__main__':
    # replace_occurrences
    print(replace_occurrences("Banana"))  # Banana
    print(replace_occurrences("rear"))  # Rea@
    print(replace_occurrences("Aardvark"))  # A@rdv@rk
    print(replace_occurrences("11a"))  # 1@a

    # swap_case_string
    print(swap_case_string("Python Exercises"))  # pYTHON eXERCISES
    print(swap_case_string("Java"))  # jAVA
    print(swap_case_string("NumPy"))  # nUMpY

    # sum_of_multipliers
    print(sum_of_multipliers(3, 3, 20))  # 63
    print(sum_of_multipliers(3, 1, 20))  # 210

    # analyze_products
    print(analyze_products({"Electronics": [{"name": "Laptop", "price": 1200}, {"name": "Smartphone", "price": 800}, ],
                            "Clothing": [{"name": "T-shirt", "price": 20}, {"name": "Jeans", "price": 50}, ], }))
    # {"Electronics": {"average price": 1000.0, "products above average": ["Laptop"],
    # "products below average": ["Smartphone"],},"Clothing": {"average price": 35.0,"products above average": ["Jeans"],
    # "products below average": ["T-shirt"], },}

    # revert_factorial
    print(revert_factorial(0))  # => -1
    print(revert_factorial(120))  # => 5
    print(revert_factorial(121))  # => -1
    print(revert_factorial(39916800))  # => 11
    print(revert_factorial(51090942171709440000))  # => 21

    # matrix_transpose
    print(matrix_transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(matrix_transpose([[1, 2, 3], [4, 5, 0]]))  # => [[1, 4, 5], [2, 5, 7], [3, 0, 3]]
    print(matrix_transpose([[1, 1], [4, 6], [3, 2]]))  # => [[1, 4, 3], [1, 6, 2], [2, 10, 5]]
    print(matrix_transpose([]))  # => []

    # Library

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780141182636", 180)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 281)
    book3 = Book("1984", "George Orwell", "9780451524935", 328)
    book4 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769480", 224)

    library = Library()

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    print(library.get_number_of_unique_books())  # 4

    print(library.sort_books_alphabetically())  # ["1984" by George Orwell,
    # "The Catcher In The Rye" by J.D. Salinger, "The Great Gatsby" by F. Scott Fitzgerald,
    # "To Kill A Mockingbird" by Harper Lee]

    print(library.get_book_with_most_pages())  # "1984" by George Orwell

    print(library.get_unique_books())  # ["The Great Gatsby" by F. Scott Fitzgerald,
    # "To Kill A Mockingbird" by Harper Lee, "1984" by George Orwell, "The Catcher In The Rye" by J.D. Salinger]

    library.remove_book(library.find_books_by_title("To Kill a Mockingbird")[0])

    print(library.get_books())  # 3

    # Ice cream kiosk
    jack = Customer("Jack", 2000)
    kiosk = Kiosk()
    chocolate_sauce = Topping("Chocolate Sauce", 50)
    raspberries = Topping("raspberry", 70)

    vanilla_ice_cream = IceCream("vanilla", 200)
    vanilla_ice_cream2 = IceCream("VANILLA", 250)
    print(vanilla_ice_cream == vanilla_ice_cream2)  # True

    vanilla_ice_cream.add_topping(chocolate_sauce)
    print(vanilla_ice_cream.get_toppings())  # [chocolate_sauce]
    print(vanilla_ice_cream == vanilla_ice_cream2)  # False

    kiosk.add_ice_cream_flavour_to_kiosk("vanilla")
    kiosk.add_ice_cream_flavour_to_kiosk("ChoCoLaTe")
    print(kiosk.get_all_ice_cream_flavours())  # ["vanilla", "chocolate"]

    kiosk.add_topping_to_kiosk(chocolate_sauce)
    kiosk.add_topping_to_kiosk(raspberries)
    print(kiosk.get_all_toppings())  # [chocolate_sauce, raspberries]
    print(kiosk.get_all_topping_names_sorted())  # ["raspberry", "Chocolate Sauce"]

    kiosk.start_new_order(jack)
    kiosk.add_to_order_ice_cream("caramel")  # - no such flavour in the kiosk
    order0 = kiosk.pay_for_order()
    print(order0)  # None
    print(kiosk.get_all_orders())  # []
    print(jack.money)  # 2000

    kiosk.start_new_order(jack)
    kiosk.add_to_order_ice_cream("vanilla")
    kiosk.add_to_order_topping(chocolate_sauce)
    kiosk.add_to_order_ice_cream("chocolate")
    order1 = kiosk.pay_for_order()
    print(len(order1))  # 2
    print(isinstance(order1[0], IceCream))  # True
    print(isinstance(order1[1], IceCream))  # True
    print(order1[0].flavour)  # "vanilla"
    print(order1[0].get_toppings())  # [chocolate sauce]
    print(order1[0].price)  # 300
    print(order1[1].flavour)  # "chocolate"
    print(order1[1].get_toppings())  # []
    print(order1[1].price)  # 250
    print(jack.money)  # 1450
    print(kiosk.get_all_orders())  # [order2]

    kiosk.start_new_order(jack)
    kiosk.add_to_order_ice_cream("vanilla")
    kiosk.add_to_order_ice_cream("chocolate")
    kiosk.add_to_order_topping(raspberries)
    order2 = kiosk.pay_for_order()
    print(jack.money)  # 880
    print(kiosk.get_all_orders())  # [order2, order3]
    print(kiosk.get_all_orders_sorted())  # [order3, order2]

    kiosk.start_new_order(jack)
    kiosk.add_to_order_ice_cream("vanilla")
    kiosk.add_to_order_topping(chocolate_sauce)
    kiosk.add_to_order_topping(raspberries)
    order3 = kiosk.pay_for_order()  # - 3rd order, for each ice cream, the cheapest topping is for free
    print(order3[0].price)  # 320
