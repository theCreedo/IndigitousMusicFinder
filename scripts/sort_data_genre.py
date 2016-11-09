import os
import json

# Create dictionaries for all files
myAnger = {}
myDisgust = {}
myFear = {}
myJoy = {}
mySadness = {}

basepath = './'
# Processes all files in given path
# EDIT FILEPATH BASED ON BASEPATH
for fname in os.listdir(basepath + '/../data/txt/tone_analyzed_songs/All/'):
    path = os.path.join(basepath, fname)
    # Enter if not directory (is file)
    if not os.path.isdir(path):
        # Assert if it's a .json file
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        # Execute if .json file
        if ext == 'txt':
            try:
                # Create out .json files to write to
                data = ''
                count = 0
                name = ''
                tonelist = []
                # Get all data from file
                # EDIT FILEPATH BASED ON BASEPATH
                with open('./../data/txt/tone_analyzed_songs/All/' + filename + '.txt', 'r') as data_file:
                    for line in data_file:
                        # Save name of file
                        if count == 0:
                            name = line
                        # Add filename and anger value to tonelist
                        if count == 3:
                            word = line.split(' ')[1]
                            tonelist.append([float(word[:len(word)-1])])
                        # Add filename and disgust value to tonelist
                        if count == 4:
                            word = line.split(' ')[1]
                            tonelist.append([float(word[:len(word)-1])])
                        # Add filename and fear value to tonelist
                        if count == 5:
                            word = line.split(' ')[1]
                            tonelist.append([float(word[:len(word)-1])])
                        # Add filename and joy value to tonelist
                        if count == 6:
                            word = line.split(' ')[1]
                            tonelist.append([float(word[:len(word)-1])])
                        # Add filename and sadness value to tonelist
                        if count == 7:
                            word = line.split(' ')[1]
                            tonelist.append([float(word[:len(word)-1])])
                        count +=1
                if len(tonelist) > 0:
                    # Save list into Anger dictionary
                    myAnger[name] = tonelist
                    # Save list into Disgust dictionary
                    myDisgust[name] = tonelist
                    # Save list into Fear dictionary
                    myFear[name] = tonelist
                    # Save list into Joy dictionary
                    myJoy[name] = tonelist
                    # Save list into Sadness dictionary
                    mySadness[name] = tonelist
            except Exception as errormsg:
                # Change Filenames based on basepath
                failedfile = open('./../data/txt/failure_log/sort_data_genre_log.txt', 'a')
                print filename + ': ' + str(errormsg)
                failedfile.write(filename + ': ' + str(errormsg) + '\n')
                failedfile.close()
#Populate anger_low_to_high.txt file with dictionary files sorted from low to high with list of percentage values
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./../data/txt/sorted_by_tone_value_songs/anger_low_to_high.txt', 'w')
for key, value in sorted(myAnger.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate disgust_low_to_high.txt file with dictionary files sorted from low to high with list of percentage values
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./../data/txt/sorted_by_tone_value_songs/disgust_low_to_high.txt', 'w')
for key, value in sorted(myDisgust.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate fear_low_to_high.txt file with dictionary files sorted from low to high with list of percentage values
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./../data/txt/sorted_by_tone_value_songs/fear_low_to_high.txt', 'w')
for key, value in sorted(myFear.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate joy_low_to_high.txt file with dictionary files sorted from low to high with list of percentage values
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./../data/txt/sorted_by_tone_value_songs/joy_low_to_high.txt', 'w')
for key, value in sorted(myJoy.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate sadness_low_to_high.txt file with dictionary files sorted from low to high with list of percentage values
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./../data/txt/sorted_by_tone_value_songs/sadness_low_to_high.txt', 'w')
for key, value in sorted(mySadness.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()