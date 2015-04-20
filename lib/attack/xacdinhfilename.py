def xacdinhfilename(url):
    if url.find("../")!=-1:
        vitri = url.rfind("../")+3
        return url[vitri:]
    else:
        vitri = url.rfind("=")+1
        return url[vitri:]
