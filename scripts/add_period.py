import os
import string

basepath = './'
# Processes all files in given path - Change Filenames based on basepath
for fname in os.listdir(basepath + '../data/txt/original_song_lyrics'):
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
                # Create out .txt files to write to folder - Change Filenames based on basepath
                outfile = open('./../data/txt/original_song_lyrics_with_periods/' + filename + '.txt', 'w')
                data = ''
                # Get the whole file and load as txt - Change Filenames based on basepath
                with open('./../data/txt/original_song_lyrics/' + filename + '.txt', 'r') as data_file:
                    data_file.readline()
                    data_file.readline()
                    for line in data_file:
                        line = string.strip(line)
                        if line:
                            outfile.write(line + '.\n')
                        else:
                            outfile.write('\n')
            except Exception as errormsg:
                # Change Filenames based on basepath
                failedfile = open('./../data/txt/failure_log/addperiod_log.txt', 'a')
                print filename + ': ' + str(errormsg)
                failedfile.write(filename + ': ' + str(errormsg) + '\n')
                failedfile.close()
            finally:
                outfile.close()
