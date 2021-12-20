from geolite2 import geolite2
import requests
import csv

##  pip3 install maxminddb && pip3 install maxminddb-geolite2      
def get_ip_location(SELF_IP):
    reader = geolite2.reader()
    location = reader.get(SELF_IP) ## initiate reader, t get
    print(type(reader))
    print(reader)
    print(type(location))
    print(location)
    print(location.values()) # print key values)
    a=(location['city']['names']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])
#https://www.udacity.com/blog/2020/11/python-string-format-whats-the-difference-between-s-and-d.html#:~:text=Of%20the%20three%20types%2C%20you,anything%20else%20but%20a%20number.
    print('''city: %s\n continent: %s\n country: %s\n location: %s\n postal: %s\n registered_country: %s\n subdivisions: %s\n'''
     % (a,b,c,d,e,f,g))


# SELF_IP = requests.get('https://api.ipify.org').text # api to pull self ip via text
IP_FIND = input(str(f'[SYS] Enter The Ip You Would Like To Look Up, The Package Will Return Their Location.'))
print(IP_FIND)
get_ip_location(IP_FIND)

#
#
# {'city': {'geoname_id': 5391811, 'names': {'de': 'San Diego', 'en': 'San Diego', 'es': 'San Diego', 'fr': 'San Diego', 'ja': 'サンディエゴ', 'pt-BR': 'San Diego', 'ru': 'Сан-Диего'}}, 'continent': {'code': 'NA', 'geoname_id': 6255149, 'names': {'de': 'Nordamerika', 'en': 'North America', 'es': 'Norteamérica', 'fr': 'Amérique du Nord', 'ja': '北アメリカ', 'pt-BR': 'América do Norte', 'ru': 'Северная Америка', 'zh-CN': '北美洲'}}, 'country': {'geoname_id': 6252001, 'iso_code': 'US', 'names': {'de': 'USA', 'en': 'United States', 'es': 'Estados Unidos', 'fr': 'États-Unis', 'ja': 'アメリカ合衆国', 'pt-BR': 'Estados Unidos', 'ru': 'США', 'zh-CN': '美国'}}, 'location': {'accuracy_radius': 20, 'latitude': 32.7977, 'longitude': -117.2335, 'metro_code': 825, 'time_zone': 'America/Los_Angeles'}, 'postal': {'code': '92109'}, 'registered_country': {'geoname_id': 6252001, 'iso_code': 'US', 'names': {'de': 'USA', 'en': 'United States', 'es': 'Estados Unidos', 'fr': 'États-Unis', 'ja': 'アメリカ合衆国', 'pt-BR': 'Estados Unidos', 'ru': 'США', 'zh-CN': '美国'}}, 'subdivisions': [{'geoname_id': 5332921, 'iso_code': 'CA', 'names': {'de': 'Kalifornien', 'en': 'California', 'es': 'California', 'fr': 'Californie', 'ja': 'カリフォルニア州', 'pt-BR': 'Califórnia', 'ru': 'Калифорния', 'zh-CN': '加利福尼亚州'}}]}
