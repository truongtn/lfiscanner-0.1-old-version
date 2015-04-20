import sys
sys.path.append('../..')
import os
from config import *
from urlparse import urlparse
from importthumuc import *
from xacdinhfilename import *
from isdir import *
def taothumuc(url):
    o = urlparse(url)
    command ="mkdir "+DIR+"lfiscanner"
    importthumuc(o.path)
    if isdir(DIR+"lfiscanner")!=True:
        
    
        os.system(command)
        print "[INFO]:lfiscanner root folder is created"
    command+="\\"+o.hostname
    if isdir(DIR+"lfiscanner"+"\\"+o.hostname)!=True:
        os.system(command)   
    
      
        print "[INFO]:domain root folder is created"
   
    
    
        
