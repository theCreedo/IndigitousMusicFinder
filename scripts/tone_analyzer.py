import os
import codecs
import json
import time
from watson_developer_cloud import ToneAnalyzerV3

# Setup IBM Watson Tone Analyzer with your given USERNAME and PASSWORD
# UNCOMMENT LINE BELOW ONCE YOU HAVE CREATED ACCOUNT WITH USERNAME/PASSWORD
# tone_analyzer = ToneAnalyzerV3(username='INSERT USERNAME HERE', password='INSERT PASSWORD HERE', version='2016-05-19')

# Function in order to make calls to Watson. Makes 3 calls before ending if calls fail
def tryWatson(data, outfile, numtries, filename):
    try:
        # Watson tone_analyzer API call
    # UNCOMMENT LINE BELOW ONCE YOU HAVE CREATED ACCOUNT WITH USERNAME/PASSWORD
        # response = tone_analyzer.tone(text=data)
        # Write to file in json if call is successful
    # UNCOMMENT LINE BELOW ONCE YOU HAVE CREATED ACCOUNT WITH USERNAME/PASSWORD
        # outfile.write(json.dumps(response))
        print 'succeeded one request on ' + filename
    except Exception as errormsg:
        print 'Hit error in Watson ' + str(numtries) + ' times\n'
        # Change Filenames based on basepath
        failedfile = open('./../data/txt/failure_log/tone_analyzer_log.txt', 'a')
        print time.strftime("%c") + ' ' + filename + ': ' + str(errormsg)
        failedfile.write(time.strftime("%c") + ' ' + filename + ': ' + str(errormsg))
        failedfile.close()
        if numtries < 3:
            tryWatson(data, outfile, numtries + 1, filename)
        if numtries == 3:
            os.remove(filename)
    pass

basepath = './'
# Processes all files in given path - Change Filenames based on basepath
for fname in os.listdir(basepath + '../data/txt/original_song_lyrics_with_periods/'):
    path = os.path.join(basepath, fname)
    # Enter if not directory (is file)
    if not os.path.isdir(path):
        # Assert if it's a .txt file
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        # Execute if .txt file
        if ext == 'txt':
            try:
                # Create out .json files to write to - Change Filenames based on basepath
                outfile = codecs.open('./../data/json/' + filename + '.json', 'w', encoding='utf8')
                data = ''
                # Get all song lyrics from file - Change Filenames based on basepath
                with codecs.open('./../data/txt/original_song_lyrics_with_periods/' + filename + '.' + ext, 'r', encoding='utf8') as fin:
                    data = fin.read()
                # Call the Watson method for api calls
                # tryWatson(data, outfile, 0, filename)
            except Exception as errormsg:
                failedfile = open('./../data/txt/failure_log/tone_analyzer_log.txt', 'a')
                print time.strftime("%c") + ' ' + filename + ': ' + str(errormsg)
                failedfile.write(time.strftime("%c") + ' ' + filename + ': ' + str(errormsg))
                failedfile.close()
                os.remove('./../data/json/' + filename + '.json')
            finally:
                outfile.close()
