#!/usr/bin/python
__author__ = 'kdyung'


#BIMM 185 EMap project
#In the interest of implementing the pipeline, this non web-implemented prototype is made to see how to communicate between the programs.
#Until I figure out how to make this communicate with the web server, this is how I am doing it.
#Using Baderlab tutorial:
#

#sample input = 12hr_topgenes.txt

import sys,os, cgi

try:
	from optparse import OptionParser
except:
	print "Module optparse not found: you need Python version 2.3 or later"
	sys.exit(-1)
version = '0.1'

"""Step 1: Generate DAVID output files

#    Select Official Gene Symbol in Step 2: Select Identifier

    Select Gene list in Step 3: Select List Type

    Click Submit list
    Select species: Homo sapiens

    Click Functional Annotation Chart - Screen shot of where to get DAVID output chart
    Download file - This is the file you can use in Enrichment Map (Dataset 1 or 2:Enrichment Results) """
    
    
# 	http://david.abcc.ncifcrf.gov/api.jsp?type=xxxxx&ids=XXXXX,XXXXX,XXXXXX,&tool=xxxx&annot=xxxxx,xxxxxx,xxxxx,
###http://david.abcc.ncifcrf.gov/content.jsp?file=DAVID_API.html

#http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
#Downloading a file using python
    
    
    
def main():
    print "Executing map_scri.py ...."
    (options,args) =  parse_command_line()
    
#    Step 1: Generate DAVID output files
    #Test input:
    infilename = 'DavidTutorial/12hr_topgenes.txt'
    infilename = 'DAVID_py/list1.txt'
    
    #following reads list of genes seperated by newline
    genelist = []
    for i in open(infilename,'r').readlines():
        genelist.extend(i.strip().split())
        print i.strip().split()
    print "Number of genes : %s"%len(genelist)
    print genelist[20]
#   Cytoscape instruction data
    gene_identifier = "OFFFICIAL_GENE_SYMBOL"
    species = 'Homo sapiens'
    list_type = 'Gene list'
    
    
    ##Generating DAVID data using url
    
    list_type = 'type=ENTREZ_GENE_ID'
    tool = '&tool=list'
    ids_str = '&ids='
    annot_str = '&annot=xxxxx,xxxxxx,xxxxx,'
    for i in genelist:
        #genes given in OFFFICIAL_GENE_SYMBOL need to convert genes to id number
        ids_str = '%s%s,'%(ids_str,i)
    url = "http://david.abcc.ncifcrf.gov/api.jsp?%s%s%s"%(list_type,ids_str,tool)
    print url
    
    #Download Functional Annotation Chart

    #do stuff

    
    
    
    return

def runDAVID():
    return


def parse_command_line():
    usage = "Poot."
    parser = OptionParser(usage=usage,version="%prog "+version)
   
    parser.add_option("-m","--3dmap",action="store",dest="map3d",metavar="<3D Map Path>",type='string',help="The path to the 3D map used in input (REQUIRED).",default='3D Map')
    
    (options, args)=parser.parse_args()
    if len(sys.argv)<1: 
        parser.print_help()
        sys.exit(-1)
 
    return (options,args)

if __name__ == "__main__" :
  main()
