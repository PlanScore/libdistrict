from libdistrict.district import District
"""@package docstring
This module has two functions: districts_in_range 
and districts_in_percent_deviation. 

Determines number of districts in a plan that fall within a target range of population.
"""

def districts_in_range(district_plan, min_target, max_target):
    """
    :param district_plan: an iterable of Districts
    :param min_target: the minimum value for the population
    :param max_target: the maximum value for the population
    :return: the number of districts with populations in range
             (min_target <= population <= max_target)
    """
    num_districts_in_range = 0

    is_district_plan(district_plan)

    for district in district_plan:
        population = district.population
        is_int_pop(district)
        if min_target <= population <= max_target:
            num_districts_in_range += 1

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

    is_district_plan(district_plan)
    	
    for district in district_plan:
        num_districts += 1
        is_int_pop(district)
        total_pop += district.population

    average_pop = total_pop / num_districts
    max_dev = percent_deviation / 100 * average_pop

    for district in district_plan:
        if (average_pop - max_dev) <= district.population <= (average_pop + max_dev):
            num_districts_in_percent_deviation += 1
    
    return num_districts_in_percent_deviation

# Helper Methods for Equal Population Functions
def is_district(district):
    if not isinstance(district, District):
        raise TypeError

def is_district_plan(district_plan):
    if district_plan is None:
        raise TypeError
    for district in district_plan:
        is_district(district)

def is_int_pop(district):
    if not isinstance(district.population, int):
        raise TypeError