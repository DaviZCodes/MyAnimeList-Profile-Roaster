import time 
import json 
from flask import Flask, jsonify
from flask_cors import CORS

from mal_api.mal_user_animelist_api import * 
from mal_api.mal_user_mangalist import *  

from web_scraper_beautifulsoup.web_scraper_profile import getUserProfile 

from openai_api.openai_api import generateRoast

app = Flask(__name__)
CORS(app)

def fetchMalProfile(username): 
    url = f"https://myanimelist.net/profile/{username}"

    user_profile = getUserProfile(url) 
    user_animelist = getAnimeList(username)
    user_top20_animelist = getUserTop20AnimeList(username)
    user_bottom20_animelist = getUserBottom20AnimeList(username) 
    user_top20_mangalist = getUserTop20MangaList(username) 
    user_bottom20_mangalist = getUserBottom20MangaList(username) 

    # json data 
    user_output = {
        "user" : username,
        "user_url" : url, 
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
    
    return user_output

def getRoast(username):
    mal_profile = fetchMalProfile(username)

    time.sleep(3)

    roast = generateRoast()

    return roast

@app.route("/roast/<username>", methods=["GET"])
def roastProfile(username): 
    roast = getRoast(username) 

    return jsonify(roast) 

if __name__ == "__main__": 
    app.run(debug=True)