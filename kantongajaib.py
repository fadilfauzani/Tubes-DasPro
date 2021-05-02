import os
import os.path
import time
import argparse
import datetime
from datetime import datetime
import sys
#Program kantong ajaib

#Kamus
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

def datatostring(data):
    s = ""
    for i in range (len(data)):
        s += str(data[i])
        if (i != len(data) - 1):
            s += ";"
    return s+ '\n'

def csvtodata(csv,type):
    datas = []
    f = open(csv, "r")
    lines  = f.readlines()
    lines.pop(0)
    i = 0
    if (type == "users"):
        while lines[i] != '9999;mark;mark;mark;mark;mark':
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],stringtodata(lines[i])[4],stringtodata(lines[i])[5]])
            i+=1
            #(id,username,nama,alamat,password,role)
        return datas
    elif(type == "gadgets"):
        while lines[i] != 'mark;mark;mark;9999;Z;9999':
            datas.append([stringtodata(lines[i])[0],stringtodata(lines[i])[1],stringtodata(lines[i])[2],int(stringtodata(lines[i])[3]),stringtodata(lines[i])[4],int(stringtodata(lines[i])[5])])
            i+=1
            #(id,nama,desk,jumlah,rarity,tahun_ditemukan)
        return datas
    elif(type == "consums"):
        while lines[i] != 'mark;mark;mark;9999;mark':
            datas.append([stringtodata(lines[i])[0],stringtodata(lines[i])[1],stringtodata(lines[i])[2],int(stringtodata(lines[i])[3]),stringtodata(lines[i])[4]])
            i+=1
            #(id,nama,desk,jumlah,rarity)
        return datas
    elif(type == "riwpin_gadgets"):
        while lines[i] != '9999;mark;mark;mark;9999;True':
            boolean = True if (stringtodata(lines[i])[5] == 'True') else False
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],int(stringtodata(lines[i])[4]),boolean])
            i+=1
            #(id,id peminjan, id gadget, tanggal, jumlah, is returned)
        return datas
    elif(type == "riwpen_gadgets"):
        while lines[i] != '9999;9999;mark;9999':
            datas.append([int(stringtodata(lines[i])[0]),int(stringtodata(lines[i])[1]),stringtodata(lines[i])[2],int(stringtodata(lines[i])[3])])
            i+=1
            #(id,id_peminjaman, tanggal,jumlah yang dikembalikan)
        return datas
    elif(type == "riw_consums"):
        while lines[i] != '9999;mark;mark;mark;9999':
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],int(stringtodata(lines[i])[4])])
            i+=1
            #(id,id pengambil, id consum, tanggal, jumlah)
        return datas
    elif(type == "riw_gachas"):
        while lines[i] != '9999;mark;mark;mark;9999':
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],int(stringtodata(lines[i])[4])])
            i+=1
            #(id,id penukar,id consum,tanggal, jumlah)
        return datas

def load(temp_path):        #F14
    global path, users, gadgets, consums, riw_consums, riwpin_gadgets, riwpen_gadgets, riw_gachas
    path = 'saves/' + temp_path
    users = csvtodata(path+'/user.csv','users')
    gadgets = csvtodata(path+'/gadget.csv','gadgets')
    consums = csvtodata(path+'/consumable.csv','consums')
    riw_consums = csvtodata(path+'/consumable_history.csv','riw_consums')
    riwpin_gadgets = csvtodata(path+'/gadget_borrow_history.csv','riwpin_gadgets')
    riwpen_gadgets = csvtodata(path+'/gadget_return_history.csv','riwpen_gadgets')
    riw_gachas = csvtodata(path+'/gacha_history.csv','riw_gachas')

def login() :               #F02
    global userid, role
    akses = False

    username = input("\nMasukan username : ")
    password = input("Masukan password : ")

    for i in range (len(users)) :
        if username == users[i][1] and hash(password,username) == users[i][4] :
            akses = True
            role = users[i][5]

    if akses : 
        print()
        print("Halo " + username + "! Selamat datang di Kantong Ajaib.")
        userid = username
    else :
        print()
        print("Username atau password salah, silahkan coba lagi.")   

def numtochr(num):
    global chrs
    return(chrs[num])
def idxchr(chr):
    global chrs
    k = 0
    while (k < len(chrs) and chrs[k] != chr ):
        k += 1
    if (k >= len(chrs)):
        k = k % 72
    return k
def listtostring(l):
    s = ''
    for i in l:
        s += i
    return s
def hash(s,key):
    global chrs
    has = []
    numkey = 0
    for i in range(len(key)):
        numkey += idxchr(key[i])
    for i in range (len(s)):
        has.append(numtochr(idxchr(s[i])*(i+numkey) % 72))
    return listtostring(has)

def register() :            #F01
    Userada = False

    nama = (input("Masukan nama : ")).title()
    username = input("Masukan username : ")
    password = input("Masukan password : ")
    alamat = input("Masukan alamat : ")

    for i in range (len(users)) : 
        if username == users[i][1] :
            Userada = True

    if (not(Userada)) : 
        users.append([len(users)+1,username,nama,alamat,hash(password,username),"user"])
        print()
        print("User " + username + " telah berhasil register ke dalam Kantong Ajaib")
    else : 
        print("Username sudah ada, registrasi gagal")

def save():                 #F15
    path = input("Masukkan nama folder penyimpanan: ")
    path = 'saves/' + path
    try:
        os.mkdir(path)
        
    except:
        pass
    user = open(path+"/user.csv","w")
    user.write("id;username;nama;alamat;password;role\n")
    gadget = open(path+"/gadget.csv","w")
    gadget.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
    consum = open(path+"/consumable.csv","w")
    consum.write("id;nama;deskripsi;jumlah;rarity\n")
    riw_consum = open(path+"/consumable_history.csv","w")
    riw_consum.write("id;id_pengambil;id_consumable;tanggal_pengambilan;jumlah\n")
    riwpin_gadget = open(path+ "/gadget_borrow_history.csv", "w")
    riwpin_gadget.write("id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned\n")
    riwpen_gadget = open(path+ "/gadget_return_history.csv","w")
    riwpen_gadget.write("id;id_peminjaman;tanggal_pengembalian;jumlah\n")
    riw_gacha = open(path+ "/gacha_history.csv","w")
    riw_gacha.write("id;id_penukar;id_consumable;tanggal_penukaran;jumlah\n")
    for i in users:
        user.write(datatostring(i))
    for i in gadgets:
        gadget.write(datatostring(i))
    for i in consums:
        consum.write(datatostring(i))
    for i in riw_consums:
        riw_consum.write(datatostring(i))
    for i in riwpin_gadgets:
        riwpin_gadget.write(datatostring(i))
    for i in riwpen_gadgets:
        riwpen_gadget.write(datatostring(i))
    for i in riw_gachas:
        riw_gacha.write(datatostring(i))
    user.write('9999;mark;mark;mark;mark;mark')
    gadget.write('mark;mark;mark;9999;Z;9999')
    consum.write('mark;mark;mark;9999;mark')
    riw_consum.write('9999;mark;mark;mark;9999')
    riwpin_gadget.write('9999;mark;mark;mark;9999;True')
    riwpen_gadget.write('9999;9999;mark;9999')
    riw_gacha.write('9999;mark;mark;mark;9999')
    user.close()
    gadget.close()
    consum.close()
    riw_consum.close()
    riwpin_gadget.close()
    riwpen_gadget.close()
    riw_gacha.close()

def idxID(id):              
    global gadgets, consums
    idx = -1
    if (id[0] == 'G'):
        for i in range(len(gadgets)):
            if (id == gadgets[i][0]):
                idx = i
    else:
        for i in range(len(consums)):
            if (id == consums[i][0]):
                idx = i
    return idx

def idValid(id):    #skema validasi input id
    if (id[0] == 'G' or id[0] == 'C'):
        return True
    else:
        return False

def idada(id):
    if (id[0] == 'G'):
        for i in gadgets:
            if (id == i[0]):
                return True
        return False
    else:
        for i in consums:
            if (id == i[0]):
                return True
        return False

def rarityValid(r):
    if (r == 'C' or r == 'B' or r == 'A' or r == 'S' ):
        return True
    else:
        return False

def tambahitem():           #F05
    global gadgets, consums
    id = input("Masukan ID: ")
    if(idValid(id)):
        if (idada(id)):
            print("\nGagal menambahkan item karena ID sudah ada.")
        else:
            nama = input("Masukan Nama: ")
            desk = input("Masukan Deskripsi: ")
            jum = input("Masukan Jumlah: ")
            while (int(jum) < 0):
                print("Jumlah salah, masukkan jumlah yang benar (>= 0)")
                jum = input("Masukan Jumlah: ")
            rarity = input("Masukan Rarity: ")
            if (rarityValid(rarity)):
                isGadget = (id[0] == 'G') #ekspresi boolean
                if (isGadget):
                    tahun = input("Masukan tahun ditemukan: ")
                    gadgets.append([id,nama,desk,jum,rarity,tahun])
                else:   #kalau bkan gadget maka consumbales
                    consums.append([id,nama,desk,jum,rarity])
                print("\nItem telah berhasil ditambahkan ke database.")
            else:
                print("\nInput rarity tidak valid!")
    else:
        print("\nGagal menambahkan item karena ID tidak valid.")

def hapusitem():            #F06
    global gadgets, consums
    id = input("Masukan ID item: ")
    if (idada(id)):
        hapus = input("Apakah anda yakin ingin menghapus " + gadgets[idxID(id)][1] + " (Y/N)? : ")
        while (hapus != 'y' and hapus != 'Y' and hapus != 'N' and hapus != 'n'):
            hapus = input("Next (Y/N)? : ")
        if (hapus == 'Y' or hapus == 'y'):
            if (id[0] == 'G'):
                gadgets.pop(idxID(id))
            else:
                consums.pop(idxID(id))
            print()
            print("Item telah berhasil dihapus dari database.")
        else:
            print("Item gagal dihapus dari database.")
    else:
        print("Tidak ada item dengan ID tersebut.")

def ubahjum():              #F07
    global gadgets, consums
    id = input('Masukan ID: ')
    if (idada(id)):
        jumlah = int(input('Masukan Jumlah: '))
        if (id[0] == 'G'):
            jumasli = int(gadgets[idxID(id)][3])
            if (jumlah > 0):
                gadgets[idxID(id)][3] = str(jumasli + jumlah)
                print(f'{jumlah} {gadgets[idxID(id)][1]} berhasil ditambahkan. Stok sekarang: {gadgets[idxID(id)][3]}')
            elif (jumlah == 0) :
                print(f'{gadgets[idxID(id)][1]} tidak ditambahkan / dibuang. Stok sekarang: {gadgets[idxID(id)][3]}')

            else:
                if (jumasli + jumlah < 0):
                    print(f'{-jumlah} {gadgets[idxID(id)][1]} gagal dibuang karena stok kurang. Stok sekarang: {gadgets[idxID(id)][3]} < {-jumlah}')
                else:
                    gadgets[idxID(id)][3] = str(jumasli + jumlah)
                    print(f'{-jumlah} {gadgets[idxID(id)][1]} berhasil dibuang. Stok sekarang: {gadgets[idxID(id)][3]}')
        else:
            jumasli = int(consums[idxID(id)][3])
            if (jumlah > 0):
                consums[idxID(id)][3] = str(jumasli + jumlah)
                print(f'{jumlah} {consums[idxID(id)][1]} berhasil ditambahkan. Stok sekarang: {consums[idxID(id)][3]}')
            else:
                if (jumasli + jumlah < 0):
                    print(f'{-jumlah} {consums[idxID(id)][1]} gagal dibuang karena stok kurang. Stok sekaran: {consums[idxID(id)][3]} < {-jumlah}')
                else:
                    consums[idxID(id)][3] = str(jumasli + jumlah)
                    print(f'{-jumlah} {consums[idxID(id)][1]} berhasil dibuang. Stok sekarang: {consums[idxID(id)][3]}')
    else:
        print("Tidak ada item dengan ID tersebut!")

def carirarity() :          #F03
    available = False
    rarity = input("Masukan rarity : ")
    print()
    print("========= HASIL PENCARIAN ==========")

    for i in range (len(gadgets)) :
        if rarity == gadgets[i][4] :
            print_data_gadget(i)
            available = True

    if not(available) :
        print()
        print("Tidak ada gadget dengan rarity", rarity)

def print_data_gadget(i) :
    print()
    print("Nama            : " + gadgets[i][1])
    print("Deskripsi       : " + gadgets[i][2])
    print("Jumlah          : " + str(gadgets[i][3]))
    print("Rarity          : " + gadgets[i][4])
    print("Tahun Ditemukan : " + str(gadgets[i][5]))

def caritahun() :           #F04
    available = False
    tahun = int(input("Masukan tahun : "))
    kategori = input("Masukan kategori : ")
    print()
    print("========= HASIL PENCARIAN ==========")

    for i in range (len(gadgets)) :
        if kategori == "=" and gadgets[i][5] == tahun :
            print_data_gadget(i)
            available = True
        elif kategori == ">" and gadgets[i][5] > tahun :
            print_data_gadget(i)
            available = True
        elif kategori == "<" and gadgets[i][5] < tahun :
            print_data_gadget(i)
            available = True
        elif kategori == ">=" and gadgets[i][5] >= tahun :
            print_data_gadget(i)
            available = True
        elif kategori == "<=" and gadgets[i][5] <= tahun :
            print_data_gadget(i)
            available = True

    if not(available) :
        print()
        print("Gadget dengan ketentuan tersebut tidak tersedia.")

def printBorrowGadget(arr):
    for i in range (len(arr)):
        print("{}. {} (x{})".format(arr[i][0],arr[i][2],arr[i][3]))

def borrowGadget():
    global gadgets, userid, riwpin_gadgets, riwpen_gadgets
    arr = []
    for i in range (len(riwpin_gadgets)):
        if ((riwpin_gadgets[i][1] == userid) and (riwpin_gadgets[i][5] == False)):
            for j in range (len(gadgets)):
                if (riwpin_gadgets[i][2] == gadgets[j][0]):
                    gadget_index = j
                    break
            total_return = 0
            for j in range (len(riwpen_gadgets)):
                if (riwpen_gadgets[j][1] == (i + 1)):
                    total_return = total_return + riwpen_gadgets[j][3]
            gadget_left = riwpin_gadgets[i][4] - total_return
            arr.append([len(arr)+1,riwpin_gadgets[i][0],gadgets[gadget_index][1],gadget_left])
    return arr

def isBorrowNumberValid(temp_riwpin_gadgets,borrow_number):
    global riwpin_gadgets, userid
    if ((borrow_number > 0) and (borrow_number <= len(temp_riwpin_gadgets))):
        return True
    else :
        return False

def isDateValid(date):
    bool = True
    try:
        datetime.strptime(date, '%d/%m/%Y')        
    except ValueError:
        bool = False
    return bool

def isThereBorrowedGadget():
    global userid, riwpin_gadgets
    bool = False
    for i in range (len(riwpin_gadgets)):
        if (riwpin_gadgets[i][1] == userid) and (riwpin_gadgets[i][5] == False):
            bool = True
            break
    return bool

def isReturnAmountValid(gadget_left,return_amount):
    if (return_amount <= gadget_left) and (return_amount > 0):
        return True
    else:
        return False

def kembalikan():           #F09
    global userid, gadgets, riwpin_gadgets, riwpen_gadgets

    if (not(isThereBorrowedGadget())):
        print("Tidak ada riwayat peminjaman")
    else:
        temp_riwpin_gadgets = borrowGadget()
        printBorrowGadget(temp_riwpin_gadgets)
        print()
        borrow_number = int(input("Masukan nomor peminjaman: "))
        return_date = input("Tanggal pengembalian: ")
        return_amount = int(input("Jumlah pengembalian: "))

        if (isBorrowNumberValid(temp_riwpin_gadgets,borrow_number) and isDateValid(return_date)):
            gadget_left = temp_riwpin_gadgets[borrow_number-1][3]
            if (isReturnAmountValid(gadget_left,return_amount)):
                gadget_index = idxID(riwpin_gadgets[temp_riwpin_gadgets[borrow_number-1][1]-1][2])
                gadget_name = gadgets[gadget_index][1]
                gadgets[gadget_index][3] = gadgets[gadget_index][3] + return_amount
                if (gadget_left == return_amount) :
                    riwpin_gadgets[temp_riwpin_gadgets[borrow_number-1][1]-1][5] = True
                riwpen_gadgets.append([len(riwpen_gadgets)+1,temp_riwpin_gadgets[borrow_number-1][1],return_date,return_amount])
                print("\nItem {} (x{}) telah dikembalikan.".format(gadget_name, return_amount))
            else:
                print("\nGagal melakukan pengembalian karena jumlah pengembalian tidak valid.")
        else:
            if (not(isBorrowNumberValid(temp_riwpin_gadgets,borrow_number)) and not(isDateValid(return_date))):
                print("\nGagal melakukan pengembalian karena nomor peminjaman dan tanggal pengembalian tidak valid.")
            elif (not(isBorrowNumberValid(temp_riwpin_gadgets,borrow_number))):
                print("\nGagal melakukan pengembalian karena nomor peminjaman tidak valid.")
            elif (not(isDateValid(return_date))):
                print("\nGagal melakukan pengembalian karena tanggal pengembalian tidak valid.")

def isConsumableIDValid(item_ID):
    global consums
    bool = False
    i = 0
    while (bool == False) and (i < len(consums)):
        if (consums[i][0] == item_ID):
            bool = True
        i = i + 1
    return bool

def isQuantityValidC(consumable_index,take_quantity):
    global consums
    if (consums[consumable_index][3] >= take_quantity) and (take_quantity > 0):
        return True
    else:
        return False

def minta():                #F10
    global userid, riw_consums, consums
    item_ID = input("Masukan ID item: ")
    take_quantity = int(input("Jumlah: "))
    take_date = input("Tanggal permintaan: ")
    if (isConsumableIDValid(item_ID) and isDateValid(take_date)):
        consumable_index = idxID(item_ID)
        if (isQuantityValidC(consumable_index,take_quantity)):
            consums[consumable_index][3] = consums[consumable_index][3] - take_quantity
            riw_consums.append([(len(riw_consums) + 1),userid,item_ID,take_date,take_quantity])
            consumable_name = consums[consumable_index][1]
            print("\nItem {} (x{}) telah berhasil diambil!".format(consumable_name,take_quantity))
        else:
            print("\nGagal melakukan permintaan karena jumlah permintaan item tidak valid.")
    else:
        if (not(isConsumableIDValid(item_ID)) and not(isDateValid(take_date))):
            print("\nGagal melakukan permintaan karena ID item dan tanggal tidak valid.")
        else:
            if (not(isConsumableIDValid(item_ID))):
                print("\nGagal melakukan permintaan karena ID item tidak valid.")
            if (not(isDateValid(take_date))):
                print("\nGagal melakukan permintaan karena tanggal tidak valid.")

def isItemIDValid(item_ID):
    global gadgets
    i = 0
    bool = False
    while (i < len(gadgets) and (bool == False)):
        if (gadgets[i][0] == item_ID):
            bool = True
        i = i + 1
    return bool

def isReturned(item_ID):
    global riwpin_gadgets, userid
    bool = True
    for i in range (len(riwpin_gadgets)):
        if (userid == riwpin_gadgets[i][1]) and (item_ID == riwpin_gadgets[i][2]):
            bool = riwpin_gadgets[i][5]
    return bool

def isQuantityValidG(gadget_index,borrow_quantity):
    global gadgets
    if (gadgets[gadget_index][3] >= borrow_quantity) and (borrow_quantity > 0):
        return True
    else :
        return False

def pinjam():               #F08
    global gadgets, riwpin_gadgets, userid
    item_ID = input("Masukan ID item: ")
    borrow_date = input("Tanggal peminjaman: ")
    borrow_quantity = int(input("Jumlah peminjaman: "))

    if (isItemIDValid(item_ID) and isDateValid(borrow_date)):
        if (isReturned(item_ID)):
            gadget_index = idxID(item_ID)
            if (isQuantityValidG(gadget_index,borrow_quantity)):
                gadgets[gadget_index][3] = gadgets[gadget_index][3] - borrow_quantity
                riwpin_gadgets.append([(len(riwpin_gadgets) + 1),userid,item_ID,borrow_date,borrow_quantity,False])
                gadget_name = gadgets[gadget_index][1]
                print("\nItem {} (x{}) berhasil dipinjam!".format(gadget_name,borrow_quantity))
            else :
                print("\nGagal melakukan peminjaman karena jumlah pinjaman tidak valid.")
        else :
            print("\nGagal melakukan peminjaman karena item belum dikembalikan.")
    else :
        if (not(isItemIDValid(item_ID)) and not(isDateValid(borrow_date))):
            print("\nGagal melakukan peminjaman karena ID item dan tanggal peminjaman tidak valid.")
        elif (not(isItemIDValid(item_ID))):
            print("\nGagal melakukan peminjaman karena ID item tidak valid.")
        elif (not(isDateValid(borrow_date))):
            print("\nGagal melakukan peminjaman karena tanggal peminjaman tidak valid.") 

def idxriw(id):
    global riwpin_gadgets
    idx = -1
    for i in range(len(riwpin_gadgets)):
        if (id == riwpin_gadgets[i][0]):
            idx = i
    return idx

def riwayatkembali():       #F12
    global riwpin_gadgets, riwpen_gadgets, gadgets
    data_borrow = sorted(riwpen_gadgets, key=lambda row: datetime.strptime(row[2],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Pengembalian          : "+ str(data_borrow[i][0]))
        print("Nama pengambil           : "+ str(carinama(riwpin_gadgets[idxriw(data_borrow[i][1])][1])))
        print("Nama Gadget              : "+ gadgets[idxID(riwpin_gadgets[idxriw(data_borrow[i][1])][2])][1])
        print("Tanggal Pengembalian     : " + data_borrow[i][2])
        print("Jumlah yang dikembalikan : "+ str(data_borrow[i][3]))
        print()
        j += 1
        i += 1
        if (j == 5 and i != len(data_borrow)):
            mau = input("Next (Y/N)? : ")
            while (mau != 'y' and mau != 'Y' and mau != 'N' and mau != 'n'):
                mau = input("Next (Y/N)? : ")
            if (mau == 'Y' or mau == "y"):
                j = 0
    if (i == 0):
        print("Riwayat pengembalian gadget masih kosong.")

def carinama(userid):
    global users
    nama = ''
    for i in range(len(users)):
        if (userid == users[i][1]):
            nama = users[i][2]
    return nama

def riwayatambil():         #F13
    global riw_consums, consums
    data_borrow = sorted(riw_consums, key=lambda row: datetime.strptime(row[3],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Pengambilan       : "+ str(data_borrow[i][0]))
        print("Nama pengambil       : "+ carinama(data_borrow[i][1]))
        print("Nama Consumable      : "+ consums[idxID(data_borrow[i][2])][1])
        print("Tanggal Pengambilan  : " + data_borrow[i][3])
        print("Jumlah               : "+ str(data_borrow[i][4]))
        print()
        j += 1
        i += 1
        if (j == 5 and i != len(data_borrow)):
            mau = input("Next (Y/N)? : ")
            while (mau != 'y' and mau != 'Y' and mau != 'N' and mau != 'n'):
                mau = input("Next (Y/N)? : ")
            if (mau == 'Y' or mau == "y"):
                j = 0
    if (i == 0):
        print("Riwayat pengambilan consumable masih kosong.")

def riwayatpinjam():        #F11
    global riwpin_gadgets, gadgets
    data_borrow = sorted(riwpin_gadgets, key=lambda row: datetime.strptime(row[3],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Peminjaman        : "+ str(data_borrow[i][0]))
        print("Nama pengambil       : "+ carinama(data_borrow[i][1]))
        print("Nama Gadget          : "+ gadgets[idxID(data_borrow[i][2])][1])
        print("Tanggal Peminjaman   : " + data_borrow[i][3])
        print("Jumlah               : "+ str(data_borrow[i][4]))
        print()
        j += 1
        i += 1
        if (j == 5 and i != len(data_borrow)):
            mau = input("Next (Y/N)? : ")
            while (mau != 'y' and mau != 'Y' and mau != 'N' and mau != 'n'):
                mau = input("Next (Y/N)? : ")
            if (mau == 'Y' or mau == "y"):
                j = 0
    if (i == 0):
        print("Riwayat peminjaman gadget masih kosong.")


def lcg(seed,modulo):
    seed = (104729 * seed + 7919) % modulo
    return seed

def getTimeNumber():
    waktu = time.localtime() # get struct_time
    times_h = int(time.strftime("%H", waktu))
    times_m = int(time.strftime("%M", waktu))
    times_s = int(time.strftime("%S", waktu))
    times = times_h + times_m + times_s
    return times

def inventory():
    global userid, consums, riw_consums, riw_gachas
    arr = []
    for i in range (len(consums)):
        total_minta = 0
        for j in range (len(riw_consums)):
            if ((riw_consums[j][2] == consums[i][0]) and (riw_consums[j][1] == userid)):
                total_minta = total_minta + riw_consums[j][4]
        total_gacha = 0
        for j in range (len(riw_gachas)):
            if ((riw_gachas[j][2] == consums[i][0]) and (riw_gachas[j][1] == userid)):
                total_gacha = total_gacha + riw_gachas[j][4]
        total_sisa = total_minta - total_gacha
        if (total_sisa != 0):
            arr.append([len(arr)+1,consums[i][0],consums[i][1],consums[i][4],total_sisa])
    return arr

def cetakInventory(arr):
    print("\n============ INVENTORY =============")
    for i in range (len(arr)):
        print("{}. {} (Rarity {}) ({})".format(arr[i][0],arr[i][2],arr[i][3],arr[i][4]))
    print("====================================")

def groupRarity(rarity):
    global consums
    arr = []
    for i in range (len(consums)):
        if (consums[i][4] == rarity):
            arr.append(consums[i][0])
    return arr

def addPool(pool,rarity,jumlah_consums,C,B,A,S):
    if (rarity == "C"):
        tambah = jumlah_consums // 50
        if (tambah == 0):
            tambah = 1
        for i in range (tambah):
            pool.append([B[lcg(i+getTimeNumber(),len(B))],"B"])
        hasil_rarity = "B"
    elif (rarity == "B"):
        tambah = jumlah_consums // 40
        if (tambah == 0):
            tambah = 1
        for i in range (tambah):
            pool.append([A[lcg(i+getTimeNumber(),len(A))],"A"])
        hasil_rarity = "A"
    elif (rarity == "A"):
        tambah = jumlah_consums // 10
        if (tambah == 0):
            tambah = 1
        for i in range (tambah):
            pool.append([S[lcg(i+getTimeNumber(),len(S))],"S"])
        hasil_rarity = "S"
    else:
        tambah = jumlah_consums
        for i in range (tambah):
            pool.append([S[lcg(i+getTimeNumber(),len(S))],"S"])
        hasil_rarity = "S"
    persen = round(tambah / len(pool) * 100,1)
    print("Chance mendapatkan Rarity {} (+ {}%)".format(hasil_rarity,persen))
    return pool

def hasilGacha(pool):
    index = lcg(getTimeNumber(),len(pool))
    arr = [pool[index][0],pool[index][1]]
    return arr

def isPilihConsumsValid(invent,pilih_consums):
    if ((pilih_consums > 0) and (pilih_consums <= len(invent))):
        return True
    else:
        return False

def isJumlahConsumsValid(invent,pilih_consums,jumlah_consums):
    if ((jumlah_consums > 0) and (jumlah_consums <= invent[pilih_consums-1][4])):
        return True
    else:
        return False

def gacha():                #FB03
    global userid, consums, riw_consums, riw_gachas

    invent = inventory()

    if (len(invent) == 0):
        print("Inventory kosong")
    else:
        C = groupRarity("C")
        B = groupRarity("B")
        A = groupRarity("A")
        S = groupRarity("S")

        pool = [] #[nama_consums, rarity_consums]
        pool.append([S[lcg(getTimeNumber(),len(S))],"S"])

        for i in range (3):
            pool.append([A[lcg(i+getTimeNumber(),len(A))],"A"])
        
        for i in range (5):
            pool.append([B[lcg(i+getTimeNumber(),len(B))],"B"])

        for i in range (15):
            pool.append([C[lcg(i+getTimeNumber(),len(C))],"C"])   

        tanggal_gacha = input("Masukan tanggal: ")
        
        cetakInventory(invent)

        pilih_consums = int(input("\nPilih consumable yang mau digunakan: "))
        while (not(isPilihConsumsValid(invent,pilih_consums))):
            print("Masukan tidak valid")
            pilih_consums = int(input("Pilih consumable yang mau digunakan: "))

        jumlah_consums = int(input("Jumlah yang akan digunakan: "))
        while (not(isJumlahConsumsValid(invent,pilih_consums,jumlah_consums))):
            print("Masukan tidak valid")
            jumlah_consums = int(input("Jumlah yang akan digunakan: "))


        print("\n{} (x{}) ditambahkan!".format(invent[pilih_consums-1][2],jumlah_consums))
        rarity = invent[pilih_consums-1][3]
        pool = addPool(pool,rarity,jumlah_consums,C,B,A,S)
        riw_gachas.append([len(riw_gachas)+1,userid,invent[pilih_consums-1][1],tanggal_gacha,jumlah_consums])

        invent = inventory()

        while (len(invent) != 0):
            lagi = input("\nTambahkan item lagi (Y/N)? : ")
            while ((lagi != "Y") and (lagi != "y") and (lagi != "N") and (lagi != "n")):
                print("Masukan tidak valid")
                lagi = input("Tambahkan item lagi (Y/N)? : ")

            if ((lagi == 'N') or (lagi == 'n')):
                break
            else:
                cetakInventory(invent)

                pilih_consums = int(input("\nPilih consumable yang mau digunakan: "))
                while (not(isPilihConsumsValid(invent,pilih_consums))):
                    print("Masukan tidak valid")
                    pilih_consums = int(input("Pilih consumable yang mau digunakan: "))

                jumlah_consums = int(input("\nJumlah yang akan digunakan: "))
                while (not(isJumlahConsumsValid(invent,pilih_consums,jumlah_consums))):
                    print("Masukan tidak valid")
                    jumlah_consums = int(input("Jumlah yang akan digunakan: "))


                print("\n{} (x{}) ditambahkan!".format(invent[pilih_consums-1][2],jumlah_consums))
                rarity = invent[pilih_consums-1][3]
                pool = addPool(pool,rarity,jumlah_consums,C,B,A,S)
                riw_gachas.append([len(riw_gachas)+1,userid,invent[pilih_consums-1][1],tanggal_gacha,jumlah_consums])

                invent = inventory()

        print("\nRolling...")
        time.sleep(3)

        hasil = hasilGacha(pool) #[id_consums,rarity_consums]

        consumable_index = idxID(hasil[0])
        
        consums[consumable_index][3] = consums[consumable_index][3] - 1
        riw_consums.append([(len(riw_consums) + 1),userid,hasil[0],tanggal_gacha,1])
        consumable_name = consums[consumable_index][1]
        print("\nSelamat, Anda mendapatkan {} (Rank {})!".format(consumable_name,hasil[1]))


def printpetunjuk():
    print("Command error. Command tidak ada atau kamu tidak memiliki akses untuk memanggil command tersebut.")
    print("ketik help untuk melihat daftar command!")
    print()

def printstate():           #for debugging
    print('Path = ' + str(path))
    print('users = \n', users)
    print('gadgets = \n',gadgets)
    print('consums = \n', consums)
    print('riw_consums = \n', riw_consums)
    print('riwpin_gadgets = \n', riwpin_gadgets)
    print('riwpen_gadgets = \n', riwpen_gadgets)
    print('role = ', role)
def helpumum():
    print('=============== HELP ===============')
    print('carirarity - untuk mencari gadget berdasarkan rarity-nya')
    print('caritahun - untuk mencari gadget berdasarkan tahun ditemukannya')
    print('save - untuk menyimpan progress anda')
    print('help - untuk menampilkan list command')
    print('exit - untuk keluar dari program')
    print('cls - untuk menbersihkan screen')
def helpuser():
    print('pinjam - untuk meminjam gadget')
    print('kembalikan - untuk mengembalikan gadget yang dipinjam')
    print('minta - untuk meminta consumable')
    print('gacha - untuk melakukan gacha')
def helpadmin():
    print('register - untuk melakukan registrasi user baru')
    print('tambahitem - untuk melakukan penambahan item')
    print('hapusitem - untuk melakukan penghapusan item')
    print('ubahjumlah - untuk mengubah jumlah item')
    print('riwayatpinjam - untuk melihat riwayat peminjaman gadget')
    print('riwayatkembali - untuk melihat riwayat pengembalian gadget')
    print('riwayatambil - untuk melihat riwaya pengambilan consumable')
    print('state - untuk menampilkan isi tiap list')

chrs = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0']

userid = ''
#nama user yang telah login
path = ''
#nama path saves
users = []
#list data user
gadgets = []
#list data gadget
consums = []
#list data consumable
riw_consums = []
#list data riwayat pengambilan consumable
riwpin_gadgets = []
#list data riwayat peminjaman gadgets
riwpen_gadgets = []
#list data riwayat pengembalian gadgets 
role =''
#role dari userid 
riw_gachas = []
#list data riwayat penggunaan consums untuk gacha

parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?", default="default_flag")
args = parser.parse_args()
if (args.folder=='default_flag'):
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: Python kantongajaib.py <nama_folder>")
    exit()
else:
    load(args.folder)
    login()
    print()
    while (True and userid != ''):
        pilihan = input(">>> ")
        print()
        if (pilihan == 'register'):
            if (role == 'admin'):
                register()
            else:
                printpetunjuk()
            print()
        elif (pilihan == 'carirarity'):
            carirarity()
            print()
        elif (pilihan == 'caritahun'):
            caritahun()
            print()
        elif (pilihan == 'tambahitem'):
            if (role == 'admin'):
                tambahitem()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'hapusitem'):
            if (role == 'admin'):
                hapusitem()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'ubahjumlah'):
            if (role == 'admin'):
                ubahjum()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'pinjam'):
            if (role == 'user'):
                pinjam()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'kembalikan'):
            if (role == 'user'):
                kembalikan()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'minta'):
            if (role == 'user'):
                minta()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'riwayatpinjam'):
            if (role == 'admin'):
                riwayatpinjam()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'riwayatkembali'):
            if (role == 'admin'):
                riwayatkembali()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'riwayatambil'):
            if (role == 'admin'):
                riwayatambil()
            else:
                printpetunjuk()
            print()
        elif(pilihan == 'gacha'):
            if (role == 'admin'):
                printpetunjuk()
            else:
                gacha()
            print()
        elif(pilihan == 'save'):
            save()
            print()
        elif(pilihan == 'help'):
            helpumum()
            if (role == 'admin'):
                helpadmin()
            else:
                helpuser()
            print()
        elif(pilihan == 'exit'):
            mau = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah (Y/N)? : ')
            while (mau != 'y' and mau != 'Y' and mau != 'N' and mau != 'n'):
                mau = input("Mau (Y/N)? : ")
            if (mau == 'Y' or mau == "y"):
                save()
            print()
            break
        elif(pilihan == 'cls'):
            os.system('cls')
        elif (pilihan =='state'):
            if (role =='admin'):
                printstate()
            else:
                printpetunjuk()
        else:
            printpetunjuk()