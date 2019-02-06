
import housing_scrape
from housing_classes import City

import functions_module


location = input("Please enter the zipcode or city and state you wish to search: (example: Colorado Springs, CO) \n")
rent = housing_scrape.scrape_rent(location)

print(rent)
