import os
import os.path
import argparse

import sys

def stringtodata(s):
    #s adalah string yang ingin diubah menjadi data
    #dipakai untuk menggantikan fungsi split
    s = s.replace("\n","")
    datas = []
    i = 0
    data = ""
    while (i < len(s)):
        if (s[i]==';'):
            datas.append(data)
            data = ""
        else:
            data += s[i]
            if (i == len(s)-1):
                datas.append(data)
        i += 1
    return datas

def csvtodata(csv):
    datas = []
    f = open(csv, "r")
    lines  = f.readlines()
    for i in lines:
        datas.append(stringtodata(i))
    return datas

def load(temp_path):
    global path, users, gadgets, consums, riw_consums, riwpin_gadgets, riwpen_gadgets
    path = 'saves/' + temp_path
    users = csvtodata(path+'/user.csv')
    gadgets = csvtodata(path+'/gadget.csv')
    consums = csvtodata(path+'/consumable.csv')
    riw_consums = csvtodata(path+'/consumable_history.csv')
    riwpin_gadgets = csvtodata(path+'/gadget_borrow_history.csv')
    riwpen_gadgets = csvtodata(path+'/gadget_return_history.csv')



parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?", default="default_flag")
args = parser.parse_args()
if (args.folder=='default_flag'):
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: Python kantongajaib.py <nama_folder>")
    exit()
else:
    load(args.folder)