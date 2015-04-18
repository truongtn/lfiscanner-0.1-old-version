import sys
sys.path.append('../..')
from config import *
import httplib, urllib
from urlparse import urlparse
def getdata(url):
    o = urlparse(url)
    HEADERS.update({"cookie":COOKIE})
    params = urllib.urlencode(THAMSOS)
    if o.query != "":
        uri = o.path + "?" + o.query
    else:
        uri = o.path
    
    conn = httplib.HTTPConnection(o.hostname)
    conn.request(METHOD, uri, params, HEADERS)
    response = conn.getresponse()
    data = response.read()
    return data
