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
#   wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
EOF
