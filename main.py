
import housing_scrape
from housing_classes import City, Zipcode

import functions_module


location = input("Please enter the zipcode or city and state you wish to search: (example: Colorado Springs, CO) \n")
is_zipcode = functions_module.zipcode_validate(location)

if is_zipcode:
    average_price, location_type = housing_scrape.scrape_rent(location)

    zip1 = Zipcode(location)
    zip1.average_rent = average_price
    zip1.city = functions_module.zipcode_lookup(location)
    zip1.zipcode_update()
   
    print(zip1)

else:
    average_price, location_type = housing_scrape.scrape_rent(location)
    city_parse = location.split(',')
    state = functions_module.stateUnabbreviate(city_parse[1].strip())
    city_name = city_parse[0]

    city1 = City(city_name, state)
    if location_type == "-houses":
        city1.average_houses = average_price
    else:
        city1.average_apartments = average_price
    city1.city_update()

    print(city1)