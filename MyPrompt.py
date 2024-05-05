from os import system

system('clear')
account_usr = 0
account_pswd = 0

def WAR():
    print("        [! WARNING !]        ")
    print("This only work on LINUX .")
    print(" ")

def cmd():
    print("PLEASE TYPE Y FOR THE BEAUTIFUL VIEW.")
    system("sudo apt install neofetch")
    system('clear')
    system('neofetch')

def ps():
    system('clear')
    system('powershell')

def choice():
    print("  1.Terminal")
    print("  2.PowerShell")
    choice_input = int(input("    >> "))
    #check 
    if choice_input == 1 :
        neofetch()

    elif choice_input == 2 :
        ps() 

def login():
    account_usr = input("Usernanme : ")
    account_pswd = input("Password : ")
    system('clear')
    choice()

WAR()
login()
