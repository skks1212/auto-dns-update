import socket
import os
from dotenv import load_dotenv
import requests
import time
import socket
import paramiko

load_dotenv()

API_KEY = os.getenv("API_KEY")
ZONE_ID = os.getenv("ZONE_ID")
EMAIL = os.getenv("EMAIL")
RECORD_ID = os.getenv("RECORD_ID")
URL = os.getenv("URL")
PORT = os.getenv("PORT")

def getIp():
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.connect(('2001:4860:4860::8888', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def updateRecord(ip):
    print("Updating IP to " + ip)
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

def check_ssh(url, port=22, timeout=5):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(url, port, timeout=timeout)
        ssh.close()
        return True
    except (paramiko.AuthenticationException, paramiko.SSHException, socket.timeout):
        return False

trys = 3

def run(trys):
    ip = getIp()
    if updateRecord(ip):
        print("IP updated successfully")
    else:
        print("IP update failed")
    
    time.sleep(5)

    # check if we can access ssh vaani.shivankacker.me
    
    if (check_ssh(URL)):
        print("SSH is open")
    else:
        if (trys > 0):
            print("SSH is closed. Retrying in 10 seconds...")
            time.sleep(10)
            run(trys - 1)
        else:
            print("SSH is closed. Max retries reached. Exiting...")

run(trys)

