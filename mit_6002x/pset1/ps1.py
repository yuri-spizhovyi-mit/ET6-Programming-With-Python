###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, "r")

    for line in f:
        line_data = line.split(",")
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    print(cows)
    cow_list = []

    for name, weight in cows.items():
        cow_list.append((name, weight))

    cows_sorted = sorted(cow_list, key=lambda x: x[1], reverse=True)

    all_trips = []
    counter = 0
    tracker = []
    while counter < len(cows_sorted):
        taken_cows = []
        total_weight = 0
        for name, weight in cows_sorted:
            if name not in tracker:
                if total_weight + weight <= limit:
                    taken_cows.append(name)
                    tracker.append(name)
                    total_weight += weight
                    counter += 1
        all_trips.append(taken_cows)

    return all_trips


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    def check_limit(part):
        min_trip_qty = 0
        optimal_trip_list = []
        for i in range(len(part)):
            update_list = True
            trip_weight = 0
            for j in range(len(part[i])):
                trip_weight += cows[part[i][j]]
            if trip_weight > limit:
                update_list = False
                break
        if update_list:
            min_trip_qty = len(part)
            optimal_trip_list = part

        return min_trip_qty, optimal_trip_list

    list_of_cows = []

    for key in cows:
        list_of_cows.append(key)

    min_qti = 10
    min_list_of_trips = []
    for part in get_partitions(list_of_cows):
        qty, checked_list = check_limit(part)
        if qty != 0 and qty < min_qti:
            min_qti = qty
            min_list_of_trips = checked_list
    print(min_qti, min_list_of_trips)


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    ## code to be timed
    greedy_cow_transport(cows, limit)
    end = time.time()
    print(end - start)

    start = time.time()
    ## code to be timed
    brute_force_cow_transport(cows, limit)
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows(
    "C:/Users/yspizhoviy/ET6-Programming-With-Python/mit_6002x/pset1/ps1_cow_data.txt"
)
limit = 10
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
# brute_force_cow_transport(cows, limit)
compare_cow_transport_algorithms()
