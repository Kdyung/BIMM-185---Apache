#!/usr/bin/python
__author__ = 'kdyung'


#BIMM 185 EMap project
#In the interest of implementing the pipeline, this non web-implemented prototype is made to see how to communicate between the programs.
#Until I figure out how to make this communicate with the web server, this is how I am doing it.
#Using Baderlab tutorial:
#
import sys,os, cgi

try:
	from optparse import OptionParser
except:
	print "Module optparse not found: you need Python version 2.3 or later"
	sys.exit(-1)
version = '0.1'


def main():
    (options,args) =  parse_command_line()
    #do stuff
    print "EMAP"
    
    
    return



def parse_command_line():
    usage = "Poot."
    parser = OptionParser(usage=usage,version="%prog "+version)
   
    parser.add_option("-m","--3dmap",action="store",dest="map3d",metavar="<3D Map Path>",type='string',help="The path to the 3D map used in input (REQUIRED).",default='3D Map')
    
    (options, args)=parser.parse_args()
    if len(sys.argv)<2 and len(options.filelist)==0: 
        parser.print_help()
        sys.exit(-1)
 
    return (options,args)

if __name__ == "__main__" :
  main()
