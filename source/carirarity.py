gadgets = [["1","aaa","aa","10","A","2000"],["2","bbb","bb","40","B","1999"]]

def carirarity() :
    available = False
    rarity = input("Masukan rarity : ")
    print()
    print("Hasil pencarian : ")

    for i in range (len(gadgets)) :
        if rarity == gadgets[i][4] :
            print()
            print("Nama            : " + gadgets[i][1])
            print("Deskripsi       : " + gadgets[i][2])
            print("Jumlah          : " + gadgets[i][3])
            print("Rarity          : " + gadgets[i][4])
            print("Tahun Ditemukan : " + gadgets[i][5])
            available = True

    if not(available) :
        print()
        print("Tidak ada gadget dengan rarity", rarity)

carirarity()
