import os

basepath = './'
# Processes all files in given path - Change Filenames based on basepath
for fname in os.listdir(basepath):
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
                outfile = open('./../txt_period/song_files_with_period/' + filename + '.txt', 'w')
                data = ''
                # Get the whole file and load as json - Change Filenames based on basepath
                with open(filename + '.txt', 'r') as data_file:
                    for line in data_file:
                    	outfile.write(line[:len(line)-1] + '.\n')
            except Exception as errormsg:
                # Change Filenames based on basepath
                failedfile = open('./../corrupted_files/failures/addperiod_errors.txt', 'a')
                print filename + ': ' + str(errormsg)
                failedfile.write(filename + ': ' + str(errormsg) + '\n')
                failedfile.close()
            finally:
                outfile.close()
