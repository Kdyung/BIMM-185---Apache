import sys, numpy, scipy,os
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist

#import the data into a native 2d python array
infile = open(sys.argv[1],'r')
clusterdata=[]
linecount = 0
while 1:
        line = infile.readline().strip()
        clusterdata.append(line)
        if not line: break
        linecount = linecount + 1

print "Input : %s"%sys.argv[1]
colHeaders = clusterdata[0].strip().split()[1:]
print colHeaders
rowHeaders = []
dataMatrix = []
for line in clusterdata[1:]:
    if len(line)>0:
	    data = line.strip().split()
	    print line
	    print data[0]
	    rowHeaders.append(data[0])
	    dataMatrix.append([float(x) for x in data[1:]])
print rowHeaders
sys.exit()
#convert native python array into a numpy array
dataMatrix = numpy.array(dataMatrix)

#calculate distance matrix and convert to squareform
distanceMatrix = dist.pdist(dataMatrix)
distanceSquareMatrix = dist.squareform(distanceMatrix)

#calculate linkage matrix
linkageMatrix = hier.linkage(distanceSquareMatrix)

#get the order of the dendrogram leaves
heatmapOrder = hier.leaves_list(linkageMatrix)

#reorder the data matrix and row headers according to leaves
orderedDataMatrix = dataMatrix[heatmapOrder,:]
rowHeaders = numpy.array(rowHeaders)
orderedRowHeaders = rowHeaders[heatmapOrder,:]

#output data for visualization in a browser with javascript/d3.js
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

#print 'var maxData = ' + str(numpy.amax(dataMatrix)) + ";"
#print 'var minData = ' + str(numpy.amin(dataMatrix)) + ";"
#print 'var data = ' + str(matrixOutput) + ";"
#print 'var cols = ' + str(colHeaders) + ";"
#print 'var rows = ' + str([x for x in orderedRowHeaders]) + ";"
