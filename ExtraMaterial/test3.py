"""Exam3."""
import string


def find_names_from_text(text: str) -> list:
    """
    Return list of names from the text.

    In the text, words are separated by single space.
    A word which starts with a capital letter is considered a name.
    Put all the words in to the result list.
    The text contains only latin letters (a-z, A-Z) and spaces.

    The names in the result should appear in the same order as in the input text.

    find_names_from_text("hello World")  => ["World"]
    find_names_from_text("hello World and John Smith")  => ["World", "John", "Smith"]
    find_names_from_text("hello world")  => []
    find_names_from_text("")  => []
    find_names_from_text("Exam")  => ["Exam"]
    find_names_from_text("YES")  => ["YES"]
    """
    # Split the text into words
    words = text.split()

    # List to store names
    names = []

    # Iterate through words and check if the first letter is uppercase
    for word in words:
        if word[0].isupper():
            names.append(word)

    return names


def growing_triplets(numbers: list) -> list:
    """
    Add elements where the previous value is lower and the next value is larger into a new list.

    Function has to create a new list, where the middle value of three consecutive numbers are added
    if the three numbers are growing in value (the first number is smaller than the second number and
    the third number is larger than the second number).

    growing_triplets([1, 2, 3]) => [2]
    growing_triplets([1, 2, 3, 4]) => [2, 3]
    growing_triplets([1, 5, 3, 4]) => []
    growing_triplets([1, 2]) => []
    growing_triplets([]) => []
    :param numbers:
    :return:
    """
    # List to store the results
    result = []

    # Iterate through the list, checking sets of three numbers
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] and numbers[i] < numbers[i + 1]:
            result.append(numbers[i])

    return result


def encode_string_with_hex_key(input_str: str, key: str) -> str:
    """
    Encode string using key.

    :param input_str - string to encode. Non-alphabetic characters are left as is.
    Caps are encoded into caps.
    :param key - hex key in which n-th number tells how much should n-th char in input_str be shifted.
    Works as round buffer, eg. if z is reached start from a again.
    The input_str and key are always the same length.

    Alphabet: abcdefghijklmnopqrstuvwxyz
    Upper case: ABCDEFGHIJKLMNOPQRSTUVWXYZ

    encode_string_with_hex_key("a", "1") -> "b"
    encode_string_with_hex_key("z", "1") -> "a"
    encode_string_with_hex_key("abc", "101") -> "bbd"
    encode_string_with_hex_key("Abc", "101") -> "Bbd"
    encode_string_with_hex_key("z.z.z", "fffff") -> "o.o.o"

    :return Encoded string
    """
    # Define the alphabets
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Encoded string
    encoded_str = ""

    for i, char in enumerate(input_str):
        # Check if the character is alphabetic and find the alphabet
        if char.isalpha():
            if char.islower():
                alphabet = lowercase
            else:
                alphabet = uppercase

            # Find the original index of the character
            index = alphabet.index(char)

            # Convert the corresponding key character from hex to decimal
            shift = int(key[i], 16)

            # Calculate the new index and perform the shift
            new_index = (index + shift) % 26

            # Append the shifted character to the encoded string
            encoded_str += alphabet[new_index]
        else:
            # Non-alphabetic characters are added as is
            encoded_str += char

    return encoded_str


def sum_of_multipliers(first_num: int, second_num: int, limit: int) -> int:
    """
    Sum all unique multipliers for two numbers.

    The task is to findg all the multipliers of two given numbers within the limit.
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
    score = []
    num = first_num
    while first_num <= limit:
        if first_num not in score:
            score.append(first_num)
        first_num += num
        if first_num > limit:
            break
    num = second_num
    while second_num <= limit:
        if second_num not in score:
            score.append(second_num)
        second_num += num
        if second_num > limit:
            break
    total = 0
    for num in score:
        total += num
    return total


def count_the_dumplings(day: int) -> int:
    """
    Count the dumplings.

    You are the production engineer of new dumpling factory.
    Each day the factory has to double it's dumpling production.
    Your manager asked you how many dumplings are we making on day X.
    As a lazy software engineer you decided to write a recursive program to count it.
    This function CANNOT contain any while/for loops.
    NB: The factory started working on day one and before that it made 0 dumplings.
    count_the_dumplings(0) => 0
    count_the_dumplings(1) => 1
    count_the_dumplings(2) => 2
    count_the_dumplings(3) => 4
    count_the_dumplings(30) ==> 536870912
    """
    if day <= 0:
        return 0
    if day == 1:
        return 1
    else:
        return 2 * count_the_dumplings(day - 1)


def prime_factorization(number: int) -> int:
    """
    Return the prime factorization of the number.

    Return dict, where the key is a prime factor and the value is count of this factor.

    12 = 2 * 2 * 3 => {2: 2, 3:1}
    1960 = 2 * 2 * 2 * 5 * 7 * 7 => {2: 3, 5: 1, 7: 2}
    79 = 71 * 1 => {79: 1}

    Prime number is a number which is divisible only by 1 and the number itself.
    For example 2, 3, 5, 7, 11, 13, 17, 19, 23 are prime numbers.

    Examples:
    2 => { 2: 1 }
    12 => { 2: 2, 3: 1 }
    1960 => { 2: 3, 5: 1, 7: 2 }
    1024 => { 2: 10 }
    79 => { 79: 1 }z
    121 => { 11: 2 }

    :param number: a number greater than 1
    :return: dict of prime factors and their counts.
    """
    # Dictionary to store prime factors and their counts
    factors = {}

    # Divide by 2 as long as the number is even
    count = 0
    while number % 2 == 0:
        count += 1
        number //= 2
    if count > 0:
        factors[2] = count

    # Check for odd factors starting from 3
    factor = 3
    while factor * factor <= number:
        count = 0
        while number % factor == 0:
            count += 1
            number //= factor
        if count > 0:
            factors[factor] = count
        factor += 2

    # If the remaining number is a prime number greater than 2
    if number > 2:
        factors[number] = 1

    return factors


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Initialize book.

        Each book has title, author and price.
        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Initialize store.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        return book not in self.books and book.rating >= self.rating

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        return book in self.books

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self.books, key=lambda book: book.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        if not self.books:
            return []
        highest_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == highest_rating]


# Complex OOP. Car dealership.


class Accessory:
    """Accessory."""

    def __init__(self, name: str, value: int):
        """Initialize accessory."""
        self.name = name
        self.value = value

    def __repr__(self):
        """
        Return string representation of accessory.

        Returns string in form "{name}, value : {value}."
        """
        return f"{self.name}, value: {self.value}"


class Car:
    """Car."""

    def __init__(self, name: str, color: str):
        """Initialize car."""
        self.name = name
        self.color = color
        self.accessories = []
        self.fuel = 100  # Assuming all cars start with 100% fuel
        self.is_premium = False  # By default, a car is not premium

    def add_accessory(self, accessory: Accessory):
        """Add accessory to the car."""
        self.accessories.append(accessory)

    def get_value(self) -> int:
        """
        Get the value of the car.

        Regular car base price is 9500, for premium car its 42 500.
        All the values of accessories are summed up.
        """
        base_price = 42500 if self.is_premium else 9500
        return base_price + sum(accessory.value for accessory in self.accessories)

    def get_fuel_left(self):
        """Return how much fuel is left in percentage."""
        return self.fuel

    def get_accessories_by_value(self):
        """Return accessories sorted by value (descending i.e. higher to lower)."""
        return sorted(self.accessories, key=lambda accessory: accessory.value, reverse=True)

    def __repr__(self):
        """
        Return string representation of the car.

        Should return "This {color} {name} contains {accessory_amount} accessories and has {fuel}% fuel left."
        """
        accessory_amount = len(self.accessories)
        return f"This {self.color} {self.name} contains {accessory_amount} accessories and has {self.fuel}% fuel left."


class Customer:
    """Customer."""

    def __init__(self, name: str, wish: str):
        """
        Initialize customer.

        The wish consists of two words.
        The first word is either "Cheap" or "Expensive".
        In case of "Cheap", the customer wants to get the car with the lowest value.
        In case of "Expensive", the customer wants to get the car with the highest value.
        The second word is the color. Customer does not want a car with another color.
        For premium customer a car with the given color is searched for from the premium cars.
        If there is no such car with the wished color, the cheapest car is taken from the premium cars.

        For example: "Cheap Red", "Expensive Yellow".
        """
        self.name = name
        self.wish = wish.split()
        self.is_premium = False
        self.garage = []

    def get_garage(self):
        """
        Return all the cars of the customer sorted by the value (ascending i.e. from lower to higher).

        Both regular and premium cars are kept in garage.
        """
        return sorted(self.garage, key=lambda car: car.get_value())

    def make_premium(self):
        """Make customer a premium customer, premium cars can be sold to the customer now."""
        self.is_premium = True

    def drive_with_car(self, driving_style: str):
        """
        Go for a drive.

        A car with the highest fuel percentage should be taken.
        If several cars have the same percentage, use the most expensive one.

        If the driving_style is "Rally", the customer takes the cheapest car instead.
        Regular driving takes 15 percentage points of fuel, "Rally" takes 35 percentage points (85% - 35% => 50%).
        If the fuel gets to zero during the drive, the car is left behind (it is no longer part of garage).
        """
        return  # No car to drive

        if driving_style == "Rally":
            # Select the car with the lowest value
            car_to_drive = min(self.garage, key=lambda car: car.get_value())
        else:
            # Select the car with the highest fuel, if tie, choose the most expensive
            car_to_drive = max(self.garage, key=lambda car: (car.get_fuel_left(), car.get_value()))

        fuel_consumption = 35 if driving_style == "Rally" else 15
        car_to_drive.fuel -= fuel_consumption

        # Remove the car from the garage if it runs out of fuel
        if car_to_drive.get_fuel_left() <= 0:
            self.garage.remove(car_to_drive)


class Dealership:
    """Dealership."""

    def __init__(self, name: str):
        """Initialize dealership."""
        self.name = name
        self.cars = []

    def add_car(self, car: Car):
        """Add car to the dealership."""
        self.cars.append(car)

    def get_all_regular_cars(self):
        """Return all the regular cars sorted by value (ascending, lower to higher)."""
        return sorted([car for car in self.cars if not car.is_premium], key=lambda car: car.get_value())

    def make_car_premium(self, car: Car):
        """Make a car premium, which can can be sold only to premium customers."""
        car.is_premium = True

    def get_all_premium_cars(self):
        """Return all the premium cars sorted by value (ascending, lower to higher)."""
        return sorted([car for car in self.cars if car.is_premium], key=lambda car: car.get_value())

    def sell_car_to_customer(self, customer: Customer):
        """
        Sell a car to customer depending on his/her wishes.

        After selling, the car is removed from the dealership and moved into customer's garage.
        In the given exercise, there is always a matching car.
        """
        pass


if __name__ == '__main__':
    print(growing_triplets([1, 2, 3, 4]))
    assert find_names_from_text("hello World and John Smith") == ["World", "John", "Smith"]
    assert find_names_from_text("hello world") == []
    assert find_names_from_text("") == []
    assert find_names_from_text("Exam") == ["Exam"]
    assert find_names_from_text("YES") == ["YES"]

    assert growing_triplets([1, 2, 3]) == [2]
    assert growing_triplets([1, 2, 3, 4]) == [2, 3]
    assert growing_triplets([1, 5, 3, 4]) == []
    assert growing_triplets([1, 2]) == []
    assert growing_triplets([]) == []

    assert encode_string_with_hex_key("a", "1") == "b"
    assert encode_string_with_hex_key("z", "1") == "a"
    assert encode_string_with_hex_key("abc", "101") == "bbd"
    assert encode_string_with_hex_key("z.z.z", "fffff") == "o.o.o"
    #
    assert sum_of_multipliers(3, 3, 20) == 63
    assert sum_of_multipliers(3, 1, 20) == 210
    #
    assert count_the_dumplings(3) == 4
    assert count_the_dumplings(0) == 0
    assert count_the_dumplings(30) == 536870912

    assert prime_factorization(12) == {2: 2, 3: 1}
    assert prime_factorization(1960) == {2: 3, 5: 1, 7: 2}

    # Book store

    store = Store("Apollo", 98.9)
    book = Book("War & Peace", "Leo Tolstoy", 10.5, 99)

    print(store.can_add_book(book))  # True

    store.add_book(book)
    print(store.get_all_books())  # [book]

    book2 = Book("War & Peace", "Leo Tolstoy", 10.5, 99)
    assert store.can_add_book(book2) is False  # cannot add book with the same title and author

    book3 = Book("War", "Leo Tolstoy", 10.5, 80)
    assert store.can_add_book(book3) is False  # cannot add book since its rating is too low

    # dealership

    blue_car = Car("Audi R4", "blue")
    green_car = Car("Ford", "green")
    wheel = Accessory("Sport wheel", 100)
    blue_car.add_accessory(wheel)
    car_dealer = Dealership("Ago Carfriend")
    car_dealer.add_car(blue_car)
    car_dealer.add_car(green_car)

    print(car_dealer.get_all_regular_cars())
    # [This green Ford contains 0 accessories and has 100% fuel left.,
    # This blue Audi R4 contains 1 accessories and has 100% fuel left.]
    print(car_dealer.get_all_premium_cars())  # []

    customer = Customer("Ago", "Cheap green")
    car_dealer.sell_car_to_customer(customer)
    print(customer.get_garage())  # [This green Ford contains 0 accessories and has 100% fuel left.]
    customer.drive_with_car("Rally")
    print(customer.get_garage())  # [This green Ford contains 0 accessories and has 65% fuel left.]
    customer.drive_with_car("Rally")
    customer.drive_with_car("Rally")
    print(customer.get_garage())  # []]

    car_dealer.make_car_premium(blue_car)
    print(car_dealer.get_all_premium_cars())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]

    customer_premium = Customer("Ago", "Expensive black")
    customer_premium.make_premium()
    car_dealer.sell_car_to_customer(customer_premium)
    print(customer_premium.get_garage())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]
