def getchuoi(noidung,vitri,symbol):
    string=""
    a = noidung.find(symbol,vitri)+1
    b = noidung.find(symbol,a)
    for i in range(a,b):
        string+=noidung[i]
    return string
