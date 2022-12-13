import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
ZONE_ID = os.getenv("ZONE_ID")
EMAIL = os.getenv("EMAIL")
RECORD_ID = os.getenv("RECORD_ID")

def listRecords():
    request = requests.get("https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/dns_records", headers={
        "X-Auth-Email": EMAIL, 
        "X-Auth-Key": API_KEY, 
        "Content-Type": "application/json"
    })
    with open('record-dump.json', 'w') as outfile:
        outfile.write(request.text)

listRecords()