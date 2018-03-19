from district import District

def districts_in_range(district_plan, min, max):
    """
    :param district_plan: an iterable of Districts
    :param min: the minimum acceptable value of the population
    :param max: the maximum value of the population
    :return: the number of districts in range
    """
    num_districts_in_range = 0

    for district in district_plan:
        if isinstance(district, District):
            population = district.population
            if isinstance(population, int):
                if population >= min and population <= max:
                    num_districts_in_range += 1

        else:
            raise TypeError

    return num_districts_in_range
