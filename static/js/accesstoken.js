let unirest = require('unirest');
let req = unirest('GET', 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials')
.headers({ 'Authorization': 'Basic TE9kUXlSQlVYWHNDUWVSZ2hVQUlXM3pHcDdlYmFHcUpGaUFpNmFxeUpHcTRwdVhPOkkxbWZyaXRDOUpVa2ZTbjJYcEFWaURTU0tEelM5eVdjVTlxd3RmdktRQ1JIaXVaUmd4ckE1VzF1UVNpWUNwTGI=' })
.send()
.end(res => {
	if (res.error) throw new Error(res.error);
	console.log(res.raw_body);
});
