from getpass import getpass
from simple_term_menu import TerminalMenu
from sys import exit
import os
import subprocess




#Chose the file 
def choose_file():
    message="Choose the file:"
    
     # Get list of files in the current directory
    all_entries = os.listdir('.')
    files = []

    for entry in all_entries:
        if os.path.isfile(entry):#verify if it's file
            files.append(entry)
 
    terminal_menu = TerminalMenu(files, title=message)
    menu_entry_index = terminal_menu.show()
    return files[menu_entry_index]



#Check the command
def command_exists(command):
    result = subprocess.run(
        ['which', command],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


#check openssl
def check_openSSL():
    if command_exists("openssl"):
        return True
    else:
        print("openssl is not installed!\n",\
              "Please install it and run this programm again.")
        exit(1) 

def password_generator():
    while True:

        input_passphrase1=getpass("Enter the passphrase: ")
        input_passphrase2=getpass("Re-enter the passphrase: ")

        if input_passphrase1 == input_passphrase2 :
            print("Passphrase match! Success.")
            input_passphrase=input_passphrase2
            break
        else:
            print("Passwords don't match. Try again.\n")
    return input_passphrase


def encryption_method():

    output=subprocess.run(
        ['openssl','enc','-ciphers'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    ciphers=output.stdout.split()

    for _ in range(2):
        del ciphers[0]
    
    for ciph in ciphers:
        print(">",ciph)
    print("Enter one of the cipher above"
          "(by default cipher -aes-256-cbc used): ")
    cipher_input=str(input()).strip()

    if cipher_input=="":
        cipher_input="-aes-256-cbc"
    confirm=str(input("Do you want to use passphrase?(y/n)"))

    if confirm.lower()=='y':

        # while True:
        #
        #     input_passphrase1=getpass("Enter the passphrase: ")
        #     input_passphrase2=getpass("Re-enter the passphrase: ")
        #
        #     if input_passphrase1 == input_passphrase2 :
        #         print("Passphrase match! Success.")
        #         input_passphrase=input_passphrase2
        #         break
        #     else:
        #         print("Passwords don't match. Try again.\n")
        password=password_generator()

    else:
        password=None
    
    return cipher_input,password
