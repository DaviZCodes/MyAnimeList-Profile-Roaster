# attempt to scrape a user's MyAnimeList profile 

import requests 
from bs4 import BeautifulSoup

# initializing global variables
USER = "Davi_Z"
URL = f"https://myanimelist.net/profile/{USER}"

'''
Dictionary to store all the relevant user profile information 
Name, Last Online, Location, Joined, About Me, Last Anime Updates, Last Manga Updates
Anime Stats (days, mean score, watching, completed, on-hold, dropped, plan to watch, episodes) 
Manga Stats (days, mean score, reading, completed, on-hold, dropped, plan to read, chapters, volumes) 
Favorites (Anime, Manga, Characters, People, Company)
'''
user_data = {}

def getProfileHTML(url): 
    response = requests.get(url)

    return response.text 

html_document = getProfileHTML(URL) 

soup = BeautifulSoup(html_document, "html.parser")

print(soup.prettify())

# print(soup.title.string)