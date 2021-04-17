import os

def datatostring(data):
    s = ""
    for i in range (len(data)):
        s += str(data[i])
        if (i != len(data) - 1):
            s += ";"
    return s+ '\n'

users = [(3,"fadil","fadill","kotabumi","asdasd","admin"),[4,"fudil","fadill","kotabumi","asdasd","user"]]
gadgets = []
consums = []
riw_consums = []
riwpin_gadgets = []
riwpen_gadgets = []
def save():
    path = input("Masukkan nama folder penyimpanan: ")
    path = 'saves/' + path
    try:
        os.mkdir(path)
        
    except:
        pass
    user = open(path+"/user.csv","w")
    user.write("id;username;nama;alamat;password;role\n")
    gadget = open(path+"/gadget.csv","w")
    gadget.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
    consum = open(path+"/consumable.csv","w")
    consum.write("id;nama;deskripsi;jumlah;rarity\n")
    riw_consum = open(path+"/consumable_history.csv","w")
    riw_consum.write("id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah\n")
    riwpin_gadget = open(path+ "/gadget_borrow_history.csv", "w")
    riwpin_gadget.write("id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah\n")
    riwpen_gadget = open(path+ "/gadget_return_history.csv","w")
    riwpen_gadget.write("id;id_peminjam;id_gadget;tanggal_peminjaman\n")
    for i in users:
        user.write(datatostring(i))
    for i in gadgets:
        gadget.write(datatostring(i))
    for i in consums:
        consum.write(datatostring(i))
    for i in riw_consums:
        riw_consum.write(datatostring(i))
    for i in riwpin_gadgets:
        riwpin_gadget.write(datatostring(i))
    for i in riwpen_gadgets:
        riwpen_gadget.write(datatostring(i))
    user.close()
    gadget.close()
    consum.close()
    riw_consum.close()
    riwpin_gadget.close()
    riwpen_gadget.close()
save()