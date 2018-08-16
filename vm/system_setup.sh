#!/bin/bash

sudo cp /etc/network/interfaces_base /etc/network/interfaces
echo -e "\nauto enp0s8\niface enp0s8 inet static\n    address 192.168.15."$1"\n    netmask 255.255.255.0\n    network 192.168.15.0\n    broadcast 192.168.15.255\n    gateway 192.168.15.1\n" >> sudo /etc/network/interfaces
