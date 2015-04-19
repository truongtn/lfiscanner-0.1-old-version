import sys
sys.path.append('../..')
import os
from config import *
from urlparse import urlparse
from importthumuc import *
from xacdinhfilename import *
def taothumuc(url):
    o = urlparse(url)
    importthumuc(o.path)
  
    command ="mkdir "+DIR+"lfiscanner"
    
    os.system(command)
    print "[INFO]:lfiscanner root folder is created"
    command+="\\"+o.hostname
    os.system(command)
    print "[INFO]:domain root folder is created"
   
    
    
        
