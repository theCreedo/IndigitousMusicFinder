import os
import codecs
import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(username='', password='', version='2016-05-19')

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
            # Write complete json data to the output file
            outfile.write(json.dumps(tone_analyzer.tone(text=data)))
            outfile.close()
