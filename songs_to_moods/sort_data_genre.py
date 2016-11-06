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
            try:
                # Create out .json files to write to
                data = ''
                count = 0
                name = ''
                # Get all data from file
                # EDIT FILEPATH BASED ON BASEPATH
                with open('./All/' + filename + '.txt', 'r') as data_file:
                    for line in data_file:
                        # Save name of file
                        if count == 0:
                            name = line
                        # Add filename and max value to Anger dictionary
                        if count == 3:
                            word = line.split(' ')[1]
                            myAnger[name] = float(word[:len(word)-1])
                        # Add filename and max value to Disgust dictionary
                        if count == 4:
                            word = line.split(' ')[1]
                            myDisgust[name] = float(word[:len(word)-1])
                        # Add filename and max value to Fear dictionary
                        if count == 5:
                            word = line.split(' ')[1]
                            myFear[name] = float(word[:len(word)-1])
                        # Add filename and max value to Joy dictionary
                        if count == 6:
                            word = line.split(' ')[1]
                            myJoy[name] = float(word[:len(word)-1])
                        # Add filename and max value to Sadness dictionary
                        if count == 7:
                            word = line.split(' ')[1]
                            mySadness[name] = float(word[:len(word)-1])
                        count +=1
            except Exception as errormsg:
                # Change Filenames based on basepath
                failedfile = open('./../corrupted_files/failures/sort_data_genre_errors.txt', 'a')
                print filename + ': ' + str(errormsg)
                failedfile.write(filename + ': ' + str(errormsg) + '\n')
                failedfile.close()
#Populate anger_low_to_hight.txt file with dictionary files sorted from low to high
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./Sorted_Tones/anger_low_to_high.txt', 'w')
for key, value in sorted(myAnger.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate disgust_low_to_high.txt file with dictionary files sorted from low to high
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./Sorted_Tones/disgust_low_to_high.txt', 'w')
for key, value in sorted(myDisgust.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate fear_low_to_high.txt file with dictionary files sorted from low to high
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./Sorted_Tones/fear_low_to_high.txt', 'w')
for key, value in sorted(myFear.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate joy_low_to_high.txt file with dictionary files sorted from low to high
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./Sorted_Tones/joy_low_to_high.txt', 'w')
for key, value in sorted(myJoy.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()

#Populate sadness_low_to_hight.txt file with dictionary files sorted from low to high
# EDIT FILEPATH BASED ON BASEPATH
outfile = open('./Sorted_Tones/sadness_low_to_high.txt', 'w')
for key, value in sorted(mySadness.iteritems(), key=lambda (k,v): (v,k)):
    outfile.write(key + str(value) + '\n')
outfile.close()