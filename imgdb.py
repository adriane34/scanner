#ImagetoDatabase
import json, requests, base64, io, PIL

ORI="76543"
API="ced040d6-dfbe-4b72-9ba7-a918fc6a5632"
BadgeNum="4369669"
CaseNum="09876"

#with open (r"C:\Users\kennethaytona\Desktop\rqconf.png", "rb") as f:
#    string=f.read()
#    stringimg=encode("base64")
#file_like=io.StringIO(stringimg)

#img=PIL.Image.open(file_like)
#img.show()

with open(r"C:\Users\kennethaytona\Desktop\SS\rqconf.png", "rb") as imageFile:
    strg=base64.b64encode(imageFile.read())

url="http://pi.shahrdar.com/api/APIAuthentication/Get"
payload={"API": API, "ORI": ORI}
headers={"content-type": "application/json"}

resp=requests.post(url=url, data=json.dumps(payload), headers=headers)

token=resp.text

url="http://pi.shahrdar.com/api/MobileService/Seize"
payload={"ORI": ORI, "Token": token, "Case": CaseNum, "BadgeNumber": BadgeNum,
         "currencies":[{"SerialNumber":"LH02861746A", "Denomination":"100",
                        "Date":"01/28/2014 17:28:19", "Photo":"strg"}]}
headers={"content-type": "application/json"}

pser=requests.post(url=url, data=json.dumps(payload), headers=headers)

print(pser.text)
print(pser)
