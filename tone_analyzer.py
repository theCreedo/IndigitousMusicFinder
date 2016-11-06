import os
import codecs
import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(username='98a2f9b7-e29f-4cd8-a6a0-a53073de93ea', password='bTsfFVjXlVSr', version='2016-05-19')


def tryWatson(data, outfile, numtries):
    try:
        response = tone_analyzer.tone(text=data)
        outfile.write(json.dumps(response))
        print 'succeeded one request\n'
    except Exception:
        print 'Hit error in Watson ' + str(numtries) + ' times\n'
        if numtries < 3:
            tryWatson(data, outfile, numtries + 1)
    pass




basepath = './'
# Processes all files in given path
for fname in os.listdir(basepath + '/txt_period/'):
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
            outfile = codecs.open('./json/' + filename + '.json', 'w', encoding='utf8')
            data = ''
            # Loop through all the lines in the file
            with codecs.open('./txt_period/' + filename + '.' + ext, 'r', encoding='utf8') as fin:
                data = fin.read()
            tryWatson(data, outfile, 0)
            outfile.close()

