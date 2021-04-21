import datetime

user_ID = 'bambang'
consumable = [['C1','Dorayaki Rasa Nasi Rames','deskripsi',50,'S']]
consumable_history = []

def isConsumableIDValid(item_ID):
    global consumable
    bool = False
    i = 0
    while (bool == False) and (i < len(consumable)):
        if (consumable[i][0] == item_ID):
            bool = True
        i = i + 1
    return bool

# Source: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def isDateValid(date):
    bool = True
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')        
    except ValueError:
        bool = False
    return bool

def isQuantityValid(consumable_index,take_quantity):
    global consumable
    if (consumable[consumable_index][3] >= take_quantity) :
        return True
    else:
        return False

def getConsumableIndex(item_ID):
    global consumable
    for i in range (len(consumable)):
        if(item_ID == consumable[i][0]):
            consumable_index = i
            break
    return consumable_index

def minta():
    item_ID = input("Masukan ID item: ")
    take_quantity = int(input("Jumlah: "))
    take_date = input("Tanggal permintaan: ")
    if (isConsumableIDValid(item_ID) and isDateValid(take_date)):
        consumable_index = getConsumableIndex(item_ID)
        if (isQuantityValid(consumable_index,take_quantity)):
            consumable[consumable_index][3] = consumable[consumable_index][3] - take_quantity
            consumable_history.append([(len(consumable_history) + 1),user_ID,item_ID,take_date,take_quantity])
            consumable_name = consumable[consumable_index][1]
            print("Item {} (x{}) telah berhasil diambil!".format(consumable_name,take_quantity))
        else:
            print("\nGagal melakukan permintaan karena item tidak mencukupi")
    else:
        if (not(isConsumableIDValid(item_ID)) and not(isDateValid(take_date))):
            print("Gagal melakukan permintaan karena ID item dan tanggal tidak valid")
        else:
            if (not(isConsumableIDValid(item_ID))):
                print("Gagal melakukan permintaan karena ID item tidak valid")
            if (not(isDateValid(take_date))):
                print("Gagal melakukan permintaan karena tanggal tidak valid")

minta()
print(consumable)
print(consumable_history)