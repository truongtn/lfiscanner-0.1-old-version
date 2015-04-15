import sys
sys.path.append('../..')
from config import *
from base64detechanddecode import *
from phpdetech import *
from httptruong import *
from urlparse import urlparse
import os
from taothumuc import *
def exportfile(url):
    b = taothumuc(url)
    data = httptruong(url)
    a =  base64detechanddecode(data)
    print b
    f = open(b,"w")
    f.write(a)
exportfile("http://localhost/dvwa/vulnerabilities/fi/?page=include.php")
