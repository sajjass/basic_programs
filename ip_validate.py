import re

ipaddr = raw_input("Enter IP Address: ")
validate_ip_address = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
if re.match(validate_ip_address, ipaddr):
    print("Valid ip address")
else:
    print "Not valid ip"