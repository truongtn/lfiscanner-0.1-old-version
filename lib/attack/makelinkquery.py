def makelinkquery(url):
    vitri = url.find("=")
    return url[0:vitri+1]
