import requests,pprint,webbrowser
from bs4 import BeautifulSoup

def song_name(url):
	link=requests.get(url)
	parser=BeautifulSoup(link.text,"html.parser")

	div=parser.find("div",class_="s_c")
	sub_div=div.find_all("div",class_="playlist_thumb_det")
	position=0
	list_=[]
	counter=0
	for i in sub_div:
		dic={}
		urls=i.find("a").get("href")
		list_.append(urls)
		all_data=i.find_all("a")
		artist=[artist.text for artist in all_data]
		song=all_data[0]
		counter+=1
		artist.remove(artist[0])
		print(counter,song.text,artist)
	user=int(input("Enter the song name:"))
	a=webbrowser.open_new_tab(list_[user-1])
url="https://gaana.com/playlist/gaana-dj-bollywood-top-50-1"
song_name(url)