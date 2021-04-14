gadgets = [['G1','Nama','desk','40']]
consums = [['C1','Nama','desk','40']]

def idxID(id):
    global gadgets, consums
    idx = -1
    if (id[0] == 'G'):
        for i in range(len(gadgets)):
            if (id == gadgets[i][0]):
                idx = i
    else:
        for i in range(len(consums)):
            if (id == consums[i][0]):
                idx = i
    return idx

    

def idValid(id):    #skema validasi input id
    if (id[0] == 'G' or id[0] == 'C'):
        return True
    else:
        return False
def idada(id):
    if (id[0] == 'G'):
        for i in gadgets:
            if (id == i[0]):
                return True
        return False
    else:
        for i in consums:
            if (id == i[0]):
                return True
        return False

def rarityValid(r):
    if (r == 'C' or r == 'B' or r == 'A' or r == 'S' ):
        return True
    else:
        return False

def tambahitem():
    global gadgets, consums
    id = input("Masukan ID: ")
    if(idValid(id)):
        if (idada(id)):
            print("\nGagal menambahkan item karena ID sudah ada")
        else:
            nama = input("Masukan Nama: ")
            desk = input("Masukan Deskripsi: ")
            jum = input("Masukan Jumlah: ")
            rarity = input("Masukan Rarity: ")
            if (rarityValid(rarity)):
                isGadget = (id[0] == 'G') #ekspresi boolean
                if (isGadget):
                    tahun = input("Masukan tahun ditemukan: ")
                    gadgets.append([id,nama,desk,jum,rarity,tahun])
                else:   #kalau bkan gadget maka consumbales
                    consums.append([id,nama,desk,jum,rarity])
            else:
                print("\nInput rarity tidak valid!")
    else:
        print("\nGagal menambahkan item karena ID tidak valid")
def hapusitem():
    global gadgets, consums
    id = input("Masukan ID item: ")
    if (idada(id)):
        hapus = input("Apakah anda yakin ingin menghapus Pintu ke ITB (Y/N)?")
        if (hapus):
            if (id[0] == 'G'):
                gadgets.pop(idxID(id))
            else:
                consums.pop(idxID(id))

    else:
        print("Tidak ada item dengan ID tersebut")
def ubahjum():
    global gadgets, consums
    id = input('Masukan ID: ')
    if (idada(id)):
        jumlah = int(input('Masukan Jumlah: '))
        if (id[0] == 'G'):
            jumasli = int(gadgets[idxID(id)][3])
            if (jumlah > 0):
                gadgets[idxID(id)][3] = str(jumasli + jumlah)
                print(f'{jumlah} {gadgets[idxID(id)][1]} berhasil ditambahkan. Stok sekarang: {gadgets[idxID(id)][3]}')
            else:
                if (jumasli + jumlah < 0):
                    print(f'{-jumlah} {gadgets[idxID(id)][1]} gagal dibuang karena stok kurang. Stok sekaran: {gadgets[idxID(id)][3]} < {-jumlah}')
                else:
                    gadgets[idxID(id)][3] = str(jumasli + jumlah)
                    print(f'{-jumlah} {gadgets[idxID(id)][1]} berhasil dibuang. Stok sekarang: {gadgets[idxID(id)][3]}')
        else:
            jumasli = int(consums[idxID(id)][3])
            if (jumlah > 0):
                consums[idxID(id)][3] = str(jumasli + jumlah)
                print(f'{jumlah} {consums[idxID(id)][1]} berhasil ditambahkan. Stok sekarang: {consums[idxID(id)][3]}')
            else:
                if (jumasli + jumlah < 0):
                    print(f'{-jumlah} {consums[idxID(id)][1]} gagal dibuang karena stok kurang. Stok sekaran: {consums[idxID(id)][3]} < {-jumlah}')
                else:
                    consums[idxID(id)][3] = str(jumasli + jumlah)
                    print(f'{-jumlah} {consums[idxID(id)][1]} berhasil dibuang. Stok sekarang: {consums[idxID(id)][3]}')
    else:
        print("Tidak ada item dengan ID tersebut!")
#tambahitem()
#print(gadgets)
#hapusitem()
#print(gadgets)
ubahjum()
print(gadgets)
print(consums)