import os
import os.path
import argparse

import sys

def load(temp_path):
    global path
    temp_path = 'saves/' + temp_path
    path = temp_path

parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?", default="default_flag")
args = parser.parse_args()
if (args.folder=='default_flag'):
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: Python kantongajaib.py <nama_folder>")
    exit()
else:
    load(args.folder)