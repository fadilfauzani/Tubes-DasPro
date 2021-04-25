import datetime

user_ID = 'udin'
gadgets = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
riwpin_gadgets = [[1,"udin","G1","20/12/2020",30,True],[2,"bambang","G1","10/12/2020",10,False],[3,"udin","G2","21/12/2020",10,False]]
riwpen_gadgets = [[1,1,"10/10/2020",30],[2,3,"10/10/2020",4]]
#[id,id_peminjaman,tanggal_pengembalian]
#[id,id_peminjaman,tanggal_pengembalian,jumlah_peminjaman]

def printBorrowGadget():
    global gadgets, user_ID, riwpin_gadgets, riwpen_gadgets
    for i in range (len(riwpin_gadgets)):
        total_return = 0
        if ((riwpin_gadgets[i][1] == user_ID) and (riwpin_gadgets[i][5] == False)):
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
    global riwpin_gadgets, user_ID
    if ((borrow_number > 0) and (borrow_number <= len(riwpin_gadgets))):
        if ((riwpin_gadgets[borrow_number - 1][5] == False) and (riwpin_gadgets[borrow_number - 1][1] == user_ID)):
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

def formatDate(date):
    if len(date) != 10:
        dd = ''
        mm = ''
        yyyy = ''
        for i in range (len(date)):
            if (date[i] == "/"):
                break
            else:
                dd = dd + date[i]
        if len(dd) != 2:
            dd = '0' + dd
        for j in range (i + 1,len(date)):
            if (date[j] == "/"):
                break
            else:
                mm = mm + date[j]    
        if len(mm) != 2:
            mm = '0' + mm
        for k in range (j + 1,len(date)):
            if (date[k] == "/"):
                break
            else:
                yyyy = yyyy + date[k]
    date = dd + '/' + mm + '/' + yyyy
    return date

def getItemIndex(item_ID):
    global gadget
    for i in range (len(gadget)):
        if (item_ID == gadget[i][0]):
            gadget_index = i
            break
    return gadget_index

def isThereBorrowedGadget():
    global user_ID, riwpin_gadgets
    bool = False
    for i in range (len(riwpin_gadgets)):
        if (riwpin_gadgets[i][1] == user_ID) and (riwpin_gadgets[i][5] == False):
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

def kembalikan():
    global user_ID, gadgets, riwpin_gadgets, riwpen_gadgets

    if (not(isThereBorrowedGadget())):
        print("Tidak ada riwayat peminjaman")
    else: 
        printBorrowGadget()

        borrow_number = int(input("Masukan nomor peminjaman: "))
        return_date = input("Tanggal pengembalian: ")
        return_amount = int(input("Jumlah pengembalian: "))

        if (isBorrowNumberValid(borrow_number) and isDateValid(return_date)):
            gadget_left = gadgetLeft(borrow_number,return_amount)
            return_date = formatDate(return_date)
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


kembalikan()
#Test

print(gadgets)
print(riwpen_gadgets)
print(riwpin_gadgets)