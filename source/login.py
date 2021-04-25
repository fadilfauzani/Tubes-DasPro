users = [["1","fadil","fadill","kotabumi","asdasd","admin"],["2","fudil","fadill","kotabumi","asdasd","user"]]

def login() :
    global user-id
    akses = False

    username = input("Masukan username : ")
    password = input("Masukan password : ")

    for i in range (len(users)) :
        if username == users[i][1] and password == users[i][4] :
            akses = True

    if akses : 
        print()
        print("Halo " + username + "! Selamat datang di Kantong Ajaib.")
        user-id = username
    else :
        print()
        print("Username atau password salah, silahkan coba lagi.")
login()