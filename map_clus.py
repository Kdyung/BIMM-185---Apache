#!/usr/bin/env python
import cgi, os, sys

import cgitb; cgitb.enable()
import sys, numpy, scipy
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

fileitem = form['file']

test=''
clusterdata = []
if fileitem.file:
   fn = os.path.basename(fileitem.filename)
   #open(fn, 'wb').write(fileitem.file.read())
   infile = open(fn,'rb')
   linecount = 0
   while 1:
        line = fileitem.file.readline().strip()
        clusterdata.append(line)
        if not line: break
        linecount = linecount + 1
   message = 'The file "' + fn + '" was uploaded successfully. Input file line count: %s.'%linecount
else:
   message = 'No file was uploaded'

#Processing Heatmap data to .js
colHeaders = clusterdata[0].strip().split(' ')[1:]
rowHeaders = []
dataMatrix = []
for line in clusterdata[1:]:
    if len(line)>0:
	    data = line.strip().split()
	    rowHeaders.append(data[0])
	    dataMatrix.append([float(x) for x in data[1:]])
dataMatrix = numpy.array(dataMatrix) 
test = clusterdata[0].strip().split()
distanceMatrix = dist.pdist(dataMatrix)
#@TODO add Choosing dist matrx type function from html 
distanceMatrix = dist.pdist(dataMatrix,'hamming') #use hamming function
distanceMatrix = dist.pdist(dataMatrix,'euclidean') #use euclidean function
 #calculate linkage Matrix
linkageMatrix = hier.linkage(distanceMatrix)
heatmapOrder = hier.leaves_list(linkageMatrix)
orderedDataMatrix = dataMatrix[heatmapOrder,:]   
rowHeaders = numpy.array(rowHeaders)
orderedRowHeaders = rowHeaders[heatmapOrder,:]
#
matrixOutput = []
row = 0
for rowData in orderedDataMatrix:
	    col = 0
	    rowOutput = []
	    for colData in rowData:
		    rowOutput.append([colData, row, col])
		    col += 1
	    matrixOutput.append(rowOutput)
	    row += 1

#print this to .js for D3.js
#test with outfile
outfile = open('map_clus_data.js','w')
outfile.write('var maxData = ' + str(numpy.amax(dataMatrix)) + ";")
outfile.write( 'var minData = ' + str(numpy.amin(dataMatrix)) + ";")
outfile.write( 'var data = ' + str(matrixOutput) + ";")
outfile.write( 'var cols = ' + str(colHeaders) + ";")
outfile.write( 'var rows = ' + str([x for x in orderedRowHeaders]) + ";")
outfile.close()

   
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)
print "<p>Test output: %s</p>"%test
print "<p>Number of genes: %s</p>"%len(rowHeaders)
print "<p>Number of conditions: %s</p>"%len(colHeaders)
print  "<a href=\"map_clus_display.html\">Display Clustering Data</a>"
#<a href="http://example.com/files/myfile.pdf" target="_blank">Download</a>
