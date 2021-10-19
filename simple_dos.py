from scapy.all import *

pkt = sniff(fiolter)

pkt[]
pkt[0].show shw
pkt[0][0].show() # ether 802.
pkt[0][1].show() # logial link control
pkt[0][3].show() # st