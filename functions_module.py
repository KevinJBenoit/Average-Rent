

import requests
from bs4 import BeautifulSoup
from time import sleep
import re


#Used to convert given state abbreviations into the names for use
##Thank you Mike Shultz on ActiveState Code for this recipe. 
#code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
def stateUnabbreviate(abbreviation):
	states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

	return states.get(abbreviation)

#Returns the city, state associated with the zipcode as a string
def zipcode_lookup(zipcode):
    
    full_url = "https://www.unitedstateszipcodes.org/" + str(zipcode) + "/" 
    #Server needed more information so I could get acceess to the page
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    #Supply agent as the header for access
    result = requests.get(full_url, headers=agent)
    
    soup = BeautifulSoup(result.text, "html.parser")

    city_soup = soup.find("dl", class_= "dl-horizontal").find("dd").get_text()

    return city_soup

#returns True or False if there was a Regex match
def zipcode_validate(user_input):
    zip_code_pattern = re.compile(r'\d{5}$')

    #regex test on user input
    result_is_zipcode = zip_code_pattern.search(user_input)

    return result_is_zipcode
