import os
import random
import binascii
from colorama import init, Fore

os.system("cls || clear") 
init()
banner = Fore.RED + f"""
                    _ _   _______      _    _           
     /\            (_|_) |__   __|    | |  | |          
    /  \   ___  ___ _ _     | | ___   | |__| | _____  __
   / /\ \ / __|/ __| | |    | |/ _ \  |  __  |/ _ \ \/ /
  / ____ \\\\__ \ (__| | |    | | (_) | | |  | |  __/>  < 
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
    choice = input(Fore.BLUE + "Your choice : " + Fore.WHITE)
    if choice not in ["1", "2", "3"]:
        os.system("cls || clear")
        print(banner)
        print(Fore.RED + "Please enter a valid choice" + Fore.WHITE)
        menu()

    if choice == "2":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624 | Student of Lycée Robespierre 2TNE" + Fore.WHITE)
        menu()
    elif choice == "3":
        print(Fore.RED + "Bye !" + Fore.WHITE)
        exit()
    if choice == "1":
        os.system("cls || clear")
        name = input(Fore.GREEN + "Enter your name : " + Fore.WHITE)
        note = 0
        while True:
            os.system("cls || clear")
            print(banner)
            print(Fore.GREEN + f"Name : {name} | Note : {note}" + Fore.WHITE)
            print(Fore.BLUE + "Convert the following text to hex" + Fore.WHITE)
            word = ""
            for i in range(10): word += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") # my teacher who told me that I had forgotten the capital letters ;(
            print(Fore.RED + word + Fore.WHITE)
            print(Fore.GREEN + "Your answer : " + Fore.WHITE, end="")
            answer = input()
            if answer == binascii.hexlify(word.encode()).decode(): note += 0.5
            else: note -= 1
            if note >= 40: # The rating system was fixed by my friend @NotFubukIl
              os.system("cls || clear")
              print(banner)
              print(Fore.GREEN + f"Name : {name} | Note : {note}" + Fore.WHITE)
              print(Fore.GREEN + "Good job You have 40 Points!" + Fore.WHITE)
              exit()

          
if __name__ == "__main__": menu()
