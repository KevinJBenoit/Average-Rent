import requests
from bs4 import BeautifulSoup

url = "https://www.rent.com/colorado/colorado-springs-houses"

number_of_rentals = 0
all_prices = []

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")


prices = soup.find_all(class_="_3e12V")

for price in prices:
    home_price = price.contents #prints out the prices e.g. ['$2,195']
    home_price = list(str(home_price[0]))  #get the only item in the list, output $2,195
    #factor lots of this loop out into a function

    home_price.pop(0) #remove the '$' and ','
    if ',' in home_price: 
        home_price.remove(',') 

    home_price = "".join(home_price) 
    home_price = int(home_price)
    all_prices.append(home_price)
    number_of_rentals += 1

print(sum(all_prices)/number_of_rentals)