import sys

sys.path.append('../attack/')
from makelinkattack import *
from httptruong import *
def base64scan(url):
    a = makelinkattack(url)
    if httptruong(url)==httptruong(a):
        return "safe"
    else:
        return "vul"
