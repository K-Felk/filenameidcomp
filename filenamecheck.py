import sys
import csv
import subprocess


def getFileNames(path): #get the filenames from the directory
        filenames = subprocess.check_output("ls " + path, shell=True, stderr=subprocess.STDOUT)
        cleanNames = []
	for name in filenames:
		fileNameEXrem = str.split(str=".")
		cleanNames = fileNameEXrem[0]
	return cleanNames


def nameCheck(identifiers, filenames): #return the URL request status code
	badNames = []
	for name in identifiers:
		if name not in filenames:
			badNames.append(name)
	return badNames

def readIdentifiers(filename): #get the file identifiers from the metadata file.  They MUST be in the first column
        identifierList = []
        try:
                f = open(filename, 'r')
        except IOError:
                print("Unable to open CSV file for reading " + filename);
                exit

        metadataReader = csv.reader(f, delimiter=',', quotechar='"')

        for row in metadataReader:
                identifierList.append(row[0])
        del identifierList[0]
	return identifierList





def logBadFileNames(badFileNames): #write bad URLS to a log file
        try:
                f = open('badFileNames.log', 'w')
        except IOError:
                print("Unable to open logfile for writing")
                exit
        for name in badFileNames:
                f.write(name + '\n')
        f.close()
        return 'true'

csvFile=sys.argv[1]
path = sys.argv[2]

IDlist = readIdentifiers(csvFile)

fileNames = getFileNames(path)


badNames = nameCheck(IDlist, fileNames)

if len(badNames) > 0:
	logBadFileNames(badNames)

print("Identifier check complete, " + str(len(badNames)) + "bad identifiers found.");
		
	
