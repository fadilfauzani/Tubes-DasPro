users = []

def register() :
    Userada = False

    nama = (input("Masukan nama : ")).title()
    username = input("Masukan username : ")
    password = input("Masukan password : ")
    alamat = input("Masukan alamat : ")

    for i in range (len(users)) : 
        if username == users[i][1] :
            Userada = True

    if (not(Userada)) : 
        users.append([len(users)+1,username,nama,alamat,password,"user"])
        print()
        print("User " + username + " telah berhasil register ke dalam Kantong Ajaib")
    else : 
        print("Username sudah ada, registrasi gagal")

register()
print(users)
register()
print(users)