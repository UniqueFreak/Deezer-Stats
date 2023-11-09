pip install deezer-python
pip install requests-oauth2client
import deezer
from pyscript import document
from requests_oauth2client import *
## https://github.com/d4vidsha/implementing-oauth-2.0-with-python/blob/main/example-oauth-2.0-with-client-credentials.py
from requests import request
import json
from datetime import datetime

# constants
SPACE = " "
APP_ID = "637461"
APP_SECRET = "some secret here"
CALLBACK_URL = "https://deezerstats12345678910.on.drv.tw/DeezerStats5/Copy%20of%20Stats.html"
EVENT_ID = "some event id from lup here"
global url 
url = "https://connect.deezer.com/oauth/auth.php?app_id=637461&redirect_uri=https://deezerstats12345678910.on.drv.tw/DeezerStats/Copy%20of%20Stats.html&perms=basic_access,email,manage_library,listening_history"
# obtain access token
def Authorise(APP_ID,APP_SECRET,CALLBACK_URL,EVENT_ID,event):
    data = {
        "grant_type": "client_credentials",
        "scope": "oapi"
    }
    global response
    response = request("POST", url, auth=(APP_ID, APP_SECRET), data=data)
    print(json.dumps(response.json(), indent=4))
    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    # make the request
    now = datetime.now().isoformat()
    url = f"https://connect.deezer.com/oauth/auth.php?{EVENT_ID}/visitors"
    headers = {
        "Authorization": token_type + SPACE + access_token, 
        "Content-Type": "application/json"
    }

    response = request("GET", url, headers=headers)
    print(response.text)
## end of git

def CodesPrint(response):
    output_div = document.querySelector("#output")
    output_div.innerText = (response.text)
client = deezer.Client()
