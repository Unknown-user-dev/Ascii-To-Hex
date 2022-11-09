import colorama
import os
import random
import binascii
from colorama import Fore, Back, Style
from colorama import init

os.system("cls || clear") 
init()
banner = Fore.RED + f"""
                    _ _   _______      _    _           
     /\            (_|_) |__   __|    | |  | |          
    /  \   ___  ___ _ _     | | ___   | |__| | _____  __
   / /\ \ / __|/ __| | |    | |/ _ \  |  __  |/ _ \ \/ /
  / ____ \\__ \ (__| | |     | | (_) | | |  | |  __/>  < 
 /_/    \_\___/\___|_|_|    |_|\___/  |_|  |_|\___/_/\_\\ 
                                                                                                           
            By : @Unknown-user-dev 
        https://github.com/Unknown-user-dev
    Idea of my teacher thanks you, I redid the code
"""

print(banner)

def menu():
    print(Fore.GREEN + """
    [1] Convert Ascii to Hex
    [2] Credits
    [3] Exit
    """)
    choice = input(Fore.BLUE + "Your choice : ")
    if choice not in ["1", "2", "3"]:
        os.system("cls || clear")
        print(banner)
        print(Fore.RED + "Please enter a valid choice")
        menu()

    if choice == "2":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624 | Student of Lycée Robespierre 2TNE")
        menu()
    elif choice == "3":
        print(Fore.RED + "Bye !")
        exit()
    if choice == "1":
        os.system("cls || clear")
        name = input(Fore.GREEN + "Enter your name : ")
        note = 0
        for i in range(40):
            os.system("cls || clear")
            print(banner)
            print(Fore.GREEN + f"Name : {name} | Note : {note}")
            print(Fore.BLUE + "Convert the following text to hex")
            word = ""
            for i in range(10):
                word += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
            print(Fore.RED + word)
            print(Fore.GREEN + "Your answer : ", end="")
            answer = input()
            if answer == binascii.hexlify(word.encode()).decode():
                note += 20
            else:
                note -= 1
       # It is necessary to solve the problem of note (If note > 40 then the program stops)
        while note > 40:
            os.system("cls || clear")
            print(banner)
            print(Fore.GREEN + f"Name : {name} | Note : {note}")
            print(Fore.GREEN + "Good job You have 40 Points!")
            exit()
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + f"Name : {name} | Note : {note}")
if __name__ == "__main__":
    menu()
