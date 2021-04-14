gadgets = [["1","aaa","aa","10","A","2000"],["2","bbb","bb","40","B","1999"]]

def print_data_gadget(i) :
    print()
    print("Nama            : " + gadgets[i][1])
    print("Deskripsi       : " + gadgets[i][2])
    print("Jumlah          : " + gadgets[i][3])
    print("Rarity          : " + gadgets[i][4])
    print("Tahun Ditemukan : " + gadgets[i][5])

def caritahun() :
    available = False
    tahun = input("Masukan tahun : ")
    kategori = input("Masukan kategori : ")
    print()
    print("Hasil pencarian : ")

    for i in range (len(gadgets)) :
        if kategori == "=" and gadgets[i][5] == tahun :
            print_data_gadget(i)
            available = True
        elif kategori == ">" and gadgets[i][5] > tahun :
            print_data_gadget(i)
            available = True
        elif kategori == "<" and gadgets[i][5] < tahun :
            print_data_gadget(i)
            available = True
        elif kategori == ">=" and gadgets[i][5] >= tahun :
            print_data_gadget(i)
            available = True
        elif kategori == "<=" and gadgets[i][5] <= tahun :
            print_data_gadget(i)
            available = True

    if not(available) :
        print()
        print("Gadget dengan ketentuan tersebut tidak tersedia.")

caritahun()
    
    