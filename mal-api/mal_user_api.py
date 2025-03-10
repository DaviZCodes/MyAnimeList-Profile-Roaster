import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")

# get user profile information 
url = 'https://api.myanimelist.net/v2/users/@me'

response = requests.get(url, headers = {
    "X-MAL-CLIENT-ID": CLIENT_ID 
})

response.raise_for_status()
user = response.json()
response.close()

print(user)