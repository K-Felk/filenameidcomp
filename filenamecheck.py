import sys
import csv
import subprocess


def getFileNames(path): #get the filenames from the directory, strip off their file extensions, return a list
        output = subprocess.check_output("ls " + path, shell=True, stderr=subprocess.STDOUT)
        filenames = output.split("\n")
        cleanNames = []
        for name in filenames:
                fileNameEXrem = name.split(".")
                cleanNames.append(fileNameEXrem[0])
        return cleanNames


def nameCheck(list1, list2): #return filenames not in the second list
        badNames = []
        for name in list1:
                if name not in list2:
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
#path to the csv file must be fIrst argument, path to the directory where the files are located is second.  FULL PATHS REQUIRED

csvFile=sys.argv[1]
path = sys.argv[2]

IDlist = readIdentifiers(csvFile)

fileNames = getFileNames(path)


#find entries in the metadata that don't match any files
badNames = nameCheck(IDlist, fileNames)

#log those bad boys
if len(badNames) > 0:
        logBadNames(badNames, "not_in_directory.log")

#now do the same in the other direction: files that aren't in the metadata

badFiles = nameCheck(fileNames, IDlist)

#log those bad boys in a separate file
if len(badFiles) > 0:
    logBadNames(badFiles, "not_in_metadata.log")

#...and we are done.

print("Identifier check complete, " + str(len(badNames)) + " bad identifiers found, " + str(len(badFiles)) +  " missing files found. ");

	
