
import housing_scrape
from housing_classes import City

import functions_module


location = input("Please enter the zipcode or city and state you wish to search: (example: Colorado Springs, CO) \n")
is_zipcode = functions_module.zipcode_validate(location)

if is_zipcode:
    average_price, location_type = housing_scrape.scrape_rent(location)
else:
    average_price, location_type = housing_scrape.scrape_rent(location)



print(f"The average price is {average_price} at the location type of {location_type}.")
