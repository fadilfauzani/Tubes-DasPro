def stringtodata(s):
    #s adalah string yang ingin diubah menjadi data
    #dipakai untuk menggantikan fungsi split
    s = s.replace("\n","")
    datas = []
    i = 0
    data = ""
    while (i < len(s)):
        if (s[i]==';'):
            datas.append(data)
            data = ""
        else:
            data += s[i]
            if (i == len(s)-1):
                datas.append(data)
        i += 1
    return datas

def csvtodata(csv,type):
    datas = []
    f = open(csv, "r")
    lines  = f.readlines()
    lines.pop(0)
    if (type == "users"):
        for i in lines:
            datas.append((int(stringtodata(i)[0]),stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3],stringtodata(i)[4],stringtodata(i)[5]))
        return datas
    elif(type == "gadgets"):
        for i in lines:
            datas.append((stringtodata(i)[0],stringtodata(i)[1],stringtodata(i)[2],int(stringtodata(i)[3]),stringtodata(i)[4],int(stringtodata(i)[5])))
        return datas
    elif(type == "consums"):
        for i in lines:
            datas.append((stringtodata(i)[0],stringtodata(i)[1],stringtodata(i)[2],int(stringtodata(i)[3]),stringtodata(i)[4]))
        return datas
    elif(type == "riwpin_gadgets"):
        for i in lines:
            datas.append((int(stringtodata(i)[0]),stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3],int(stringtodata(i)[4])))
        return datas
    elif(type == "riwpen_gadgets"):
        for i in lines:
            datas.append((int(stringtodata(i)[0]),stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3]))
        return datas
    elif(type == "riw_consums"):
        for i in lines:
            datas.append((stringtodata(i)[0],stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3],int(stringtodata(i)[4])))
        return datas
print(csvtodata("saves/2021/user.csv","user"))
print(csvtodata("saves/2021/gadget.csv","gadget"))
print(csvtodata("saves/2021/consumable_history.csv","riw_consums"))