#API
import json,requests

#Distribution
#API='f083a584-420d-4e8b-b3da-3e6a970de6a5'
#ORI='123456'
API=input("Please input a valid API: ")
ORI=input("Please input a valid ORI: ")

url='http://pi.shahrdar.com/api/APIAuthentication/Get'
payload={'API': API, 'ORI': ORI}
headers={'content-type': 'application/json'}

resp=requests.post(url=url, data=json.dumps(payload), headers=headers)

print(resp.url)
print(resp.text)
print(resp.status_code)
print(resp.headers)

#Adds currency
url='http:/pi.shahrdar.com/api/MobileService/Seize'
payload={'Currencies':[{'SerialNumber': SerialNumber, 'Denomination': Denomination},
                       {'SerialNumber': SerialNumber, 'Denomination': Denomination}],
         'BadgeNumber': BadgeNumber, 'Case': Case, 'Token': Token}
headers={'content-type': 'application/json'}

respo=requests.post(url=url, data=json.dumps(payload), header=headers)

print(respo.url)
print(respo.text)
print(respo.status_code)
print(respo.headers)

#Checks currency
url='http:/pi.shahrdar.com/api/MobileService/Query'
payload={'Currencies':[{'SerialNumber': SerialNumber, 'Denomination': Denomination},
                       {'SerialNumber': SerialNumber, 'Denomination': Denomination}],'Token': Token}
headers={'content-type': 'application/json'}

res=requests.get(url=url, data=json.dumps(payload), header=headers)

print(res.url)
print(res.text)
print(res.status_code)
print(res.headers)

#Deletes currency
url='http:/pi.shahrdar.com/api/MobileService/Delete'
payload={'Currencies':[{'SerialNumber': SerialNumber, 'Denomination': Denomination},
                       {'SerialNumber': SerialNumber, 'Denomination': Denomination}],'Token': Token}
headers={'content-type': 'application/json'}

respon=requests.get(url=url, data=json.dumps(payload), header=headers)

print(respon.url)
print(respon.text)
print(respon.status_code)
print(respon.headers)

#BadgeNumber locator
BadgeNummber=input("PLease input a valid Badge Number: ")
Token=resp.text

url='http:/pi.shahrdar.com/api/APIAuthentication/BadgeCheck'
payload={'BadgeNumber': BadgeNumber, 'Token': Token}
headers={'content-type': 'application/json'}

respons=requests.get(url=url, data=json.dumps(payload), header=headers)

print(respons.url)
print(respons.text)
print(respons.status_code)
print(respons.headers)

#Checks case number
Case=input("Please input a valid case number: ")
Token=resp.text

url='http:/pi.shahrdar.com/api/APIAuthentication/CaseCheck'
payload={'Case': Case, 'Token': Token}
headers={'content-type': 'application/json'}

response=requests.get(url=url, data=json.dumps(payload), header=headers)

print(response.url)
print(response.text)
print(response.status_code)
print(response.headers)

#API and Agency
ORI=input("Please input a valid ORI: ")
API=input("Please input a valid API: ")

url='http://pi.shahrdar.com/api/APIAuthentication/AgencyCheck'
payload={'ORI': ORI, 'API': API}
headers={'content-type': 'application/json'}

responses=requests.post(url=url, data=json.dumps(payload), headers=headers)

print(responses.url)
print(responses.text)
print(responses.status_code)
print(responses.headers)

#API and Agent
url='http://pi.shahrdar.com/api/APIAuthentication/AgentCheck'
payload={'BadgeNumber': BadgeNumber, 'API': API}
headers={'content-type': 'application/json'}

respond=requests.post(url=url, data=json.dumps(payload), headers=headers)

print(respond.url)
print(respond.text)
print(respond.status_code)
print(respond.headers)
