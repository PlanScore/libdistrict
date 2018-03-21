from district import District


def districts_in_range(district_plan, min_target, max_target):
    """
    :param district_plan: an iterable of Districts
    :param min_target: the minimum value for the population
    :param max_target: the maximum value for the population
    :return: the number of districts with populations in range
             (min_target <= population <= max_target)
    """
    num_districts_in_range = 0

    for district in district_plan:
        if isinstance(district, District) and district is not None:
            population = district.population
            if isinstance(population, int):
                if min_target <= population <= max_target:
                    num_districts_in_range += 1

        else:
            raise TypeError

    return num_districts_in_range


def districts_in_percent_deviation(district_plan, percent_deviation):
    """
    :param district_plan: an iterable of Districts
    :param percent_deviation: the acceptable deviation percentage
    :return: the number of districts with populations
             that are with the percent_deviation range
    """
    num_districts_in_percent_deviation = 0
    num_districts = 0
    population = 0

    for district in district_plan:
        if isinstance(district, District) and district is not None:
            num_districts += 1
            pop = district.population
            if isinstance(pop, int):
                population += district.population
        else:
            raise TypeError

    ideal = population / num_districts
    max_dev = percent_deviation / 100 * ideal

    for district in district_plan:
        if (ideal - max_dev) <= district.population <= (ideal + max_dev):
            num_districts_in_percent_deviation += 1
    
    return num_districts_in_percent_deviation
