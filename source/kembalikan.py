import datetime

user_ID = 'udin'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
gadget_borrow_history = [[1,"udin","G1","20/12/2020",30,True],[2,"bambang","G1","10/12/2020",10,False],[3,"udin","G2","21/12/2020",10,False]]
gadget_return_history = [[1,1,"10/10/2020"]]
#[id,id_peminjaman,tanggal_pengembalian]
#[id,id_peminjaman,tanggal_pengembalian,jumlah_peminjaman]

def printBorrowGadget():
    global gadget, user_ID, gadget_borrow_history
    for i in range (len(gadget_borrow_history)):
        if ((gadget_borrow_history[i][1] == user_ID) and (gadget_borrow_history[i][5] == False)):
            for j in range (len(gadget)):
                if (gadget_borrow_history[i][2] == gadget[j][0]):
                    gadget_index = j
                    break
            print("{}. {}".format(gadget_borrow_history[i][0],gadget[gadget_index][1]))

def isBorrowNumberValid(borrow_number):
    global gadget_borrow_history, user_ID
    if ((borrow_number > 0) and (borrow_number <= len(gadget_borrow_history))):
        if ((gadget_borrow_history[borrow_number - 1][5] == False) and (gadget_borrow_history[borrow_number - 1][1] == user_ID)):
            return True
        else:
            return False
    else :
        return False

def isDateValid(date):
    bool = True
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')        
    except ValueError:
        bool = False
    return bool

def getItemIndex(item_ID):
    global gadget
    for i in range (len(gadget)):
        if (item_ID == gadget[i][0]):
            gadget_index = i
            break
    return gadget_index

def isThereBorrowedGadget():
    global user_ID, gadget_borrow_history
    bool = False
    for i in range (len(gadget_borrow_history)):
        if (gadget_borrow_history[i][1] == user_ID) and (gadget_borrow_history[i][5] == False):
            bool = True
            break
    return bool

def kembalikan():
    global user_ID, gadget, gadget_borrow_history, gadget_return_history

    if (not(isThereBorrowedGadget())):
        print("Tidak ada riwayat peminjaman")
    else: 
        printBorrowGadget()

        borrow_number = int(input("Masukan nomor peminjaman: "))
        return_date = input("Tanggal pengembalian: ")

        if (isBorrowNumberValid(borrow_number) and isDateValid(return_date)):
            gadget_index = getItemIndex(gadget_borrow_history[borrow_number-1][2])
            gadget_name = gadget[gadget_index][1]
            gadget[gadget_index][3] = gadget[gadget_index][3] + gadget_borrow_history[borrow_number-1][4]
            gadget_borrow_history[borrow_number-1][5] = True
            gadget_return_history.append([len(gadget_return_history)+1,borrow_number,return_date])
            print("Item {} (x{}) telah dikembalikan".format(gadget_name, gadget_borrow_history[borrow_number-1][4]))
        else:
            if (not(isBorrowNumberValid(borrow_number)) and not(isDateValid(return_date))):
                print("Gagal melakukan pengembalian karena nomor peminjaman dan tanggal pengembalian tidak valid")
            elif (not(isBorrowNumberValid(borrow_number))):
                print("Gagal melakukan peminjaman karena nomor peminjaman tidak valid")
            elif (not(isDateValid(return_date))):
                print("Gagal melakukan peminjaman karena tanggal pengembalian tidak valid") 


kembalikan()
#Test
'''
print(gadget)
print(gadget_return_history)
print(gadget_borrow_history)
'''