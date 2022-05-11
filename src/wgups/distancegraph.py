class Location:
    """Models a location in the delivery area.

    Attributes:
        label: the full address of the location
    """

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return f"({self.label})"


class DistanceGraph:
    """Models distances between locations as a weighted, undirected
    graph.

    Attributes:
        distance_dict: A dictionary with locations as keys, and a dictionary of
        locations and distances as the value
    """

    def __init__(self):
        self.distance_dict = {}

    def __str__(self):
        rep = ""
        for key in self.distance_dict:
            internal_dict = \
                '\n    '.join([f"{str(loc)}: "
                               f"{str(self.distance_dict[key][loc])}"
                               for loc in self.distance_dict[key]])
            rep += f"{str(key)}\n    {internal_dict}\n"
        return rep

    def add_location(self, new_location):
        """Adds a new location to distance_dict.

        Arg:
            new_location: new location to add to distance_dict

        """
        self.distance_dict[new_location] = {}

    def add_route(self, location_a, location_b, distance):
        """Adds a route distance between two locations.

        Args:
            location_a: the first location
            location_b: the second location
            distance: the distance between location_a and location_b

        """
        self.distance_dict[location_a][location_b] = distance
        self.distance_dict[location_b][location_a] = distance

def test_distance_graph():
    saltlake = DistanceGraph()
    l1 = Location("Museum")
    l2 = Location("Church")
    l3 = Location("School")
    l4 = Location("Town Hall")
    saltlake.add_location(l1)
    saltlake.add_location(l2)
    saltlake.add_location(l3)
    saltlake.add_location(l4)
    print(saltlake)
    saltlake.add_route(l1, l2, 1.0)
    saltlake.add_route(l1, l3, 1.5)
    saltlake.add_route(l2, l3, 3.2)
    saltlake.add_route(l2, l4, 5.7)
    print(saltlake)