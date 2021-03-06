#!/usr/bin/env python

#BIMM 185 EMap project
#In the interest of implementing the pipeline, this non web-implemented prototype is made to see how to communicate between the programs.
#Until I figure out how to make this communicate with the web server, this is how I am doing it.
#Using Baderlab tutorial:
#

#sample input = 12hr_topgenes.txt
import cgi, os

import cgitb; cgitb.enable()
from suds.client import Client

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass


def DAVIDenrich(listF, idType, bgF='', resF='', bgName = 'Background1',listName='List1', category = '', thd=0.1, ct=2):
    message=""
    inputListIds = ','.join(listF.split())
    flagBg = False
    client = Client('http://david.abcc.ncifcrf.gov/webservice/services/DAVIDWebService?wsdl')
    client.service.authenticate('kyung@ucsd.edu')
    message = "User Authentication"

    listType = 0
    #print 'Percentage mapped(list):',
    client.service.addList(inputListIds,idType,listName,listType)
    if flagBg:
        listType = 1
        #print 'Percentage mapped(background):', 
        client.service.addList(inputBgIds,idType,bgName,listType)

    #print 'Use categories:', 
    client.service.setCategories(category) #problems
    
    #chartReport = client.service.getChartReport(thd,ct) #Problems -KY
    chartReport = ""
    
    #chartRow = len(chartReport)
    #print 'Total chart records:',chartRow
    
    resF = "map_scri_job"
    #resF is output filename and directory)-KY
    if len(resF) == 0 or not os.path.exists(resF):
        if flagBg:
            resF = resF + '.withBG.chartReport'
        else:
            resF = resF + '.chartReport'
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
        print '<p>write file:', resF, 'finished!<p>'
        return resF




form = cgi.FieldStorage()

genelist =""
infilename = ''

fileitem = form['file']
if fileitem.file:   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   #open(fn, 'wb').write(fileitem.file.read()) #edited
   linecount = 0
   infilename = fn
   while 1:
        line = fileitem.file.readline().strip()
        genelist = genelist+line
        if not line: break
        linecount = linecount + 1
   message = 'The file "' + fn + ' was uploaded successfully. Line count :  %s'%linecount
       # It's an uploaded file; count lines
   
else:
   message = 'No file was uploaded'
   #return
   
#process lines

#outfile=""
outfile = DAVIDenrich(listF = genelist, idType = 'GENE_SYMBOL', listName = 'list'+infilename, category = 'abcd,BBID,BIOCARTA,COG_ONTOLOGY,INTERPRO,KEGG_PATHWAY,OMIM_DISEASE,PIR_SUPERFAMILY,SMART,SP_PIR_KEYWORDS,UP_SEQ_FEATURE')

print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)
print "<p>File output : %s</p>"%outfile
print "<p>Currently there is an issue with accessing the DAVID Web Service -KY</p>"
print "<a href=\"map_scri_job.chartReport\" target=\"_blank\">Download</a>"
