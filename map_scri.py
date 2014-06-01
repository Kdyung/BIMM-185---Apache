#!/usr/bin/python
__author__ = 'kdyung'


#BIMM 185 EMap project
#In the interest of implementing the pipeline, this non web-implemented prototype is made to see how to communicate between the programs.
#Until I figure out how to make this communicate with the web server, this is how I am doing it.
#Using Baderlab tutorial:
#

#sample input = 12hr_topgenes.txt

import sys,os, cgi
import web


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
    infilename = options.inlist
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
    
    
    #Download Functional Annotation Chart
    #do stuff
    DAVIDenrich(listF = infilename, idType = 'AFFYMETRIX_3PRIME_IVT_ID', listName = 'list1', category = 'abcd,BBID,BIOCARTA,COG_ONTOLOGY,INTERPRO,KEGG_PATHWAY,OMIM_DISEASE,PIR_SUPERFAMILY,SMART,SP_PIR_KEYWORDS,UP_SEQ_FEATURE')

    return


#David Python client contains code ChartReport.py that is edited to use for development. This method is borrowed from CHartReport and requires connecting to the client to work
#Requires running DAVIDWebService_Client.py run beforehand
# by courtesy of HuangYi @ 20110424
def DAVIDenrich(listF, idType, bgF='', resF='', bgName = 'Background1',listName='List1', category = '', thd=0.1, ct=2):
    from suds.client import Client
    import os
    if len(listF) > 0 and os.path.exists(listF):
        inputListIds = ','.join(open(listF).read().split('\n'))
        print 'List loaded.'        
    else:
        print 'No list loaded.'
        raise
    flagBg = False
    if len(bgF) > 0 and os.path.exists(bgF):
        inputBgIds = ','.join(open(bgF).read().split('\n'))
        flagBg = True
        print 'Use file background.'
    else:
        print 'Use default background.'
    client = Client('http://david.abcc.ncifcrf.gov/webservice/services/DAVIDWebService?wsdl')
    print 'User Authentication:',client.service.authenticate('kyung@ucsd.edu')
    listType = 0
    print 'Percentage mapped(list):', client.service.addList(inputListIds,idType,listName,listType)
    if flagBg:
        listType = 1
        print 'Percentage mapped(background):', client.service.addList(inputBgIds,idType,bgName,listType)
    print 'Use categories:', client.service.setCategories(category)
    chartReport = client.service.getChartReport(thd,ct)
    chartRow = len(chartReport)
    print 'Total chart records:',chartRow
    
    if len(resF) == 0 or not os.path.exists(resF):
        if flagBg:
            resF = listF + '.withBG.chartReport'
        else:
            resF = listF + '.chartReport'
    with open(resF, 'w') as fOut:
        fOut.write('Category\tTerm\tCount\t%\tPvalue\tGenes\tList Total\tPop Hits\tPop Total\tFold Enrichment\tBonferroni\tBenjamini\tFDR\n')
        for row in chartReport:
            rowDict = dict(row)
            categoryName = str(rowDict['categoryName'])
            termName = str(rowDict['termName'])
            listHits = str(rowDict['listHits'])
            percent = str(rowDict['percent'])
            ease = str(rowDict['ease'])
            Genes = str(rowDict['geneIds'])
            listTotals = str(rowDict['listTotals'])
            popHits = str(rowDict['popHits'])
            popTotals = str(rowDict['popTotals'])
            foldEnrichment = str(rowDict['foldEnrichment'])
            bonferroni = str(rowDict['bonferroni'])
            benjamini = str(rowDict['benjamini'])
            FDR = str(rowDict['afdr'])
            rowList = [categoryName,termName,listHits,percent,ease,Genes,listTotals,popHits,popTotals,foldEnrichment,bonferroni,benjamini,FDR]
            fOut.write('\t'.join(rowList)+'\n')
        print 'write file:', resF, 'finished!'

def getDAVIDurl(genelist = []):
        ##Generating DAVID data using url
    list_type = 'type=ENTREZ_GENE_ID'
    tool = '&tool=list'
    ids_str = '&ids='
    annot_str = '&annot=xxxxx,xxxxxx,xxxxx,'
    for i in genelist:
        #genes given in OFFFICIAL_GENE_SYMBOL need to convert genes to id number
        ids_str = '%s%s,'%(ids_str,i)
    url = "http://david.abcc.ncifcrf.gov/api.jsp?%s%s%s"%(list_type,ids_str,tool)
    return url
    

def parse_command_line():
    usage = "Poot."
    parser = OptionParser(usage=usage,version="%prog "+version)
   
    parser.add_option("-l","--list",action="store",dest="inlist",metavar="<Gene List Input>",type='string',help="The path to the input gene list (for DAVID).",default='DavidTutorial/12hr_topgenes.txt')
    
    (options, args)=parser.parse_args()
    if len(sys.argv)<1: 
        parser.print_help()
        sys.exit(-1)
 
    return (options,args)

if __name__ == "__main__" :
  main()
