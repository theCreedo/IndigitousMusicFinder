import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import pickle

app = Flask(__name__)

@app.route('/')
def home():
	binned_songs = pickle.load(open('../topic_groupings/Anger.p', 'rb'))
	song_list = []
	# for key, val in binned_songs.items():
	# 	for song in val:
	# 		with open('../txt/' + song['title'] + '.txt') as lyric_file:
	# 			song_list.append(lyric_file.read())
	for key, val in binned_songs.items():
		for song in val:
			song_list.append((song['saying'], '../images/' + song['title'] + '.png'))
	return render_template('display_lyrics.html', songs=song_list)

