
"""
TODO update class with the feedback from Azavea
This class may change significantly or be removed altogether
Need to consider how to expand to include 3rd parties and communities of interest
"""


class District:

    def __init__(self, id=None, population=None, votes=None, blue_votes=None, red_votes=None, geometry=None):
        """
        :param id: the unique identifier for this district
        :param population: population of this district
        :param votes: all votes in this district for the election
        :param blue_votes: democratic votes in this district for the election
        :param red_votes: republic votes in this district for the election
        :param geometry: spatial geometry of this district
        """
        self.id = id
        self.population = population
        self.votes = votes
        self.blue_votes = blue_votes
        self.red_votes = red_votes
        self.geometry = geometry
