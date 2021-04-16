import datetime

userid = 'bambang'
consumable = [['C1','Dorayaki Rasa Nasi Rames','deskripsi',50,'S']]
consumable_history = []

def isIdValid(id):
    global consumable
    bool = False
    i = 0
    while (bool == False) and (i < len(consumable)):
        if (consumable[i][0] == id):
            bool = True
        else:
            i = i + 1
    return bool

def idStored(id):
    global consumable
    bool = False
    i = 0
    while (bool == False):
        if (consumable[i][0] == id):
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

def isJumlahValid(id,jumlah):
    global consumable
    if (consumable[id][3] >= jumlah) :
        return True
    else:
        return False

def getTransactionID():
    global consumable_history
    return len(consumable_history) + 1

def minta():
    id = input("Masukan ID item: ")
    jumlah = int(input("Jumlah: "))
    tanggal = input("Tanggal permintaan: ")
    if (isIdValid(id) and isDateValid(tanggal)):
        iid = idStored(id)
        if (isJumlahValid(iid,jumlah)):
            consumable[iid][3] = consumable[iid][3] - jumlah
            consumable_history.append([getTransactionID(),userid,id,tanggal,jumlah])
            print("Item {} (x{}) telah berhasil diambil!".format(consumable[iid][1], jumlah))
        else:
            print("\nGagal melakukan permintaan karena item tidak mencukupi")
    else:
        if (not(isIdValid(id)) and not(isDateValid(tanggal))):
            print("Gagal melakukan permintaan karena ID item dan tanggal tidak valid")
        else:
            if (not(isIdValid(id))):
                print("Gagal melakukan permintaan karena ID item tidak valid")
            if (not(isDateValid(tanggal))):
                print("Gagal melakukan permintaan karena tanggal tidak valid")

minta()