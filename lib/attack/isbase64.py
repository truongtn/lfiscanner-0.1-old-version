import base64
import binascii
import string
import re
from loaibotag import *
def isbase64(noidung):
    
    noidung=noidung[0:len(noidung)]
    
    result = re.match("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$", noidung)
    
    if len(str(result))>10:
        return "co"
    else:
        return "khong"
