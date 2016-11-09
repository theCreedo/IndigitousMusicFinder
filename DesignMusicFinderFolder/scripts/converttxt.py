import os
import string

basepath = './'
for fname in os.listdir(basepath + '/txt/'):
    path = os.path.join(basepath, fname)
    if not os.path.isdir(path):
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        if ext == 'txt':
            infile = open('./txt/' + filename + '.' + ext, 'r')
            outfile = open('./txt_period/' + filename + '.' + ext, 'w')
            infile.readline()
            infile.readline()
            infile.readline()
            for line in infile:
                line = string.strip(line)
                if line:
                    outfile.write(line + '.\n')
                else:
                    outfile.write('\n')
