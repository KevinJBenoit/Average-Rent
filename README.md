# Average-Rent
Web scraper of rent.com city location

User enters either a zip code or city and state to search.
Zipcode inputs will gather prices from all the available housing types; houses, apartments, condos, townhouses because of a tighter search radius.
Zipcodes are passed through zipcode_lookup web scrapper to link them to their city/state and then are stored in a dictionary in the City() class with their associated average rental price. These values get averaged and stored in total_average_rent.
City + state inputs will prompt for additional input of either houses or apartments, as large cities can have bigger differences between the two housing types and will get stored in their appropriate class member.

Data will be pickled to store data past program execution.

If the same location is searched again, the appropriate data member will be updated with the more current average rental price and written to the pickle file.

Example of output from 3 zipcode searches; 92835 - 92831 - 92835 and 3 city/state seraches; Fullerton, CA "houses" - Fullerton, CA "apartments" - Fullerton, CA "houses"
[name = Fullerton, state = California, zipcodes: {'92835': 3425.0, '92831': 1800.89}, total_average_rent = 2612.945, average_apartments = 1617.92, average houses = 2915.98, last_update = 2019-02-11 13:12]
