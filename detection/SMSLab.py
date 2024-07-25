# import requests

# def sendsms(mobile):
# 	url = "https://www.fast2sms.com/dev/bulkV2"
# 	payload = "sender_id=FTWSMS&message=Your vehicle has been detected.\nPlease contact the police for further details. &language=english&route=v3&numbers="+str(mobile)
# 	headers = {
# 	'authorization': "Y5Txk66xX7jcpCTqi9vcrnR7JVobaTaHec296HhuBOnKVxMowSNraGKDb9uU",
# 	'Content-Type': "application/json",
# 	'Cache-Control': "no-cache",
# 	}
# 	response = requests.request("POST", url, data=payload, headers=headers)
# 	print(response.text)

# 	return

# # 'Content-Type': "application/x-www-form-urlencoded",


import json
import requests

def sendsms(mobile):
	# url = "https://api2.juvlon.com/v4/httpSendMail"
	# data = {"ApiKey":"OTUxMDgjIyMyMDIzLTA1LTEyIDIyOjUwOjMx",
	# 		"requests":[{"subject":"Vehicle Detected",
	# 						"from":"jediba9680@appxapi.com",
	# 						"body":"Your vehicle has been detected.\nPlease contact the police for further details.",
	# 						"to":str(email)}]}
	# data_json = json.dumps(data)
	# r = requests.post(url, data=data_json)

	# print(r)

	url = "https://www.fast2sms.com/dev/bulkV2"
	payload = "sender_id=TXTIND&message=Your vehicle has been detected.\nPlease contact the police for further details. &route=q&numbers="+str(mobile)
	headers = {
	'authorization': "Y5Txk66xX7jcpCTqi9vcrnR7JVobaTaHec296HhuBOnKVxMowSNraGKDb9uU",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)