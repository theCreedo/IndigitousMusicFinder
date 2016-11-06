import matplotlib.pyplot as plt
import numpy as np
import os
import math

# Dictionary of index mappings for moods
moods = {'Anger':0, 'Disgust':1, 'Fear':2, 'Joy':3, 'Sadness':4}
basepath = './'
imgcount = 0
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
                anger = 0.0
                disgust = 0.0
                fear = 0.0
                joy = 0.0
                sadness = 0.0
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
                            anger = float(word[:len(word)-1])
                        # Add filename and max value to Disgust dictionary
                        if count == 4:
                            word = line.split(' ')[1]
                            disgust = float(word[:len(word)-1])
                        # Add filename and max value to Fear dictionary
                        if count == 5:
                            word = line.split(' ')[1]
                            fear = float(word[:len(word)-1])
                        # Add filename and max value to Joy dictionary
                        if count == 6:
                            word = line.split(' ')[1]
                            joy = float(word[:len(word)-1])
                        # Add filename and max value to Sadness dictionary
                        if count == 7:
                            word = line.split(' ')[1]
                            sadness = float(word[:len(word)-1])
                        count +=1
                        # Displays the text for each tone
                        tone = ('Fear','Disgust','Anger','Joy','Sadness')
                        y_pos = np.arange(len(tone))
                        # Creates the performance
                plt.rcdefaults()
                performance =  np.array([fear,disgust,anger,joy,sadness])
                error = np.array([0, 0, 0, 0, 0])
                k = plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
                k[0].set_color('#551a8b')
                k[1].set_color('#77dd77')
                k[2].set_color('#d60029')
                k[3].set_color('#ffff00')
                k[4].set_color('#ffa500')
                plt.yticks(y_pos, tone)
                plt.xlabel('Percentage of Tone')
                plt.title('How\'s the song, ' + filename + ', feeling?')
                # Plots the text
                # plt.show()
                # Saves the file as an image
                if imgcount < 10:
                    plt.savefig('./images/' + filename + '.png')
                elif imgcount < 100:
                    plt.savefig('./images/' + filename + '.png')
                else:
                    plt.savefig('./images/' + filename + '.png')
                plt.clf()
                imgcount += 1
            except Exception as errormsg:
                # Change Filenames based on basepath
                failedfile = open('./../corrupted_files/failures/data_visualization_plot_errors.txt', 'a')
                print filename + ': ' + str(errormsg)
                failedfile.write(filename + ': ' + str(errormsg) + '\n')
                failedfile.close()