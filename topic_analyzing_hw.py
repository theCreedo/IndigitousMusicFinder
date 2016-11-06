###########
# Solution, homework 2
#
# Name and EID: Joshua Pham, jhp2352
# Option chosen: B
###

# Utility functions for all tasks

import nltk
import string
import gensim
import itertools
from collections import defaultdict, Counter
import os

isInitialDictionaryDone = True

def listchunks(mylist, n):
	if n > 0:
		return [mylist[i:i + n] for i in range(0, len(mylist), n)]
	else:
		return None

# Remove stopwords from a document, returning the document's contents chunked up by 100 words.
def preprocess(doc):
	stopword_filename = "./stopwords-augmented.txt"
	f = open(stopword_filename)
	stopwords = set(f.read().split())
	f.close()
	stopwords.add('--')
	stopwords.add('``')
	stopwords.add("''")
	for punct in string.punctuation:
		stopwords.add(punct)
	
	chunked_doc = []
	for chunk in listchunks([w.lower() for w in doc if w.lower() not in stopwords], 100):
		chunked_doc.append(chunk)
	return chunked_doc

# Original function taken from website with some additional functionality:
# - gathers information on the top topics by using a Counter that is initialized in the caller.
# - Also passes topic words to a structure that is defined in the caller.
def make_and_show_lda_model(texts, gdict, numtopics, sotu_topic_frequencies, topics, show_docs = True):
	# represent the corpus in sparse matrix format, bag-of-words
	corpus = [gdict.doc2bow(text) for text in texts]
	# now we make an LDA object.
	# in case we have a larger text collection (such as the Brown corpus),
	# make sure to set "passes" to a reasonably high number in order not to have all topics
	# come out equal. 20 seems to work.
	lda_obj = gensim.models.ldamodel.LdaModel( \
		corpus, id2word=gdict, num_topics=numtopics, passes = 20)

	# how do our texts look: how important is each topic there?
	if show_docs:
		print("Showing how important each topic is for each document")
		lda_corpus = lda_obj[corpus]
		for docindex, doc in enumerate(lda_corpus):
			print( "Chunk excerpt ", docindex, ":", end = " ")
			for word in texts[docindex][:20]: print( word, end = " ")
			print("\n")
			for topic, weight in doc:
				topic_words = [x[0] for x in sorted(lda_obj.show_topic(topic), key=lambda x : x[1])]
				topics[topic] = topic_words
				print( "Topic", topic,", which has keywords: ", topic_words, \
					"\nWith weight of", round(weight, 2))
				sotu_topic_frequencies[topic] += 1
			print("\n")

	# returns which topics were most frequently shown. Used for final printing of
	# most frequent documents.

def saveInitialDictionary(originals_words):
	gdict = gensim.corpora.Dictionary(originals_words)
	gdict.save('./gdict_originals_words.dict')
	return gdict

def sotuForDates(start, end, directory):
	selection = []
	years = list(range(start, end + 1))
	actual_years = []
	for year in years:
		if year in directory:
			selection.append(directory[year])
			actual_years.append(year)
		print()
	return actual_years, selection

fileids_all = nltk.corpus.inaugural.fileids()
originals_words = {}
for fileid in fileids_all:
	originals_words[int(fileid.split('-')[0])] = \
		preprocess(nltk.corpus.inaugural.words(fileid))

# gdict = gensim.corpora.Dictionary.load('./gdict_originals_words.dict')

#### TASK 1
gdict = saveInitialDictionary((itertools.chain.from_iterable(originals_words.values())))
sotu_topics_frequencies = Counter()
topics = {}
for sotu in originals_words.values():
	make_and_show_lda_model(sotu, gdict, 25, sotu_topics_frequencies, topics, show_docs = True)

# Number of topics: 25
# Topic 0: ['management', 'relations', 'allies', 'liberty', 'citizens', 'people', 'foreign', 'own', 'confederacy', 'spirit']
# Topic 1: ['individual', 'tasks', 'grim', 'interdependent', 'life', 'government', 'abnormal', 'war', 'prices', 'charge'] 
# Topic 2: ['steps', 'industry', 'faith', 'freedom', 'government', 'confidence', 'public', 'citizens', 'fellow', 'own'] 
# Topic 3: ['revolutionary', 'united', 'democracy', 'found', 'increase', 'power', 'welfare', 'convention', 'powers', 'government'] 
# Topic 4: ['duty', 'military', 'support', 'sacred', 'political', 'liberty', 'peace', 'preservation', 'government', 'union'] 
# Topic 5: ['people', 'united', 'extended', 'system', 'constitution', 'national', 'public', 'powers', 'union', 'government'] 
# Topic 6: ['assigned', 'progression', 'sense', 'bitter', 'century', 'personal', 'unmindful', 'administration', 'manifestation', 'republic'] 
# Topic 7: ['boldly', 'act', 'history', 'ashamed', 'level', 'help', 'government', 'world', 'role', 'america'] 
# Topic 8: ['duty', 'appropriate', 'power', 'constitution', 'themselves', 'subject', 'opinion', 'practical', 'individual', 'free'] 
# Topic 9: ['expressly', 'congress', 'constitutional', 'questions', 'majority', 'minority', 'secede', 'government', 'people', 'constitution'] 
# Topic 10: ['earth', 'sea', 'commerce', 'physical', 'condition', 'hand', 'equal', 'nations', 'extended', 'rights'] 
# Topic 11: ['called', 'price', 'special', 'america', 'earth', 'believe', 'federal', 'people', 'americans', 'government']
# Topic 12: ['nor', 'power', 'generation', 'ideas', 'time', 'free', 'people', 'door', 'freedom', 'world']
# Topic 13: ['census', 'communities', 'wealth', 'mutual', 'courage', 'population', 'power', 'body', 'respect', 'people']
# Topic 14: ['domestic', 'near', 'development', 'war', 'public', 'protective', 'ships', 'union', 'laws', 'naval']
# Topic 15: ['government', 'economy', 'birthright', 'challenge', 'citizens', 'americans', 'world', 'nation', 'history', 'freedom']
# Topic 16: ['assume', 'indicate', 'furnishes', 'citizens', 'government', 'justification', 'taxing', 'support', 'american', 'people'] 
# Topic 17: ['debt', 'public', 'surplus', 'pay', 'policy', 'peace', 'taxation', 'loans', 'government', 'revenue'] 
# Topic 18: ['indispensably', 'lessons', 'confidence', 'share', 'avoid', 'degree', 'pecuniary', 'opportunities', 'government', 'public'] 
# Topic 19: ['war', 'negotiate', 'unite', 'absolute', 'instead', 'explore', 'control', 'fear', 'nations', 'power'] 
# Topic 20: ['expression', 'popular', 'understanding', 'america', 'service', 'government', 'common', 'god', 'world', 'responsibility'] 
# Topic 21: ['permanent', 'late', 'united', 'secures', 'spain', 'parties', 'importance', 'gulf', 'mississippi', 'limits']
# Topic 22: ['prudence', 'arms', 'introduction', 'discipline', 'experience', 'encouragement', 'national', 'government', 'importance', 'military']
# Topic 23: ['people', 'time', 'institutions', 'citizens', 'fellow', 'possess', 'war', 'individual', 'country', 'result']
# Topic 24: ['privileges', 'measures', 'drawn', 'confidence', 'opposition', 'nation', 'government', 'persons', 'citizens', 'citizen']

# Discussion:
# The resulting topics seem to reflect the concerns of a starting president. "Free" seems to be a common word used to describe
# topics, as do words that describe character, names for collections of people, and areas of concern – sea, allies, taxation, and union.
# However, they are separate. For example, topic 13 describes the responsibility of a collective populous, whereas topic 17
# describes earning income for the country. Because SOTU addresses are centered on different topics depending on the time period,
# the topics diverge enough to be distinct.
# The number of topics at 25 ended up being a good threshhold to separate topics.

# #### TASK 2
for idx, (years, sotu_timeslice) in enumerate([sotuForDates(1945, 1963, originals_words), \
							sotuForDates(1964, 1988, originals_words), \
							sotuForDates(1989, 2006, originals_words)]):
	gdict = saveInitialDictionary(list(itertools.chain.from_iterable(sotu_timeslice)))
	print("*******  TIME PERIOD ", idx, "  **********")
	
	# initialize to pass into make_and_show_lda_model
	sotu_topic_frequencies = Counter()
	topics = {}
	
	for year, sotu in zip(years, sotu_timeslice):
		print('SOTU from ', year)
		gdict = saveInitialDictionary(sotu)
		make_and_show_lda_model(sotu, gdict, 25, sotu_topic_frequencies, topics, show_docs = True)

	print("*******")
	for topic, count in sotu_topic_frequencies.most_common()[:4]:
		print("Topic", topic, " with count of ", count, "\n\tkeywords:", topics[topic])

## COMMENTS ON TASK 2
# Cutoff points: [1945, 1963], [1964, 1988], [1989, 2006]
# Number of topics used: 25
# Top topics for [1945, 1963]:
# (the remaining topics here are truncated for brevity; available upon request)
	# Topic 3  with count of  4 
	# 	keywords: ['allies', 'hardship', 'foe', 'past', 'little', 'meet', 'supporting', 'free', 'help', 'pledge']
	# Topic 9  with count of  4 
	# 	keywords: ['beyond', 'doubt', 'peace', 'instruments', 'destruction', 'offer', 'hope', 'free', 'nations', 'pledge']
	# Topic 14  with count of  4 
	# 	keywords: ['peace', 'unite', 'negotiate', 'absolute', 'explore', 'control', 'instead', 'fear', 'power', 'nations']
	# Topic 1  with count of  3 
	# 	keywords: ['vice', 'forms', 'rights', 'god', 'nation', 'committed', 'forebears', 'century', 'human', 'president']
# Top topics for [1964, 1988]:
	# Topic 8  with count of  6 
	# 	keywords: ['liberty', 'worthy', 'ourselves', 'americans', 'happiness', 'ready', 'progress', '."', 'act', 'government']
	# Topic 6  with count of  5 
	# 	keywords: ['yes', 'national', 'citizens', 'americans', 'economy', 'dignity', 'opportunity', 'people', 'american', 'government']
	# Topic 11  with count of  5 
	# 	keywords: ['monumental', 'history', 'front', 'memorial', 'america', 'god', 'day', 'beyond', 'row', 'lincoln']
	# Topic 16  with count of  5 
	# 	keywords: ['blow', 'people', 'destroy', 'security', 'weapons', 'world', 'human', 'nuclear', 'peace', 'freedom']
# Top topics for [1989, 2006]:
	# Topic 15  with count of  5 
	# 	keywords: ['time', 'permanent', 'free', 'justice', 'hope', 'human', 'history', 'america', 'freedom', 'liberty']
	# Topic 22  with count of  5 
	# 	keywords: ['free', 'enemies', 'honor', 'day', 'america', 'seen', 'president', 'fire', 'freedom', '¡']
	# Topic 7  with count of  4 
	# 	keywords: ['people', 'human', 'choice', 'influence', 'chosen', 'nation', '¡¦', 'freedom', 'america', 'own']
	# Topic 23  with count of  4 
	# 	keywords: ['people', 'self', 'own', 'act', 'ownership', 'character', 'americans', 'freedom', '¡', 'society']
# Discussion of results:
# 	I chose the oldest slice to represent addresses about WW2 and its recovery. To an
# 	extent, the words, such as "peace", "negotiate", "instruments", "destruction", etc...
# 	reflect a nation in recovery from wartime.
# 	I chose the middle slice to look at addresses from the Cold War and the rise of the Civil Rights movement.
# 	I found the words "security", "nuclear", and "blow", among others, to accurately represent Cold War sentiments, whereas
# 	words like "liberty", "yes", and "opportunity" to correspond to movements toward securing Civil Rights.
# 	Finally, the most recent slice reflects optimism and individualism in an age of growing connectedness. However, Topic 22
# 	best represents presidential response to 9/11, with words like "enemy", "honor", and "fire". Perhaps since it is most
# 	recent, the topics seem very distinct and well-defined, spanning topics from terrorism to individualism.

#### Task 3

article_topics_frequencies = Counter()
topics = {}

docs_for_gdict = []
for filename in os.listdir(os.path.relpath('opinions')):
	filepath = os.path.join(os.path.relpath('opinions'), filename)
	print(filepath)
	f = open(filepath)
	cleaned_article = preprocess(f.read().split())
	docs_for_gdict.append(cleaned_article)

gdict = saveInitialDictionary(list(itertools.chain.from_iterable(docs_for_gdict)))
for doc in docs_for_gdict:
	make_and_show_lda_model(doc, gdict, 25, article_topics_frequencies, topics, show_docs = True)

print("*******")
for topic, count in article_topics_frequencies.most_common():
	print("Topic", topic, " with count of ", count, "\n\tkeywords:", topics[topic])

## Discussion of results
# Number of topics used: 25
# 
# Topic 23  with count of  17 
# 	keywords: ['walls', 'brought', 'remain', 'unseen', 'invisible,', 'leave', 'streets.', 'spheres.', 'bounded', 'marginalized,']
# Topic 5  with count of  11 
# 	keywords: ['example', 'individuals', 'rates', 'policy', 'recidivism', 'restrictions', 'offenders', 'electronic', 'technology', 'monitoring']
# Topic 3  with count of  10 
# 	keywords: ['companies', 'monitored', 'ankle', 'illicit', 'electronic', 'offenders', 'report', 'interpreted', 'incarceration', 'monitors']
# Topic 18  with count of  10 
# 	keywords: ['data', 'alasdair', 'search', 'page', 'sites', 'future', 'moran', 'views,', 'rae', '—']
# Topic 0  with count of  9 
# 	keywords: ['gilad', 'workshop', 'raise.', 'political', 'people', 'policies', 'decisional', 'designing', '—', 'bots']
# Topic 8  with count of  9 
# 	keywords: ['alexandra', '—', 'human', 'pass', 'platforms', 'themselves', 'people', 'social', 'twitter', 'bots']
# Topic 9  with count of  9 
# 	keywords: ['—', 'reason', 'earthquakes', 'commonly', 'tweet', 'tweets', 'stopped', '@clearcongress', 'data', 'people']
# Topic 13  with count of  8 
# 	keywords: ['result', 'introduce', 'racing', 'spent', 'knocking', '74', 'monitoring', 'signal', 'electronic', 'devices']
# Topic 19  with count of  8 
# 	keywords: ['means', 'monitoring', 'electronic', 'move', 'ambition', 'crime', 'world', 'patterns', 'probation', 'people']
# Topic 4  with count of  7 
# 	keywords: ['bots,', 'public', 'journalism', 'seek', 'libel.', 'tool', 'swiss', 'bot,', 'bots', 'bot']
# Topic 10  with count of  7 
# 	keywords: ['public', 'design,', 'power.', 'avoid', 'continue', 'automated', 'preserve', 'allow', 'social', 'bots']
# Topic 11  with count of  7 
# 	keywords: ['offenders.', 'points,', 'technology', 'heart', 'assists', 'pacemaker', 'individuals', 'muscles', 'device', 'devices']
# Topic 15  with count of  7 
# 	keywords: ['gps', 'mateescu.', 'sex', 'probation', 'monitoring', 'public', 'people', 'electronic', 'offenders', '—']
# Topic 2  with count of  6 
# 	keywords: ['monitoring,', 'design', 'parole', 'onto', 'monitoring', 'non-custodial', 'population', 'electronic', 'probation', 'people']
# Topic 7  with count of  6 
# 	keywords: ['12-year-old', 'found', 'house', 'ankle', 'monitoring', 'students', 'people', 'court', 'police', 'electronic']
# Topic 20  with count of  6 
# 	keywords: ['recognition', 'uncanny', 'alien', 'plot-vital', 'visual/textual', 'peer', 'subjectivity', 'doesn’t', 'sense', 'pet']
# Topic 21  with count of  6 
# 	keywords: ['public', 'restricted', 'monitoring', 'own', 'offenders', 'electronic', 'space', 'city', 'people', '—']
# Topic 22  with count of  6 
# 	keywords: ['legitimate', 'epn', 'bots', 'people', 'trending', 'government', 'message', 'tactics,', 'drown', '#yamecanse']
# Topic 1  with count of  5 
# 	keywords: ['(epn)', 'army', 'twitter', 'government', 'support', '(think', 'term', 'accounts', 'peña', 'nieto']
# Topic 12  with count of  4 
# 	keywords: ['otherwise', 'cc', 'opportunity', 'lighter', 'ankle', 'monitors', 'question', 'monitoring', 'electronic', 'people']
# Topic 14  with count of  4 
# 	keywords: ['alexandra', 'challenge', 'meanwhile,', 'actors.', 'democratic', 'actors', 'policies', 'speech', 'people', 'bots']
# Topic 17  with count of  4 
# 	keywords: ['fake', 'government’s', 'real', 'real,', 'ironic', 'attempt', 'fake.', 'rendered', 'pass', 'support']
# Topic 6  with count of  3 
# 	keywords: ['interpersonal', 'levels', 'level', 'crisis', 'society', 'european', 'pierre', 'social', 'distrust', 'trust']
# Topic 16  with count of  3 
# 	keywords: ['internet', 'limitless', 'platforms,', 'bots,', 'unpredictable', 'futures', 'doesn’t', 'technology', 'nature', '—']
# Topic 24  with count of  2 
# 	keywords: ['fake-like', 'robots.txt),', 'server', 'developers', 'website', 'crawler', 'search', 'bot?', 'bots', 'web']

# Comments:
# The choice of articles was primarily from Medium, which is a platform with heavy opinion
# from many sides of tech. Keywords used to search include "data", "society", and "bots", including
# publications with articles around these terms.
# The topics that were generated were fairly accurate, with most articles able to be described using one topic.
# These articles approached the topic of "data society bots" from human perspectives, substantiated by research,
# and several topics picked up on the collaborative, surveying nature of this opinion.
# The top ranked topics all contain the term "monitoring", which is fair because many of these articles argue about
# this. However, it is interesting that there is a distinction between topics around monitoring bot activity versus
# bots monitoring people's activity.
# The top-most topic, which trumps the others by quite a margin, revolves around the subversive and invisible nature
# of bots.
