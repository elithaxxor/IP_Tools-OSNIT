import requests
import json
import urllib.request
# from geolite2 import geolite2
# import geoip2.webservice

def convert_strDict(REQ):
    Dict = dict((x.strip(), y.strip())
                 for x, y in (element.split('-')
                 for element in REQ.split(', ')))
    return Dict



class Get_IP():

    def Get_ip(self):
        SELF_IP = requests.get('https://api.ipify.org').text  # api to pull self ip via text
        #SELF_IP = ('76.172.85.231')  # api to pull self ip via text
        REQ00 = f"http://api.ipapi.com/{SELF_IP}?access_key=4c30512e8afe7d0a27c11e5deb4fce34"
        REQ = requests.get(REQ00).text
        res = json.loads(REQ), print(), print()
        print(SELF_IP)
        print('X' * 50)
        req_str = REQ.split(',', -1)
        #	 print(req_str)
        print('X' * 50)
        print(type(req_str))
        ip = req_str[0]
        continent = req_str[3]
        country = req_str[5]
        state = req_str[7]
        city = req_str[8]
        zip = req_str[9]
        print(ip)
        print(continent)
        print(country)
        print(state)
        print(city)
        print(), print(),
        print('X' * 50)

        return SELF_IP


get_info = Get_IP()
IPA = get_info.Get_ip()
#IP = get_info.Get_ip.ip
print(IPA)
print('Famished')
print(get_info)


#
#
