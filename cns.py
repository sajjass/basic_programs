import requests

url = "https://upmk4gw0me.execute-api.ap-southeast-1.amazonaws.com/TEST/v1/application"
input_file = "/Users/sajjas/CNS/repos/com.mobileiron.performance/jmeter/data/cns/cns_v1_requests_copy.json"

with open(input_file, 'r') as rf:
    payload_data = rf.readlines()

for payload in payload_data:
    print "Request - \n", payload
    headers = {
        'content-type': "application/json",
        'authorization': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2OGY3ZTE5MS0xMTFjLTQyZmItOGEzZC1hY2EyMmI4NWNiMzgiLCJpc3MiOiJNb2JpbGVpcm9uIiwiaWF0IjoxNTIyNzM4MzI0fQ.AmTgh8Yd_QAsD-X_vcRqowEjtkJdt4IvK-PBmEcPl_U",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print "\n Response - \n", response.text