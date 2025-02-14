"""Exam0."""
from typing import Optional


def find_capital_letters(s: str) -> str:
    """
    Return only capital letters from the string.

    #1

    If there are no capital letters, return empty string.
    The string contains only latin letters (a-z and A-Z).
    The letters should be in the same order as they appear in the input string.

    find_capital_letters("ABC") => "ABC"
    find_capital_letters("abc") => ""
    find_capital_letters("aAbBc") => "AB"
    """
    result = ''
    for capital in s:
        if capital.isupper():
            result += capital
    return result


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or (abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2):
        return True
    return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #3

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    result = []
    r_str_split = results_string.split(',')
    for r in r_str_split:
        parts = r.split(' ')
        name = ' '.join(parts[:-1])
        score = parts[-1]
        if name and score.isdigit() and int(score) >= min_result:
            result.append(name)
    return result


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for i in range(3):
        # Rows.
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] != 0:
            return game[i][0]
        # Columns.
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != 0:
            return game[0][i]
    # Diagonals.
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0:
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != 0:
        return game[0][2]
    # Draw.
    return 0


def rainbows(field: str, lower=False) -> int:
    """
    Count rainbows.

    #5

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1  # Lisaks vikerkaarele on veel sümboleid
    assert rainbows("WoBniar") == 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    assert rainbows("rainbowobniar") == 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    field = field.lower()
    print(field)
    if len(field) < len('rainbow'):
        return 0
    if field.startswith('rainbow') or field.startswith('wobniar'):
        return 1 + rainbows(field[7:], lower)
    else:
        return rainbows(field[1:], lower)


def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #6

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    start = max_length = max_start = 0
    seen_chars = set()

    for end in range(len(text)):
        lower_char = text[end].lower()

        while lower_char in seen_chars:
            seen_chars.remove(text[start].lower())
            start += 1

        seen_chars.add(lower_char)
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_start = start

    return text[max_start:max_start + max_length]


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Initialize student."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    average_grade = 0
    if grades:
        average_grade = sum(grades) / len(grades)
    return Student(name, round(average_grade, 3), credit_points)


def get_top_student_with_credit_points(students: list, min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    top_student = None
    highest_average_grade = -1
    for student in students:
        if student.credit_points >= min_credit_points and student.average_grade > highest_average_grade:
            top_student = student
            highest_average_grade = student.average_grade
    return top_student


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    if student:
        sum_of_grades = student.average_grade * grades_count
        sum_of_grades += new_grade
        student.average_grade = round(sum_of_grades / (grades_count + 1), 3)
        student.credit_points += credit_points
        return student


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    return sorted(students, key=lambda student: (-student.credit_points, -student.average_grade, student.name))


class Room:
    """Room."""

    def __init__(self, number: int, price: int):
        """Initialize room."""
        self.number = number
        self.price = price
        self.features = []
        self.booked = False

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        if self.booked or feature in self.features:
            return False
        self.features.append(feature)
        return True

    def get_features(self) -> list:
        """Return all the features of the room."""
        return self.features

    def get_price(self) -> int:
        """Return the price."""
        return self.price

    def get_number(self) -> int:
        """Return the room number."""
        return self.number


class Hotel:
    """Hotel."""

    def __init__(self):
        """Initialize hotel."""
        self.rooms = []

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise, add the room to hotel and return True.
        """
        for rom in self.rooms:
            if rom.number == room.number:
                return False
        self.rooms.append(room)
        return True

    def book_room(self, required_features: list) -> Optional[Room]:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        best_match = None
        max_features_count = -1
        for room in self.rooms:
            if not room.booked:
                matched_features = len(set(required_features) & set(room.get_features()))
                if matched_features > max_features_count or (matched_features == max_features_count and room.number < best_match.number):
                    best_match = room
                    max_features_count = matched_features

        if best_match:
            best_match.booked = True
        return best_match

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        return [room for room in self.rooms if not room.booked]

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        return self.rooms

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        return [room for room in self.rooms if room.booked]

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        profits = {}
        for room in self.rooms:
            if room.booked:
                for feature in room.get_features():
                    profits[feature] = profits.get(feature, 0) + room.get_price()
        return profits

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        feature_profits = self.get_feature_profits()
        if not feature_profits:
            return None
        return min(feature_profits, key=lambda feature: (-feature_profits[feature], feature))


if __name__ == '__main__':
    print(find_capital_letters("ABC"))
    print(find_capital_letters("abc"))
    print(find_capital_letters("aAbBc"))

    print(close_far(1, 2, 10))  # = > True
    print(close_far(1, 2, 3))  # = > False
    print(close_far(4, 1, 3))  # = > True

    print(get_names_from_results("ago 123,peeter 11", 0))  # = > ["ago", "peeter"]
    print(get_names_from_results("ago 123,peeter 11,33", 10))  # = > ["ago", "peeter"]  # 33 does not have the name
    print(get_names_from_results("ago 123,peeter 11", 100))  # = > ["ago"]
    print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11))  # = > ["ago", "peeter",  "kitty11!!"]
    print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12))  # = > ["ago", "kusti riin"]

    game = [[1, 2, 1],
            [2, 1, 2],
            [2, 1, 1]]
    print(tic_tac_toe(game))  # = > 1

    print(rainbows("rainbowThisIsJustSomeNoise"))  # = > 1  # Lisaks vikerkaarele on veel sümboleid
    print(rainbows("WoBniar"))  # = > 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    print(rainbows("rainbowobniar"))  # = > 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    hotel = Hotel()
    room1 = Room(1, 100)
    room1.add_feature("tv")
    room1.add_feature("bed")
    room2 = Room(2, 200)
    room2.add_feature("tv")
    room2.add_feature("sauna")
    hotel.add_room(room1)
    hotel.add_room(room2)
    # TODO: try to add room with existing number, try to add existing feature to room
    assert hotel.get_rooms() == [room1, room2]
    assert hotel.get_booked_rooms() == []

    assert hotel.book_room(["tv", "president"]) == room1
    assert hotel.get_available_rooms() == [room2]
    assert hotel.get_booked_rooms() == [room1]

    assert hotel.book_room([]) == room2
    assert hotel.get_available_rooms() == []

    assert hotel.get_feature_profits() == {
        'tv': 300,
        'bed': 100,
        'sauna': 200
    }
    assert hotel.get_most_profitable_feature() == 'tv'

    # TODO: try to add a room so that two or more features have the same profit
