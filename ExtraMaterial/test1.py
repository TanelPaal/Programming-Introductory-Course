"""Exam1 (2023-01-04)."""
import string
from typing import Optional


def count_digits(text: str) -> int:
    """
    Return the count of digits in a string.

    count_digits("123") => 3
    count_digits("a") => 0
    count_digits("") => 0
    count_digits("0a9r44") => 4
    """
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    return count


def pairwise_min(numbers: list[int]) -> list[int]:
    """
    Return a list where for every element pair in the input list the minimum of those is used.

    If there are odd number of elements, ignore the last lonely element.

    pairwise_min([1, 2, 3, 4]) => [1, 3]
    pairwise_min([]) => []
    pairwise_min([1, 9, 2]) => [1]
    pairwise_min([9, 9, 2, 2]) => [9, 2]
    """
    result = []
    for i in range(0, len(numbers) - 1, 2):
        result.append(min(numbers[i], numbers[i + 1]))
    return result


def same_length(texts: list[str]) -> list[str]:
    """
    Normalize the lengths of the elements and return a list of those normalized elements in reverse order.

    You have to find the longest element in the list.
    Append "_" to every shorter element so that all the lengths are equal.
    Return a list of those equal-length elements in reverse alphabetical order.

    same_length(["a", "ab", "abc"]) => ["abc", "ab_", "a__"]
    same_length([]) => []
    same_length(["_", "ab_", "a"]) => ["ab_", "a__", "___"]
    """
    result = []
    for i in texts:
        result.append(i.ljust(len(max(texts, key=len)), "_"))
    return sorted(result, reverse=True)


def max_average(data: list, n: int) -> float:
    """
    Find maximum average with window width of n.

    max_average([1, 2, 3], 2) = (2 + 3) / 2
      possible variants with window 2: [1, 2], [2, 3]
    max_average([1, 7, 4, 5, 6], 3) = (7 + 4 + 5) / 3 = 5.333333
      possible variants with window 3: [1, 7, 4], [7, 4, 5], [4, 5, 6]

    :param data - data with at least n + 1 elements.
    :param n - Window width. Amgount of consecutive numbers to take into calculation. n > 0.

    :return Maximum average achgievable with current parameters.
    """
    result = []
    for i in range(len(data) - n + 1):
        result.append(sum(data[i:i + n]) / n)
    return max(result)


def factorial(n):
    """Calculate factorial. Recursive."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def count_leaf_items(item_list):
    """Recursively cog items in a (potentially
       nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count


def fuel_calculator(fuel: int) -> int:
    """
    Find needed amount of fuel for a given mass.

    Amount of fuel needed = mass divided by three, rounded down, subtract two
    + fuel needed for the fuel itself
    + fuel needed for the fuel's fuel + etc.

    Negative fuel rounds to zero.

    The solution has to be recursive! (no loops allowed)

    Examples:
    fuel_calculator(10) -> 1 + 0 = 1
    fuel_calculator(151) -> 48 + 14 + 2 + 0 = 64
    """
    if fuel <= 0:
        return 0
    else:
        return max(0, fuel // 3 - 2) + fuel_calculator(max(0, fuel // 3 - 2))


def longest_alphabet(text: str) -> str:
    """
    Find the longest substring which contains consecutive letters from alphabet.

    The input contains only lower case ascii letters (a - z).
    If there are several matches with the longest length, return the one which is lower alphabetically.

    longest_alphabet("abc") => "abc"
    longest_alphabet("abcklmn") => "klmn"
    longest_alphabet("klmabcopq") => "abc"
    longest_alphabet("a") => "a"
    longest_alphabet("xyab") => "ab"
    """
    alphabet = string.ascii_letters
    best = ""
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            word = text[start:end]
            if word in alphabet:
                if len(word) > len(best):
                    best = word
                elif len(word) == len(best):
                    if word < best:
                        best = word
    return best


class Donut:
    """Donut class."""

    def __init__(self, filling: str, icing: str):
        """
        Donut class constructor.

        :param filling: donut filling
        :param icing: donut icing
        """
        self.filling = filling
        self.icing = icing

    def get_filling(self):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        return self.filling

    def get_icing(self):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        return self.icing


class DonutFactory:
    """DonutFactory class."""

    def __init__(self):
        """DonutFactory class constructor."""
        self.donuts = []

    def add_donuts(self, donuts: list):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        for i in donuts:
            self.donuts.append(i)

    def get_donuts(self) -> list:
        """
        Return list of all donuts present on the line at the moment.

        :return: list of all donuts
        """
        return self.donuts

    def pack_donuts_by_filling_and_icing(self) -> dict:
        """
        Method should return dict with donuts divided by filling and icing.

        Dict key must be represented as tuple of filling and icing and value as list of donuts with
        given filling and icing.
        {(filling, icing): [donut1, donut2]}

        After packing, the production line for donuts should be empty (everything is packed).

        :return: dict
        """
        result = {}
        for donut in self.donuts:
            key = (donut.filling, donut.icing)
            if key in result:
                result[key].append(donut)
            else:
                result[key] = [donut]
        self.donuts = []
        return result

    def sort_donuts_by_icing_and_filling(self) -> list:
        """
        Method should return list of donuts sorted by icing in alphabetical order and then by filling in alphabetical order.

        :return: sorted list of donuts
        """
        return sorted(self.donuts, key=lambda donut: (donut.icing, donut.filling))

    def get_most_popular_donut(self) -> dict:
        """
        Method should return dict with icing and filling of the most popular donut.

        {'icing': most_pop_donut_icing, 'filling': most_pop_donut_filling}
        If there are several icing-filling combinations with the same amount of donuts,
        use the one which icing is alphabetically lower (a comes before b).

        Hint: you could use the result similar to pack_donuts_by_filling_and_icing method,
        but you cannot empty the production line of donuts.
        So, a common custom method can help here, which returns the dict.
        The most popular combination is the one element of the dict which has the most donuts
        (len on dict value is the highest).

        :return: dict with icing and filling of most pop donut
        """
        result = {}
        for donut in self.donuts:
            key = (donut.filling, donut.icing)
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
        return {"icing": max(result, key=result.get)[1], "filling": max(result, key=result.get)[0]}

    def get_donuts_by_flavour(self, flavour: str) -> list:
        """
        Get list of donuts that have the same icing or filling as given in method parameter.

        :return: list of donuts with the given flavour.
        """
        result = []
        for donut in self.donuts:
            if donut.filling == flavour or donut.icing == flavour:
                result.append(donut)
        return result


class TravelItem:
    """Travel item."""

    def __init__(self, location: str, duration: int):
        """Initialize travel item with location and duration."""
        self.location = location
        self.duration = duration

    def get_location(self) -> str:
        """Return location."""
        return self.location

    def get_duration(self) -> int:
        """Return duration."""
        return self.duration


class TravelPackage:
    """Travel package combines multiple travel items."""

    def __init__(self, name: str):
        """Initialize the package with the given name."""
        self.name = name
        self.packages = []

    def create_duplicate(self, new_name: str) -> 'TravelPackage':
        """
        Create a duplicate travel package.

        The new package will be created with the new name.
        Also, all the items should be copied to the new package.
        """
        duplicate = TravelPackage(new_name)
        duplicate.packages = [TravelItem(item.location, item.duration) for item in self.packages]
        return duplicate

    def get_total_duration(self) -> int:
        """Return the total duration of travel items in the package."""
        return sum(item.duration for item in self.packages)

    def get_items(self) -> list[TravelItem]:
        """Return list of TravelItem objects."""
        return self.packages

    def get_name(self) -> str:
        """Return the name of the package."""
        return self.name


class TravelAgency:
    """Travel agency coordinates travel items and packages."""

    def __init__(self):
        """Initialize the agency."""
        self.packages = {}  # Key: package name, Value: TravelPackage object

    def add_item_to_package(self, package_name: str, item: TravelItem) -> bool:
        """
        Add an item to the travel package.

        If this item already exists in the package with the given name,
        the method returns False (and the item is not added).

        Otherwise:
        If there is no package with the given name, then the package is created.
        The item is added to the package with the given name.
        The method returns True.
        """
        if package_name not in self.packages:
            self.packages[package_name] = TravelPackage(package_name)
        package = self.packages[package_name]
        if any(existing_item.location == item.location and existing_item.duration == item.duration for existing_item in
               package.get_items()):
            return False
        package.packages.append(item)
        return True

    def get_packages(self) -> list[TravelPackage]:
        """Return list of packages in the insertion order."""
        return list(self.packages.values())

    def get_packages_by_location(self, location: str) -> list[TravelPackage]:
        """Return a list of TravelPackage objects where at least one item has the given location."""
        return [package for package in self.packages.values() if
                any(item.location == location for item in package.get_items())]

    def search_package(self, locations: list, min_duration: int = None, max_duration: int = None) -> Optional[
        TravelPackage]:
        """
        Find a package which has all the locations specified in the list.

        If min_duration or max_duration is specified, then filter out packages,
        where total duration is between those values.

        If only min_duration is specified, use only those packages where total duration is greater or equal to that.
        If only max_duration is specified, use only those packages where total duration is less or equal to that.
        If both are specified, use packages where total duration is between those values.
        If none are specified, use all the packages.

        If locations list is empty, then every package matches.

        If multiple packages match, it doesn't matter which one to return.

        Return the found packages. If nothing matches, return None.
        """
        for package in self.packages.values():
            if locations and not all(any(item.location == loc for item in package.get_items()) for loc in locations):
                continue
            duration = package.get_total_duration()
            if min_duration and duration < min_duration:
                continue
            if max_duration and duration > max_duration:
                continue
            return package
        return None

    def get_package_overview_by_locations(self) -> str:
        """
        Create an overview where for every location all the packages are listed.

        The overview contains locations (strings) ordered alphabetically.
        And for every location a list of package names where this location is included, also ordered alphabetically.

        The format:

        location1:
         - package1
         - package2
        location2:
         - package1
         - package3

        The location has no spaces in front of it and is followed by the colon.
        The package has space, minus and space in front of it.
        There is no new line in the end of the string.

        If there are no packages, return empty string.
        """
        location_dict = {}
        for package in self.packages.values():
            for item in package.get_items():
                location_dict.setdefault(item.location, []).append(package.get_name())

        overview = ""
        for location in sorted(location_dict.keys()):
            overview += f"{location}:\n"
            for package_name in sorted(location_dict[location]):
                overview += f" - {package_name}\n"
        return overview.strip()


if __name__ == '__main__':
    print(max_average([1, 7, 4, 5, 6], 3))
    assert count_digits("123") == 3
    assert count_digits("a") == 0

    assert pairwise_min([1, 2, 4, 3]) == [1, 3]
    assert pairwise_min([1, 1, 4, 3, 5]) == [1, 3]

    assert same_length(["a", "b"]) == ["b", "a"]
    assert same_length(["aaa", "b"]) == ["b__", "aaa"]

    assert max_average([1, 2, 3, 3], 2) == 3.0  # (3 + 3) / 2
    assert max_average([1, 7, 2, 3, 3], 1) == 7.0
    assert max_average([1, 7, 2, 3, 3], 3) == 4.0  # (7 + 2 + 3) / 3
    assert max_average([8, 2, 9], 2) == 5.5  # (2 + 9) / 2

    assert fuel_calculator(151) == 64
    assert fuel_calculator(-1) == 0

    assert longest_alphabet("abc") == "abc"
    assert longest_alphabet("abcklmn") == "klmn"
    assert longest_alphabet("klmabcopq") == "abc"
    assert longest_alphabet("a") == "a"
    assert longest_alphabet("xyab") == "ab"

    # donut examples

    donut_factory = DonutFactory()
    donut1 = Donut('chocolate', 'sugar')
    donut2 = Donut('caramel', 'chocolate')
    donut3 = Donut('cherry', 'marshmallow')
    donut4 = Donut('chocolate', 'sugar')
    donut5 = Donut('vanilla', 'cream')
    donut6 = Donut('vanilla', 'cream')
    donut7 = Donut('cherry', 'marshmallow')
    donut8 = Donut('chocolate', 'sugar')

    donuts = [donut1, donut2, donut3, donut4, donut5, donut6, donut7, donut8]

    donut_factory.add_donuts(donuts)
    assert donut_factory.get_most_popular_donut() == {'icing': 'sugar', 'filling': 'chocolate'}
    assert donut_factory.get_donuts_by_flavour("marshmallow") == [donut3, donut7]
    assert donut_factory.sort_donuts_by_icing_and_filling() == [donut2, donut5, donut6, donut3, donut7, donut1,
                                                                donut4, donut8]
    assert donut_factory.pack_donuts_by_filling_and_icing() == {
        ('chocolate', 'sugar'): [donut1, donut4, donut8],
        ('caramel', 'chocolate'): [donut2],
        ('cherry', 'marshmallow'): [donut3, donut7],
        ('vanilla', 'cream'): [donut5, donut6]
    }

    # travel agency
    item_tallinn = TravelItem("Tallinn", 200)
    item_tartu = TravelItem("Tartu", 150)

    agency = TravelAgency()
    assert agency.get_packages() == []

    assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is True
    assert agency.add_item_to_package("Shorty in Tallinn", item_tallinn) is False

    assert agency.add_item_to_package("Estonian trip", item_tallinn) is True
    assert agency.add_item_to_package("Estonian trip", item_tartu) is True

    assert len(agency.get_packages()) == 2
    assert agency.get_packages()[0].get_name() == "Shorty in Tallinn"
    assert agency.get_packages()[1].get_name() == "Estonian trip"

    assert agency.get_packages()[1].get_total_duration() == 350

    packages = agency.get_packages_by_location("Tallinn")
    assert len(packages) == 2
    assert packages[0].get_name() == "Shorty in Tallinn"
    assert packages[1].get_name() == "Estonian trip"

    assert agency.get_packages_by_location("Narva") == []

    package = agency.search_package(["Tartu"])
    assert package.get_name() == "Estonian trip"
    package = agency.search_package(["Tallinn"])
    assert package.get_name() in ["Estonian trip", "Shorty in Tallinn"]
    package = agency.search_package(["Tallinn"], min_duration=300)
    assert package.get_name() == "Estonian trip"

    assert agency.get_package_overview_by_locations() == "Tallinn:\n - Estonian trip\n - Shorty in Tallinn\nTartu:\n - Estonian trip"
