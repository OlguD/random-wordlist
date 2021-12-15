import string
import random
import colorama
from colorama import Fore,Back,Style
import time

colorama.init()

def banner():
    print(Fore.LIGHTCYAN_EX)
    print("""
    
        /$$      /$$                           /$$       /$$ /$$             /$$    
    | $$  /$ | $$                          | $$      | $$|__/            | $$    
    | $$ /$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$$      | $$ /$$  /$$$$$$$ /$$$$$$  
    | $$/$$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$      | $$| $$ /$$_____/|_  $$_/  
    | $$$$_  $$$$| $$  \ $$| $$  \__/| $$  | $$      | $$| $$|  $$$$$$   | $$    
    | $$$/ \  $$$| $$  | $$| $$      | $$  | $$      | $$| $$ \____  $$  | $$ /$$
    | $$/   \  $$|  $$$$$$/| $$      |  $$$$$$$      | $$| $$ /$$$$$$$/  |  $$$$/
    |__/     \__/ \______/ |__/       \_______/      |__/|__/|_______/    \___/  
                                                                                
                                                                            
                                                                                  version : 0.1
                                                                                  Author  : OlguD
    
    """)
    print(Fore.RED)
    print("#### I DO NOT ACCEPT ANY LEGAL RESPONSIBILITY !!!! ")

def creator():
    n_str = ""
    global new_str, word_list_many, total
    random_words = ""
    total = 0

    asc_letter = list(string.ascii_letters)
    print(Fore.LIGHTWHITE_EX)

    word_list_long = int(input("Enter the max lenght : "))
    word_list_many = int(input("How many word do you want : "))

        
    print(Fore.GREEN)
    print("[[[+] creating a wordlist]]")
    
    while word_list_many >= total:
        time.sleep(0.25)
        random_words = random.choices(asc_letter, k=word_list_long)
        new_str = "".join(random_words)
        total+=1
        print(Fore.YELLOW)
        print(f"%d => "%(total) + str(new_str))


        
        with open("wordlist.txt", "w") as wrl:
            n_str+=new_str                                                      
            wrl.write(n_str + "\n")           #<==  kontrol et burayı 
            wrl.close()
           

        if word_list_many == total:
            print(Fore.GREEN)
            print("Succesfully created.. ")
            break



banner()
creator()

