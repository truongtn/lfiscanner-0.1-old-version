import sys
sys.path.append('../..')
from config import *
from isbase64 import *
import base64
from xacdinhdong import *
from loaibotag import *
def base64detechanddecode(noidung):
   
    DONG=xacdinhdong(noidung)
    for i in range(0,len(DONG)):
        for j in range(0,len(DONG[i])):
            try:
                
                DONG[i] = DONG[i].replace("<td>","")
                DONG[i] = DONG[i].replace("</td>","")
                if ord(DONG[i][j])>126 or ord(DONG[i][j])<33:
                    DONG[i]=DONG[i].replace(DONG[i][j],"")
            except:
                nope=1
  
  
        
        
        if DEBUG==1:
            dongdebug = DONG[i]
            print "batdau~~~"+dongdebug
            print "~~~kethuc"
        
        if isbase64(DONG[i])=="co":
            
            
           
            
            return base64.decodestring(DONG[i])
    
