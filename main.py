import os
import re
import random
import array
import string
import sys
from tokenize import String
from colorama import Fore
import hashlib
import pwnedpasswords

os.system("clear")
os.system("cls")
print(Fore.GREEN + u'\u2713 ' + Fore.WHITE + "==> Starting ...")
print(Fore.GREEN + u'\u2713 ' + Fore.WHITE + "==> Checking Requirements ...")
print(Fore.GREEN + u'\u2713 ' + Fore.WHITE + "==> Started ...")
print(Fore.GREEN + u'\u2713 ' + Fore.WHITE + "==> WELCOME !")

def pwned():
    verifyindb = input(Fore.WHITE + '! ' + Fore.WHITE + "==> Enter Password To Check In DB : ")
    dbmain = pwnedpasswords.check(verifyindb)
    if dbmain >= 1:
        print(Fore.RED + u'\u2717 ' + Fore.WHITE + "==> Password Is Not Preffered")
        print(Fore.RED + u'\u2717 ' + Fore.WHITE + "==> Leaked in " + str(dbmain) + " Sites/Applications")
            
    elif dbmain == 0:
        print(Fore.GREEN + u'\u2713 ' + Fore.WHITE + "==> Acceptable")
            
    else:
        print(Fore.RED + u'\u2717 ' + Fore.WHITE + "==> Random error occured")
        


def passgen():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password = password + x
    print(Fore.YELLOW + '! ' + Fore.WHITE + "==> Suggested : " + password)


# OPTION 1 :

def start():
    mainsys = input(
        "1. Cool Passwords\n2. Encode Password \n3. Verify Encoded Passwords\n4. Verify In DB\n0. Exit\nEnter Your Choice : ")
    if mainsys == '1':
        verify = input(Fore.WHITE + '! ' + Fore.WHITE +
                    "==> Enter Your Password : ")
        bool = 0
        while True:
            if (len(verify) < 8):
                print(Fore.YELLOW + '! ' + Fore.WHITE +
                    "==> Password length should be more than 8(digits/characters)")
                bool = -1
                break
            elif not re.search("[a-z]", verify):
                print(Fore.YELLOW + '! ' + Fore.WHITE +
                    "==> Must add a Lowercase character (a-z)")
                bool = -1
                break
            elif not re.search("[A-Z]", verify):
                print(Fore.YELLOW + '! ' + Fore.WHITE +
                    "==> Must add a Uppercase character (A-Z)")
                bool = -1
                break
            elif not re.search("[0-9]", verify):
                print(Fore.YELLOW + '! ' + Fore.WHITE +
                    "==> Must add number(s) (0-9)")
                bool = -1
                break
            elif not re.search("[_@$!#%^&*/|\`~;:><]", verify):
                print(Fore.YELLOW + '! ' + Fore.WHITE +
                    "==> Must add a special character (_@$!#%^&*/|\`~;:><)")
                bool = -1
                break
            elif re.search("\s", verify):
                bool = -1
                break
            else:
                bool = 0
                print(Fore.GREEN + u'\u2713 ' + Fore.WHITE + "==> Valid Password")
                break

        if bool == -1:
            print(Fore.RED + u'\u2717 ' + Fore.WHITE + "==> Not a Valid Password")
            passgen()
        start()
        

    # OPTION 2 :
    elif mainsys == '2':
        verifyencode = input(Fore.WHITE + '! ' + Fore.WHITE +
                            "==> Enter Your Password To Encode: ")
        str = (verifyencode)
        result = hashlib.sha256(str.encode())
        print(Fore.GREEN + u'\u2713 ' + Fore.WHITE +
            'SHA256 is : ', result.hexdigest())
        start()

    # OPTION 3 :
    elif mainsys == '3':
        passverify = input(Fore.WHITE + '! ' + Fore.WHITE +
                        "==> Enter Your Password First: ")
        str = (passverify)
        result = hashlib.sha256(str.encode())
        shaverify = input(Fore.WHITE + '! ' + Fore.WHITE +
                        "==> Enter Your SHA256: ")
        if result.hexdigest() == shaverify:
            print("Verified Successfully")

        else:
            print("Incorrect InFo")
        start()

    # OPTION 4 :
    elif mainsys == '4':
        pwned()
        start()

    # OPTIONS 0 :
    elif mainsys == '0':
        os.system("exit")

    else:
        print(Fore.RED + u'\u2717 ' + Fore.WHITE + "==> Invalid Command Try Again!!!")
        start()
start()