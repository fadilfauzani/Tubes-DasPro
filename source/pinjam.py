import datetime

userid = 'udin'
gadgets = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
riwpin_gadgets = [[1,"udin","G1","20/12/2020",10, False],[2,"bambang","G1","10/12/2020",10, False]]
gadget_return_history = []

def isItemIDValid(item_ID):
    global gadgets
    i = 0
    bool = False
    while (i < len(gadgets) and (bool == False)):
        if (gadgets[i][0] == item_ID):
            bool = True
        i = i + 1
    return bool

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

def pinjam():
    global gadgets, riwpin_gadgets, userid
    item_ID = input("Masukan ID item: ")
    borrow_date = input("Tanggal peminjaman: ")
    borrow_quantity = int(input("Jumlah peminjaman: "))

    if (isItemIDValid(item_ID) and isDateValid(borrow_date)):
        borrow_date = formatDate(borrow_date)
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

pinjam()

'''
print(gadgets)
print(riwpin_gadgets)
'''