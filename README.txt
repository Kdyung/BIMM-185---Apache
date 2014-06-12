Web-Implemented Enrichment Mapping using DAVID Prototype
Web-Implemented Clustering of Gene expression Data
====================
README
Author: Kyra Yung
Date: April 27th, 2014


Description
===




Usage
===
All components accessed via web page index.html
In Apache2


Required Software
===
(All components are included in github directories)
Using DAVID Web client for python requires suds (a lightweight SOAP python client for consuming Web Services). Download and install suds-0.4 (or later version) from https://fedorahosted.org/suds/
Suds requires python-setuptools-devel to install. (Link: https://pypi.python.org/pypi/setuptools#installation-instructions)
scipy python library-

INSTALL
====
Setting up DAVID Client:
    The DAVID Web service requires suds. If suds is not installed, install suds by downloading version 0.4 or later and following the documentation, or go to the python-suds-0.4 folder included and install using setup.py using the documentation.
    If suds is installed, run DAVIDWebService_Client.py with the following command
        >python DAVIDWebService_Client.py
    Evecuting the DAVID Web Service requires registration to the DAVID web site. Currently registered with email 'kyung.ucsd.edu'. The python code DAVIDWebService_Client.py, which initiates the client, is modified for this fact.
    After running python script DAVIDWebService_Client.py in the DAVID_py directory, the program will be able to access the Web service programmatically.
Setting up Clustering Client:
    Install scipy to the python libraries.
    Instructions here: http://www.scipy.org/install.html
    For Linux:
        >sudo apt-get install python-numpy python-scipy
    
All other components included and linked to in project directories.

   


Project Status:
===
5-18-14
Working on connecting to DAVID still, there are some problems such as complications communicating with the DAVID API. It is unknown whether it is preferable to use the web service python client (5-9-14 the service is currently down) or using the url (which returns dubious output).






Directories Included (Descriptions)
===
/sampledata/
 Sample data from Bader Lab for generating an Enrichment map. Data contained is Estradiol-treated MCF7 cells, 12 and 24hrs (Gene Expression Omnibus: GSE11352).
 
/samplecode/
 Code used for testing and learning purposes.
 
/ DAVID_py/
Files for python client of DAVID web service.
NOTE: Web service registered with the email: kyung@ucsd.edu 
DAVIDWEbService_Client.py was edited to reflect this and executed.

/js/ and /fonts/
Both initally directories belonging to the Bootstrap library. Also contain other scripts used for building web client.



Implemented Components:
D3.js
A java application that is a web page element manipulator. Used to bind web page elements.
Copyright (c) 2010-2014, Michael Bostock
All rights reserved.







Citations and References
======
DAVID Web Client:
Xiaoli Jiao, Brad T. Sherman, Da Wei Huang, Robert Stephens, Michael W. Baseler, H. Clifford Lane, Richard A. Lempicki DAVID-WS: A Stateful Web Service to Facilitate Gene/Protein List Analysis Bioinformatics 2012 doi:10.1093/bioinformatics/bts251

Suds:
 
Bootstrap:
 
D3:
