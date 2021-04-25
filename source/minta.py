import datetime

user_ID = 'bambang'
consums = [['C1','Dorayaki Rasa Nasi Rames','deskripsi',50,'S']]
riw_consums = []

def isConsumableIDValid(item_ID):
    global consums
    bool = False
    i = 0
    while (bool == False) and (i < len(consums)):
        if (consums[i][0] == item_ID):
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

def isQuantityValid(consumable_index,take_quantity):
    global consums
    if (consums[consumable_index][3] >= take_quantity) :
        return True
    else:
        return False

def idxID(item_ID):
    global consums
    for i in range (len(consums)):
        if(item_ID == consums[i][0]):
            consumable_index = i
            break
    return consumable_index

def minta():
    global user_ID, riw_consums, consums
    item_ID = input("Masukan ID item: ")
    take_quantity = int(input("Jumlah: "))
    take_date = input("Tanggal permintaan: ")
    if (isConsumableIDValid(item_ID) and isDateValid(take_date)):
        take_date = formatDate(take_date)
        consumable_index = getConsumableIndex(item_ID)
        if (isQuantityValid(consumable_index,take_quantity)):
            consums[consumable_index][3] = consums[consumable_index][3] - take_quantity
            riw_consums.append([(len(riw_consums) + 1),user_ID,item_ID,take_date,take_quantity])
            consumable_name = consums[consumable_index][1]
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

print(consums)
print(riw_consums)
