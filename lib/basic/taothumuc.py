import sys
sys.path.append('../..')
import os
from config import *
from urlparse import urlparse
from importthumuc import *
def taothumuc(url):
    o = urlparse(url)
    importthumuc(o.path)
  
    command ="mkdir "+DIR+"lfiscanner"
    
    os.system(command)
    command+="\\"+o.hostname
    os.system(command)
    for i in range(0,len(DONG2)):
        command+="\\"+DONG2[i]
        os.system(command)
        print command
        
    FILENAME = command + "\\"
    
    vitri = url.find("=")
    if url.find("=",vitri+1)!=-1:
        vitri = url.find("=",vitri+1)
    for i in range(vitri+1,len(url)):
        FILENAME = FILENAME + url[i]
    FILENAME = FILENAME[6:]
    return FILENAME
    
    
        
