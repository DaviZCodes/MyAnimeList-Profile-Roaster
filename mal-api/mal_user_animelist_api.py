import requests
import os
from dotenv import load_dotenv

load_dotenv()

# getting the client_id from the env 
CLIENT_ID = os.getenv("CLIENT_ID")

# initializing global variables 
USER = "Davi_Z"

# get user profile information 

def getAnimeList(user, limit, sort="anime_title", offset=0, status=None, nsfw=True): 
    '''
    status can be reading, completed, on_hold, dropped, and plan_to_read
    important status parameters for me are plan_to_read and list_updated_at

    sort can be list_score, list_updated_at, anime_title, and anime_start_date
    '''

    url = f"https://api.myanimelist.net/v2/users/{user}/animelist?sort={sort}&limit={limit}&offset={offset}&fields=list_status&nsfw={str(nsfw).lower()}"

    if status: 
        url = url + f"&status={status}"

    response = requests.get(url, headers = {
        "X-MAL-CLIENT-ID": CLIENT_ID 
    })

    response.raise_for_status()
    animelist = response.json()
    response.close()
    data = animelist["data"]

    return data

# dictionary to store {anime_title: {completed, score, num_episodes_watched, is_rewatching, updated_at}}
top20_anime_dict = {}
bottom10_anime_dict = {} # given that the max limit is 1000, the bottom 10 might be inaccurate if the user's list exceeds 1000 anime 

# top 20 user animelist sorted by list_score 
top20_animelist = getAnimeList(USER, 20, sort="list_score")

# top 20 anime 
for i in range(len(top20_animelist)): 
    anime_title = top20_animelist[i]["node"]["title"]
    anime_list_status = top20_animelist[i]["list_status"]
    anime_score = anime_list_status["score"]

    if anime_score != 0: 
        top20_anime_dict[anime_title] = anime_list_status

# 1000 user animelist 
user_animelist_sorted_by_list_score = getAnimeList(USER, 1000, sort="list_score")

# bottom 10 anime 
temp_index = len(user_animelist_sorted_by_list_score) - 1
bottom10_scored_anime = 0
while temp_index != 0 and bottom10_scored_anime < 10:
    anime_title = user_animelist_sorted_by_list_score[temp_index]["node"]["title"]
    anime_list_status = user_animelist_sorted_by_list_score[temp_index]["list_status"]
    anime_score = anime_list_status["score"]

    if anime_score != 0: # score 0 means an unscored anime 
        bottom10_anime_dict[anime_title] = anime_list_status
        bottom10_scored_anime += 1

    temp_index -= 1

# print statements
print(top20_anime_dict) 