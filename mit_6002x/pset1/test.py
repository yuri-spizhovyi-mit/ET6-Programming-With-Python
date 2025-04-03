cows = {
    "Maggie": 3,
    "Herman": 7,
    "Betsy": 9,
    "Oreo": 6,
    "Moo Moo": 3,
    "Milkshake": 2,
    "Millie": 5,
    "Lola": 2,
    "Florence": 2,
    "Henrietta": 9,
}


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
    def check_limit():
        min_trip_qty = 0
        optimal_trip_list = []
        list_of_cows = [
            [
                "Maggie",
                "Herman",
                "Betsy",
                "Oreo",
                "Moo Moo",
                "Milkshake",
                "Millie",
                "Lola",
                "Florence",
                "Henrietta",
            ]
        ]
        for i in range(len(list_of_cows)):
            update_list = True
            trip_weight = 0
            for j in range(len(list_of_cows[i])):
                trip_weight += cows[list_of_cows[i][j]]
            if trip_weight > limit:
                update_list = False
                break
        if update_list:
            min_trip_qty = len(list_of_cows)
            optimal_trip_list = list_of_cows
        print(min_trip_qty, optimal_trip_list)

    return check_limit()


brute_force_cow_transport(cows, 10)
