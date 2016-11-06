import os
import json

mood = {'Anger':0, 'Disgust':1, 'Fear':2, 'Joy':3, 'Sadness':4}
myAnger = {}
myDisgust = {}
myFear = {}
myJoy = {}
mySadness = {}
basepath = './'
# Processes all files in given path
for fname in os.listdir(basepath + '/songs_to_moods/All/'):
    path = os.path.join(basepath, fname)
    # Enter if not directory (is file)
    if not os.path.isdir(path):
        # Assert if it's a .json file
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        # Execute if .json file
        if ext == 'txt':
            # Create out .json files to write to
            # outfile = open('./songs_to_moods/' + filename + '.txt', 'w')
            data = ''
            count = 0
            # Loop through all the lines in the file
            name = ''
            with open('./songs_to_moods/All/' + filename + '.txt', 'r') as data_file:
                for line in data_file:
                    if count == 0:
                        name = line
                    if count == 3:
                        word = line.split(' ')[1]
                        myAnger[name] = float(word[:len(word)-1])
                    if count == 4:
                        myDisgust[name] = float(word[:len(word)-1])
                    if count == 5:
                        myFear[name] = float(word[:len(word)-1])
                    if count == 6:
                        myJoy[name] = float(word[:len(word)-1])
                    if count == 7:
                        mySadness[name] = float(word[:len(word)-1])
                    count +=1

print 'Anger'
for key, value in sorted(myAnger.iteritems(), key=lambda (k,v): (v,k)):
    print "%s%s" % (key, value)
print '\nDisgust'
for key, value in sorted(myDisgust.iteritems(), key=lambda (k,v): (v,k)):
    print "%s%s" % (key, value)
print '\nFear'
for key, value in sorted(myFear.iteritems(), key=lambda (k,v): (v,k)):
    print "%s%s" % (key, value)
print '\nJoy'
for key, value in sorted(myJoy.iteritems(), key=lambda (k,v): (v,k)):
    print "%s%s" % (key, value)
print '\nSadness'
for key, value in sorted(mySadness.iteritems(), key=lambda (k,v): (v,k)):
    print "%s%s" % (key, value)
            # outfile.write(max_sentence + '\n' + tone_word_sentence + '\n' + str(round(max_tone_sentence * 100)))
            # outfile.close()