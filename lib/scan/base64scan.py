import sys

sys.path.append('../attack/')
from makelinkattack import *
from base64detech import *
from httptruong import *
def base64scan(url):
    a = makelinkattack(url)
    if (httptruong(url)==httptruong(a)) or (base64detech(httptruongfds(urlfsdf)=="khong"):
        return "safe"
    else:
        return "vul"
