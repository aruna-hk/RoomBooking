import requests
import 
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer GWixc88seeHi6o197c2TIXHzG9N6'
}
timestamp = 
payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQxMTI4MTcwNzU2",
    "Timestamp": "20241128170756",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254708374149,
    "PartyB": 174379,
    "PhoneNumber": 254708374149,
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
}
print(payload)
response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
print(response.text.encode('utf8'))
