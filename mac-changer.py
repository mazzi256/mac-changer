#!/usr/bin/env/ python3

import subprocess
import optparse
import re


"""
handling terminal/commandline commnads for easy execution of the script
"""
parser = optparse.OptionParser()
parser.add_option(
    "-i",
    "--interface",
    dest="interface",
    help="Enters the interface name you want to change its MAC Address",
)
parser.add_option(
    "-n",
    "--mac",
    dest="new_mac",
    help="Enters the new MAC Address to replace the original MAC Address",
)
(options, args) = parser.parse_args()

# subprocess.call("ifconfig", shell=True)  # shows the interfaces
interface = options.interface  # interface name
new_mac = options.new_mac  # new mac address


# Checking for current mac Address
def current_mac(interface):
    try:
        current_mac_output = subprocess.check_output(["ifconfig", interface])
        current_mac_output = current_mac_output.decode(
            "utf-8"
        )  # converting byt to string
        current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", current_mac_output)
        print("You are changing: " + current_mac.group(0) + " to " + new_mac)
    except Exception as e:
        print(e)


current_mac(interface=interface)


def mac_spoof(interface, new_mac):
    try:
        subprocess.call(
            [
                f" sudo ifconfig {interface} down && ifconfig {interface} hw ether {new_mac} && ifconfig {interface} up "
            ],
            shell=True,
        )
    # print("changed your MAC Address to " + new_mac)
    except Exception as e:
        print(e)


if not interface:
    print("No interface specified")
elif not new_mac:
    print("No new mac address specified")
mac_spoof(interface, new_mac)


def mac_changer():
    # checking if mac has ben changed!
    # subprocess.call("ifconfig", shell=True)  # shows the interfaces
    try:
        _ifconfig_output = subprocess.check_output(["ifconfig", interface])
        _ifconfig_output = _ifconfig_output.decode("utf-8")  # converting byt to string
        _ifconfig_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", _ifconfig_output)

        _ifconfig_mac = _ifconfig_mac.group(0)
        if _ifconfig_mac == new_mac:
            print("MAC Address changed successfully to " + new_mac)
        else:
            print("MAC Address not changed")
    except Exception as e:
        print(e)


mac_changer()
