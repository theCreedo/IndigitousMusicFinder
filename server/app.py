import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import pickle
from collections import deque
import re

app = Flask(__name__)

@app.route('/')
def home():
	binned_songs = pickle.load(open('../topic_groupings/Joy.p', 'rb'))

	# create a regex string out of an external file with profanity words
	censored_regex = '|'.join(open('censored_profanity.txt').read().split('\n'))

	# list of lyrics snippets from all songs.
	saying_context_list = []
	for key, val in binned_songs.items():
		for song in sorted(val, reverse=False, key=lambda x: x['score']):

			# get the lines surrounding the saying
			with open('../txt/' + song['title'] + '.txt') as lyric_file:
				lyrics_lines = lyric_file.read().split('\n')

				five_lines = deque(lyrics_lines[:5])
				for line in lyrics_lines[5:]:
					if not line or line == '\n':
						continue
					if song['saying'] in five_lines[2]:
						break

					# replace all occurrences of profanity
					line = re.sub(censored_regex, '*****', line)
					
					five_lines.popleft()
					five_lines.append(line)

				saying_context_list.append((five_lines, url_for('static', filename=song['title'] + '.png')))

		break # break here, meaning we only display the songs for the first topic.

	return render_template('display_lyrics.html', songs=saying_context_list)

