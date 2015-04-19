import sys
import string
sys.path.append('../')
from config import *
sys.path.append('../lib/attack/')
from exportfile import *
sys.path.append('../lib/crawler/')
from  gethref import *
from  getdata import *
from phpaccept import *
from urlparse import urlparse
sys.path.append('../lib/attack/')
from makelinkattack import *
sys.path.append('../lib/attack/')
from makelinkquery import *
from xacdinhfilename import *
def attackController(url):
    goc =  makelinkattack(url)
    exportfile(goc)
    o = urlparse(url)
    linkquery = makelinkquery(url)
    print linkquery
    HOSTNAME = o.hostname
    
    gethref(getdata(url))
    print PATH
    for path in PATH:
        
        full = linkquery +path
        #print full
        #full = full.repalce("/","\\")
        full = makelinkattack(full)
        print full
        #print url
        exportfile(full)
        
attackController("http://localhost/dvwa/vulnerabilities/fi/?page=include.php")
        
 
    
