import sys
sys.path.append('../..')
from config import *
import httplib, urllib
from urlparse import urlparse
def httptruong(url):
    
    o = urlparse(url)
    HEADERS.update({"cookie":COOKIE})
    params = urllib.urlencode(THAMSOS)
    if o.query != "":
        uri = o.path + "?" + o.query
    else:
        uri = o.path

    conn = httplib.HTTPConnection(o.hostname)
    if HEADER_ENABLE==1:
        conn.request(METHOD, uri, params, HEADERS)
    elif HEADER_ENABLE==0:
        conn.request(METHOD, uri,params)
    
    response = conn.getresponse()
    data = response.read()
    if DEBUG ==1:
        print "Response status: "+str(response.status)
     
    return data

