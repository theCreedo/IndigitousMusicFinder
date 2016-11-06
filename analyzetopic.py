import nltk
import gensim
import os
import codecs
import string

## Build the initial Gensim dictionary and store it

# clean text by removing stopwords, then return collections of lines.
# Possibly, since these are song lyrics, we should return collections of groups of trigrams.
def clean_text(text):
	stopword_filename = "./stopwords.txt"
	with open(stopword_filename) as f:
		stopwords = set(f.read().split())
	for punct in string.punctuation:
		stopwords.add(punct)
	exclude = set(string.punctuation)

	cleaned_text_list = list(filter(lambda x: x not in stopwords, \
		[''.join(ch for ch in s if ch not in exclude) for s in text.split()]))

	if len(cleaned_text_list) < 3:
		return cleaned_text_list
	else:
		trigram_list = []
		trigram = cleaned_text_list[:3]
		for word in cleaned_text_list[3:]:
			trigram_list.append(trigram)
			print(trigram)
			trigram.append(word)
			trigram = trigram[1:]
		print()
		return trigram_list


# Gather all the lines, in all the songs, to create a gensim dictionary.
# The training happens in line-sized units.
def generate_song_lines():
	songs_lines = []
	basepath = './'
	for fname in os.listdir(basepath + './txt_period/'):
	    path = os.path.join(basepath, fname)
	    # Enter if not directory (is file)
	    if not os.path.isdir(path):
	        # Assert if it's a .txt file
	        filewhole = path.split('.')
	        filename = filewhole[1][1:]
	        ext = filewhole[-1]
	        # Execute if .txt file
	        if ext == 'txt':
	            # Create out .json files to write to
	            with codecs.open('./txt_period/' + path, 'r', encoding='utf8') as fin:
	                for line in fin:
	                	cleaned = clean_text(line[:-1])
	                	if cleaned:
	                		songs_lines.append(cleaned)
	return songs_lines

def make_and_show_lda_model(line, gdict, numtopics):
	# represent the corpus in sparse matrix format, bag-of-words
	print(line)
	corpus = [gdict.doc2bow(trigram) for trigram in line]
	# now we make an LDA object.
	# in case we have a larger text collection (such as the Brown corpus),
	# make sure to set "passes" to a reasonably high number in order not to have all topics
	# come out equal. 20 seems to work.
	lda_obj = gensim.models.ldamodel.LdaModel( \
		corpus, id2word=gdict, num_topics=numtopics, passes = 15)

	# how do our line look: how important is each topic there?
	print("Showing how important each topic is for each document")
	lda_corpus = lda_obj[corpus]
	for docindex, doc in enumerate(lda_corpus):
		for topic, weight in doc:
			topic_words = [x[0] for x in sorted(lda_obj.show_topic(topic), key=lambda x : x[1])]
			print( "Topic", topic,", which has keywords: ", topic_words, \
				"\nWith weight of", round(weight, 2))


# gdict = gensim.corpora.Dictionary(generate_song_lines())
# gdict.save('./songs_lines.dict')
gdict = gensim.corpora.Dictionary.load('./songs_lines.dict')

make_and_show_lda_model(clean_text("You look as good as the day I met you. \
I forget just why I left you,. \
I was insane."), gdict, 4)
