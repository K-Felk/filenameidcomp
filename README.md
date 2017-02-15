# filenameidcomp
A python script that extracts identifiers from a csv file and compares them against a list of file names, and logs any names that don't match

Usage:  python filenamecheck.py csv_filename path_to_directory

Script will extract file identifiers from the first column of the csv file.  It will assume the first cell in the column is a column header and skip it.

script then grabs all the filenames from the specified directory (it does not search subdirectories) chops off the file extension, and checks to see if the identifier is in the resulting list of formatted filenames.  any names that don't match are logged.
