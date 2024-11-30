import requests
from accesstoken import accesstoken
import base64
import datetime

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + accesstoken()['access_token']
}

print(headers)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(timestamp)
payload = {
    "BusinessShortCode": 174379,
    "Password": base64.b64encode(("174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + timestamp).encode()).decode(),
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254714261231,
    "PartyB": 174379,
    "CallBackURL": "https://google.com",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
}
print(payload)
response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)

print(response.text.encode('utf8'))
