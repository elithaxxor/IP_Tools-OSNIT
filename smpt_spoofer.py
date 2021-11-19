import smtplib
import email
from email import encoders
from email.mime.text import MIMEText #text
from email.mime.base import MIMEBase #for attachment
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from smtplib import SMTP
import logging
from logging import handlers
import pywhatkit as kit
import os
from datetime import datetime
import time
import threading
import pywhatkit
import datetime
import getpass as gp




SERVER = smtplib.SMTP('smtp.gmail.com', 25) #or 597
# SERVER.connect("smtp.gmail.com", 25)
SERVER.ehlo() # starts the smptp process.
SERVER.starttls()



USER_NAME = gp.getpass(prompt='[SYS] Your email login: : ', stream=None)
PASS = gp.getpass(prompt='[SYS] Enter password: : ', stream=None)
SERVER.login(USER_NAME, PASS)
RECEIVER = input(f'[SYS] Receiver: ' )
SUBJECT = input(f'[SYS] Subject: ' )
FAKE_NAME = input('[SYS] Spoof ID: ')



def write_msg():
    MESSAGE_TEXT = input(f'[SYS] .txt name:')
    with open(MESSAGE_TEXT, 'a') as f:
        MESSAGE = input(f'[SYS] Enter your message: :')
        f.write(MESSAGE)
        f.close()



        msg = MIMEMultipart() # try taking outside of loop
        msg['From'] = FAKE_NAME
        msg['To'] = RECEIVER
        msg['Subject'] = SUBJECT

        with open('mail_01.txt', 'r') as f:
            msg.attach(MIMEText(MESSAGE, 'plain')) ## adds a header and text to message object
            print(f'[SYS] Sent {MESSAGE} to {RECEIVER}')
            f.close()

        #logger = logging.getLogger()
        #logger.addHandler(smtp_handler)
    filename = 'server_00.png' # or specify path
    attachment = open(filename, 'rb')  # RB for 'reading bytes' to work with image data
    p = MIMEBase('application', 'octet-stream') #octet-stream - used to process image data. --> converts to binary
    p.set_payload(attachment.read()) ## sets image binary code to p using set_payload function
    encoders.encode_base64(p) #
    p.add_header('Content-Disposition', f'attachment; filename = {filename}') ## creates header
    msg.attach(p) ## adds payload to message
    text = msg.as_string()
    SERVER.sendmail(USER_NAME, RECEIVER, text)
    SERVER.close()
# except Exception as e:
#     logger.exception('Unhandled Exception')
#     print(str(e))
#     SERVER.close()
#






    ## EMAIL.ERROR https://docs.python.org/3/library/email.errors.html#email.errors.MessageParseError
# except Exception email.errors.MessageError:
#     print(f'[SYS] ERROR Message Error')
#     pass
# except Exception email.errors.HeaderParseError:
#     print(f'[SYS] Header Parse Error')
#     pass
# except Exception email.errors.MessageParseError:
#     print(f'[SYS] Message Parse Error')
#     pass
# except Exception email.errors.MessageError:
#     pass
