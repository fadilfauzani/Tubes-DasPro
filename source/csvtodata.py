def stringtodata(s):
    #s adalah string yang ingin diubah menjadi data
    #dipakai untuk menggantikan fungsi split
    s = s.replace("\n","")
    datas = []
    i = 0
    data = ""
    while (i < len(s)):
        if (s[i]==','):
            datas.append(data)
            data = ""
        else:
            data += s[i]
            if (i == len(s)-1):
                datas.append(data)
        i += 1
    return datas

def csvtodata(csv):
    datas = []
    f = open(csv, "r")
    lines  = f.readlines()
    for i in lines:
        datas.append(stringtodata(i))
    return datas
print(csvtodata("saves/2020/user.csv"))
