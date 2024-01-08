"""Exam2 (2023-01-07)."""
from typing import Optional


def find_first_pair(text: str) -> str:
    """
    Find the first (consecutive) pair of the same symbols.

    If there are no such pair, return an empty string ("").

    It doesn't matter if there are more than 2 same consecutive symbols.

    find_first_pair("abbcc") => "bb"
    find_first_pair("abcccc") => "cc"
    find_first_pair("abBcccc") => "cc"
    find_first_pair("helo  world") => "  "
    find_first_pair("2022 was good") => "22"
    find_first_pair("2023 is the best") => ""
    find_first_pair("") => ""
    """
    # Iterate over the string, stopping one character before the end
    for i in range(len(text) - 1):
        # Check if the current character is the same as the next one
        if text[i] == text[i + 1]:
            # Return the pair if found
            return text[i:i + 2]
    # Return an empty string if no pair is found
    return ""


def remove_non_palindrome_numbers(numbers: list) -> list:
    """
    Return list where all the non-palindrome numbers are removed.

    Palindrome number is a number which reads forward and backward the same: 1, 121, 55, 1001.
    If the number is a negative number, the minus does not count. So -1, -121, -99 are also palindromes.
    The result list should contain only palindromes.

    remove_non_palindrome_numbers([1, 2, 3]) => [1, 2, 3]
    remove_non_palindrome_numbers([1, 12, 62, 33]) => [1, 33]
    remove_non_palindrome_numbers([]) => []
    remove_non_palindrome_numbers([12]) => []
    remove_non_palindrome_numbers([-12]) => []
    remove_non_palindrome_numbers([-121]) => [-121]
    remove_non_palindrome_numbers([-121, 0, 12, 21, -12, 999]) => [-121, 0, 999]
    """
    def is_palindrome(num: int) -> bool:
        """Check if a number is a palindrome, ignoring the sign."""
        num_str = str(abs(num))  # Convert to string, ignoring the sign
        return num_str == num_str[::-1]  # Check if the string is the same when reversed

    return [num for num in numbers if is_palindrome(num)]


def add_symbols(string: str, symbols: str) -> str:
    """
    Return given string with added symbols where needed.

    If letter in string exists in symbols, double it in result.
    If number in string exists in symbols, triple it in result.

    It does not change the result when any symbol appears more than once in symbols.

    add_symbols("ab12", "b12a") -> "aabb111222"
    add_symbols("xyz", "xxxxxx") -> "xxyz"
    add_symbols("aaaa", "b") -> "aaaa"
    add_symbols("aab", "a") -> "aaaab"
    """
    result = []

    for char in string:
        if char.isalpha() and char in symbols:  # Check if the character is a letter and in symbols
            result.append(char * 2)  # Double the character
        elif char.isdigit() and char in symbols:  # Check if the character is a number and in symbols
            result.append(char * 3)  # Triple the character
        else:
            result.append(char)  # Include the character as-is

    return ''.join(result)


def h_index(articles: list) -> int:
    """
    Given a list where each value represents the times of citations of one article.

    Return a h index of the person.

    H-index is the largest number such that a number of publications
    have at least the same number of citations.

    Examples:
    [4, 2, 4] => 2
    [1, 2, 2] => 2
    [] => 0
    [1, 1, 1, 1] => 1
    [3, 5, 7] => 3
    [2, 5, 7] => 2
    [5, 4, 7, 3, 6] => 4
    """
    # Sort the list in descending order
    articles.sort(reverse=True)

    # Find the H-index
    for i, citations in enumerate(articles):
        if citations < i + 1:
            return i

    return len(articles)


def sum_of_digits_recursion(s: str) -> int:
    """
    Return sum of all the digits.

    The input string contains different symbols.
    Sum all the digits.

    The function has to be recursive (no loops allowed).

    sum_of_digits_recursion("123") => 6
    sum_of_digits_recursion("a") => 0
    sum_of_digits_recursion("") => 0
    sum_of_digits_recursion("1-2-3-99") => 24
    """
    if not s:  # Base case: if the string is empty
        return 0

    first_char = s[0]
    rest = s[1:]

    if first_char.isdigit():  # Check if the first character is a digit
        return int(first_char) + sum_of_digits_recursion(rest)
    else:
        return sum_of_digits_recursion(rest)


def cross_sum(num: int) -> int:
    if num < 10:
        return num
    return cross_sum(sum(int(digit) for digit in str(num)))


def combine_numbers(numbers: list) -> int:
    """
    Find two elements in the list which give the highest cross sum.

    Cross sum is the sum of all the digits in the number.
    In this exercise you have to apply cross sum calculation until the result is below 10.
    For example: cross sum of 123 => 1 + 2 + 3 => 6
    cross sum on 991 => 9 + 9 + 1 => 19. Because it is not below 10, we calculate 1 + 9 => 10. And again 1 + 0 => 1.

    Here you have to take 2 different elements from the list, put them together
    (writing the first number in front of the second number) and then calculate cross sum.
    And the combined numbers which have the highest cross sum, is the result.

    The order of the combination should be the same as the elements appear in the list.

    combine_numbers([1, 2, 3]) => 23
      we can get the combinations: 12, 13, 23. 23 is the highest
    combine_numbers([1]) => 0
      there are no combinations possible, therefore return 0
    combine_numbers([9, 1]) => 91
      combinations: 91. 9 + 1 => 10, 1 + 0 => 1
    combine_numbers([1, 2, 3, 12, 66]) => 312
      combinations:
      12 => 1 + 2 = 3,
      13 => 1 + 3 = 4,
      112 => 1 + 1 + 2 = 4,
      166 => 1 + 6 + 6 = 13 => 4,
      23 => 5
      212 => 5
      266 => 14 => 5
      312 => 6
      366 => 15 => 6
      1266 => 15 => 6

    the highest cross sum is 6, and we return the first combination (the leftmost) 312.

    Simplification:
    if the function does not calculate second or third round for cross sum, then max points are 60%
    e.g. 991 would give 19
    (in those tests there are no combinations which give cross sum higher than 9)
    """
    if len(numbers) < 2:
        return 0

    max_cross_sum = 0
    result = 0

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                combined_num = int(str(numbers[i]) + str(numbers[j]))
                current_cross_sum = cross_sum(combined_num)

                if current_cross_sum > max_cross_sum:
                    max_cross_sum = current_cross_sum
                    result = combined_num

    return result


class Candy:
    """Candy."""

    def __init__(self, name: str, filling: str):
        """
        Candy class constructor.

        :param name: candy name
        :param filling: candy filling
        """
        self.name = name
        self.filling = filling


class CandyShop:
    """Candy shop."""

    def __init__(self):
        """Initialize candy Shop."""
        self.candies = []

    def add_candies(self, candies: list):
        """
        Add list of fresh candies to already existing ones.

        :param candies: list of candies to add
        :return:
        """
        self.candies += candies

    def get_candies(self) -> list:
        """
        Return list of all candies existing in the shop.

        :return: list of all candies
        """
        return self.candies

    def get_candies_by_filling(self, filling: str) -> list:
        """
        Get list of candies that have the same filling as given in parameter value.

        :return: list
        """
        return [i for i in self.candies if i.filling == filling]


    def sort_candies_by_filling(self) -> list:
        """
        Return list of candies sorted by filling in alphabetical order.

        If filling is the same, then sort
        by name in alphabetical order.

        :return: sorted list of candies
        """
        return sorted(self.candies, key=lambda x: (x.filling, x.name))
    def get_most_popular_candy_name_and_filling(self) -> dict[str, str]:
        """
        Find the most popular candy name and filling.

        Method should return dict with name and filling of the most popular candy in the shop (type of candy which name
        and filling is present the most in the shop). NB! You should consider the most popular combination of name and filling.
        {name: most_pop_candy_name, filling: most_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of most pop candy
        """
        result = {}
        for candy in self.candies:
            key = (candy.filling, candy.name)
            if key in result:
                result[key].append(candy)
            else:
                result[key] = [candy]
        max_candy = max(result.items(), key=lambda x: len(x[1]))
        return {'name': max_candy[0][1], 'filling': max_candy[0][0]}

    ### alternatiivne:
    #fillings = list(map(lambda x: x.name + ',' + x.filling, self.candy_list))
    #fillings2 = list(map(lambda x: x.name + ',' + x.filling, self.candy_list))
    #fillings2 = sorted(fillings2, key=lambda x: -fillings.count(x))
    #x = fillings2[0].split(',')
    #return {'name': x[0], 'filling': x[1]}

    def get_least_popular_candy_name_and_filling(self) -> dict[str, str]:
        """
        Find the least popular candy name and filling.

        Method should return dict with name and filling of the least popular candy in the shop (type of candy which name
        and filling is present the least in the shop). NB! You should consider the least popular combination of name and filling.
        {name: least_pop_candy_name, filling: least_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of least pop candy
        """
        result = {}
        for candy in self.candies:
            key = (candy.filling, candy.name)
            if key in result:
                result[key].append(candy)
            else:
                result[key] = [candy]
        max_candy = min(result.items(), key=lambda x: len(x[1]))
        return {'name': max_candy[0][1], 'filling': max_candy[0][0]}
    ### alternative:
    #fillings = list(map(lambda x: x.name + ',' + x.filling, self.candy_list))
    #fillings2 = list(map(lambda x: x.name + ',' + x.filling, self.candy_list))
    #fillings2 = sorted(fillings2, key=lambda x: -fillings.count(x))
    #x = fillings2[-1].split(',')
    #return {'name': x[0], 'filling': x[1]}

    def collect_candies_by_filling(self) -> dict[str, list[Candy]]:
        """
        Group candies by filling.

        Method should return dict with candies divided by filling, where dict key is filling and dict value is list
        of candies with this filling.
        {candy_filling: [candy1, candy2]}

        :return: dict of candies divided by filling
        """
        result = {}
        for candy in self.candies:
            key = candy.filling
            if key in result:
                result[key].append(candy)
            else:
                result[key] = [candy]
        return result


# Complex OOP


class Plant:
    """The plants that the plant store sells and the plant collector can purchase."""

    def __init__(self, species: str, rarity: int, size: int):
        """
        Initialize the plant.

        The price for the plant is taken from the table based on the size and rarity.
        """
        self.species = species
        self.rarity = rarity
        self.size = size
        self.price = self.calculate_price(rarity, size)
    def __repr__(self):
        """Return string representation of the plant, which is the species of the plant."""
        return self.species

    def update_rarity(self, rarity: int):
        """Update the rarity of the plant."""
        self.rarity = rarity
        self.price = self.calculate_price(rarity, self.size)

    @staticmethod
    def calculate_price(rarity: int, size: int) -> int:
        # Assuming a simple formula for price calculation
        return rarity * size * 10


class PlantStore:
    """Plant store where the different plants are sold and the plant collectors can purchase from."""

    def __init__(self, name: str, pricing_coefficient: float):
        """Initialize plant store."""
        self.name = name
        self.pricing_coefficient = pricing_coefficient
        self.stock = {}
        self.members_only_stock = {}
        self.members = set()

    def update_stock(self, plant: Plant, amount: int):
        """
        Add plants and their amounts to the stock.

        If the plant is already in stock, adds new amount to current amount.
        """
        self.stock[plant] = self.stock.get(plant, 0) + amount

    def update_members_only_stock(self, plant: Plant, amount: int):
        """
        Add plants and their amounts to the members only stock.

        If the plant is already in stock, adds new amount to current amount.
        """
        self.members_only_stock[plant] = self.members_only_stock.get(plant, 0) + amount

    def sell_plant(self, plant: Plant, customer: 'PlantCollector'):
        """
        Sell the plant to the customer, removing one plant of that type from stock.

        It is important to note that plants that are in the members only stock are to be removed
        from that particular stock and are only sold to customers with a
        membership.
        """
        if customer in self.members and plant in self.members_only_stock:
            self.members_only_stock[plant] -= 1
            if self.members_only_stock[plant] <= 0:
                del self.members_only_stock[plant]
        elif plant in self.stock:
            self.stock[plant] -= 1
            if self.stock[plant] <= 0:
                del self.stock[plant]
        customer.add_to_collection(plant)

    def get_members_only_stock(self) -> dict[Plant, int]:
        """Return the members only stock."""
        return self.members_only_stock

    def get_stock(self) -> dict[Plant, int]:
        """Return the stock available to all customers."""
        return self.stock

    def assign_membership(self, customer: 'PlantCollector'):
        """Add a customer to the members list."""
        self.members.add(customer)

    def get_stock_value(self) -> int:
        """
        Calculate the sale value of the whole stock (both regular and members only stock).

        Multiply the prices and amounts of each plant and then also multiply everything
        by the store's pricing coefficient. Note that the members only stock plants
        do not need to be multiplied by the pricing coefficient, their price is already their sale price.
        """
        total_value = sum(plant.price * amount for plant, amount in self.stock.items())
        members_only_value = sum(plant.price * amount for plant, amount in self.members_only_stock.items())
        return int(total_value * self.pricing_coefficient + members_only_value)

    def is_in_stock(self, plant_name: str, customer: 'PlantCollector') -> bool:
        """
        Respond to a customer's query about whether a plant by that name (species) is in stock.

        It is important to note that if a plant is in members only stock and the customer is not a member,
        the plant is not 'in stock' for them, even if the store actually has the plant they are asking for.
        Returns the boolean True if the plant is in stock, and False if not.
        """
        for plant in self.stock.keys():
            if plant.species == plant_name:
                return True
        if customer in self.members:
            for plant in self.members_only_stock.keys():
                if plant.species == plant_name:
                    return True
        return False

    def get_plant_details(self, plant_name: str) -> Plant:
        """
        Return the full plant object by name (species).

        If no such plant exists in the store's stock, returns None.
        """
        for plant in self.stock.keys():
            if plant.species == plant_name:
                return plant
        for plant in self.members_only_stock.keys():
            if plant.species == plant_name:
                return plant
        return None


class PlantCollector:
    """Plant collector who buys and collects plants."""

    def __init__(self, name: str):
        """Initialize the plant collector."""
        self.name = name
        self.collection = {}
        self.wishlist = set()
        self.space = {}

    def add_to_collection(self, plant: Plant):
        """Add a plant to the collector's collection if not already there."""
        if plant not in self.collection:
            self.collection[plant] = 1
        else:
            self.collection[plant] += 1

    def add_to_wishlist(self, plant_name: str):
        """Add a plant's name to the collector's wishlist if not already there."""
        self.wishlist.add(plant_name)

    def remove_from_wishlist(self, plant_name: str):
        """Remove a plant name from the collector's wishlist."""
        self.wishlist.discard(plant_name)

    def add_space(self, space_type: int, space_amount: int):
        """
        Add space to the collector's home.

        If there are no spaces of that size, create a new entry in the dict, otherwise
        add to the amount that already exists.
        """
        self.space[space_type] = self.space.get(space_type, 0) + space_amount

    def calculate_collection_value(self) -> int:
        """
        Calculate the collector's plant collection value.

        Add the prices of all the plants together.
        """
        return sum(plant.price for plant in self.collection)

    def most_expensive_wishlist_plant(self, store: PlantStore) -> Optional[str]:
        """
        Find the most expensive wishlist plant.

        As different stores have different prices (pricing coefficient can be
        different), a PlantStore object is also given as an argument to the function.
        Return the name of the most expensive
        plant or if none of the plants in the wishlist are in stock at the store, return None.
        """
        expensive_plant = None
        max_price = 0
        for plant_name in self.wishlist:
            plant = store.get_plant_details(plant_name)
            if plant and plant.price > max_price:
                max_price = plant.price
                expensive_plant = plant_name
        return expensive_plant

    def buy_wishlist_plant(self, store: PlantStore) -> str:
        """
        Buy the plant that's both the most expensive and biggest one on their wishlist that they have space for.

        It's important to note that a store always carries only one size of any given plant,
        so if a plant is sold at the store, it is only available in that one size.
        If a plant is bought, it should be added to the collection, removed from wishlist and the store and also place it
        somewhere in the home of the collector, meaning a corresponding free space slot should be removed.
        If purchasing a plant was successful, this function returns the species of the plant, if not, returns the string
        "No wishlist plants are for sale in this store of fit in your home!"
        """
        # Implementation details depend on the specifications of the plant size, space, and store's stock management
        # Here is a simplified version
        for plant_name in sorted(self.wishlist,
                                 key=lambda x: store.get_plant_details(x).price if store.get_plant_details(x) else 0,
                                 reverse=True):
            plant = store.get_plant_details(plant_name)
            if plant and store.is_in_stock(plant_name, self) and self.space.get(plant.size, 0) > 0:
                store.sell_plant(plant, self)
                self.add_to_collection(plant)
                self.remove_from_wishlist(plant_name)
                self.space[plant.size] -= 1
                return plant_name
        return "No wishlist plants are for sale in this store of fit in your home!"

    def buy_wishlist_member(self, store: PlantStore, biggest: bool, name: str, object_plant: Plant) -> str:
        """
        Buy a wishlist plant if a member of the store. The choice of plant depends on the 'biggest' flag and other criteria.
        """
        if self not in store.members:
            return "Not a member or desired plant not available in members only stock."

        # Filter wishlist plants available in the member's stock
        available_wishlist_plants = [store.get_plant_details(plant_name) for plant_name in self.wishlist if store.get_plant_details(plant_name) in store.members_only_stock]

        if not available_wishlist_plants:
            return "No wishlist plants are available in the members only stock."

        # Choose the plant based on criteria
        if biggest:
            desired_plant = max(available_wishlist_plants, key=lambda p: p.size)
        elif name:
            desired_plant = next((p for p in available_wishlist_plants if p.species == name), None)
        elif object_plant:
            desired_plant = object_plant if object_plant in available_wishlist_plants else None
        else:
            return "Invalid selection criteria."

        if desired_plant and self.space.get(desired_plant.size, 0) > 0:
            store.sell_plant(desired_plant, self)
            self.add_to_collection(desired_plant)
            self.remove_from_wishlist(desired_plant.species)
            self.space[desired_plant.size] -= 1
            return desired_plant.species

        return "Cannot buy this plant or not enough space."

    def buy_plant(self, plant_name: str, store: PlantStore) -> str:
        """
        Buy the plant if it is possible.

        Buys the plant with the given name from the store if it is in stock. Add the plant to collection, remove from wishlist,
        remove from the stock of the store and amend the amount of space available in the home.
        If the purchase is successful, returns the species of the plant, if not, returns the string "Cannot buy this plant!"
        """
        plant = store.get_plant_details(plant_name)
        if plant and store.is_in_stock(plant_name, self) and self.space.get(plant.size, 0) > 0:
            store.sell_plant(plant, self)
            self.add_to_collection(plant)
            self.remove_from_wishlist(plant_name)
            self.space[plant.size] -= 1
            return plant.species
        return "Cannot buy this plant!"

    def buy_plant_member(self, plant_name: str, store: PlantStore) -> str:
        """Check if plant in members only stock."""
        if self not in store.members:
            return "Not a member or plant not available in members only stock."

        plant = store.get_plant_details(plant_name)
        if plant in store.members_only_stock and self.space.get(plant.size, 0) > 0:
            store.sell_plant(plant, self)
            self.add_to_collection(plant)
            self.remove_from_wishlist(plant_name)
            self.space[plant.size] -= 1
            return plant.species
        return "Cannot buy this plant!"


if __name__ == '__main__':
    assert find_first_pair("abbcc") == "bb"
    assert find_first_pair("helloo") == "ll"
    assert find_first_pair("1233") == "33"
    assert find_first_pair("12333") == "33"

    assert remove_non_palindrome_numbers([1, 2, 3]) == [1, 2, 3]
    assert remove_non_palindrome_numbers([-1, -6, -12]) == [-1, -6]
    assert remove_non_palindrome_numbers([]) == []
    assert remove_non_palindrome_numbers([12, 345]) == []

    assert add_symbols("aab", "a") == "aaaab"
    assert add_symbols("aab1", "a12") == "aaaab111"

    assert h_index([4, 2, 4]) == 2
    assert h_index([5, 4, 7, 3, 6]) == 4

    assert sum_of_digits_recursion("123") == 6
    assert sum_of_digits_recursion("") == 0

    assert combine_numbers([1, 2, 3]) == 23
    assert combine_numbers([1]) == 0
    assert combine_numbers([1, 2, 3, 12, 66]) == 312

    # Candy shop
    candy_shop = CandyShop()
    candy1 = Candy('candy1', 'chocolate')
    candy2 = Candy('candy2', 'caramel')
    candy3 = Candy('candy3', 'nut')
    candy4 = Candy('candy1', 'chocolate')
    candy5 = Candy('candy2', 'vanilla')
    candy6 = Candy('candy2', 'vanilla')
    candy7 = Candy('candy3', 'nut')
    candy8 = Candy('candy1', 'chocolate')

    candies = [candy1, candy2, candy3, candy4, candy5, candy6, candy7, candy8]

    candy_shop.add_candies(candies)

    assert candy_shop.get_candies_by_filling('chocolate') == [candy1, candy4, candy8]
    assert candy_shop.get_least_popular_candy_name_and_filling() == {"name": "candy2", "filling": "caramel"}
    assert candy_shop.get_most_popular_candy_name_and_filling() == {"name": "candy1", "filling": "chocolate"}
    assert candy_shop.collect_candies_by_filling() == {"chocolate": [candy1, candy4, candy8],
                                                       "caramel": [candy2],
                                                       "nut": [candy3, candy7],
                                                       "vanilla": [candy5, candy6]}

    # Plantstore
    jungle_garden = PlantStore("Jungle Garden", 1.2)
    assert jungle_garden.name == "Jungle Garden"
    assert jungle_garden.pricing_coefficient == 1.2
    assert jungle_garden.stock == {}
    assert jungle_garden.members_only_stock == {}

    lancifolia = Plant("Calathea Lancifolia", 0, 2)
    monstera_deliciosa = Plant("Monstera Deliciosa", 0, 0)
    micans = Plant("Philodendron Micans", 1, 1)
    jungle_garden.update_stock(lancifolia, 9)
    jungle_garden.update_stock(monstera_deliciosa, 3)
    jungle_garden.update_stock(micans, 8)

    expected_stock = {
        micans: 8,
        lancifolia: 9,
        monstera_deliciosa: 3
    }
    assert jungle_garden.get_stock() == expected_stock
