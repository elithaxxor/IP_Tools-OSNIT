import socket
import hmtl.parser import HTMLParser 


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')


## The Client
class WebBrowserC:
    print(f'[+] Address" ')
    def webbrowser(self):
        IP = input('')
        PORT = 80
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((IP, PORT))
        cmd = "GET f'{IP}'\r\n\r\n".encode() ## change \r\n to headers later".encode()
        ### ADD HEADERS HERE #### 
        clientSocket.send(cmd)
        while True:
            clientData = clientSocket.recv(512)
            if len(clientData) < 1:
                break
            print(clientData.decode(), end='')

        clientSocket.close()


browser = WebBrowserC()
browser.webbrowser()
parser()



