# dupFinder.py
import os, sys
import hashlib
import posixpath
import ntpath

def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups

     
# Joins two dictionaries
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

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    file1 = open('C:\\Users\\famil\\Desktop\\Jonas\\SO2\\ChurrosService\\ChurrosLog.txt', 'a+')
    if len(results) > 0:
        print('Duplicatas Encontradas: ', end = '\n')
        for result in results:
            i = 0
            for subresult in result:
                print('\t\t%s %i' % (subresult, i))
                
                if i>0:

                    file1.write('%s\r\n' % path_leaf(subresult))
                    getPath = subresult.replace(os.sep, ntpath.sep)
                    os.remove(getPath)
                i += 1
            print('___________________')
        file1.close
    else:
        print('Não há duplicatas.')

'''
def runFinder(folders): 
    duplicates = {}
    for f in folders:
        time.sleep(5)
        # Iterate the folders given
        if os.path.exists(f):
            # Find the duplicated files and append them to the dups
            joinDicts(dups, findDup(f))
        else:   
            print('%s is not a valid path, please verify' % i)
            sys.exit()
            printResults(duplicates)
'''