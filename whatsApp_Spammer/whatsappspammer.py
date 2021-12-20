import sys, os, re, random, traceback
import time
import pyautogui
import random
from datetime import datetime, timedelta, time
import time
import pywhatkit
from rich import print

#from dateutil.relativedelta import relativedelta

width = os.get_terminal_size().columns  # set the width to center goods
width_len = width
cwd = os.getcwd()



def display_header():
    print('whatsapp spammer--'.center(width))
    x = 'x'
    # pretty = f'xxx DOWNLOAD {list_or_dict} xxx'
    # print(f'{pretty : ^70}')
    print(f"{x * 20: ^70}")
    # zero = (f'[USAGE] - [0] {dl.href_str}')
    one = (f'[USAGE] - [1] This is a python program that spams WhatsApp messages via the web interface.')
    two = (
        f'[USAGE] - [2] You will see your mouse move with out you contorling it,  Do not be alarm, the program is workin.')
    three = (f'[USAGE] - [3] You can edit the send list by going to the CWD and editing spam.txt')
    four = (f'[USAGE] - [4] Each line indicates a new message, do not leave blank spaces or blank lines.')
    five = (f'**********************************************************************************************')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    # print(f"{zero:^70}")
    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print()


class current_time(datetime):
    all_obj = []
    global now
    now = datetime.now()
    global custom_date_time
    custom_date_time = timedelta(hours=3, minutes=5, seconds=30)
    global end_loop
    end_loop = (now + custom_date_time)
    global sleeper
    sleeper = random.randint(3, 4)
    random = random
    global hour_universal
    hour_universal = now.strftime("%H")
    global min_universal
    min_universal = now.strftime("%M")
    global year_universal
    year_universal = now.strftime("%Y")
    global month_universal
    month_universal = now.strftime("%m")
    global day_universal
    day_universal = now.strftime("%d")

    # global hour_universal
    #  date time format ("%d/%m/%Y %H:%M:%S")
    def __init__(self, time, re, hour, random):
        super().__init__(current_time, self, time, re, hour, random)

        all_object.append(self)
        self.time = time
        self.re = re
        #global hour
        self.year = year
        self.hour = hour
        self.random = random
        self.min09 = datetime.now().strftime('%M:%S.%f')[:-4]

    def __repr__(self):
        return f"current_time({self.time}{self.hour}{self.random}{self.min09})"

      #  return f"current_time(current time = {self.time}, current hour = {self.hour} current min = {self.min09} current random = {self.random}) "

    def __str__(self):
        return f"current_time(current time = {self.time}, current hour = {self.hour} current min = {self.min09} current random = {self.random}) "


    @classmethod  ## to update recursive time
    def check_time_class(cls):
        print('year ', year_universal)
        print('month ', month_universal)
        print('day ', day_universal)
        print('hour ', hour_universal)
        print('min ', min_universal)
        return hour_universal, min_universal


    def check_time(): ## to print current time
        print('year', year_universal)
        print('month', month_universal)
        print('day', day_universal)
        print('hour', hour_universal)
        print('min', min_universal)
        return hour_universal, min_universal


    def min_pattern(self):
        time_pattern = re.compile(r"[:\d:]")
        time_list = time_pattern.findall(str(now))
        min_str = ''
        min_list = time_list[11:13]
        min_list = min_list[0:2]
        min_str = min_str.join(min_list[0:2])
        return min_str

    def hour_pattern(self):
        hour_pattern = re.compile(r"[:\d:]")
        time_hour_list = hour_pattern.findall(str(now))
       # print(time_hour_list)
        hour_str = ''
        hour_list = time_hour_list[8:11]
        hour_list = hour_list[0:2]
        #print(hour_list)
       # print(), print('X' * 25)
        hour_str = hour_str.join(hour_list[0:2])
        return hour_str

    def add_mins(now):
        print('shawna')
        print(current_time.check_time())
        print('objects being parsed')
        print(current_time.all_obj)
        min05 = int(min05)
        hour01 = int(hour01)
        print('Minutes BEFORE conversion', min05)
        print(min05)
        print('Minutes AFTER conversion', min05)
        min05 = min05 + int(sleeper)
        print('Hour AFTER conversion', hour01)
        return hour01, min05


    def time_now(self):
        print('objects being parsed')
        print(current_time.all_obj)
        print ('FROM GLOBAL CLASS (global param)', current_time.min_universal)
        print ('FROM GLOBAL CLASS (global param)', current_time.hour_universal)
        global hour
        hour = self.hour
        global now
        now = self.now
        time.sleep(sleeper)
        min00 = current_time.min_pattern(now)
        global timer
        timer = random.randrange(3.0, 6.0)
        print('now', now)
        print('current hour', now.hour)
        print(f'Current min,  {min00}')
        print('custom_date_time', custom_date_time)
        time_right_now = datetime.strptime("%H:%M:%S")


        print(f'The time right now {time_right_now}')
        min04 = date_time.strftime("%H")
        print(min04)

        return hour, min04, now,

    def convert_timeformat(self):
        hour = int(self) - int(12)
        return hour

    def sendMsg(self, now):

        #    lass_now = current_time(int(now))
        #print(class_now)
        print('objects being parsed')
        print(current_time.all_obj)
        print('11111')
        print(current_time.check_time())

        with open('spambot.txt', 'r') as file:
            hour01 = -1
            min05 = -1
            line = file.readline()
            ticker = 0
            try:
               # hour01 = None
               # min05 = None
                while str(now) != end_loop:  # end_loop:
                    for each_line in file:
                        # hour01 = None
                        # min05 = None
                        if now == end_loop:
                            ticker += 1
                            return f'SENT [{ticker}] MESSAGES to [INSERT USER PHONE# INPUT] '
                        else:
                            def time_recursion(now):
                                print('objects being parsed')
                                print(current_time.all_obj)

                                print('22222222')
                                print(current_time.now)
                                print('this is the time before passing to add_mins func')
                              #  print(min05)
                                current_time00 = datetime.now()
                                hour01 = time.strftime('%H')
                                min05 = time.strftime('%M')

                                print('NEW TIME FROM timedate.now()')
                                print(current_time00)
                                print('NEW HOUR from timedate.now()')
                                print(hour01)
                                print()
                                print('NEW MIN AFTER RECURSION: ')
                                print(min05)

                                min05 = int(min05)
                                min05 = min05 + int(sleeper)
                                print('NEW MIN ADDING SLEEPER')
                                print(min05)


                                hour01 = int(hour01)
                                print('Minutes AFTER conversion', min05)
                                min05 = min05 + int(sleeper)

                                print(f'3333333 ')
                                print('this is the time after passing to add_mins func')

                                return hour01, min05



                            print('STARTING RECURSION 92109')
                            print(hour01, min05)

                            if (hour01 and min05) == -1:
                                hour01, min05 = current_time.check_time()
                                #hour01 = time.strftime('%H')
                                #min05 = time.strftime('%M')
                                print(f'\t\tRECURSION START: {hour01}:{min05}')
                                pass

                            else:
                                print(f" {ticker} {'X' * 35} {ticker}")
                                print('\t\t RESTARTING MESSAGE LOOP ')
                                pass


                            print(f" {ticker} {'X' * 35} {ticker}")
                            print('shawna01')
                            print(f'\t\t Current Hour Start: {hour01}')
                            print(f'\t\t Current Message Min: {min05}')
                            print('\t\tSleep timer is set to ', sleeper)
                            print(f'\t\t{hour01}:{min05}')
                            print(f" {ticker} {'X' * 35} {ticker}")



                        if ticker == 0:
                            print(f'First pass, adding sleep timer of [{sleeper}]')
                            min05 = int(min05)
                            min05 += int(sleeper)
                            pass

                        else:
                            pass

                        print(f" [{ticker}] {'X' * 35} [{ticker}]")
                        print(f' Parsed Ticker / Sleeper Check, moving on message send')
                        print(f'Min: [{min05}] :: hour :: [{hour01}] Sleeper: [{sleeper}] \n')
                        print(f'The message: {each_line} will be printed at {hour01}:{min05} (12 hour format')
                        print()

                        print(f"{'X' * 50} [{ticker}]")
                        print('8888888')

                        if int(x_time) >= 0: ## 12 AM in 24 hr format
                            print('Keeping format.')
                            print('Hour: ', hour01)
                            print('Min: ', int(min05))
                            print('X' * 5)
                            print(f'{hour01}:{min05}')
                            print(f" [{ticker}] {'X' * 35} [{ticker}]")

                            print('shawna02')
                            print(f'\t\t Current Start Hour: [{hour01}]')
                            print(f'\t\t Current Message Min: [{min05}]')
                            print(f'\t\t Sleep timer is set to , [{sleeper}]')
                            print(f'\t\t ** [{hour01}:{min05}] ** ')
                            print(f" {ticker} {'X' * 35} {ticker}")
                           ############# FIX PASS/FAIL ###############
                            if int(min05) > 60:
                                min05 = int(min05) - int(sleeper)
                                print('Converting minute since it is above 61 seconds')
                                print(f'reset timer (min): [{min05}]')
                            else:
                                pass

                            print('Parsing DATE-TIME ')
                            print(f'{"x" * 35} [{ticker}]')
                            pywhatkit.sendwhatmsg('+18622371332', f'{each_line}', int(hour01), int(min05))  # nested F-string to parse print ^^ otherwise times comeout weird
                            pyautogui.typewrite(each_line)
                            pyautogui.press('enter')
                            each_line = file.readline()

                            if each_line:
                                ticker += 1
                                print(f'** Sent Message :: [#{ticker}] at [{hour01}:{min05}]')
                                print(f'Hour Sent: , [{hour01}]')
                                print(f'Min Sent: , [{min05}]')
                                print('The Current Sleep time is', sleeper)
                                print(f"[#{ticker}] {'X' * 35}")

                                hour01, min05 = time_recursion(now)
                                print('new hour, min', hour01, min05)
                                #hour01, min05 = current_time.add_mins(hour01, min05)

                                print('New Time after ADD MINS func')
                                print(f'{hour01}:{min05}')

                                break
                        else:
                            continue

                        # elif:
                        # print('Message loop breaking')
                        # sys.exit(0)

            except Exception as E:
                traceback.print_exc()
                print(f' Error in parsing Loop - see send msg class:: . {str(E)}')
                sys.exit(0)





    # end_loop = input("[YYYY/MM/DD/HH/MM/DD]")
    # print(r'Enter the time you would like to start the attack do not include "/": ')
    # date_time_start = datetime.fronttimestamp(timestamp)
    # time_of_attack = date_time.stftime("%H:%M:%S")
    # d = date_time.strftime("%X")
    # print(d)
    # print(f'The attack is initiated at: [{time_of_attack}]')

### end_loop = now + custom_date_time

try:
    #
    # print(r'Enter the time you would like to start the attack do not include "/": ')
    # custom_date_time = input("[YYYY/MM/DD/HH/MM/DD] ")
    # date_time_start = datetime.fronttimestamp(timestamp)
    # custom_date_time = date_time.strftime("%X")
    # print(d)
    # print(f'The attack is initiated at: [{time_of_attack}]')

    display_header()
    print(f'Current Class Dict') # \n {}')

    class_dict = current_time.time_now.__dict__
    for iter in class_dict:
        print(class_dict[iter])

   # current_time.__dict__()


    print()
    print(f'-- WHATSAPP SPAMMER --'.center(width))
    print('Current OS Navigator: ', os.name)
    print(f'Current Working Directory: {cwd}')
    print(current_time.check_time())

    hour02, now02, = current_time.check_time()
    print(f'Spammer Initiating at --[{hour02}:{now02}]')
    print(hour02)
    print(now02)

    # print(type(time_right_now))
    #print(time_right_now)
    print()
    print()

    print('starting loop')
    print('objects being parsed')
    print(current_time.all_obj)

    print('__repr__')
    print(current_time.all_obj)

    print('__dict__')
    print(current_time.all_obj)



    for instance in current_time.all_obj:
        print(instance.time)
        print(instance.hour)
        print(instance.random)
        print(instance.time)


    while str(now) != end_loop:
        print(f' The loop is set to end in (hour, min, second):  {custom_date_time} \n')
        print(f'END LOOP TIME: {end_loop} \n')

        print('objects being parsed')
        print(current_time.all_obj)

        print()
        # x_time = current_time.min_pattern(custom_date_time)

        x_time = current_time.hour_pattern(custom_date_time)
        y_time = current_time.min_pattern(custom_date_time)

        print()
        print(f'12 HR Format:: {x_time}:{y_time}')

        print()

        print('Parsing 12 hour conversion, as int is less than 1')
        print()
        min_cycle01 = current_time.sendMsg(x_time, y_time)
        print(min_cycle01)

        if min_cycle01:
            print('YAYYY MIN MADE IT THIS FAR LETS SEE WHAT IT IS', min_cycle01)
            current_time.sendMsg(x_time, y_time)
            print(current_time.__str__())
            print(current_time.__repr__())

            continue


except Exception as e:
    traceback.print_exc()
    #traceback.print_exception(e)
    print(str(e))
    print(f'system exiting due to sendMSG error.'.center(width))

    sys.exit(1)

finally:
    print('Either you have reached the message limit, or there was an error in the program. See Error Code Above')
