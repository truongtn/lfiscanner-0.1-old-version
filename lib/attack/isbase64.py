import base64
import binascii
def isbase64(noidung):
    if noidung != "":
        try:
            base64.decodestring(noidung)
        except binascii.Error:
            return "khong"
    

    
    
