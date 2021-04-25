from datetime import datetime

gadgets = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019'],['G3','Time Machine','deskripsi',10,'S','2020']]
riwpin_gadgets = [[1,"udin","G1","20/12/2020",10, False],[2,"bambang","G1","10/12/2020",10, False],[3,"petruk","G2","24/04/2021",5, False],[4,"sinta","G3","10/03/2021",7, False],[5,"lola","G1","24/04/2021",8, False],[6,"Suzuke","G2","20/01/2021",1, False]]
riwpen_gadgets = [[1,1,"10/10/2020",30],[2,3,"10/10/2020",4]]

def idxID(id):
    global gadgets, riwpin_gadgets
    idx = -1
    if (id[0] == 'G'):
        for i in range(len(gadgets)):
            if (id == gadgets[i][0]):
                idx = i
    else:
        for i in range(len(riwpin_gadgets)):
            if (id == riwpin_gadgets[i][0]):
                idx = i
    return idx

def idxriw(id):
    global riwpin_gadgets
    idx = -1
    for i in range(len(riwpin_gadgets)):
        if (id == riwpin_gadgets[i][0]):
            idx = i
    return idx

def riwayatkembali():
    global riwpin_gadgets, riwpen_gadgets, gadgets
    data_borrow = sorted(riwpen_gadgets, key=lambda row: datetime.strptime(row[2],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Pengembalian          : "+ str(data_borrow[i][0]))
        print("Nama pengambil           : "+ str(riwpin_gadgets[idxriw(data_borrow[i][1])][1]))
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

def riwayatpinjam():
    global riwpin_gadgets, gadgets
    data_borrow = sorted(riwpin_gadgets, key=lambda row: datetime.strptime(row[3],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Peminjaman        : "+ str(data_borrow[i][0]))
        print("Nama pengambil       : "+ data_borrow[i][1])
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

def riwayatambil():
    global riw_consums, consums
    data_borrow = sorted(riw_consums, key=lambda row: datetime.strptime(row[3],'%d/%m/%Y') ,reverse=True)
    i = 0
    j = 0
    while (i<len(data_borrow) and j<5):
        print("ID Pengambilan       : "+ str(data_borrow[i][0]))
        print("Nama pengambil       : "+ data_borrow[i][1])
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
        
riwayatkembali()
#riwayatpinjam()
