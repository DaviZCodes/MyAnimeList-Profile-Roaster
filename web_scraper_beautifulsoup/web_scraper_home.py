# scraping MyAnimeList  

import requests 
from bs4 import BeautifulSoup

# initializing global variables
URL = "https://myanimelist.net"

def getHTML(url): 
    response = requests.get(url)

    return response.text 

home_html = getHTML(URL) 

soup = BeautifulSoup(home_html, "html.parser")

TOP_ANIME_URL = URL + "/topanime.php"

top_anime_html = getHTML(TOP_ANIME_URL)

soup2 = BeautifulSoup(top_anime_html, "html.parser")

# print(soup2.prettify())

# print(soup2.title)
headers = soup2.find("tr", class_ = "table-header")
# print(headers.find_all('td'))

# get third anime from the top 50 
row_content = soup2.find_all("tr", class_ = "ranking-list")
# print(row_content[2].find("div", class_="di-ib clearfix").find('a').text)
