import requests

def accesstoken():
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic TE9kUXlSQlVYWHNDUWVSZ2hVQUlXM3pHcDdlYmFHcUpGaUFpNmFxeUpHcTRwdVhPOkkxbWZyaXRDOUpVa2ZTbjJYcEFWaURTU0tEelM5eVdjVTlxd3RmdktRQ1JIaXVaUmd4ckE1VzF1UVNpWUNwTGI=' })
    return response.json()
