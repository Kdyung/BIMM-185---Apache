#!/usr/bin/python

#Script for analyzing clustering according to HOMER tool and tutorial.
#http://homer.salk.edu/homer/basicTutorial/clustering.html


#Code Sampled: http://blog.nextgenetics.net/?e=44
#   by Damian Kao

# Pycluster needed. 
    #Installed >?

# Take input of normalized gene expression matrix
#test file: /SampleData/expdata_ng

import numpy
import Pycluster


def main():




def getData(filename = '/SampleData/expdata_ng'):
    #open the file assuming the data above is in a file called 'dataFile'
    inFile = open('dataFile','r')
    #save the column/row headers (conditions/genes) into an array
    colHeaders = inFile.next().strip().split()[1:]
    rowHeaders = []
    dataMatrix = []

    for line in inFile:
	    data = line.strip().split('\t')
	    rowHeaders.append(data[0])
	    dataMatrix.append([float(x) for x in data[1:]])

    #convert native data array into a numpy array
    dataMatrix = numpy.array(dataMatrix) 
    return dataMatrix
    
    
    

if __name__ == "__main__" :
  main()
