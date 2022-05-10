# Internal Modules
import package


class Truck:
    """" Models a delivery truck.

    A Truck can carry a maximum of 16 packages, travels 18 miles per
    hour, leaves the hub no earlier than 8:00AM. Loading and delivering
    are instantaneous.
    """
    def __init__(self):
        self.mileage = 0
        self.package_list = package.PackageHashTable(100)

    def deliver(self, item):
        self.package_list.remove(item)

    def load(self, item):
        self.package_list.append(item)
