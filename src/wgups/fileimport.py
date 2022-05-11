# Standard Library
import csv

# Internal Modules
import package
import distancegraph


def receive_packages(filename, package_table):
    # Package File Column Numbers
    id_column = 0
    address_column = 1
    city_column = 2
    state_column = 3
    zip_column = 4
    deadline_column = 5
    mass_column = 6
    notes_column = 7

    with open(filename, encoding='UTF-8', newline='') as csvfile:
        package_reader = csv.reader(csvfile, delimiter=',')

        # Consume headers
        next(package_reader)
        next(package_reader)

        # Insert rows into_package_table
        for row in package_reader:
            pckg = package.Package(package_id=int(row[id_column]),
                                   address=row[address_column],
                                   city=row[city_column],
                                   state=row[state_column],
                                   zip_code=row[zip_column],
                                   delivery_deadline=row[deadline_column],
                                   package_weight=row[mass_column],
                                   delivery_status='At the hub',
                                   special_notes=row[notes_column])
            package_table.insert(pckg)


def create_graph(filename, distance_graph):
    with open(filename, newline='') as csvfile:
        distance_reader = csv.reader(csvfile, delimiter=',')
        # Consume headers
        next(distance_reader)
        # Insert rows into_package_table
        locations = []
        for row in distance_reader:
            clean_label = row[1].replace("\n", " ").strip()
            location = distancegraph.Location(clean_label)
            locations.append(location)
            distance_graph.add_location(location)
            column = 2
            while True:
                if row[column] == "0.0":
                    break
                location_two = locations[column - 2]
                distance_graph.add_route(location, location_two, row[column])
                column += 1


def test_receive_package():
    packages = package.PackageHashTable(100)
    receive_packages('WGUPS Package File.csv', packages)
    print(packages)


def test_create_graph():
    citygraph = distancegraph.DistanceGraph()
    create_graph('WGUPS Distance Table.csv', citygraph)
    print(citygraph)


test_create_graph()
