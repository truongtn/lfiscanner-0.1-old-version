import sys
sys.path.append('../..')
from  config import *
from isbase64 import *
import base64
from xacdinhdong import *
from phpdetech import *
def base64detech(noidung):
    xacdinhdong(noidung)
    for i in range(0,len(DONG)):
        #if isbase64(DONG[i])!="khong" and phpdetech(DONG[i])=="co":

            #return base64.decodestring(DONG[i])
        if isbase64(DONG[i])!="khong":

            return base64.decodestring(DONG[i])
