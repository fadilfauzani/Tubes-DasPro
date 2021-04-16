import datetime

userid = 'udin'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
gadget_borrow_history = [[1,"udin","G1","20/12/2020",30],[2,"bambang","G1","10/12/2020",10],[3,"udin","G2","21/12/2020",10]]
gadget_return_history = [[1,"udin","G1","10/10/2020"]]

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

def isNomorPeminjamanValid(nomorPeminjaman):
    global userid, gadget_borrow_history
    if nomorPeminjaman > len(gadget_borrow_history):
        return False
    else:
        indeks = nomorPeminjaman - 1
        if (gadget_borrow_history[indeks][1] == userid):
            return True
        else:
            return False

def apakahSudahDikembalikan(nomorPeminjaman):
    global gadget_return_history
    bool = False
    for i in range (len(gadget_return_history)):
        if nomorPeminjaman == gadget_return_history[i][0]:
            bool = True
            break
    return bool

def kembalikan():
    global gadget_borrow_history, gadget_return_history

    for i in range (len(gadget_borrow_history)):
        if (gadget_borrow_history[i][1] == userid) and not(apakahSudahDikembalikan(i + 1)) :
            for j in range (len(gadget)):
                if (gadget_borrow_history[i][2] == gadget[j][0]):
                    namaGadget = gadget[j][1]
            print("{}. {}".format(gadget_borrow_history[i][0],namaGadget))
    
    nomorPeminjaman = int(input("Masukan nomor peminjaman: "))
    tanggal = input("Tanggal pengembalian: ")

    if (isDateValid(tanggal) and isNomorPeminjamanValid(nomorPeminjaman) and not(apakahSudahDikembalikan(nomorPeminjaman))):
        gadget_return_history.append([nomorPeminjaman,userid,gadget_borrow_history[nomorPeminjaman-1][2],tanggal])
        for j in range (len(gadget)):
            if (gadget_borrow_history[nomorPeminjaman - 1][2] == gadget[j][0]):
                iid = j
                namaGadget = gadget[j][1]
                break
        gadget[iid][3] = gadget[iid][3] + gadget_borrow_history[nomorPeminjaman-1][4]
        print("Item {} (x{}) telah dikembalikan.".format(namaGadget,gadget_borrow_history[nomorPeminjaman-1][4]))
    else:
        if(not(isDateValid(tanggal)) and (not(isNomorPeminjamanValid(nomorPeminjaman))) or (apakahSudahDikembalikan(nomorPeminjaman))):
            print("Gagal melakukan peminjaman karena nomor peminjaman dan tanggal tidak valid")
        else:
            if not(isNomorPeminjamanValid(nomorPeminjaman)):
                print("Gagal melakukan peminjaman karena nomor peminjaman tidak valid")
            if (not(isDateValid(tanggal))):
                print("Gagal melakukan peminjaman karena tanggal tidak valid")

kembalikan()

# Test
# print(gadget)
# print(gadget_return_history)