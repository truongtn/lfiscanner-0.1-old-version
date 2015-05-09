def loaibotag(noidung):
    ketqua=""
    a= noidung.find(">")+1
    b = noidung.find("<",a)
    for i in range(a,b):
        ketqua+=noidung[i]
    return ketqua
    

