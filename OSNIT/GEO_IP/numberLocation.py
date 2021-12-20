#import phonenumbers
#from myNumber import number
import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import PhoneNumberType
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import numpy as np
import pandas as pd
import folium
import webbrowser
import time
import googlemaps
from datetime import datetime
from googleapiclient.discovery import build
import gmaps
#import geocoder
import gmaps
import gmaps.datasets
import ipywidgets as widgets
import geopy


## shodon shodan.io (for accessing IOT devices) 
SHODON_KEY = 'O49Ksy1HyForTiu99jJGRk7nJY2JSwvN'


Key = '813978e32347461bb2d53b777a9545e2'
print('Enter Phone number to see past locations: ')
number=input('**')
phonenumber = phonenumbers.parse(number)
print(f'{number}')
print(type(number))
print(f'{phonenumber}')
print(type(phonenumber))
time.sleep(5)

yourLocation = geocoder.description_for_number(phonenumber, 'en')
Region = geocoder.description_for_number(phonenumber, 'en')
isValid = phonenumbers.is_valid_number(phonenumber)
# Checking possibility of a number
isPossible = phonenumbers.is_possible_number(phonenumber)
serviceProvider = carrier.name_for_number(phonenumber, 'en')
#sserviceProvider = phonenumbers.parse(phonenumber)


print(f'[LOCATION] {yourLocation}')
time.sleep(1)
print(f'[REGION] {Region}')
time.sleep(1)
print(f'[VALID] {isValid}')
time.sleep(1)
print(f'[Is Possible?] {isPossible}')
time.sleep(1)
print(f'[SERVICE-PROVIDER?] {serviceProvider}')
time.sleep(1)




numNum2 = phonenumbers.parse(number)

#print(f'[SERVICEPROVIDER] {serviceProvider}')
##print('*' * 100)

######################
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
print('Query;', query)
print('Results;', results)

#for x in range(len(results)):     ### ---> DEBUGGING - TO VIEW ARRAY BEFORE CONVER TO DF
    #print(f'{results[x]} \n', 'x' * 100)
#print(type(query)) #<- debug purpose
#print(type(results)) #<-debug purpose
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f'[COORDINATES] {lat} , {lng}\n')
df = pd.DataFrame(results)
print('*' * 100)
print(f'[EXPORT] ..saved as coordinates.txt {df.head(2)}')
df.to_csv(r'\coordinates.csv', index = False)
#########################
myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = yourLocation).add_to(myMap)
myMap.save('eyespy.html')
print(f'[MAP]** saved to eyespy.html')
#file:///Users/macbook/Documents/CS/PROJECT/phone_number/eyespy.html

#pd.read_html(myMap.save('eyespy.html'))
webbrowser.open('eyespy.html')
webbrowser.open('/Users/macbook/Documents/CS/PROJECT/phone_number/eyespy.html')


# ##############
# Geocoding API	-	-	-	Details
# Geolocation API	-	-	-	Details
# Places API
# ##############


books_service = build('books', 'v1', developerKey='api_key')


api_key = "AIzaSyCY6INDQICh3uR6yhcxdtrzZrYrzR5Lkv4"
r"https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCY6INDQICh3uR6yhcxdtrzZrYrzR5Lkv4"


#phonelocate = Client(key='AIzaSyCY6INDQICh3uR6yhcxdtrzZrYrzR5Lkv4')
#
# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#
# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)




import json
import time
import urllib.error
import urllib.parse
import urllib.request

# The maps_key defined below isn't a valid Google Maps API key.
# You need to get your own API key.
# See https://developers.google.com/maps/documentation/timezone/get-api-key
API_KEY = "AIzaSyCY6INDQICh3uR6yhcxdtrzZrYrzR5Lkv4"
TIMEZONE_BASE_URL = "https://maps.googleapis.com/maps/api/timezone/json"
API_HREF = r"https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCY6INDQICh3uR6yhcxdtrzZrYrzR5Lkv4"


def timezone(lat, lng, timestamp):
    # Join the parts of the URL together into one string.
    params = urllib.parse.urlencode(
        {"location": f"{lat},{lng}", "timestamp": timestamp, "key": API_KEY,}
    )
    url = f"{TIMEZONE_BASE_URL}?{params}"

    current_delay = 0.1  # Set the initial retry delay to 100ms.
    max_delay = 5  # Set the maximum retry delay to 5 seconds.

    while True:
        try:
            # Get the API response.
            response = urllib.request.urlopen(url)
        except urllib.error.URLError:
            pass  # Fall through to the retry loop.
        else:
            # If we didn't get an IOError then parse the result.
            result = json.load(response)
            print(result)
            if result["status"] == "OK":
                return result["timeZoneId"]
            elif result["status"] == "UNKNOWN_ERROR":
                # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                # ZERO_RESULTS. There is no point retrying these requests.
                raise Exception(result["error_message"])
        if current_delay > max_delay:
            raise Exception("Too many retry attempts.")

        print("Waiting", current_delay, "seconds before retrying.")

        time.sleep(current_delay)
        current_delay *= 2  # Increase the delay each time we retry.


if __name__ == "__main__":
    tz = timezone(39.6034810, -119.6822510, 1331161200)
    print(f"Timezone: {tz}")
