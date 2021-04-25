from datetime import datetime

gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019'],['G3','Time Machine','deskripsi',10,'S','2020']]
gadget_borrow_history = [[1,"udin","G1","20/12/2020",10, False],[2,"bambang","G1","10/12/2020",10, False],[3,"petruk","G2","24/04/2021",5, False],[4,"sinta","G3","10/03/2021",7, False],[5,"lola","G1","24/04/2021",8, False],[6,"Suzuke","G2","20/01/2021",1, False]]
gadget_return_history = []

def idxID(id):
    global gadget, gadget_borrow_history
    idx = -1
    if (id[0] == 'G'):
        for i in range(len(gadget)):
            if (id == gadget[i][0]):
                idx = i
    else:
        for i in range(len(gadget_borrow_history)):
            if (id == gadget_borrow_history[i][0]):
                idx = i
    return idx


def riwayatpinjam():
    global gadget_borrow_history, gadget
    data_borrow = sorted(gadget_borrow_history, key=lambda row: datetime.strptime(row[3],'%d/%m/%Y') ,reverse=True)
    for row in data_borrow:
        print("ID Peminjaman: "+ str(row[0]))
        print("Nama pengambil: "+ row[1])
        print("Nama Gadget: "+ gadget[idxID(row[2])][1])
        print("Tanggal Peminjaman: " + row[3])
        print("Jumlah: "+ str(row[4]))
        
        
riwayatpinjam()
