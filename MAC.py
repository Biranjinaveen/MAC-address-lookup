import json

import requests


mac_address = input("Enter MAC Address : ")   							      		  #Get the MAC Address From  the USER
# 44:38:39:ff:ef:57
if mac_address :													#check mac address entered or not
	url = "https://api.macaddress.io/v1?apiKey=at_zYaa4jVII0UL3cLVW0OEpYv5vOBDJ&output=json&search=" + mac_address    #URL API End point to search MAC Address
else  :
	print("MAC Address Should not be empty")
	quit()													# Stop the script if not entered
headers = {}
resp = requests.get(url, headers=headers)								  #CALL API and store response in resp variable
# print (resp.content.vendorDetails.companyName)
data = json.loads(resp.content)											  # Convert JSON object to Python LIST
print("The Company Name For The Enter MAC Address Is : " + data['vendorDetails']['companyName'])		  # Print the company name 
# print (resp)
