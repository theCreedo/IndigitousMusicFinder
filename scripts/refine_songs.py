import os

# script to remove weird empty lines and reformat files (stanza separated)
# that gensim works better with
for file in os.listdir('./../data/txt/original_song_lyrics_with_periods/'):
	with open('./../data/txt/refined_song_lyrics/' + file, 'w') as outf:
		stanza = ""
		blockCount = 0
		with open('./../data/txt/original_song_lyrics_with_periods/' + file) as inf:
			for line in inf:
				if line != '.\n':
					if line == '\n' or blockCount >= 4: # fake stanza length if no breaks
						blockCount = 0
						outf.write(stanza + '\n')
						stanza = ""
					else:
						blockCount += 1
						stanza += line