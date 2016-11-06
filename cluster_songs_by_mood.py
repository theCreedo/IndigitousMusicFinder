import analyzetopic as anato
from gensim import corpora, models, similarities
import os
import pickle
from collections import defaultdict

gdict = anato.getgdict()

def pickleTopicsForMood(mood):
	songs_to_topics = {}
	for fname in os.listdir('./songs_to_moods/' + mood):
		path = './txt_period/song_files_with_period/' + fname
		# topics = anato.getStanzaTopics(gdict, path)
		topics = anato.getSongTopics(gdict, path)
		topics = [x for sublist in topics for x in sublist] # flatten list of lists
		songs_to_topics[fname] = topics
		print("analyzed", fname, "got", topics)
	pickle.dump(songs_to_topics, open( "songs_to_topics_" + mood + ".p", "wb"))

def retrieveSimilarSongs(mood):
	songs_to_topics = pickle.load(open("songs_to_topics_" + mood + ".p", 'rb'))
	
	# corpus is a list of bags of words per song, a matrix representation that gensim understands.
	corpus = [gdict.doc2bow(song) for song in songs_to_topics.values()]
	titles = [title for title in songs_to_topics.keys()]
	# print(corpus)

	# generate num_topics topics for the entire song corpus
	lda = models.ldamodel.LdaModel(corpus, id2word=gdict, num_topics=50)
	corpus_lda = lda[corpus]

	binned_songs = defaultdict(list)

	# in terms of these generated topics, look at the topics most captured
	# by individual songs.
	for idx, song_bow in enumerate(corpus):
		top_topic = sorted(enumerate(lda[song_bow]), reverse=True, key=lambda x: x[1])[0]
		
		with open('./songs_to_moods/' + mood + '/' + titles[idx]) as metafile:
			meta_list = metafile.read().split('\n')
			meta = {}
			meta['title'] = meta_list[0]
			meta['score'] = float(meta_list[2])
			meta['saying'] = meta_list[8]

			binned_songs[top_topic[0]].append(meta)

	# We've grouped songs according to their top-ranked topic.
	# Now, display the topics and their best-matched songs.

	for key, val in binned_songs.items():
		print("Topic", lda.show_topic(key))
		sorted_songs = sorted(val, reverse=True, key=lambda x: x['score'])
		for song in sorted_songs:
			print("\t", song['score'], song['title'], '\n\t\t', song['saying'])

# these are known hypernyms... an advanced method could be
# developed that substantiates the query with its hypernyms etc.

pickleTopicsForMood('Anger')
retrieveSimilarSongs("Anger")



# First step: studying the progression of happiness through the songs.
# Then: studying the topics conveyed. This may involve clustering... but
# the end goal is to just order the songs by mood, grouped by topic.
# Topic: could cluster or suggest from query.
