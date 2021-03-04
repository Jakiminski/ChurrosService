import os # os.chdir(path), os.getcwd(), os.remove(file)
import sys
import hashlib
import posixpath
import ntpath

def findDup(parentFolder):
	dups = {}
	for dirName, subdirs, fileList in os.walk(parentFolder):
		#print('Procurando em \'%s\'' % dirName)
		for filename in fileList:
			# pega path do arquivo
			path = os.path.join(dirName, filename)
			# calcula hash
			file_hash = hashfile(path)
			# add/append filepath
			if file_hash in dups:
				dups[file_hash].append(path)
			else:
				dups[file_hash] = [path]
	return dups

def joinDicts(dict1, dict2):
	for key in dict2.keys():
		if key in dict1:
			dict1[key] = dict1[key] + dict2[key]
		else:
			dict1[key] = dict2[key]

def hashfile(path, blocksize = 65536):
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()

def allpaths(folder, pathlist = []):
	for f in os.scandir(folder):
		if f.is_dir():
		 	pathlist.append(f.path)
		 	allpaths(f.path,pathlist)
	return pathlist

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def results(dict1, logfile):
	results = list(filter(lambda x: len(x) > 1, dict1.values()))
	if len(results) > 0:
		#print('Duplicatas descobertas...')
		for result in results:
			i = 0
			#print('{}: {}'.format(i+1,result))
			for subresult in result:
				#print('{}:\t{}'.format(i, subresult))
				if i>0:
					logfile.write('%s\r\n' % path_leaf(subresult))
					pathname = subresult.replace(os.sep, ntpath.sep)
					#print('{}:\t{}'.format(i, subresult))
					if os.path.exists(pathname):
						os.remove(pathname)
				i += 1
		logfile.close()
		return True
	
	else:
		print('Não havia arquivos repetidos.')
		return False

################################################

if __name__ == '__main__':
	# lista com todas as pastas e subpastas
	folder = 'C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService\\root'
	folders = hash4dup.allpaths(folder,[folder,])
	#print('All paths found.')
	
	duplicates = {}
	for f in folders: # Iterate the folders given
		#print(f)
		# Find the duplicated files and append them to the dups
		if os.path.exists(f):
			print('Searching duplicates inside:\t\'{}\''.format(f))
			joinDicts(duplicates, findDup(f))
	print('Making log.')
	logfile = open('C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService\\DeleteLog.txt', 'a+')
	self.isrunning = not results(duplicates, logfile)