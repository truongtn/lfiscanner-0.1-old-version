import sys
sys.path.append('../..')
from  config import *
sys.path.append('../basic')
from httptruong import *
def crawler(url):
    httptruong(url).find("href")==-1
    
