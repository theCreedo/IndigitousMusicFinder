import os
import json
from pprint import pprint


mood = {'Anger':0, 'Disgust':1, 'Fear':2, 'Joy':3, 'Sadness':4}
basepath = './'
# Processes all files in given path
for fname in os.listdir(basepath + '/json/'):
    path = os.path.join(basepath, fname)
    # Enter if not directory (is file)
    if not os.path.isdir(path):
        # Assert if it's a .json file
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        # Execute if .json file
        if ext == 'json':
            data = ''
            # Loop through all the lines in the file
            with open('./json/' + filename + '.json', 'r') as data_file:
                data = json.load(data_file)
            tone_word_whole = ''
            max_tone_whole = 0.0
            for tone in data['document_tone']['tone_categories'][0]['tones']:
                if tone['score'] > max_tone_whole:
                    tone_word_whole = tone['tone_name']
                    max_tone_whole = tone['score']
            max_sentence = ''
            tone_word_sentence = ''
            max_tone_sentence = 0.0
            mood_index = mood.get(tone_word_whole)
            for sentences in data['sentences_tone']:
                if (len(sentences['tone_categories'])>0):
                    if sentences['tone_categories'][0]['tones'][mood_index]['score'] > max_tone_sentence:
                        tone_word_sentence = sentences['tone_categories'][0]['tones'][mood_index]['tone_name']
                        max_tone_sentence = sentences['tone_categories'][0]['tones'][mood_index]['score']
                        max_sentence = sentences['text']
            # Create out .json files to write to
            outfile = open('./songs_to_moods/' + tone_word_whole + '/' + filename + '.txt', 'w')
            outfile.write(filename + '\n' + tone_word_whole + '\n' + str(max_tone_whole) + '\n' + max_sentence + '\n' + tone_word_sentence + '\n' + str(max_tone_sentence))
            outfile.close()

