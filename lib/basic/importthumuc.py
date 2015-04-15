import sys
sys.path.append('../..')
from config import *
def importthumuc(noidung):
    if noidung[len(noidung)-1]!="/":
        
        noidung+="/"
    string=""
    for i in range(1,len(noidung)):
    
        if noidung[i]!="/":
            string = string + noidung[i]
        
        else:
            DONG2.append(string)
            string = ""

