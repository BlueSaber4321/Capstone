'''
WARNING
This respository is not to be used in a production enviroment :)
It is just a demonstration for a capstone project.
'''

TS_KEY = [redacted] # have it point to an env file later with a key (dont forget to add it to .gitignore)

print("Starting init of imports.\n\n\n")
import os, hashlib, ipaddress, sqlite3, pymongo

print("Checking hardware..")
# add something here for checking if its running on a raspberry pi
# so we are sure we have some sort of pinout and enough power since
# i am not optimizing this. :/

print("Checking if on the network.\n")

if ipaddress.ip_interface : None
print("No interface found to be connected, check if you are online!\nExiting!!\n")
exit() #force program exit if no interface found to be online.
else
print("Interface found, attempting connection to Tailscale.") # hope and pray it connects


# space it out from initialization
print("\n\n\n")
rawInput = input("Scan ID: \n")
print("\n\nHashing to SHA256 to compare with either DB or local..\n")
hashStore = hashlib.sha256(rawInput)
