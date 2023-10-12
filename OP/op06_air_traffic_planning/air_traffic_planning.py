"""Air traffic planning."""


def update_delayed_flight(schedule: dict[str, tuple[str, str]], delayed_flight_number: str, new_departure_time: str) -> dict[str, tuple[str, str]]:
    """
    Update the departure time of a delayed flight in the flight schedule.

    Return a dictionary where the time of the specified flight is modified.
    This means that the result dictionary should not contain the old time,
    instead a new departure time points to the specified flight.
    The input schedule cannot be changed.

    :param schedule: Dictionary of flights ({time string: (destination, flight number)})
    :param delayed_flight_number: Flight number of the delayed flight
    :param new_departure_time: New departure time for the delayed flight
    :return: Updated flight schedule with the delayed flight's departure time changed
    """
    # Create a new dict to store the updated schedule.
    updated_schedule = {}

    for time, (destination, flight_number) in schedule.items():
        # Check if the flight number matches the delayed flight.
        if flight_number == delayed_flight_number:
            # Update the delayed flight.
            updated_schedule[new_departure_time] = (destination, flight_number)
        else:
            # Copy flights over to updated schedule as is (if it doesn't have a delay).
            updated_schedule[time] = (destination, flight_number)

    return updated_schedule


def cancel_flight(schedule: dict[str, tuple[str, str]], cancelled_flight_number: str) -> dict[str, tuple[str, str]]:
    """
    Create a new schedule where the specified flight is cancelled.

    The function cannot modify the existing schedule parameter.
    Instead, create a new dictionary where the cancelled flight is not added.

    :param schedule: Dictionary of flights ({time: (destination, flight number)})
    :param cancelled_flight_number: Flight number of the cancelled flight
    :return: New flight schedule with the cancelled flight removed
    """
    # Create a new dict to store updated schedule.
    updated_schedule = {}

    for time, (destination, flight_number) in schedule.items():
        # Check if the flight number matches the cancelled flight.
        if flight_number != cancelled_flight_number:
            # If it doesn't match, add it to the updated schedule.
            updated_schedule[time] = (destination, flight_number)

    return updated_schedule


def busiest_time(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour(s) at the airport based on the flight schedule.

    Finds the busiest hour(s) at the airport based on the flight schedule. The busiest hour(s)
    is/are determined by counting the number of flights departing in each hour of the day.
    All flights departing with the same hour in their departure time, are counted into the same hour.

    The function returns a list of strings of the busiest hours, sorted in ascending order, such as ["08", "21"].

    :param schedule: Dictionary containing the flight schedule, where keys are departure times
                     in the format "HH:mm" and values are tuples containing destination and flight number.
    :return: List of strings representing the busiest hour(s) in 24-hour format, such as ["08", "21"].
    """
    # Create a dict to count the number of flights for each hour.
    hour_counts = {}

    for departure_time in schedule.keys():
        hour, minutes = departure_time.split(':')
        if hour in hour_counts:
            hour_counts[hour] += 1
        else:
            hour_counts[hour] = 1

    # Find the max flight count.
    max_flight_count = max(hour_counts.values())

    # Create a list of hours with the maximum flight count.
    busiest_hours = [hour for hour, count in hour_counts.items() if count == max_flight_count]

    # Sort the busiest hours in ascending order.
    busiest_hours.sort()

    return busiest_hours


def connecting_flights(schedule: dict[str, tuple[str, str]], arrival: tuple[str, str]) -> list[tuple[str, str]]:
    """
    Find connecting flights based on the provided arrival information and flight schedule.

    The function takes a flight schedule and the arrival time and location of a flight,
    and returns a list of available connecting flights. A connecting flight is considered
    available if its departure time is at least 45 minutes after the arrival time, but less
    than 4 hours after the arrival time. Additionally, a connecting flight must not go back
    to the same place the arriving flight came from.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :param arrival: Tuple containing the arrival time and the location the flight is
                    arriving from. For example:
                    ("11:05", "Tallinn")

    :return: A list of tuples containing the departure time and destination of the
             available connecting flights, sorted by departure time. For example:
             [
                 ("14:00", "Paris"),
                 ("15:00", "Berlin")
             ]
             If no connecting flights are available, the function returns an empty list.
    """
    arrival_time, arrival_location = arrival
    connecting_flights = []

    for departure_time, (destination, flight_number) in schedule.items():
        if destination != arrival_location:  # Avoid returning to the same location.
            # Convert times to minutes for easier comparison.
            arrival_minutes = int(arrival_time.split(":")[0]) * 60 + int(arrival_time.split(":")[1])
            departure_minutes = int(departure_time.split(":")[0]) * 60 + int(departure_time.split(":")[1])

            # Check if the flight departs at least 45 minutes after the arrival time.
            if departure_minutes >= arrival_minutes + 45:
                # Check if the flight departs less than 4 hours after the arrival time.
                if departure_minutes < arrival_minutes + 4 * 60:
                    connecting_flights.append((departure_time, destination))

    # Sort the connecting flights by departure time.
    connecting_flights.sort()

    return connecting_flights


def time_components(time: str) -> (int, int):
    """
    Take the time given, separate hours and minutes, and return integers in tuple.

    :param time:
    :return:
    """
    components_list = [int(component) for component in time.split(':')]
    components_tuple = tuple(components_list)

    return components_tuple


def busiest_hour(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour-long slot(s) in the schedule.

    One hour slot duration is 60 minutes (or the diff of two times is less than 60).
    So, 15:00 and 16:00 are not in the same slot.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :return: A list of strings representing the starting time(s) of the busiest hour-long
             slot(s) in ascending order. For example:
             ["08:00", "15:20"]
             If the schedule is empty, returns an empty list.
    """
    if not schedule:
        return []

    busiest_hours = []  # Initialize a list to store hour-long slots with the most flights.

    for index, time in enumerate(schedule):
        hour, minute = time_components(time)  # Extract hour and minute from the current time.

        keys = list(schedule.keys())
        busiest_hour = []  # Initialize a list to store the current hour-long slot's times.
        for comparing_to in keys[index:]:
            comparing_hour, comparing_minute = time_components(comparing_to)

            # Calculate the hour difference, accounting for minute differences.
            hour_difference = comparing_hour - hour - int(comparing_minute < minute)

            if hour_difference == 0:
                busiest_hour.append(comparing_to)  # Add times in the same hour-long slot.
            else:
                break  # If the next time is in a different hour, stop processing.

        if len(busiest_hour) > 0:
            busiest_hours.append(busiest_hour)  # Store the hour-long slot if it has flights.

    lengths = [len(time_list) for time_list in busiest_hours]  # Get the number of flights in each hour-long slot.
    max_length = max(lengths)  # Find the maximum number of flights in any slot.

    times = []  # Initialize a list to store the starting times of the busiest slots.
    for hour in busiest_hours:
        length = len(hour)

        if length == max_length:
            times.append(hour[0])  # If the slot has the maximum number of flights, add its starting time.

    return sorted(list(times))  # Sort and return the list of starting times of the busiest slots.


def most_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the most passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the most popular destination.
    """
    destination_passenger_count = {}

    for departure_time, (destination, flight_number) in schedule.items():
        passengers = passenger_count.get(flight_number, 0)  # Get the number of passengers for the flight.
        # Update the total passenger count for the destination.
        destination_passenger_count[destination] = destination_passenger_count.get(destination, 0) + passengers

    # Find the destination with the highest total passenger count.
    most_popular = max(destination_passenger_count, key=destination_passenger_count.get)
    return most_popular


def least_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the fewest passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the least popular destination.
    """
    destination_passenger_count = {}

    for departure_time, (destination, flight_number) in schedule.items():
        passengers = passenger_count.get(flight_number, 0)  # Get the number of passengers for the flight.
        # Update the total passenger count for the destination.
        destination_passenger_count[destination] = destination_passenger_count.get(destination, 0) + passengers

    # Find the destination with the highest total passenger count.
    least_popular = min(destination_passenger_count, key=destination_passenger_count.get)
    return least_popular


if __name__ == '__main__':
    schedule = {
        "06:15": ("Tallinn", "OWL6754"),
        "11:35": ("Helsinki", "BHM2345")
    }
    print("\nUpdate Delayed Flight:")
    new_schedule = update_delayed_flight(schedule, "OWL6754", "09:00")
    print(schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_schedule)
    # {'09:00': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}

    print("\nCancel Flight:")
    new_schedule = cancel_flight(schedule, "OWL6754")
    print(schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_schedule)
    # {'11:35': ('Helsinki', 'BHM2345')}

    print("\nBusiest Time:")
    schedule = {
        "04:35": ("Maardu", "MWL6754"),
        "06:15": ("Tallinn", "OWL6754"),
        "06:30": ("Paris", "OWL6751"),
        "07:29": ("London", "OWL6756"),
        "08:00": ("New York", "OWL6759"),
        "11:30": ("Tokyo", "OWL6752"),
        "11:35": ("Helsinki", "BHM2345"),
        "19:35": ("Paris", "BHM2346"),
        "20:35": ("Helsinki", "BHM2347"),
        "22:35": ("Tallinn", "TLN1001"),
    }
    print(busiest_time(schedule))
    # ['06', '11']

    print("\nConnecting Flights:")
    print(connecting_flights(schedule, ("04:00", "Tallinn")))
    # [('06:30', 'Paris'), ('07:29', 'London')]

    print(busiest_hour(schedule))
    # ['06:15', '06:30', '07:29', '11:30']
    # 19:35 does not match because 20:35 is not in the same slot

    # flight number: number of passengers
    passengers = {
        "MWL6754": 100,
        "OWL6754": 85,
        "OWL6751": 103,
        "OWL6756": 87,
        "OWL6759": 118,
        "OWL6752": 90,
        "BHM2345": 111,
        "BHM2346": 102,
        "BHM2347": 94,
        "TLN1001": 1
    }
    print(most_popular_destination(schedule, passengers))
    # Paris

    print(least_popular_destination(schedule, passengers))
    # Tallinn
