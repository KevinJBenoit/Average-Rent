
"""
User enters either a zip code or city and state to search. If zip is entered, apartments + condos + houses + townhouses
will be scraped. If city/state is entered only houses will be scraped.
"""



from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from functions_module import stateUnabbreviate



base_url = "https://www.rent.com/"
page_number = 1

#regex pattern for zipcodes, 5 numbers
zip_code_pattern = re.compile(r'\d{5}$')

#prompt for a city search or zipcode search
user_search = input("Please enter the zipcode or city and state you wish to search: (example: Colorado Springs, CO) \n")

print("Average rental price: ")

#regex test on user input
result = zip_code_pattern.search(user_search)

#if regex True, it is a zipcode
if result:
    zipcode = result.group()
    search_url = "zip-" + zipcode

#if regex False, it is a city
else:
    city = user_search
    city_parse = city.split(',') #separates the city name and state abbreviation
    state = stateUnabbreviate(city_parse[1].strip()) #accesses the state initials, removes whitespace char, and send to function

    #check if valid state abbreviation
    if state == None:
        print("Sorry, location not found.")
        quit()

    city = city_parse[0] #access city name
    search_url = state.lower() + "/" + city.replace(" ", "-").lower() + "-houses" #format into a proper url for houses only for citys

#initiate number of rentals and price list
number_of_rentals = 0
all_prices = []

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

    sleep(3)#slow things down to be ethical   ʕ•ᴥ•ʔ    

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

print("$" + str(average_price) + "/month is the average price from", number_of_rentals, "rentals found.")
