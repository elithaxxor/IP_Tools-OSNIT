import subprocess
import re

command_output = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True).stdout.decode()
profile_names = (re.findall('All User Profile     :(.*)\r'), capture_output=True).stdout.decode()
print(f'[SYSTEM] Current Profile Names \n {profile_names}')
print(f'[SYSTEM].. Creating list with  Profile Names + passwords \n)

wifi_list = ()
if len(profile_names) !=0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', name], capture_output=True).stdout.decode()
        if re.search("Security         : Absent", profile_info):
            continue
        else:
            wifi_profile['SSID'] = name
            profile_info_pass = subprocess.run(['netsh', 'wlan', 'show', 'profile', name], capture_output=True).stdout.decode() #continues the loop
            password = re.search(":Key Content      :(.*)\r")
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi.append(wifi_profile)
for x in range(len(wifi_list)):
    print(wifi_list[x])

    
