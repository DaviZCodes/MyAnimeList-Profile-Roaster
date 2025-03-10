import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")

# get user profile information 

def getMangaList(user, sort, limit, offset=0, status=None): 
    '''
    user is the username
    status can be reading, completed, on_hold, dropped, and plan_to_read

    important query paramters for me are plan_to_read and list_updated_at
    '''
    url = f"https://api.myanimelist.net/v2/users/{user}/mangalist?sort={sort}&limit={limit}&offset={offset}"

    if status: 
        url = url + f"&status={status}"

    response = requests.get(url, headers = {
        "X-MAL-CLIENT-ID": CLIENT_ID 
    })

    response.raise_for_status()
    mangalist = response.json()
    response.close()
    data = mangalist["data"]

    return data

# top 10 manga 
user_mangalist = getMangaList("Davi_Z", "list_score", 10)
length = len(user_mangalist) 

for i in range(length): 
    print(user_mangalist[i]["node"]["title"])