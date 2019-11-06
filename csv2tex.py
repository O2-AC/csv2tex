#!/usr/bin/env python
import csv
import sys


# This script needs to be called with one argument,
# e.g. the csv filename. Abort if requirements are 
# not met.

if len(sys.argv) != 2:
    print("Usage: csv2tex <file.csv>")
    sys.exit()
# read in csv file line by line
# this will generate the the data array in the form:
# [[row1],[row2],...] with row1=[x,y,z,...]

data = []
with open(sys.argv[1]) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data.append(row)
# print as tex code
tex = ''

# count columns
nCol = len(data[0])
tex = tex + '\\begin{tabular}{l' + (nCol - 1) * 'c' + '}\n\\hline\n'
# This reads all lines and parses them to tex output 
for n in range(len(data)):
    newLine = ''
    for i in data[n]:
        newLine = newLine + i + '&' 
    newLine = newLine[:-1]
    newLine = newLine + '\\\\'
    newLine = newLine + '\n'
    if n == 0:
        newLine = newLine + '\\hline\n'
    tex = tex + newLine
newLine = newLine[:-3]
newLine = newLine + '\n'
newLine = newLine + '\\hline'
tex = tex + newLine
tex = tex + '\n\\end{tabular}'

print(tex)  

