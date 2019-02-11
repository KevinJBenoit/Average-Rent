# Average-Rent
Web scraper of rent.com city location

User enters either a zip code or city and state to search. If zip is entered, apartments + condos + houses + townhouses
will be scraped. If city/state is entered only houses will be scraped.


Data will be pickled to store data past program execution.
Zipcodes are stored in a dictionary with their associated average rental price. These values get averaged and stored in total_average_rent.

City + State + houses/apartments get stored in their appropriate class member.

If the same location is searched again, the appropriate data member will be updated with the more current average rental price and written to the pickle file.
