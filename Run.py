from fileinput import close
from runpy import run_module, run_path
import os, glob, pyperclip

# Makes the Required files available
if glob.glob("md5.txt"):
    print("\n <md5.txt is available> \n")
else:
    file = open(r".\md5.txt", "x")
    file.close

if glob.glob("URL.txt"):
    print("\n <URL.txt is available> \n")
else:
    file2 = open(r".\URL.txt", "x")
    file2.close

def Menue():
    print("\nthis is the debug tool")
    print("0. Exit Progam")
    print("1. Basic md5 converter")
    print("2. hydrus api")
    Choice = int(input("What code do you want to run? > "))
    if Choice == 0:
        exit()

    elif Choice == 1:
        run_module(mod_name='md5_URL_Converter')
        Menue()

    elif Choice == 2:
        # run_module(mod_name='Hydrus_API')
        print("\n Not working yet. \n")
        Menue()

    else:
        print("\n <Invalid anser> \n")
        Menue()

Menue()