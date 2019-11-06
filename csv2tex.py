#!/usr/bin/env python
import csv
import sys
import getopt

# This script needs to be called with one argument,
# e.g. the csv filename. Abort if requirements are 
# not met.

#if len(sys.argv) != 2:
#    print("Usage: csv2tex <file.csv>")
#    sys.exit()

# Input validation with getopt()

optlist, args = getopt.getopt(sys.argv[1:], 'i:')

if args == []:
    print("Missing the .csv filename")
    print("")
    print("Usage: csv2tex [options] <file.csv>")
    print("")
    print("     options:")
    print("     -i   : Specify the column names that should be ignored")
    print("            separated by comma") 
    sys.exit()

# read in csv file line by line
# this will generate the the data array in the form:
# [[row1],[row2],...] with row1=[x,y,z,...]

data = []
with open(args[0]) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data.append(row)
# print as tex code
tex = ''
data = [ x for x in data if x != [] ]
# remove ignored column
if optlist != []: # check if arguments were given, skip if not
    if ',' in optlist[0][1]: # check if more than one column should be ignored
        colNames = optlist[0][1].split(',')
    else:
        colNames = optlist[0][1]
    if type(colNames) in [list]: # check if colNames is a list
        for x in colNames:
            indexCol = data[0].index(x)
            for n in range(len(data)):
                del data[n][indexCol]
    else:
        indexCol = data[0].index(optlist[0][1])
        for n in range(len(data)):
            del data[n][indexCol]
# count columns
nCol = len(data[0])
tex = tex + '\\begin{tabular}{l' + (nCol - 1) * 'c' + '}\n\\hline\n'
# This reads all lines and parses them to tex output 
for n in range(len(data)-1):
    newLine = ''
    for i in data[n]:
        newLine = newLine + i + '&' 
    newLine = newLine[:-1]
    newLine = newLine + '\\\\'
    newLine = newLine + '\n'
    if n == 0:
        newLine = newLine + '\\hline\n'
    tex = tex + newLine
newLine = ''
n = n + 1
for i in data[n]:
    newLine = newLine + i + '&'
newLine = newLine[:-1]
tex = tex + newLine
newLine = newLine[len(newLine):]
newLine = newLine + '\\\\'
newLine = newLine + '\n'
newLine = newLine + '\\hline'
tex = tex + newLine
tex = tex + '\n\\end{tabular}'

print(tex)  

