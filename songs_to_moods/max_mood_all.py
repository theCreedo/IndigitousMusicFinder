import os
import json
import math

# Dictionary of index mappings for moods
moods = {'Anger':0, 'Disgust':1, 'Fear':2, 'Joy':3, 'Sadness':4}
basepath = './'
# Processes all files in given path - Change Filenames based on basepath
for fname in os.listdir(basepath + '../json/'):
    path = os.path.join(basepath, fname)
    # Enter if not directory (is file)
    if not os.path.isdir(path):
        # Assert if it's a .json file
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        # Execute if .json file
        if ext == 'json':
            try:
                # Create out .txt files to write to folder - Change Filenames based on basepath
                outfile = open('./All/' + filename + '.txt', 'w')
                data = ''
                # Get the whole file and load as json - Change Filenames based on basepath
                with open('./../json/' + filename + '.json', 'r') as data_file:
                    data = json.load(data_file)
                # Instantiate the main tone of a song
                entire_tone_word = ''
                # Instantiate the max value of tone of a song
                entire_max_tone = 0.0
                # Used for averaging and getting a good 0-11 scale later
                total_tone_value = 0.0
                for tone in data['document_tone']['tone_categories'][0]['tones']:
                    # Add up all tone_values
                    total_tone_value += tone['score']
                    if tone['score'] > entire_max_tone:
                        # Save highest tone word and max tone
                        entire_tone_word = tone['tone_name']
                        entire_max_tone = tone['score']
                # Instantiate the max toned sentence a song
                max_sentence = ''
                # Instantiate the main tone of a sentence
                sentence_tone_word = ''
                # Instantiate the max value of tone of a sentence
                sentence_max_tone = 0.0
                tone_index = moods.get(entire_tone_word)
                for sentences in data['sentences_tone']:
                    # Covers weird null value within tone_categories in certain json files
                    if (len(sentences['tone_categories'])>0):
                        if sentences['tone_categories'][0]['tones'][tone_index]['score'] > sentence_max_tone:
                            # Save highest tone word, and max tone, and max sentence
                            sentence_tone_word = sentences['tone_categories'][0]['tones'][tone_index]['tone_name']
                            sentence_max_tone = sentences['tone_categories'][0]['tones'][tone_index]['score']
                            max_sentence = sentences['text']
                outfile.write(filename + '\n' + entire_tone_word + '\n' + str(round(entire_max_tone/total_tone_value * 100))+ '\n')
                # Write out the tone and the score on 0-100 scale
                for tone in data['document_tone']['tone_categories'][0]['tones']:
                    outfile.write(tone['tone_name'] + ' ' + str(round(tone['score']/total_tone_value * 100)) + '\n')
                # Write out the sentence, the given tone word, and the max tone word value
                outfile.write(max_sentence + '\n' + sentence_tone_word + '\n' + str(round(sentence_max_tone * 100)))
                print filename
            # Potential exceptions due to corrupted files
            except Exception as errormsg:
                # Change Filenames based on basepath
                failedfile = open('./../corrupted_files/max_mood_all_errors.txt', 'a')
                print filename + ': ' + str(errormsg)
                failedfile.write(filename + ': ' + str(errormsg))
                failedfile.close()
            # Close outfile in the end
            finally:
                outfile.close()
