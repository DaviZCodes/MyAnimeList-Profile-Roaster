# scraping a user's MyAnimeList profile 

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
user_profile_dict = {}

def getProfileHTML(url): 
    response = requests.get(url)

    return response.text 

html_document = getProfileHTML(URL) 

soup = BeautifulSoup(html_document, "html.parser")

# print(soup.prettify())

'''
getting the user profile information such as: 
last online, gender, birthday, location, joined 
'''

user_profile = soup.find_all("div", class_ = "user-profile")

# user profile 
user_status = user_profile[0].find("ul", class_ = "user-status")
user_clearfix_all = user_status.find_all("li", class_ = "clearfix")

for li in user_clearfix_all:
    user_status_title = li.find("span", class_ = "user-status-title").text.strip()
    user_status_data = li.find("span", class_ = "user-status-data").text.strip()
    user_profile_dict[user_status_title] = user_status_data 

'''
forum posts, reviews, recommendations, interest stacks, blog posts, and clubs 
'''
user_status_all = user_profile[0].find_all("ul", class_ = "user-status")

for li in user_status_all[2].find_all("li", class_ = "link"): 
    user_status_title = li.find("span", class_ = "user-status-title").text.strip()
    user_status_data = li.find("span", class_ = "user-status-data").text.strip() 

    user_profile_dict[user_status_title] = user_status_data 

# friends 
user_profile_extra = user_profile[0].find_all("a", class_ = "all-link")
user_num_friends = int(next((link for link in user_profile_extra if "friends" in link["href"]), None).text.strip().split()[1].strip("()"))

user_profile_dict["Number Of Friends"] = user_num_friends

# profile about me 
user_profile_about = soup.find("div", class_ = "user-profile-about").text.strip()

user_profile_dict["About Me"] = user_profile_about

'''
user statistics 
important information is anime and manga stats (days, mean score, and etc.) and the latest anime and manga updates 
'''
user_statistics = soup.find("div", class_ = "user-statistics")
user_anime_basic_stats = user_statistics.find("div", class_ = "stats anime").find("div", class_ = "stat-score")

user_anime_days = float(user_anime_basic_stats.find("div", class_ = "di-tc al pl8 fs12 fw-b").text.strip().split()[1])
user_anime_mean_score = float(user_anime_basic_stats.find("span", class_ = "score-label").text.strip())

user_anime_detailed_stats = user_statistics.find("div", class_ = "mt12 ml8 mr8 clearfix").text.strip()
print(user_anime_detailed_stats)