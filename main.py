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
    elif choice == "1":
        print(Fore.GREEN + "Select your difficulty")
        print(Fore.GREEN + """
        [1] Easy (10 characters)
        [2] Hard (20 characters)
        """)
        choice = input(Fore.BLUE + "Your choice : ")
        if choice == "1":
            os.system("cls || clear")
            name = input(Fore.GREEN + "Enter your name : ")
            note = 0
            os.system("cls || clear")
            print(banner)
            print(Fore.GREEN + f"Hello {name} welcome to Ascii to Hex")
            print(Fore.BLUE + f"Your note is {note}")
            ascii = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
            print(Fore.GREEN + f"Convert this in hex : {ascii}")
            hex = input(Fore.GREEN + "Enter your answer : ")
            if hex == binascii.hexlify(ascii.encode()).decode():
                print(Fore.GREEN + "Good job")
                note += 0.5
            else:
                print(Fore.RED + "Wrong")
                note -= 1
            if note == 40:
                print(Fore.GREEN + f"Congratulation {name} you win")
                menu()
        elif choice == "2":
            os.system("cls || clear")
            name = input(Fore.GREEN + "Enter your name : ")
            note = 0
            os.system("cls || clear")
            print(banner)
            print(Fore.GREEN + f"Hello {name} welcome to Ascii to Hex")
            print(Fore.BLUE + f"Your note is {note}")
            ascii = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(20))
            print(Fore.GREEN + f"Convert this in hex : {ascii}")
            hex = input(Fore.GREEN + "Enter your answer : ")
            if hex == binascii.hexlify(ascii.encode()).decode():
                print(Fore.GREEN + "Good job")
                note += 0.5
            else:
                print(Fore.RED + "Wrong")
                note -= 1
            if note == 40:
                print(Fore.GREEN + f"Congratulation {name} you win")
                menu()
    else:
        print(Fore.RED + "Wrong")
        note -= 1
    if note == 40:
        print(Fore.GREEN + f"Congratulation {name} you win")
        menu()
if __name__ == "__main__":
    menu()





