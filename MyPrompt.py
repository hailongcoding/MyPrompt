from os import system

system('cls')
account_usr = 0
account_pswd = 0

def WAR():
    print("        [! WARNING !]        ")
    print("This only work on WINDOWS .")
    print(" ")

def cmd():
    system('cls')
    system('cmd')

def ps():
    system('cls')
    system('powershell')

def choice():
    print("  1.Command Prompt")
    print("  2.PowerShell")
    choice_input = int(input("    >> "))
    #check 
    if choice_input == 1 :
        cmd()

    elif choice_input == 2 :
        ps() 

def login():
    account_usr = input("Usernanme : ")
    account_pswd = input("Password : ")
    system('cls')
    choice()

WAR()
login()