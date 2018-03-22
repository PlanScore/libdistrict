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
    total_pop = 0

    for district in district_plan:
        if isinstance(district, District) and district is not None:
            num_districts += 1
            if isinstance(district.population, int):
                total_pop += district.population
        else:
            raise TypeError

    average_pop = total_pop / num_districts
    max_dev = percent_deviation / 100 * average_pop

    for district in district_plan:
        if (average_pop - max_dev) <= district.population <= (average_pop + max_dev):
            num_districts_in_percent_deviation += 1
    
    return num_districts_in_percent_deviation
