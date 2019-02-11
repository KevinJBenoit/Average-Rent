
import housing_scrape
from housing_classes import City
import functions_module
import pickle


location = input("Please enter the zipcode or city and state you wish to search: (example: Colorado Springs, CO) \n")
is_zipcode = functions_module.zipcode_validate(location)




if is_zipcode:
    #call the web scraper
    average_price, location_type = housing_scrape.scrape_rent(location)

    #get the city, state from the zipcode
    city = functions_module.zipcode_lookup(location)

    #parse the name, and get the full state name and full city name assigned, can be refactored
    city_parse = city.split(',')
    state = functions_module.stateUnabbreviate(city_parse[1].strip())
    city_name = city_parse[0]

    #create a city with the appropriate zipcode
    city1 = City(city_name, state)
    city1.zipcodes.update({location: average_price}) #update the dictionary with a key value pair {zipcode : price}
    city1.city_update() #a new value was added, update the latest date/time



#else not a zipcode but a city and state
else:
    #call web scraper
    average_price, location_type = housing_scrape.scrape_rent(location)

    #parse the name, and get the full state name and full city name assigned
    city_parse = location.split(',')
    state = functions_module.stateUnabbreviate(city_parse[1].strip())
    city_name = city_parse[0]

    city1 = City(city_name, state)
    #if user wanted houses search, update the housing member
    if location_type == "-houses":
        city1.average_houses = average_price
    #else the user wanted apartments, update the apartment member
    else:
        city1.average_apartments = average_price
    city1.city_update()


#try to load the picle file
try:
    with open("cities.pickle", "rb") as file:
        all_cities = pickle.load(file)
#pickle file does not exist, create it
except IOError:
        all_cities = []
        with open("cities.pickle", "wb") as file:
            pickle.dump(all_cities, file)
        pass



#if there are any cities already in the pickle file
if all_cities:
    
    #for all the cities present in the pickle file
    for data_city in all_cities:
        

        #if zipcode was entered
        if is_zipcode:
            #if there any codes already present
            if data_city.zipcodes:
                #for all the codes in this pickle city. Create a copy so that dictionary can be updated while iterating
                for codes in data_city.zipcodes.copy():
                    #if the zipcode already is present
                    if codes == location:
                        #update that zipcode
                        data_city.zipcodes[location] = city1.zipcodes[location]
                    #the zipcode is unique, add it to the pickle dictionary
                    else:
                        data_city.zipcodes.update({location: average_price})    
                   
                        
            #this is the first zipcode for this city
            else:
                data_city.zipcodes.update({location: average_price})
                data_city.last_update = city1.last_update
            #average all the zipcode prices, update the date/time
            data_city.total_average_rent = sum(data_city.zipcodes.values()) / len(data_city.zipcodes)
            data_city.last_update = city1.last_update


        #elif city was entered and is already present, update the pickled values with the more current one searched
        elif str(data_city.name) == str(city1.name) and str(data_city.state) == str(city1.state):
            #if houses were entered, update houses
            if location_type == "-houses":
                data_city.average_houses = city1.average_houses
            else:
            #if apartments were entered, update apartments
                data_city.average_apartments = city1.average_apartments
            
            #update the date/time
            data_city.last_update = city1.last_update


        #location was not a zipcode, and is a new city location
        else:
            all_cities.append(city1)


#else, this is the first city in the pickle file append the city info
else:
    all_cities.append(city1)



#write the data to the pickle file
with open("cities.pickle", "wb") as file:
    pickle.dump(all_cities, file)

#read the newly written pickle file
with open("cities.pickle", "rb") as file:
        load_pickle = pickle.load(file)

#print the pickle file info
print(load_pickle)