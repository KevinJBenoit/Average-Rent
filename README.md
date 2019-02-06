# Average-Rent
Web scraper of rent.com city location

Asks user for input of either a zipcode or city + state to gather an average rent/month for that location.
Zipcode inputs will gather prices from all the available housing types; houses, apartments, condos, townhouses because of smaller search radius
City + state inputs will prompt for additional input of either houses or apartments, as large cities can have big differences between the two housing types.
Data will be stored in City() class, which will also include a Zipcode() class within that for grouped data.
