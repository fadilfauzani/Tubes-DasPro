import os
import os.path
import argparse
import datetime
from datetime import datetime
import sys

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
        while lines[i] != 'mark':
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],stringtodata(lines[i])[4],stringtodata(lines[i])[5]])
            i+=1
            #(id,username,nama,alamat,password,role)
        return datas
    elif(type == "gadgets"):
        while lines[i] != 'mark':
            datas.append([stringtodata(lines[i])[0],stringtodata(lines[i])[1],stringtodata(lines[i])[2],int(stringtodata(lines[i])[3]),stringtodata(lines[i])[4],int(stringtodata(lines[i])[5])])
            i+=1
            #(id,nama,desk,jumlah,rarity,tahun_ditemukan)
        return datas
    elif(type == "consums"):
        while lines[i] != 'mark':
            datas.append([stringtodata(lines[i])[0],stringtodata(lines[i])[1],stringtodata(lines[i])[2],int(stringtodata(lines[i])[3]),stringtodata(lines[i])[4]])
            i+=1
            #(id,nama,desk,jumlah,rarity)
        return datas
    elif(type == "riwpin_gadgets"):
        while lines[i] != 'mark':
            boolean = True if (stringtodata(lines[i])[5] == 'True') else False
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],int(stringtodata(lines[i])[4]),boolean])
            i+=1
            #(id,id peminjan, id gadget, tanggal, jumlah, is returned)
        return datas
    elif(type == "riwpen_gadgets"):
        while lines[i] != 'mark':
            datas.append([int(stringtodata(lines[i])[0]),int(stringtodata(lines[i])[1]),stringtodata(lines[i])[2],int(stringtodata(lines[i])[3])])
            i+=1
            #(id,id_peminjaman, tanggal,jumlah yang dikembalikan)
        return datas
    elif(type == "riw_consums"):
        while lines[i] != 'mark':
            datas.append([int(stringtodata(lines[i])[0]),stringtodata(lines[i])[1],stringtodata(lines[i])[2],stringtodata(lines[i])[3],int(stringtodata(lines[i])[4])])
            i+=1
            #(id,id pengambil, id consum, tanggal, jumlah)
        return datas

def load(temp_path):        #F14
    global path, users, gadgets, consums, riw_consums, riwpin_gadgets, riwpen_gadgets
    path = 'saves/' + temp_path
    users = csvtodata(path+'/user.csv','users')
    gadgets = csvtodata(path+'/gadget.csv','gadgets')
    consums = csvtodata(path+'/consumable.csv','consums')
    riw_consums = csvtodata(path+'/consumable_history.csv','riw_consums')
    riwpin_gadgets = csvtodata(path+'/gadget_borrow_history.csv','riwpin_gadgets')
    riwpen_gadgets = csvtodata(path+'/gadget_return_history.csv','riwpen_gadgets')

def login() :               #F02
    global userid, role
    akses = False

    username = input("Masukan username : ")
    password = input("Masukan password : ")

    for i in range (len(users)) :
        if username == users[i][1] and password == users[i][4] :
            akses = True
            role = users[i][5]

    if akses : 
        print()
        print("Halo " + username + "! Selamat datang di Kantong Ajaib.")
        userid = username
    else :
        print()
        print("Username atau password salah, silahkan coba lagi.")   

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
        users.append([len(users)+1,username,nama,alamat,password,"user"])
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
    riwpen_gadget.write("id;id_peminjaman;tanggal_peminjaman;jumlah\n")
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
    user.write('mark')
    gadget.write('mark')
    consum.write('mark')
    riw_consum.write('mark')
    riwpin_gadget.write('mark')
    riwpen_gadget.write('mark')
    user.close()
    gadget.close()
    consum.close()
    riw_consum.close()
    riwpin_gadget.close()
    riwpen_gadget.close()

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
            print("\nGagal menambahkan item karena ID sudah ada")
        else:
            nama = input("Masukan Nama: ")
            desk = input("Masukan Deskripsi: ")
            jum = input("Masukan Jumlah: ")
            rarity = input("Masukan Rarity: ")
            if (rarityValid(rarity)):
                isGadget = (id[0] == 'G') #ekspresi boolean
                if (isGadget):
                    tahun = input("Masukan tahun ditemukan: ")
                    gadgets.append([id,nama,desk,jum,rarity,tahun])
                else:   #kalau bkan gadget maka consumbales
                    consums.append([id,nama,desk,jum,rarity])
            else:
                print("\nInput rarity tidak valid!")
    else:
        print("\nGagal menambahkan item karena ID tidak valid")

def hapusitem():            #F06
    global gadgets, consums
    id = input("Masukan ID item: ")
    if (idada(id)):
        hapus = input("Apakah anda yakin ingin menghapus Pintu ke ITB (Y/N)?")
        if (hapus == 'Y' or hapus == 'y'):
            if (id[0] == 'G'):
                gadgets.pop(idxID(id))
            else:
                consums.pop(idxID(id))
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
            else:
                if (jumasli + jumlah < 0):
                    print(f'{-jumlah} {gadgets[idxID(id)][1]} gagal dibuang karena stok kurang. Stok sekaran: {gadgets[idxID(id)][3]} < {-jumlah}')
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
    print("Hasil pencarian : ")

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
    print("Hasil pencarian : ")

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

def printBorrowGadget():
    global gadgets, userid, riwpin_gadgets, riwpen_gadgets
    for i in range (len(riwpin_gadgets)):
        total_return = 0
        if ((riwpin_gadgets[i][1] == userid) and (riwpin_gadgets[i][5] == False)):
            for j in range (len(gadgets)):
                if (riwpin_gadgets[i][2] == gadgets[j][0]):
                    gadget_index = j
                    break
            for j in range (len(riwpen_gadgets)):
                if (riwpen_gadgets[j][1] == (i + 1)):
                    total_return = total_return + riwpen_gadgets[j][3]
            gadget_left = riwpin_gadgets[i][4] - total_return
            print("{}. {} (x{})".format(riwpin_gadgets[i][0],gadgets[gadget_index][1],gadget_left))

def isBorrowNumberValid(borrow_number):
    global riwpin_gadgets, userid
    if ((borrow_number > 0) and (borrow_number <= len(riwpin_gadgets))):
        if ((riwpin_gadgets[borrow_number - 1][5] == False) and (riwpin_gadgets[borrow_number - 1][1] == userid)):
            return True
        else:
            return False
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

def gadgetLeft(borrow_number,return_amount):
    global riwpin_gadgets, riwpen_gadgets
    total_return = 0    
    for i in range (len(riwpen_gadgets)):
        if (riwpen_gadgets[i][1] == borrow_number):
            total_return = total_return + riwpen_gadgets[i][3]
    gadget_left = riwpin_gadgets[borrow_number-1][4] - total_return
    return gadget_left

def isReturnAmountValid(gadget_left,return_amount):
    if (return_amount <= gadget_left):
        return True
    else:
        return False

def kembalikan():           #F09
    global userid, gadgets, riwpin_gadgets, riwpen_gadgets

    if (not(isThereBorrowedGadget())):
        print("Tidak ada riwayat peminjaman")
    else: 
        printBorrowGadget()

        borrow_number = int(input("Masukan nomor peminjaman: "))
        return_date = input("Tanggal pengembalian: ")
        return_amount = int(input("Jumlah pengembalian: "))

        if (isBorrowNumberValid(borrow_number) and isDateValid(return_date)):
            gadget_left = gadgetLeft(borrow_number,return_amount)
            if (isReturnAmountValid(gadget_left,return_amount)):
                gadget_index = idxID(riwpin_gadgets[borrow_number-1][2])
                gadget_name = gadgets[gadget_index][1]
                gadgets[gadget_index][3] = gadgets[gadget_index][3] + return_amount
                if (gadget_left == return_amount) :
                    riwpin_gadgets[borrow_number-1][5] = True
                riwpen_gadgets.append([len(riwpen_gadgets)+1,borrow_number,return_date,return_amount])
                print("Item {} (x{}) telah dikembalikan".format(gadget_name, return_amount))
            else:
                print("Gagal melakukan peminjaman karena jumlah pengembalian tidak valid")
        else:
            if (not(isBorrowNumberValid(borrow_number)) and not(isDateValid(return_date))):
                print("Gagal melakukan pengembalian karena nomor peminjaman dan tanggal pengembalian tidak valid")
            elif (not(isBorrowNumberValid(borrow_number))):
                print("Gagal melakukan peminjaman karena nomor peminjaman tidak valid")
            elif (not(isDateValid(return_date))):
                print("Gagal melakukan peminjaman karena tanggal pengembalian tidak valid")

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
    if (consums[consumable_index][3] >= take_quantity) :
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
            print("Item {} (x{}) telah berhasil diambil!".format(consumable_name,take_quantity))
        else:
            print("\nGagal melakukan permintaan karena item tidak mencukupi")
    else:
        if (not(isConsumableIDValid(item_ID)) and not(isDateValid(take_date))):
            print("Gagal melakukan permintaan karena ID item dan tanggal tidak valid")
        else:
            if (not(isConsumableIDValid(item_ID))):
                print("Gagal melakukan permintaan karena ID item tidak valid")
            if (not(isDateValid(take_date))):
                print("Gagal melakukan permintaan karena tanggal tidak valid")

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
    if (gadgets[gadget_index][3] >= borrow_quantity):
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
                print("Item {} (x{}) berhasil dipinjam!".format(gadget_name,borrow_quantity))
            else :
                print("Gagal melakukan peminjaman karena jumlah melebihi batas")
        else :
            print("Gagal melakukan peminjaman karena item belum dikembalikan")
    else :
        if (not(isItemIDValid(item_ID)) and not(isDateValid(borrow_date))):
            print("Gagal melakukan peminjaman karena ID item dan tanggal peminjaman tidak valid")
        elif (not(isItemIDValid(item_ID))):
            print("Gagal melakukan peminjaman karena ID item tidak valid")
        elif (not(isDateValid(borrow_date))):
            print("Gagal melakukan peminjaman karena tanggal peminjaman tidak valid") 

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
        print("Tanggal Peminjaman       : " + data_borrow[i][2])
        print("Jumlah yang dikembalikan : "+ str(data_borrow[i][3]))
        print()
        j += 1
        i += 1
        if (j == 5 and i != len(data_borrow)):
            print("Next?(Y/N)")
            mau = input()
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
            print("Next?(Y/N)")
            mau = input()
            if (mau == 'Y' or mau == "y"):
                j = 0
    if (i == 0):
        print("Riwayat peminjaman gadget masih kosong.")

def riwayatambil():         #F13
    global riw_consums, consums
    data_borrow = sorted(riw_consums, key=lambda row: datetime.strptime(row[3],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Pengambilan       : "+ str(data_borrow[i][0]))
        print("Nama pengambil       : "+ carinama(data_borrow[i][1]))
        print("Nama Consumable      : "+ consums[idxID(data_borrow[i][2])][1])
        print("Tanggal Peminjaman   : " + data_borrow[i][3])
        print("Jumlah               : "+ str(data_borrow[i][4]))
        print()
        j += 1
        i += 1
        if (j == 5 and i != len(data_borrow)):
            print("Next?(Y/N)")
            mau = input()
            if (mau == 'Y' or mau == "y"):
                j = 0
    if (i == 0):
        print("Riwayat pengambilan consumable masih kosong.")

def printpetunjuk():
    print("Command error. Command tidak ada atau kamu tidak memiliki akses untuk memanggil command tersebut")
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
    print('login - untuk melakukan login ke dalam sistem')
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
def helpadmin():
    print('register - untuk melakukan registrasi user baru')
    print('tambahitem - untuk melakukan penambahan item')
    print('hapusitem - untuk melakukan penghapusan item')
    print('ubahjumlah - untuk mengubah jumlah item')
    print('riwayatpinjam - untuk melihat riwayat peminjaman gadget')
    print('riwayatkembali - untuk melihat riwayat pengembalian gadget')
    print('riwayatambil - untuk melihat riwaya pengambilan consumable')
    print('state - untuk menampilkan isi tiap list')

userid = ''
path = ''
users = []
gadgets = []
consums = []
riw_consums = []
riwpin_gadgets = []
riwpen_gadgets = []
role =''

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
        pilihan = input(">>>")
        print()
        if (pilihan == 'login'):
            login()
            print()
        elif (pilihan == 'register'):
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
            print('Apakah Anda mau melakukan penyimpanan file yang sudah diubah?(y/n)')
            mau = input()
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
                printpetunjuk
        else:
            printpetunjuk()
            print()