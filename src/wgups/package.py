class Package:
    """Models a package.

    Attributes
        package_id(int): id assigned to package
        address(str): street address of delivery destination
        city(str): city of delivery destination
        state(str): two-letter state acronym of delivery destination
        zip_code(str): zip code of delivery destination
        delivery_deadline: deadline time for delivery
        package_weight(float): weight of package in kilos
        delivery_status(str): status of package ('At the hub',
                         'En route', 'Delivered at [time]')
        special_notes(str): additional notes for package

        """
    def __init__(self, package_id, address, city, state, zip_code,
                 delivery_deadline, package_weight, delivery_status,
                 special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.special_notes = special_notes

    def __str__(self):
        return (f"Package ID:        {self.package_id}\n"
                f"Address:           {self.address}, {self.city}, "
                f"{self.state}, {self.zip_code}\n"
                f"Delivery Deadline: {self.delivery_deadline}\n"
                f"Package Weight:    {self.package_weight}\n"
                f"Delivery Status:   {self.delivery_status}\n"
                f"Special Notes:     {self.special_notes}\n")


class PackageHashTable:
    """Stores packages into a hash table.

    Attributes:
        capacity: number of buckets in the hash table
        table: stores the buckets of the hash table
    """
    def __init__(self, capacity):
        self.table = []
        self.capacity = capacity
        for i in range(capacity):
            self.table.append([])

    def __str__(self):
        table_info = []
        for i in range(len(self.table)):
            if len(self.table[i]) != 0:
                for j in range(len(self.table[i])):
                    table_info.append(str(self.table[i][j]))
        return '\n'.join(table_info)

    def insert(self, package):
        """Inserts a package into the hash table.

        Args:
            package: package to insert into hash table]

        """
        bucket = self._get_bucket(package.package_id)
        self.table[bucket].append(package)

    def _get_bucket(self, package_id):
        """Determines which bucket a package with the package_id
        belongs.

        Args:
             package_id: the package_id of the package

        Returns:
            the bucket to which the package with the package_id belongs

        """
        return package_id % len(self.table)

    def update(self, package):
        """Updates an existing package in the table.

        Args:
            package: the new package used to update

        """
        bucket = self._get_bucket(package.package_id)
        for i in reversed(range(len(self.table[bucket]))):
            if self.table[bucket][i].package_id == package.package_id:
                self.table[bucket][i] = package

    def search(self, package_id):
        """Searches for a package with the package_id in the table.

        Args:
            package_id: the package_id of the package to search for

        Returns:
            package with the package_id if it is in the table,
            otherwise None
        """
        bucket = self._get_bucket(package_id)
        for pckg in reversed(self.table[bucket]):
            if pckg.package_id == package_id:
                return pckg
        return None


def test_package():
    p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115,
                 "10:30AM", 21, "At the Hub", None)
    p11 = Package(101, "2600 Taylorsville Blvd", "Salt Lake City", "UT", 84118,
                  "EOD", 1, "At the Hub", None)
    p1new = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115,
                    "10:30AM", 21, "Delivered", None)
    print(p1)
    print(p11)
    packages = PackageHashTable(100)
    packages.insert(p1)
    packages.insert(p11)
    print(packages)

    packages.update(p1new)
    print(packages)

    print("Searching for package 1:")
    if packages.search(1) is not None:
        print(packages.search(1))
    else:
        print("None found.")

    print("Searching for package 101:")
    if packages.search(101) is not None:
        print(packages.search(101))
    else:
        print("None found.")

    print("Searching for package 5:")
    if packages.search(5) is not None:
        print(packages.search(5))
    else:
        print("None found.")
