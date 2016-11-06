import os
import json

mood = {'Anger':0, 'Disgust':1, 'Fear':2, 'Joy':3, 'Sadness':4}
# Create dictionaries for all files
myAnger = {}
myDisgust = {}
myFear = {}
myJoy = {}
mySadness = {}

basepath = './'
# Processes all files in given path
for fname in os.listdir(basepath + '/All/'):
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
            data = ''
            count = 0
            name = ''
            # Get all data from file
            with open('./All/' + filename + '.txt', 'r') as data_file:
                for line in data_file:
                    if count == 0:
                        name = line
                    if count == 3:
                        word = line.split(' ')[1]
                        myAnger[name] = float(word[:len(word)-1])
                    if count == 4:
                        word = line.split(' ')[1]
                        myDisgust[name] = float(word[:len(word)-1])
                    if count == 5:
                        word = line.split(' ')[1]
                        myFear[name] = float(word[:len(word)-1])
                    if count == 6:
                        word = line.split(' ')[1]
                        myJoy[name] = float(word[:len(word)-1])
                    if count == 7:
                        word = line.split(' ')[1]
                        mySadness[name] = float(word[:len(word)-1])
                    count +=1

outfile = open('./Anger/sorted_low_to_high.txt', 'w')
for key, value in sorted(myAnger.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()
outfile = open('./Disgust/sorted_low_to_high.txt', 'w')
for key, value in sorted(myDisgust.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()
outfile = open('./Fear/sorted_low_to_high.txt', 'w')
for key, value in sorted(myFear.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()
outfile = open('./Joy/sorted_low_to_high.txt', 'w')
for key, value in sorted(myJoy.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()
outfile = open('./Sadness/sorted_low_to_high.txt', 'w')
for key, value in sorted(mySadness.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()