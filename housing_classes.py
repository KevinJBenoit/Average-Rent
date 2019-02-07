
import datetime

class City():
    def __init__(self, name, state):
        self.name = name
        self.state = state 
        self.zipcodes = []
        self.total_average_rent = 0
        self.average_apartments = 0
        self.average_houses = 0
        self.last_update = "-"
    def __repr__(self):
        return f"name = {self.name}, state = {self.state}, total_average_rent = {self.total_average_rent}, average_apartments = {self.average_apartments}, average houses = {self.average_houses}, last_update = {self.last_update}"

    def full_name(self):
        return self.name + ", " + self.state

    def city_update(self):
        now = datetime.datetime.now()

        #thank you Eliot from SaltyCrane.com for example on getting current date and time using datetime
        self.last_update = now.strftime("%Y-%m-%d %H:%M")

    #takes a list, prices, and sets their average to self.average_apartments
    def add_apartments(self, prices):
        self.average_apartments = 0
        for price in prices:
            self.average_apartments += price
        self.average_apartments /= len(prices)
        self.city_update() #renew the last_update to the current date/time

    #takes a list, prices, and sets their average to self.average_houses
    def add_houses(self, prices):
        self.average_houses = 0
        for price in prices:
            self.average_houses += price
        self.average_houses /= len(prices)
        self.city_update() #renew the last_update to the current date/time

    def average_all(self):
        self.total_average_rent = (self.average_apartments + self.average_houses) / 2
    


class Zipcode():
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.average_rent = 0
        self.city = ""
        self.last_update = "-"
    def __repr__(self):
        return f"{self.zipcode} has an average rent of ${self.average_rent}/month. It was last updated on {self.last_update}"

    def zipcode_update(self):
        now = datetime.datetime.now()

        #thank you Eliot from SaltyCrane.com for example on getting current date and time using datetime
        self.last_update = now.strftime("%Y-%m-%d %H:%M")