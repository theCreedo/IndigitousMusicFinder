import os

basepath = './'
for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if not os.path.isdir(path):
        filewhole = path.split('.')
        filename = filewhole[1][1:]
        ext = filewhole[-1]
        if ext == 'txt':
            infile = open(filename + '.' + ext, 'r')
            outfile = open(filename + '_dot.' + ext, 'w')
            for line in infile:
                outfile.write(line[:-1] + '.\n')
