import datetime

userid = 'udin'
gadget = [['G1','Gateway to Anywhere','deskripsi',50,'S','2020'],['G2','Ditto Bread','deskripsi',10,'A','2019']]
gadget_borrow_history = [[1,"udin","G1","20/12/2020",30],[2,"bambang","G1","10/12/2020",10],[3,"udin","G2","21/12/2020",10]]
# penambahan jumlah pada gadget_return_history.csv
gadget_return_history = [[1,"udin","G1","10/10/2020",10]]

def fborrowHistory(userid, gadget, gadget_borrow_history, gadget_return_history):
    arr = []
    for i in range (len(gadget)):
        total = 0
        for j in range (len(gadget_borrow_history)):
            if (userid == gadget_borrow_history[j][1]) and (gadget[i][0] == gadget_borrow_history[j][2]):
                total = total + gadget_borrow_history[j][4]
            if (userid == gadget_return_history[j][1]) and (gadget[i][0] == gadget_return_history[j][2]):
                total = total - gadget_return_history[j][4]
            if (total != 0):
                No = len(arr) + 1
                arr.append(No,[gadget[i][1],total])
    return arr


#def cetakBorrowHistory():

def kembalikan():
    global userid, gadget, gadget_borrow_history, gadget_return_history

    borrowHistory = fborrowHistory(userid, gadget, gadget_borrow_history, gadget_return_history)
    print(borrowHistory)

    #cetakBorrowHistory()

# Test
# print(gadget)
# print(gadget_return_history)