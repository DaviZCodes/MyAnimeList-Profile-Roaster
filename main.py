import json 

from mal_api.mal_user_animelist_api import * 
from mal_api.mal_user_mangalist import *  

from web_scraper_beautifulsoup.web_scraper_profile import getUserProfile 

USER = "Xinil"
URL = f"https://myanimelist.net/profile/{USER}"

user_profile = getUserProfile(URL) 
user_animelist = getAnimeList(USER)
user_top20_animelist = getUserTop20AnimeList(USER)
user_bottom20_animelist = getUserBottom20AnimeList(USER) 
user_top20_mangalist = getUserTop20MangaList(USER) 
user_bottom20_mangalist = getUserBottom20MangaList(USER) 

# json data 
user_output = {
    "user" : USER,
    "user_url" : URL, 
    "user_profile": user_profile,
    "user_top20_animelist": user_top20_animelist,
    "user_bottom20_animelist": user_bottom20_animelist, 
    "user_top20_mangalist": user_top20_mangalist,
    "user_bottom20_mangalist": user_bottom20_mangalist
}

# put all of the information to a .txt file 
output_file = "user_output.txt" 

with open(output_file, "w") as file: 
    json.dump(user_output, file, indent=3)