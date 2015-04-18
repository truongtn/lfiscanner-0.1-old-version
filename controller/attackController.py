import sys

sys.path.append('../')
from config import *
sys.path.append('../lib/attack/')
from exportfile import *
sys.path.append('../lib/crawler/')
from  gethref import *
from  getdata import *
from phpaccept import *
from urlparse import urlparse
def attackController(url):

    o = urlparse(url)
    HOSTNAME = o.hostname
    gethref(getdata(url))
    for path in PATH:
        full = HOSTNAME+o.path+path
        exportfile(full)
        print full
attackController("http://localhost/dvwa/vulnerabilities/fi/?page=include.php")
        
 
    
