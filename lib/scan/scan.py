import fixpath
from colorama import init, Fore, Back, Style

from base64scan import *
def scan(url):
    init()
    if base64scan(url)=="vul":
        print(Fore.YELLOW+'[INFO]: This path can be exploited by filter [BASE64 CONVERT]')
        return "base64scan"
    
