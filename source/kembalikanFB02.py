import datetime

userid = 'udin'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
gadget_borrow_history = [[1,"udin","G1","20/12/2020",30],[2,"bambang","G1","10/12/2020",10],[3,"udin","G2","21/12/2020",10],[4,"udin","G1","20/12/2020",30]]
# penambahan jumlah pada gadget_return_history.csv
gadget_return_history = [[1,"udin","G1","10/10/2020",10]]

def fborrowHistory(userid, gadget, gadget_borrow_history, gadget_return_history):
    arr = []
    for i in range (len(gadget)):
        total = 0
        for j in range (len(gadget_borrow_history)):
            if (userid == gadget_borrow_history[j][1]) and (gadget[i][0] == gadget_borrow_history[j][2]):
                total = total + gadget_borrow_history[j][4]
        for j in range (len(gadget_return_history)):
            if (userid == gadget_return_history[j][1]) and (gadget[i][0] == gadget_return_history[j][2]):
                total = total - gadget_return_history[j][4]
        if (total != 0):
            No = len(arr) + 1
            arr.append([No,gadget[i][1],total,gadget[i][0],i])
    return arr

def cetakBorrowHistory(borrowHistory):
    for i in range (len(borrowHistory)):
        print("{}. {} (x{})".format(borrowHistory[i][0],borrowHistory[i][1],borrowHistory[i][2]))

def isDateValid(tanggal):
    bool = True
    try:
        datetime.datetime.strptime(tanggal, '%d/%m/%Y')        
    except ValueError:
        bool = False
    return bool

def isNoPeminjamanValid(No,borrowHistory):
    if (No > len(borrowHistory) or (No <= 0)):
        return False
    else:
        return True

def isJumlahValid(No,jumlah,borrowHistory):
    if (jumlah > 0) and jumlah <= borrowHistory[No-1][2]:
        return True
    else:
        return False

def kembalikanFB02():
    global userid, gadget, gadget_borrow_history, gadget_return_history

    borrowHistory = fborrowHistory(userid, gadget, gadget_borrow_history, gadget_return_history)

    cetakBorrowHistory(borrowHistory)

    No = int(input("Masukkan nomor peminjaman: "))
    tanggal = input("Tanggal pengembalian: ")
    jumlah = int(input("Banyak pengembalian: "))

    if (isNoPeminjamanValid(No,borrowHistory)) and (isDateValid(tanggal)) :
        if (isJumlahValid(No,jumlah,borrowHistory)):
            noPengembalian = len(gadget_return_history) + 1
            gadget_return_history.append([noPengembalian,userid,borrowHistory[No-1][0],tanggal,jumlah])
            gadget[borrowHistory[No-1][4]][3] = gadget[borrowHistory[No-1][4]][3] + jumlah
            print("Item {} (x{}) telah dikembalikan.".format(borrowHistory[No-1][1],jumlah))
        else:
            print("Gagal melakukan pengembalian karena jumlah pengembalian tidak valid")
    else:
        if (not(isDateValid(tanggal)) and not(isNoPeminjamanValid(No,borrowHistory))):
            print("Gagal melakukan pengembalian karena nomor peminjaman dan tanggal tidak valid")
        else:
            if not(isNoPeminjamanValid(No,borrowHistory)):
                print("Gagal melakukan pengembalian karena nomor peminjaman tidak valid")
            if (not(isDateValid(tanggal))):
                print("Gagal melakukan pengembalian karena tanggal tidak valid")


kembalikanFB02()

print(gadget)
print(gadget_borrow_history)
print(gadget_return_history)

