import sys
sys.path.append('../..')
from config import *

def xacdinhdong(noidung):
    
    noidung=noidung+"\n"
    string=""

    for i in range(0,len(noidung)):
    
        if( (noidung[i]!="\n") and (noidung[i]!=" ")):
            string = string + noidung[i]
        
        else:
            if( noidung[i]!="\n" or noidung[i]!=" "):
                DONG.append(string)
                string = ""
        

