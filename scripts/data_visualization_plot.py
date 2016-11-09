import matplotlib.pyplot as plt
import numpy as np
import os
import math
import ast

# Dictionary of index mappings for moods
moods = {'Anger':0, 'Disgust':1, 'Fear':2, 'Joy':3, 'Sadness':4}
basepath = './'
imgcount = 0
# Processes all files in given path
# EDIT FILEPATH BASED ON BASEPATH
for fname in os.listdir(basepath + '../data/txt/sorted_by_tone_value_songs/'):
	path = os.path.join(basepath, fname)
	# Enter if not directory (is file)
	if not os.path.isdir(path):
		# Assert if it's a .txt file
		filewhole = path.split('.')
		filename = filewhole[1][1:]
		ext = filewhole[-1]
		tonemood = filename.split('_')
		# Execute if .txt file
		if ext == 'txt':
			try:
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
				with open('./../data/txt/sorted_by_tone_value_songs/' + filename + '.txt', 'r') as data_file:
					for line in data_file:
						# Save name of file
						if count % 2 == 0:
							name = line
						else:
							# print line
							# print line[0]
							values = ast.literal_eval(line)
							strvalue0 = str(values[0])
							strvalue1 = str(values[1])
							strvalue2 = str(values[2])
							strvalue3 = str(values[3])
							strvalue4 = str(values[4])
							anger =  float(strvalue0[1:len(strvalue0)-1])
							disgust =  float(strvalue1[1:len(strvalue1)-1])
							fear =  float(strvalue2[1:len(strvalue2)-1])
							joy =  float(strvalue3[1:len(strvalue3)-1])
							sadness =  float(strvalue4[1:len(strvalue4)-1])
							# Displays the text for each tone
							tone=('Fear','Disgust','Anger','Joy','Sadness')
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
							plt.title('How\'s the song, ' + name + ', feeling?')
							# Plots the text
							# plt.show()
							# Saves the file as an image, ordered by lowest to highest
							plt.xlim(0,100)
							if imgcount < 10:
								plt.savefig('./../data/images/' + tonemood[0] + '/00' + str(imgcount) + '_' + name + '.png')
							elif imgcount < 100:
								plt.savefig('./../data/images/' + tonemood[0] + '/0' + str(imgcount) + '_' + name + '.png')
							else:
								plt.savefig('./../data/images/' + tonemood[0] + '/' + str(imgcount) + '_' + name + '.png')
							plt.clf()
							imgcount += 1
						count+=1
			except Exception as errormsg:
				# Change Filenames based on basepath
				failedfile = open('./../data/txt/failure_log/data_visualization_plot_log.txt', 'a')
				print filename + ': ' + str(errormsg)
				failedfile.write(filename + ': ' + str(errormsg) + '\n')
				failedfile.close()