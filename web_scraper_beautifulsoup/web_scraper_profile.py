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
important information is anime and manga stats (days, mean score, and etc.) 
'''
user_statistics = soup.find("div", class_ = "user-statistics")
user_anime_basic_stats = user_statistics.find("div", class_ = "stats anime").find("div", class_ = "stat-score")

user_anime_days = float(user_anime_basic_stats.find("div", class_ = "di-tc al pl8 fs12 fw-b").text.strip().split()[1])
user_anime_mean_score = float(user_anime_basic_stats.find("span", class_ = "score-label").text.strip())

user_anime_detailed_stats = user_statistics.find("div", class_ = "mt12 ml8 mr8 clearfix")
user_anime_status_left_container_values = user_anime_detailed_stats.find_all("span", class_ = "di-ib fl-r lh10")

# User anime Watching, Completed, On-Hold, Dropped, and Plan to Watch 
user_anime_status_left_container_titles = ["Anime Watching", "Anime Completed", "Anime On-Hold", "Anime Dropped", "Anime Plan to Watch"]

for i in range(len(user_anime_status_left_container_titles)):
    user_profile_dict[user_anime_status_left_container_titles[i]] = int(user_anime_status_left_container_values[i].text.strip())

'''
More user profile anime data such as Total Entries, Rewatched, and Episodes 
''' 
user_anime_status_right_container_values = user_anime_detailed_stats.find("ul", class_ = "stats-data fl-r").find_all("span", class_ = "di-ib fl-r")

# User anime Total Entries, Rewatched, and Episodes 
user_anime_status_right_container_titles = ["Total Entries", "Rewatched", "Episodes"]

for i in range(len(user_anime_status_right_container_titles)):
    user_profile_dict[user_anime_status_right_container_titles[i]] = int(user_anime_status_right_container_values[i].text.strip().replace(",", ""))

# User anime Last Anime Updates 
user_anime_last_anime_and_manga_updates = soup.find_all("div", class_ = "statistics-updates")

# initialize a new key and value pair in the user_profile_dict of "User Last Anime and Manga" to an empty list 
user_profile_dict["User Last Anime and Manga Updates"] = []

# update the empty list with the user's last anime and manga updates 
for i in range(6): 
    # get the 6 last anime and manga updates' title, update date, and status (Completed, Watching, and etc.), episodes watched, and score 
    user_last_anime_and_manga_title = user_anime_last_anime_and_manga_updates[i].find("div", class_ = "data").find("a").text.strip()
    user_last_anime_and_manga_update_date = user_anime_last_anime_and_manga_updates[i].find("div", class_ = "data").find("div", class_ = "graph-content").text.strip()
    user_last_anime_and_manga_updates_status_and_scores = user_anime_last_anime_and_manga_updates[i].find("div", class_ = "data").find("div", class_ = "fn-grey2").get_text(separator = " ", strip = True).replace("·", "")
    formatted_user_anime_last_anime_and_manga_updates = [anime_data for anime_data in user_last_anime_and_manga_updates_status_and_scores.split(" ") if anime_data.strip()]
    
    user_last_anime_and_manga_dict = {}
    user_last_anime_and_manga_dict[user_last_anime_and_manga_title] = [user_last_anime_and_manga_update_date, formatted_user_anime_last_anime_and_manga_updates]

    user_profile_dict["User Last Anime and Manga Updates"].append(user_last_anime_and_manga_dict)

print(user_profile_dict)

# User manga Reading, Completed, On-Hold, Dropped, and Plan to Read 
user_manga_status_left_container_titles = ["Manga Reading", "Manga Completed", "Manga On-Hold", "Manga Dropped", "Manga Plan to Watch"]

# Favorites 

# Comments (First page only)