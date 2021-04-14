users = []

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

def register() :
    a = open("user.csv", "r")
    data = csvtodata("user.csv")
    lines = len(data)
    a.close()
    kondisi = True

    nama = input("Masukan nama : ")
    username = input("Masukan username : ")
    password = input("Masukan password : ")
    alamat = input("Masukan alamat : ")

    for i in range (lines) : 
        if username == data[1][i] :
            kondisi = False

    if kondisi : 
        users.append([str(lines),username,nama,alamat,password,"user"])
        print ()
        print ("User " + username + " telah berhasil register ke dalam Kantong Ajaib")
    else : 
        print ("Username sudah ada, registrasi gagal")

register()
