import phonenumbers
from phonenumbers import geocoder
from phonenumbers import PhoneNumberType
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import numpy as np
import pandas as pd
import folium
import webbrowser


Key = '813978e32347461bb2d53b777a9545e2'

number = input('Enter Phone number to see past locations: ')
phonenumber = phonenumbers.parse(number)
print(f'{number}')
yourLocation = geocoder.description_for_number(number, 'en')
print(f'[LOCATION] {yourLocation}')
numNum2 = phonenumbers.parse(number)

#serviceProvider = carrier.name_for_number(numNum2, 'en')
#print(f'[SERVICEPROVIDER] {serviceProvider}')
##print('*' * 100)

######################
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
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
