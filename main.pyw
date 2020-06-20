import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import *



window=Tk()
window.title("Lyric Word Counter")
window.geometry("700x300")


pythonlogo_path = "pylogo.png"

def get_song_name():
	band = enter_artist_value.get()
	band.lower()
	band.replace(" ", "-")
	song = enter_songtitle_value.get()
	song.lower()
	song.replace(" ","-")
	find_song(band, song)


def find_song(artist, song_name):
	t = requests.get("https://www.lyricfinder.org/lyrics/677387/%s?track=%s" % (artist, song_name), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
	if t.status_code == 404:
		print("Error: 404 error, retype the song name!")
		raise "Error, try running the program again and typing another band/song name in"
	c = t.content
	content = bs(c, "html.parser")
	all_lyrics = content.find("div", {"class":"col-lg-6"})
	unwanted = all_lyrics.find("p")
	unwanted.extract()
	text_lyrics = all_lyrics.text
#	print(all_lyrics)
	
	lyric_words = text_lyrics.split()
	
	word_counts = Counter(lyric_words)
	print(word_counts)
	prominent_words = dict(Counter(word_counts).most_common(5))

	# objects = word_counts.keys()
	# count = word_counts.values()
	
	objects = prominent_words.keys()
	count = prominent_words.values()

	plt.bar(objects, count, align='center', alpha=0.5)
	plt.ylabel('Times Used')

	plt.title("Word usage in %s, by %s." % (song_name, artist))

	plt.show()
	# print(lyric_words)
	

	


#the-suburbs


#TEMPORARY
e2=Label(window,text="Artist:")
e2.grid(row=3,column=0)
e2.configure(font=("Courier",30))

enter_artist_value=StringVar()
enter_artist=Entry(window,textvariable=enter_artist_value)
enter_artist.grid(row=4,column=0)
enter_artist.configure(font=("Ariel",20))


e1=Label(window,text="Song Name:")
e1.grid(row=6,column=0)
e1.configure(font=("Courier",30))

enter_songtitle_value=StringVar()
enter_songtitle=Entry(window,textvariable=enter_songtitle_value)
enter_songtitle.grid(row=7,column=0)
enter_songtitle.configure(font=("Ariel",20))


b1=Button(window,text="Go!",command=get_song_name)
b1.grid(row=9,column=0)

window.mainloop()