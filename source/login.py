users = []

def login() :
    akses = False

    username = input("Masukan username : ")
    password = input("Masukan password : ")

    for i in range (len(users)) :
        if username == users[i][1] and password == users[i][4] :
            akses = True

    if akses : 
        print ("Halo " + username + "! Selamat datang di Kantong Ajaib.")
    else :
        print ("Username atau password salah, silahkan coba lagi.")
