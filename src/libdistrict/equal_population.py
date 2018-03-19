from district import District

def districts_in_range(district_plan, min_target, max_target):
    """
    :param district_plan: an iterable of Districts
    :param min_target: the minimum acceptable value of the population
    :param max_target: the maximum value of the population
    :return: the number of districts in range
    """
    num_districts_in_range = 0

    for district in district_plan:
        if isinstance(district, District):
            population = district.population
            if isinstance(population, int):
                if population >= min_target and population <= max_target:
                    num_districts_in_range += 1

        else:
            raise TypeError

    return num_districts_in_range
