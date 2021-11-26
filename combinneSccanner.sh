#!/bin/bash
# configs
upstream=wlan0
phy=wlan
# Create new interfaces file
cat <<EOF > /etc/network/interfaces
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet dhcp
# Remove if you don't want static IP
allow-hotplug $phy
iface $phy inet static
    address 10.0.0.1
    netmask 255.255.255.0
    network 10.0.0.0
    broadcast 10.0.0.255
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
EOF


#!/bin/bash
#categories=$(grep -r categories /usr/share/nmap/scripts/*.nse | grep -oP '".*?"' | sort -u  | cut -d '"' -f2)
iface=$1
target=$2
portsTCP="Null"
portsUDP="Null"


if [[ $(id -u) -ne 0 ]]; then
	echo "[!] Please run as root"
	exit 2
else
	if [ $# -ne 2 ];then
		echo "[*] Usage: bash $0 <iface> <target>"
		exit 1
	else
		ifconfig $iface &> /dev/null

		if [ $? -eq  0 ]; then
			if [[ $target =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
				echo "[+] Discovering ports..."
				masscan $target -p1-65535,U:1-65535 -oG out.grep --rate=1000 -e $iface

				echo ""
				grep open out.grep | grep tcp > tmptcp.grep
				if [ $? -eq 0 ]; then
					portsTCP=$(awk '{print $7}' tmptcp.grep | cut -d "/" -f1 | tr "\n" ",")
				fi

				grep open out.grep | grep udp > tmpudp.grep
				if [ $? -eq 0 ]; then
					portsUDP=$(awk '{print $7}' tmpudp.grep | cut -d "/" -f1 | tr "\n" ",")
				fi

				if [ $portsTCP != "Null" ]; then
					echo "[+] Scan TCP ports"
					echo "nmap $target -p $portsTCP -n -T4 -sV -Pn -sC"
					nmap $target -p $portsTCP -n -T4 -sV -Pn -sC
				fi
				if [ $portsUDP != "Null" ]; then
					echo "[+] Scan UDP ports"
					echo "nmap $target -sU -p $portsUDP -n -T4 -sV -Pn -sC"
					nmap $target -sU -p $portsUDP -n -T4 -sV -Pn -sC
				fi
				echo "[*] Finished"
			else
				echo "[!] Invalid IP"
				exit 2
			fi
		else
			echo "[-] You are not connected to $iface"
		fi
	fi
fi
