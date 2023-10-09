"""Airport schedule."""


def destinations_and_times(flights: list) -> dict:
    """
    Create a dictionary containing destinations with the departure times for this destination today.

    Flights list is in the format: "Tallinn,08:00,01h30m,OWL1234"
    Where different parts are separated by comma:
    - destination
    - departure time
    - flight duration
    - flight number

    Result format: {destination1: [time1, time2, ...], destination2: [time1, time2, ...]}.

    The order of departure times and destinations are not important.

    :param flights: given list from database.
    :return: dictionary where keys are destinations and values are lists of departure times.
    """
    result = {}  # Create an empty dict to store results.

    for flight in flights:
        flight_info = flight.split(',')  # Split the info using comma.

        # Extract destination and departure time from flight info.
        destination = flight_info[0]
        departure_time = flight_info[1]

        # Check if the destination is already in the result dict.
        if destination in result:
            # If it's already in dict, then append the departure time.
            result[destination].append(departure_time)
        else:
            # If it's not in dict, create a new entry.
            result[destination] = [departure_time]

    return result


def sort_dict_values(dictionary: dict) -> dict:
    """
    Sort dictionary values in ascending order.

    This function should be applied to the previous function's result to get the departure times ordered.

    Return a dictionary where all the values are in ascending order.
    The order of the keys is not important.
    """
    sorted_dict = {}

    for key in dictionary:

        sorted_values = sorted(dictionary[key])

        sorted_dict[key] = sorted_values

    return sorted_dict


def flights_to_destination(flights: list, destination: str) -> list:
    """
    Return flight times for the given destination.

    People want to know when flights for their chosen destination take off today.
    Using the functions written before, find and return the list of departure times
    (in ascending order) for that destination today.

    If there are no flights to the chosen destination, return empty list.

    :param flights: given list from database (the same as in destinations_and_times).
    :param destination: chosen destination for which we want to know the departure times.
    :return: list of departures (sorted in ascending order) for that destination.
    """
    # Create a dict of destinations and departure times using the destinations_and_times function.
    destination_dict = destinations_and_times(flights)

    # Check if the destination is in the dictionary.
    if destination in destination_dict:
        # Sort the departure times in ascending order.
        sorted_departure_times = sorted(destination_dict[destination])
        return sorted_departure_times
    else:
        return []


def flights_schedule(flights: list) -> dict:
    """
    Return flight schedule by departure times.

    Create a dictionary containing the flight schedule for the day, where the keys are the departure times,
    and the values are tuples which contain the destination and the flight number
    {time1: (destination, flight_number), time2: (destination, flight_number), ...}.

    The input list is in the same format as in destinations_and_times.
    The order of the keys (departure times) are not important.

    :param flights: given list from database (the same as in destinations_and_times).
    :return: dictionary where the keys are departure times and values are tuples containing the destination and
    flight number.
    """
    # Create an empty dict to store flight schedule.
    schedule = {}

    for flight in flights:
        flight_info = flight.split(',')  # Split the info using comma.

        # Extract departure time, destination, and flight number from the flight info.
        destination = flight_info[0]
        departure_time = flight_info[1]
        flight_number = flight_info[3]

        flight_tuple = (destination, flight_number)

        # Add the departure time as a key in the schedule dict with the tuple as it's value.
        schedule[departure_time] = flight_tuple

    return schedule


def destinations_list(schedule: dict) -> list:
    """
    Return a list of unique destinations for the day from the given flight schedule, sorted alphabetically.

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :return: Alphabetically sorted list of unique destinations.
    """
    # Create an empty set to store unique destinations
    unique_destinations = set()

    # Go through the values in the schedule dict and add destinations to the set
    for destination, flight_number in schedule.values():
        unique_destinations.add(destination)

    # Convert the set to a sorted list
    sorted_destinations = sorted(unique_destinations)

    return sorted_destinations


def airlines_operating_today(schedule: dict, airline_names: dict) -> set:
    """
    Return a set of unique airline names that have flights operating today.

    Schedule is the result of the flights_schedule function.
    Airline names are presented as a dictionary where the key is the airline code
    and the value is the corresponding airline name.

    Flight code contains 3 letters and 4 numbers. The 3-letter code indicates the airline code.
    So, the 3-letter code should be taken from the airline_names dictionary (key).

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing airline codes and corresponding names.
    :return: Set of unique airline names operating today.
    """
    operating_airlines = set()
    for departure_time, flight_info in schedule.items():
        # Extract the 3-letter airline code from the flight code (3-letter code is at index 1).
        airline_code = flight_info[1][:3]

        # Check if the airline code exists in the airline_names dict.
        if airline_code in airline_names:
            # Add the corresponding airline name to the set.
            operating_airlines.add(airline_names[airline_code])

    return operating_airlines


def destinations_by_airline(schedule: dict, airline_names: dict) -> dict:
    """
    Return a dictionary of destinations by airline names.

    Returns a dictionary where the keys are airline names and the values are sets of unique destinations
    that the airline is flying to today.

    Airline names is in the same format as in airlines_operating_today.
    The 3-letter code from the flight number can be used to find the airline name.

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing mapping of airline codes to airline names.
    :return: Dictionary of airline names to sets of destinations.
    """
    airline_destinations = {}

    for departure_time, flight_info in schedule.items():
        # Extract the 3-letter airline code from the flight code (3-letter code is at index 1).
        airline_code = flight_info[1][:3]

        # Check if the airline code exists in the airline_names dict.
        if airline_code in airline_names:
            # Get the airline name from the airline_names dict.
            airline_name = airline_names[airline_code]
            # Get the destination from the flight information.
            destination = flight_info[0]

            # Check if the airline name already exists in airline_destinations.
            if airline_name in airline_destinations:
                # If it exists, add the destination to the existing set.
                airline_destinations[airline_name].add(destination)
            else:
                # If it doesn't exist, create a new set with the destination and add it to airline_destinations.
                airline_destinations[airline_name] = {destination}

    return airline_destinations


if __name__ == '__main__':
    flights = [
        "Tallinn,08:00,01h30m,OWL1234",
        "Helsinki,10:35,01h00m,BHM5678",
        "Tallinn,09:00,01h30m,OWL1235",
    ]

    print(destinations_and_times(flights))
    # {'Tallinn': ['08:00', '09:00'], 'Helsinki': ['10:35']}

    flights_dict = {'Tallinn': ['10:00', '09:00'], 'Helsinki': ['10:35']}
    print(sort_dict_values(flights_dict))
    # {'Tallinn': ['09:00', '10:00'], 'Helsinki': ['10:35']}

    print(flights_to_destination(flights, "Tallinn"))
    # ['08:00', '09:00']
    print(flights_to_destination(flights, ""))
    # []

    print(flights_schedule(flights))
    # {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}

    schedule = {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}
    print(destinations_list(schedule))
    # ['Helsinki', 'Tallinn']

    airlines = {"OWL": "Owlbear Airlines", "BHM": "Beholder's Majesty Airlines"}

    print(airlines_operating_today(schedule, airlines))
    # {'Owlbear Airlines', "Beholder's Majesty Airlines"}

    print(destinations_by_airline(schedule, airlines))
    # {'Owlbear Airlines': {'Tallinn'}, "Beholder's Majesty Airlines": {'Helsinki'}}
