def phpaccept(noidung):
    if noidung.find("http://")!=-1 or noidung.find(".php")==-1:
        return "fail"

