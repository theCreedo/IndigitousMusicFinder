import os

for fname in os.listdir('./static/'):
	if not os.path.isdir(fname):
		print(fname)
		outfname = '_'.join(fname.split('_')[1:-1])
		print(outfname)
		with open('./static/' + outfname, 'wb') as outf:
			with open('./static/' + fname, 'rb') as inf:
				outf.write(inf.read())
