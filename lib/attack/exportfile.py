import sys
sys.path.append('../..')
from config import *
from base64detechanddecode import *
from phpdetech import *
from httptruong import *
from urlparse import urlparse
import os
from taothumuc import *
from xacdinhfilename import *
sys.path.append('../thirdparty/')

import fixpath
from colorama import init, Fore, Back, Style
def exportfile(url2):
    init()
    o = urlparse(url2)
    taothumuc(url2)
    data = httptruong(url2)
    
    a =  base64detechanddecode(data)

    print xacdinhfilename(url2)
    b = DIR+"lfiscanner\\"+o.hostname+"\\"+xacdinhfilename(url2)
    try:
        f = open(b,"w")
        f.write(a)
        print (Fore.GREEN+'[SUCCESS]: '+b+' has been exported successfully')
        f.close()
        
    except (RuntimeError, TypeError, NameError,IOError):
        print(Fore.RED+'[WARNING]: "' +b +'" is error, can not be exported\n')
        pass

