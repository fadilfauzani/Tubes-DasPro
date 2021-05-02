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
    lines.pop(0)        #menghilangan bagian judul
    if (type == "users"):
        while lines[i][0] != 'xxx':     #mark
            datas.append((int(stringtodata(i)[0]),stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3],stringtodata(i)[4],stringtodata(i)[5]))
            i += 1
        return datas
    elif(type == "gadgets"):
        while lines[i][0] != 'xxx':
            datas.append((stringtodata(i)[0],stringtodata(i)[1],stringtodata(i)[2],int(stringtodata(i)[3]),stringtodata(i)[4],int(stringtodata(i)[5])))
            i += 1
        return datas
    elif(type == "consums"):
        while lines[i][0] != 'xxx':
            datas.append((stringtodata(i)[0],stringtodata(i)[1],stringtodata(i)[2],int(stringtodata(i)[3]),stringtodata(i)[4]))
            i+=1
        return datas
    elif(type == "riwpin_gadgets"):
        while lines[i][0] != 'xxx':
            datas.append((int(stringtodata(i)[0]),stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3],int(stringtodata(i)[4])))
            i+=1
        return datas
    elif(type == "riwpen_gadgets"):
        while lines[i][0] != 'xxx':
            datas.append((int(stringtodata(i)[0]),stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3]))
            i+=1
        return datas
    elif(type == "riw_consums"):
        while lines[i][0] != 'xxx':
            datas.append((stringtodata(i)[0],stringtodata(i)[1],stringtodata(i)[2],stringtodata(i)[3],int(stringtodata(i)[4])))
            i+=1
        return datas
print(csvtodata("saves/2021/user.csv","user"))
print(csvtodata("saves/2021/gadget.csv","gadget"))
print(csvtodata("saves/2021/consumable_history.csv","riw_consums"))