entries_count = input("Enter devices count : ")
input_text = {"organizationId": "0c039a47-5ade-4e70-9f07-a2be91aa8add",
              "name": "com.mobileiron.ios.emailplus.enterprise",
              "deviceToken": "1000",
              "platformType":"APNS_SANDBOX",
              "serialNumber":"1000",
              "interval":"300",
              "identifierForVendor":"identifier"
              }
with open("/Users/sajjas/Desktop/1000k_cns_devices_entries.txt", "w") as wf:
    for i in range(0, entries_count):
        input_text["deviceToken"] = int(input_text["deviceToken"]) + i
        input_text["serialNumber"] = int(input_text["serialNumber"]) + i

        wf.write(str(input_text)+"\n")
        print i

with open("/Users/sajjas/Desktop/cns_entries.txt", "r") as rf:
    print rf.read()