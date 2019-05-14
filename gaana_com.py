song_name=input("Enter the favourite song name: ").strip().split(" ")
url = "https://gaana.com/search/songs/"
for i in song_name:
    url+=i+"%20"
url = url[:(len(url)-5)]

import requests
from bs4 import BeautifulSoup
import webbrowser
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

mainDiv = soup.find('div', class_="songlist-type2")
songList = mainDiv.findAll('h3', class_="item-heading")
songLinkList = []
index = 1
print("Here are some matching results ")
for i in songList:
    print(str(index)+". "+i.find('a').get_text())
    songLink = i.find('a')["href"]
    songLinkList.append(songLink)
    index+=1
song = int(input("Choose a song : "))
print(webbrowser.open(songLinkList[song-1]))