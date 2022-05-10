# Internal Modules
import package
import fileimport

AVG_PACKAGES_PER_DAY = 40
PACKAGES_FILENAME = 'WGUPS Package File.csv'

packages = package.PackageHashTable(AVG_PACKAGES_PER_DAY * 2)
fileimport.receive_packages(PACKAGES_FILENAME, packages)

print(packages)
