gadgets = [["1","aaa","aa","10","A","2000"],["2","bbb","bb","40","B","1999"]]

tahun = input("Masukan tahun : ")
kategori = input("Masukan kategori : ")
print()
print ("Hasil pencarian : ")

def print_data_gadget() :
    print()
    print("Nama            : " + gadgets[i][1])
    print("Deskripsi       : " + gadgets[i][2])
    print("Jumlah          : " + gadgets[i][3])
    print("Rarity          : " + gadgets[i][4])
    print("Tahun Ditemukan : " + gadgets[i][5])

for i in range (len(gadgets)) :
    if kategori == "=" and gadgets[i][5] == tahun :
        print_data_gadget()
    elif kategori == ">" and gadgets[i][5] > tahun :
        print_data_gadget()
    elif kategori == "<" and gadgets[i][5] < tahun :
        print_data_gadget()
    elif kategori == ">=" and gadgets[i][5] >= tahun :
        print_data_gadget()
    elif kategori == "<=" and gadgets[i][5] <= tahun :
        print_data_gadget()
    
    