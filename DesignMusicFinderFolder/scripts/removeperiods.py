import os

# script to remove weird empty lines and reformat files (stanza separated)
# that gensim works better with
for file in os.listdir('./txt_period/song_files_with_period/'):
	with open('./temp/' + file, 'w') as outf:
		stanza = ""
		blockCount = 0
		with open('./txt_period/song_files_with_period/' + file) as inf:
			for line in inf:
				if line != '.\n':
					if line == '\n' or blockCount >= 4: # fake stanza length if no breaks
						blockCount = 0
						outf.write(stanza + '\n')
						stanza = ""
					else:
						blockCount += 1
						stanza += line