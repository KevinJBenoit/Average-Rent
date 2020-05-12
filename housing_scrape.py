
"""
Function is passed either zipcode or city/state and will have 2 return values.
If zipcode all housing types will be scraped and rents averaged and zipcode housing type returned.
If city + state passed an additional prompt for if houses or apartments will be scrapped, the rent and that housing type will be returned.
"""



from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from functions_module import stateUnabbreviate, zipcode_validate

def scrape_rent(user_search):

    base_url = "https://www.rent.com/"
    page_number = 1

    #regex test on user input
    result_is_zipcode = zipcode_validate(user_search)

    #if regex True, it is a zipcode
    if result_is_zipcode:
        housing_type = None
        zipcode = result_is_zipcode.group()
        search_url = "zip-" + zipcode

    #if regex False, it is a city
    else:
        #input for if houses or apartments will be scraped
        user_housing = input("Would you like to search houses or apartments? \n")
        if user_housing.lower() == "houses":
            housing_type = "-houses"
        else:
            housing_type = "-apartments"

        city = user_search
        city_parse = city.split(',') #separates the city name and state abbreviation
        state = stateUnabbreviate(city_parse[1].strip()) #accesses the state initials, removes whitespace char, and send to function

        #check if valid state abbreviation
        if state == None:
            print("Sorry, location not found.")
            quit()

        city = city_parse[0] #access city name

        search_url = state.lower() + "/" + city.replace(" ", "-").lower() + housing_type #format into a proper url

    #initiate number of rentals and price list
    number_of_rentals = 0
    all_prices = []

    print("Fetching average rental price.... ")

    #loops until there are no pages left to scrape
    while page_number:
        #generate the url location to be scraped
        full_url = base_url + search_url + "?page=" + str(page_number) #if there is another page it will continue

        #scrapes the html from given page
        res = requests.get(full_url)
        soup = BeautifulSoup(res.text, "html.parser")

        #get the class that contains price data
        prices = soup.find_all(class_="_3e12V")


        #extract and manipulate each price contained in prices
        for price in prices:
            home_price = price.contents #extracts out the prices e.g. ['$2,195']
            home_price = list(str(home_price[0]))  #get the only item in the list, output is $2,195
 
            #remove special characters
            special_chars = (',', '$', '+')
            for char in home_price:
                if char in special_chars:
                    home_price.remove(char)
           
            #brings the list together into one string
            home_price = "".join(home_price) 

            #removes non numeric price postings such as "Contact Us" ect.
            if home_price.isdigit():
                all_prices.append(int(home_price))
                number_of_rentals += 1

        sleep(2)#slow things down to be ethical    

        #check if there is another page button
        next_page = soup.find(class_="_1_EJB")
        if next_page:
            page_number += 1
        else:
            page_number = None

    #check if there are any rentals listed in location
    if number_of_rentals == 0:
        print("There are no rentals in your location.")
        quit()


    average_price = round((sum(all_prices)/number_of_rentals), 2)


    if housing_type:
        return average_price, housing_type
    else:
        #housing_type was None, set housing_type to the zipcode given
        return average_price, result_is_zipcode.group()
