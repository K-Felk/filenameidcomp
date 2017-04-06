import sys
import csv
import subprocess
import requests

def readURLs(filename): #get the URLs from the metadata file.  They MUST be in the first column
	identifierList = []


    	try:
		f = open(filename, 'r')
    	except IOError:
        	print("Unable to open CSV file for reading " + filename);
        	exit

	metadataReader = csv.reader(f, delimiter=',', quotechar='"')

    	for row in metadataReader:
        	if ";" in row[0]:
			for splitrow in row[0].split(";"):
				identifierList.append(splitrow.strip());
		else :
			identifierList.append(row[0])
        #assume first row in the csv is a header
        del identifierList[0]
	
	return identifierList

def logBadNames(badFileNames, logfilename): #write bad names to a log file
    	try:
        	f = open(logfilename, 'w')
    	except IOError:
        	print("Unable to open logfile " + logfilename + " for writing")
                exit
    	for name in badFileNames:
        	f.write(name + '\n')
    	f.close()
    	return 'true'


def checkURLs(URLlist): #check the urls and get the status code.
	
	badURLlist = []

	for URL in URLlist:
	
		response = requests.head(URL)		
		status = response.status_code
		if status != 200:
			badURLlist.append(URL)

	return badURLlist	

#path to the csv file must be fIrst argument.  FULL PATHS REQUIRED
csvFile=sys.argv[1]

URLs = readURLs(csvFile)

badURLs = checkURLs(URLs)

logBadNames(badURLs, "badURLs.log")

print("Identifier check complete, " + str(len(badURLs)) + " bad URLs found.");
