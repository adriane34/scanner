import json, requests
import time
import datetime
import base64

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%m/%d/%Y %H:%M:%S')
ORI = "76543"
get_token_url = "http://pi.shahrdar.com/api/APIAuthentication/Get"
query_currency_url = "http://pi.shahrdar.com/api/MobileService/Query"
scan_currency_url = "http://pi.shahrdar.com/api/MobileService/Seize"
rem_currency_url = "http://pi.shahrdar.com/api/MobileService/Delete"

token_payload = {"API":"ced040d6-dfbe-4b72-9ba7-a918fc6a5632","ORI":ORI}


headers = {"content-type": "application/json"}

def get_Token( API_ORI ): # Gets token from server
        resp = requests.post(url=get_token_url, data=json.dumps(API_ORI), headers=headers)
        token = json.loads(resp.text)
        return token;

def get_currency_query( query_currency_payload ): # querys db for serial and denomination of currency
        currency_query_result = requests.post(url=query_currency_url,data=json.dumps(query_currency_payload), headers=headers)
        _currency_query_result = json.loads(currency_query_result.text)
        return _currency_query_result;

# Adds a list of currencies to the db
def scan_currency( scan_currency_payload ):
        scan_currency_results = requests.post(url=scan_currency_url,data=json.dumps(scan_currency_payload), headers=headers)
        _scan_currency_result = json.loads(scan_currency_results.text)
        return _scan_currency_result;

# Deletes currencies to the db
def rem_currency( rem_currency_payload):
        rem_currency_results = requests.post(url=rem_currency_url,data=json.dumps(rem_currency_payload), headers=headers)
        _rem_currency_result = json.loads(rem_currency_results.text)
        return _rem_currency_result;
        
_token = get_Token(token_payload)

with open(r"C:\Users\kennethaytona\Desktop\SS\rqconf.png", "rb") as imageFile:
    strg=base64.b64encode(imageFile.read())

while True:
        selection = int(input("Select 1 - query | 2 - scan | 3 - remove : "))
        if selection == 0:
                break
        if selection == 1:
                _query_currency_payload = {"currencies":[{"SerialNumber":"LH02861746B","Denomination":"20"}],"token":_token}
                print (get_currency_query( _query_currency_payload))

        if selection == 2:
                _case = input("Enter Case Number: ")
                badgeNumber = input("Enter Badge Number: ")
                _scan_currency_payload = { "ORI":ORI, "Token":_token, "Case":_case,"BadgeNumber":badgeNumber, "currencies":[{"SerialNumber":"LH023456765F","Denomination":"100","Date":st,"Photo":"strg"}]}
                print (scan_currency( _scan_currency_payload ))

        if selection == 3:
                SerialNumber=input("Please enter the serial number: ")
                Denomination=input("Please enter the denomination: ")
                _remove_currency_payload = { "currencies":[{"SerialNumber":SerialNumber,"Denomination":Denomination}],"token":_token}
                print (rem_currency(_remove_currency_payload))
