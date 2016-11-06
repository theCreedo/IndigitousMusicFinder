import analyzetopic as anato
from gensim import corpora, models, similarities
import os
import pickle

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

pickleTopicsForMood('Joy')

def retrieveSimilarSongs(mood, query):
	songs_to_topics = pickle.load(open("songs_to_topics_" + mood + ".p", 'rb'))
	print(songs_to_topics)
	
	# corpus is a list of bags of words per song, a matrix representation that gensim understands.
	corpus = [gdict.doc2bow(song) for song in songs_to_topics.values()]
	# print(corpus)

	# generate num_topics topics for the entire song corpus
	lda = models.ldamodel.LdaModel(corpus, id2word=gdict, num_topics=50)
	corpus_lda = lda[corpus]

	# in terms of these generated topics, look at the topics most captured
	# by individual songs.
	# for idx, song_bow in enumerate(corpus):
		# print(song_bow)
		# for topic, weight in enumerate(lda[song_bow]):
		# 	print(idx, lda.show_topic(topic))
			
	# vec_bow = gdict.doc2bow(query.lower().split())
	# print(vec_bow)
	# vec_lda = lda[vec_bow]

	# index = similarities.MatrixSimilarity(corpus_lda)
	# sims = index[vec_lda]
	# print(list(enumerate(sims)))

# these are known hypernyms... an advanced method could be
# developed that substantiates the query with its hypernyms etc.

# retrieveSimilarSongs("Joy", "sin compassion")

# retrieveSimilarSongs("Joy", "")



# First step: studying the progression of happiness through the songs.
# Then: studying the topics conveyed. This may involve clustering... but
# the end goal is to just order the songs by mood, grouped by topic.
# Topic: could cluster or suggest from query.
