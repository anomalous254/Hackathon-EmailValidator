# loading imports
# code by: Nyando | anomalous254 

from single_email_validator import validate_single_email
from emails_validator import validate_emails
from termcolor import colored, cprint
import time
import csv, sys
import os

# global contants to be used  in the workflow of this script
NUM = 105
CHOICES = ['1', '2', '3','4','clear']
BANNER_COLOR = 'blue'
banner = """
 ___________                 .__ .__       ____   ____        .__   .__     .___         __                  
\_   _____/  _____  _____   |__||  |      \   \ /   /_____   |  |  |__|  __| _/_____  _/  |_  ____ _______  
 |    __)_  /     \ \__  \  |  ||  |       \   Y   / \__  \  |  |  |  | / __ | \__  \ \   __\/  _ \\_  __ \ 
 |        \|  Y Y  \ / __ \_|  ||  |__      \     /   / __ \_|  |__|  |/ /_/ |  / __ \_|  | (  <_> )|  | \/ 
/_______  /|__|_|  /(____  /|__||____/       \___/   (____  /|____/|__|\____ | (____  /|__|  \____/ |__|    
        \/       \/      \/                               \/                \/      \/    
"""
banner2 = """
 >David Njoroge >>> https://github.com/Ndegwadavid/  && am_request >>> https://github.com/anomalous254/<
 
 1 ... Validate Single Email
 2 ... Valiadate 1+ Emails
 3 ... Help
 4 ... quit
"""
BANNER = f"""
{colored(  '*'*NUM, BANNER_COLOR)}
{colored(banner, BANNER_COLOR, attrs=["blink"])}
{colored(banner2, BANNER_COLOR)}
{colored(  '*'*NUM, BANNER_COLOR)}
"""

# function thatshows the user how to use the script/tool
def show_help():
    print(f"""
{print('-'*NUM)} 
   
{colored('COMMANDS', 'white', "on_blue")} 

[+] clear            Clears the Terminal

{colored('INSTRUCTIONS', 'white', "on_blue")}

[+] validate a single email in formart xyz@xyz.xyz'
[+] Upon receiving an error ensure email is in the correct format'
[+] in bulk validation supply the path to the location of the csv emails list'
[+] Does not validate a blank input'
[+] Received an error? open an issue here https://github.com/NdegwaDavid or https://github.com/anomalous254'
                                          '
          
          """)
    
    
    


# Function that shows options for the user needs for the script


def show_options():
    
    # clears the terminal and display the option workflow
    os.system('cls || clear')
    print(colored(BANNER, BANNER_COLOR))
    # getting and sanitizing  the user input and storing the user choice in variable choice
    try:
        va = colored('(Enter Choice)', 'blue')
        choice = None
        while choice not in CHOICES:
            choice = input(colored(f'[+] @email-validator -- {va} > ', 'yellow'))
    except KeyboardInterrupt:
        print(colored('\n[-]Bye', 'yellow'))
        print(colored('*'*NUM, BANNER_COLOR))
        sys.exit()
        
    # adding functional logic from the user input
    if choice == '1':
        
         os.system('cls || clear')
         validate_single_email()
         
    if choice == '2':

        os.system('cls || clear')
        validate_emails()
            
    if choice == '4':
        
        print('  Killing Session...')
        time.sleep(2)
        print(colored('[-]Bye', 'yellow'))
        print(colored('*'*NUM, BANNER_COLOR))
        sys.exit()
        
    if choice == '3':
        show_help()
        
    if choice == 'clear':
        os.system('cls || clear')
        show_options()

if __name__ == '__main__':
    show_options()
