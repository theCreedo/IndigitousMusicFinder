import analyzetopic as anato
from gensim import corpora, models, similarities
import os
import pickle

def pickleTopicsForMood(mood):
	songs_to_topics = {}
	for fname in os.listdir('./songs_to_moods/' + mood):
		topics = anato.getStanzaTopics(anato.gdict, "./txt_period/song_files_with_period/mercy_mendes.txt")
		topics = [x for sublist in topics for x in sublist] # flatten list of lists
		songs_to_topics[fname] = topics
		print("analyzed", fname)
	pickle.dump(songs_to_topics, open( "songs_to_topics_" + mood + ".p", "wb"))

# pickleTopicsForMood('Joy')

def retrieveSimilarSongs(mood, query):
	songs_to_topics = pickle.load(open("songs_to_topics_" + mood + ".p", 'rb'))
	# print(songs_to_topics)
	corpus = [anato.gdict.doc2bow(song) for song in songs_to_topics.values()]
	print(corpus)
	lda = models.ldamodel.LdaModel(corpus, id2word=anato.gdict, num_topics=4)
	corpus_lda = lda[corpus]

	vec_bow = anato.gdict.doc2bow(query.lower().split())
	print(vec_bow)
	vec_lda = lda[vec_bow]
	print(vec_lda)

# these are known hypernyms... an advanced method could be
# developed that substantiates the query with its hypernyms etc.
retrieveSimilarSongs("Joy", "sin compassion")

# retrieveSimilarSongs("Joy", "")


