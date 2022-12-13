import socket
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
ZONE_ID = os.getenv("ZONE_ID")
EMAIL = os.getenv("EMAIL")
RECORD_ID = os.getenv("RECORD_ID")

def getIp():
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.connect(('2001:4860:4860::8888', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def updateRecord(ip):
    print("Updating IP to " + ip + " with API key " + API_KEY)
    request  = requests.put("https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/dns_records/" + RECORD_ID, headers={
        "X-Auth-Email": EMAIL,
        "X-Auth-Key": API_KEY,
        "Content-Type": "application/json"
        }, json={
            "type": "AAAA",
            "name": "vaani",
            "content": ip,
            "ttl": 1,
            "proxied": False
            })

    return request.status_code == 200

ip = getIp()

if updateRecord(ip):
    print("IP updated successfully")
else:
    print("IP update failed")
