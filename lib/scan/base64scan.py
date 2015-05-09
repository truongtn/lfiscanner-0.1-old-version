import sys
from phpdetech import *
sys.path.append('../../')
from config import *
sys.path.append('../attack/')
from makelinkattack import *
from isbase64 import *
from httptruong import *
from base64detechanddecode import *
def base64scan(url):
    a = makelinkattack(url)
    b = httptruong(a)
    c = base64detechanddecode(b)
    if c is None:
        
      
        return "safe"
    else:
        return "vul"
  
