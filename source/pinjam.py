import datetime

userid = 'bambang'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020']]
gadget_borrow_history = []

def isIdValid(id):
    global gadget
    bool = False
    i = 0
    while (bool == False) and (i < len(gadget)):
        if (gadget[i][0] == id):
            bool = True
        else:
            i = i + 1
    return bool

def idStored(id):
    global gadget
    bool = False
    i = 0
    while (bool == False):
        if (gadget[i][0] == id):
            bool = True
        else:
            i = i + 1
    return i

# Source: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def isDateValid(tanggal):
    bool = True
    try:
        datetime.datetime.strptime(tanggal, '%d/%m/%Y')        
    except ValueError:
        bool = False
    return bool

def isJumlahPeminjamanValid(id,jumlahPeminjaman):
    global gadget
    if (gadget[id][3] >= jumlahPeminjaman) :
        return True
    else:
        return False

def getTransactionID():
    global gadget_borrow_history
    return str(len(gadget_borrow_history) + 1)

def pinjam():
    global gadget, gadget_borrow_history
    id = input("Masukan ID item: ")
    tanggal = input("Tanggal peminjaman: ")
    jumlahPeminjaman = int(input("Jumlah peminjaman: "))
    if (isIdValid(id) and isDateValid(tanggal)):
        iid = idStored(id)
        if (isJumlahPeminjamanValid(iid,jumlahPeminjaman)):
            gadget[iid][3] = gadget[iid][3] - jumlahPeminjaman
            gadget_borrow_history.append([getTransactionID(),userid,id,tanggal,jumlahPeminjaman])
            print("Item {} (x{}) berhasil dipinjam!".format(gadget[iid][1], jumlahPeminjaman))
        else:
            print("\nGagal melakukan peminjaman karena item tidak mencukupi")
    else:
        if (not(isIdValid(id)) and not(isDateValid(tanggal))):
            print("Gagal melakukan peminjaman karena ID item dan tanggal tidak valid")
        else:
            if (not(isIdValid(id))):
                print("Gagal melakukan peminjaman karena ID item tidak valid")
            if (not(isDateValid(tanggal))):
                print("Gagal melakukan peminjaman karena tanggal tidak valid")
pinjam()

# Test output
'''
for i in range (len(gadget_borrow_history)):
    for j in range (5):
        print(gadget_borrow_history[i][j], end = ' ')
    print()
'''
