import datetime

user_ID = 'udin'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
gadget_borrow_history = [[1,"udin","G1","20/12/2020",10, False],[2,"bambang","G1","10/12/2020",10, False]]
gadget_return_history = []

def isItemIDValid(item_ID):
    global gadget
    i = 0
    bool = False
    while (i < len(gadget) and (bool == False)):
        if (gadget[i][0] == item_ID):
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

def isReturned(item_ID):
    global gadget_borrow_history, user_ID
    bool = True
    for i in range (len(gadget_borrow_history)):
        if (user_ID == gadget_borrow_history[i][1]) and (item_ID == gadget_borrow_history[i][2]):
            bool = gadget_borrow_history[i][5]
    return bool

def isQuantityValid(gadget_index,borrow_quantity):
    global gadget
    if (gadget[gadget_index][3] >= borrow_quantity):
        return True
    else :
        return False

def getItemIndex(item_ID):
    global gadget
    for i in range (len(gadget)):
        if (item_ID == gadget[i][0]):
            gadget_index = i
            break
    return gadget_index

def pinjam():
    item_ID = input("Masukan ID item: ")
    borrow_date = input("Tanggal peminjaman: ")
    borrow_quantity = int(input("Jumlah peminjaman: "))

    if (isItemIDValid(item_ID) and isDateValid(borrow_date)):
        if (isReturned(item_ID)):
            gadget_index = getItemIndex(item_ID)
            if (isQuantityValid(gadget_index,borrow_quantity)):
                gadget[gadget_index][3] = gadget[gadget_index][3] - borrow_quantity
                gadget_borrow_history.append([(len(gadget_borrow_history) + 1),user_ID,item_ID,borrow_date,borrow_quantity,False])
                gadget_name = gadget[gadget_index][1]
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

print(gadget)
print(gadget_borrow_history)