import statistics
from libdistrict.district import District


def efficiency_gap(district_plan, party_a, party_b):
    """
    :param district_plan: an iterable of Districts
    :param party_a: key value / name of party a (Democratic by convention - positive scores denote pro-Democratic asymmetries)
    :param party_b: key value / name of party b (Republican by convention - negative scores denote pro-Republican asymmetries)
    :return: the efficiency gap (positive for party a, negative for party b)
    """

    is_district_plan(district_plan)

    party_a_wasted = 0
    party_b_wasted = 0
    total_votes = 0

    for district in district_plan:
        party_a_votes = district.party_votes[party_a]
        party_b_votes = district.party_votes[party_b]
        total_votes += (party_a_votes + party_b_votes)
        win_threshold = (party_a_votes + party_b_votes) / 2

        if party_a_votes > party_b_votes:
            party_a_wasted += (party_a_votes - win_threshold)
            party_b_wasted += party_b_votes
        elif party_a_votes < party_b_votes:
            party_a_wasted += party_a_votes
            party_b_wasted += (party_b_votes - win_threshold)
        else:
            pass

    return (party_b_wasted - party_a_wasted) / total_votes



def mean_median_diff(district_plan, party):
    """
    :param district_plan: an iterable of Districts
    :param party: the key specifying which party to analyze
    :return: median - mean number of votes across all districts
    a negative score means the analyzed party has an advantage
    a positive score means the analyzed party has a disadvantage
    """

    is_district_plan(district_plan)

    votes_per_district = []

    # store all votes for party in a sequence
    for district in district_plan:
        party_votes = district.party_votes[party]
        votes_per_district.append(party_votes)

    # get the median votes for a district
    party_votes_median = statistics.median(votes_per_district)

    # get the mean for the district
    party_votes_mean = statistics.mean(votes_per_district)

    return party_votes_median - party_votes_mean

def is_district(district):
    if not isinstance(district, District):
        raise TypeError

def is_district_plan(district_plan):
    if district_plan is None:
        raise TypeError
    for district in district_plan:
        is_district(district)