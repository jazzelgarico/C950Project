# Internal Modules
import package
import fileimport
import distancegraph


class Truck:
    """" Models a delivery truck.

    A Truck can carry a maximum of 16 packages, travels 18 miles per
    hour, leaves the hub no earlier than 8:00AM. Loading and delivering
    are instantaneous.
    """

    def __init__(self):
        self.mileage = 0
        self.package_list = []
        self.location = None

    def deliver(self, item):
        """Delivers a package.

        Updates the truck's location, mileage, and the package's
        delivery status to "Delivered at [time delivered]"

        Args:
            item: the package to be delivered

        """
        item.update_delivery_status("Delivered")
        miles_driven = 0  # UPDATE
        self.package_list.remove(item)
        self.mileage += miles_driven

    def load(self, item_loader):
        """Loads the truck.

        Updates package_list according to the item_loader

        Args:
            item_loader: a list of packages to load into the truck
        """
        for item in item_loader():
            self.package_list.append(item)
            item.update_delivery_status("En route")


class Loader:
    """Determines which packages to load into a Truck.

    """
    def __init__(self, package_table):
        self.load_list = []
