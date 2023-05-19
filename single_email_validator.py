# loading imports
from email_validator_engine import EmailValidatorEngine
from termcolor import colored
import os
import sys
import time



# global contants to be used  in the workflow of this script
NUM = 105
BANNER_COLOR = 'green'
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
 
 [+] Single Email Validator
 [+] q to quit
"""
BANNER = f"""
{colored('*'*NUM, BANNER_COLOR)}
{colored(banner, BANNER_COLOR, attrs=["blink"] )}
{colored(banner2, BANNER_COLOR)}
{colored('*'*NUM, BANNER_COLOR)}
"""

# this function checks if a single email is valid or not
def validate_single_email():
  # displays the banner
  print(colored(BANNER, BANNER_COLOR))
  
  state = True # to be used to terminate the while loop if false
  
  # getting the email address from the user and the api key for zerobounce api email validation    
  while state:
    try:
      
      va = colored('(Enter Email Address)', 'blue')
      print(colored('[+] Note: Some of the ISP block the Port 25 SMTP On Use In This Tool', 'white', 'on_blue'))
      data = str(input(colored(f'\n[+] @email-validator -- {va}> ', 'yellow')))
    
      
      # exiting the script ogic
      if data == 'q':
        
          state = False
          print(colored('[+] Bye \n', 'yellow'))
          print(colored('*' * NUM, BANNER_COLOR))
          sys.exit()
          
      if data in 'clear':
        os.system('cls || clear')
        validate_single_email()
          
      if '>' in data:
        print('-'*NUM)
        print(colored(f'  [-] Invalid Email Address : xss', 'red'))
        print('Initializing...')
        time.sleep(3)
        os.system('cls || clear')
        validate_single_email()
        
      if '.' in data[0]:
        print('-'*NUM)
        print(colored(f'[-] Invalid Email Address ', 'red'))
        print('Initializing...')
        time.sleep(3)
        os.system('cls || clear')
        validate_single_email()
        
      if '@' not in data:
        print('-'*NUM)
        print(colored(f'[-] Invalid Email Address ', 'red'))
        print('Initializing...')
        time.sleep(3)
        os.system('cls || clear')
        validate_single_email()
          
      
      # creating an email instance from the class EEmailValidatorEngine class
      email_instanace = EmailValidatorEngine(data)
      
      # returning the boolean value of email instance if true or false
      value = email_instanace.is_valid()
      
      # checking if the email is valid or not based on the boolean >>value
      if value:
        print(colored(f'[+] Email Address > {data} : valid \n', 'white', 'on_blue'))
        print('-'*NUM)
        sys.exit()
      
      else:
        print(colored(f'[-] Email Address > {data} : invalid \n', 'white', 'on_red'))
        print('-'*NUM)
        sys.exit()
          
    except KeyboardInterrupt:
      state = False
      print(colored('[+] Bye \n', 'yellow'))
      print(colored('*' * NUM, BANNER_COLOR))
      sys.exit()

      
  
        
        
    
