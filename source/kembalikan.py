import datetime

userid = 'bambang'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020']]
gadget_borrow_history = []
gadget_return_history = []

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

def kembalikan():
    global gadget_borrow_history, 