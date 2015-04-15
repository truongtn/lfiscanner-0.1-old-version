from base64detech import *
def phpdetech(noidung):
    if(len(noidung)>=5):
        a = noidung[0] + noidung[1] + noidung[2] + noidung[3] + noidung[4]
        if a=="<?php":
            return "co"
    
