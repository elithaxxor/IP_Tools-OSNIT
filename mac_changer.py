import subprocess, uuid, optparse, pprint, platform, traceback, sys
import netifaces, os, random, string, time
from netifaces import (AF_LINK,
                       )
from pprint import pprint




class ChangeMac():
    def __init__(self):
        self.mac_uuid = uuid.getnode()
        self.mac_uuid_hex = hex(uuid.getnode())
        self.available_interfaces = netifaces.interfaces()
        self.parser = optparse.OptionParser()
        super(ChangeMac)
    @staticmethod
    def get_sysInfo():
        try:
            width = os.get_terminal_size().columns  # set the width to center goods
            terminal = os.environ.get('TERM')
            width_len = width
            cwd = os.getcwd()
            #  IP_INFO = f"\033[1;35;0m {IPx.IP}"
            current_version = platform.release()
            system_info = platform.platform()
            os_name0 = platform.system()
            current_platform = platform.system()
            platform_name = sys.platform
            ## new adds
            big_names = platform.uname()
            processor = platform.processor()
            architecture = platform.architecture()
            user_id = os.uname()
            login = os.getlogin()
            print()
            print(f"{'X'* 50}".center(width))
            print(f'**[SYSTEM INFO]**'.center(width))
            print()
            print(f'\033[1;35;m [CURRENT_PLATFORM]--[{current_platform}]  ...? '.center(width))
            print(f'\033[1;35;m [PLATFORM_NAME]--[{platform_name}]  ...? '.center(width))
            print(f'\033[1;35;m [CURRENT_VERSION]--[{current_version}]  ...? '.center(width))
            print(f'\033[1;35;m [OS-NAME]--[{os_name0}] + [{terminal}] ...? '.center(width))
            print(f'\033[1;35;m [SYSTEM-INFO]--[{system_info}]  ...? '.center(width))
            print(f'\033[1;35;0m [CURRENT-VERSION]--[{current_version}]  ...? '.center(width))
            print(f'\033[1;35;0m [UUID]--[{big_names}]  ...? '.center(width))
            print(f'\033[1;35;0m [PROCESSOR]--[{processor}]  ...? '.center(width))
            print(f'\033[1;35;0m [ARCHITECTURE]--[{architecture}]  ...? '.center(width))
            print(f'\033[1;35;0m [USER-ID]--[{user_id}]  ...? '.center(width))
            print(f'\033[1;35;0m [LOGIN]--[{login}]  ...? '.center(width))
            print(f"{'X'* 50}".center(width))
            print()

        except Exception as e:
            print()
            print('X'*50)
            traceback.print_exc()
            print(f'[Error In Parsing SYS Info] \n{str(e)}')


    def get_uuid(self):
        try:
            print(f'[+] [The Current MAC-HEX]: \n {self.mac_uuid_hex}')
            print(f'[+] [The Current MAC-BASE-10]: \n {self.mac_uuid}')
            print('\n'), print('X'*50)
            print('\n'), print('X'*50)
            print(f'[+]  [Available NICs] : \n {self.available_interfaces}'), print()
            print(f'[+]**Enter The Interface: ')
            NIC = input()#, print()
            MAC = netifaces.ifaddresses(str(NIC))[netifaces.AF_LINK]
            print(f'[+] **[NIC INFO] [{NIC}]: \n **[MAC INFO] [{MAC}]')
            print()
            print('X'*50)

            return NIC, MAC

        except Exception as e:
            print()
            print('X'*50)
            traceback.print_exc()
            print(f'Error In UID {str(e)}')

    def get_arguments(self):
        try:
            self.parser.add_option('-i', '--interface', dest='interface', help='interface to change mac')
            self.parser.add_option('-m', '--mac', dest='new', help='New Mac Address')
            (options, arguments) = self.parser.parse_args()
            if not options.interface:
                self.parser.error('**Please Specify a Valid Interface [--help for info]')
            elif not options.new:
                self.parser.error('**Please Specify a valid MAC Address [--help for info]')
            return options, arguments

        except Exception as e:
            print()
            print('X'*50)
            traceback.print_exc()
            print(f'Error In UID {str(e)}')
            sys.exit(1)


    def mac_generator(self):
        print()
        print('X' * 50)
        print(f'[MAC-GENERATOR **STARTED]')
        resp_yes = ["yes","Yes","YES","y","Y"]
        no = ["no","No","NO","n","n"]
        print(f'**Should I generate a random MAC for you?')
        answer = input('')

        if answer in resp_yes:
            letters = string.ascii_letters
            print(letters)

            print()
            print('X'*50)
            print(f'[INITIATING RANDOM MAC]')
            new_mac = ''
            random_num = []
            for i in range(0, 12):
                # random_list.append(random.randint(0, 1000))
                random_num.append(random.randrange(0, 10, 2))
            print(f'RANDOM-NUMBERS\n [{random_num}])')
            random_letter = []
            for z in range(0, 12):
                random_letter.append(random.choice(string.ascii_letters))
            print(f'RANDOM-LETTERS\n [{random_letter}])')
            noRand_mac = zip(random_num, random_letter)
            noRand_mac = list(noRand_mac)
            randMac = random.shuffle(noRand_mac)
            print(f'[NEW-RANDOM-MAC\n [{randMac}])')
            print('X' * 50)
            return randMac

        else:
            print(f'**Please Specify The MAC Address.')
            new_mac = input()
            return new_mac



    # Output [994, 287, 65, 994, 936, 462, 839, 160, 689, 624]

    @staticmethod
    def change_mac(interface, new_mac):
        try:
            print()
            print('X' * 50)
            print(f'[CHANGE-MAC-SEQUENCE **STARTED]')
            subprocess.call(['ifconfig', interface, 'down'])
            subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
            subprocess.call(['ifconfig', interface, 'up'])
            new_mac = netifaces.ifaddresses(str(interface))[netifaces.AF_LINK]
            print(f'[THE NEW MAC IS**[{new_mac}]')
            print('X' * 50)

            sys.exit(0)
        except Exception as e:
            traceback.print_exc()
            print(f'Error In UID {str(e)}')
            sys.exit(1)




ChangeMac.get_sysInfo() ## get sys info
print(f'[INITIATING MAC-GENERATOR]')
time.sleep(2)
macChanger = ChangeMac() #initiate class
nic, mac = macChanger.get_uuid() ## get mac/nic
nic = str(nic)
mac = str(mac)
print()
print('X'*50)
print(f'[ENTERED NIC], {str(nic)} \n [CURRENT-MAC] {str(mac)}')
time.sleep(2)
new_mac = macChanger.mac_generator() # mac generator
print(f'[NEW-MAC]-- {str(new_mac)}\n [OLD-MAC]-- {str(mac)}')
time.sleep(2)


print()
print('X'*50)
print(f'[STARTING MAC-CHANGE-SEQUENCE]')
ChangeMac.change_mac(nic, mac)## get to work
time.sleep(2)
print(f'[END]')
print('X'*50)

#macChanger.change_mac(nic, mac)

#opt, arg = change_mac.get_arguments() ##set params
#print(f'[OPTIONS]-- {str(opt)}\n [ARGS]-- {str(arg)}')

