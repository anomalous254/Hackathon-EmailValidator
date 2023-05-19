## this script validates more than one email address

# loading imports
from email_validator_engine import EmailValidatorEngine
from csv import reader
from termcolor import colored
import os
import sys
import time
import threading


# global contants to be used  in the workflow of this script
NUM = 105
BANNER_COLOR = 'white'
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
 
 [+] Multiple Email Validator
"""
BANNER = f"""
{colored('*'*NUM, BANNER_COLOR)}
{colored(banner, BANNER_COLOR, attrs=["blink"] )}
{colored(banner2, BANNER_COLOR)}
{colored('*'*NUM, BANNER_COLOR)}
"""
valid_file = open('OUTPUT/valid_emails.txt', 'a')
invalid_file = open('OUTPUT/invalid_emails.txt', 'a')

def get_email_from_csv_file(file_name):
  with open(f'INPUT/{file_name}', 'r') as f:
      emails = reader(f)

      for data in emails:
          email = data[0]
          # creating an email instance from the class EEmailValidatorEngine class
          email_instanace = EmailValidatorEngine(email)

          # returning the boolean value of email instance if true or false
          value = email_instanace.is_valid()

          if value:
            valid_file.write(email+ '\n')
            print(colored(f'[+] Email Address > {email} : valid \n', 'blue'))
            print('-'*NUM)
            

          elif value == False:
            invalid_file.write(email + '\n')
            print(colored(f'[-] Email Address > {email} : invalid \n', 'red'))
            print('-'*NUM)
            

# this function checks if a single email is valid or not
def validate_emails():

  # displays the banner
  print(colored(BANNER, BANNER_COLOR,))

  state = True  # to be used to terminate the while loop if false

  # getting the email address from the user and the api key for zerobounce api email validation
  while state:

    try:

      va = colored('(Enter Name Of File)', 'blue')
      print(colored('[+] MAKE SURE YOU PASTE THE CSV FILE CONTAINING EMAILS TO BE VALIDATED IN THE INPUT FOLDER','white', 'on_blue'))
      print(colored('[+] Note: Some of the ISP block the Port 25 SMTP On Use In This Tool', 'white', 'on_blue'))
      file_name = str(input(colored(f'\n[+] @email-validator -- {va}> ', 'yellow')))
      
      # path to check if user file exists or not
      path = f'INPUT/{file_name}'
      
      try:
        if os.path.isfile(path):
          print(colored('[+] File Found : )', 'green', attrs=["blink"]))
          # starts the validation
          get_email_from_csv_file(file_name)
          print(colored(f'[+] FINISHED VALIDATION!!! ', 'white', 'on_blue'))
          print(colored('[+] NOTE PLEASE CHECK THE valid.txt and invalid.txt files IN OUTPUT DIRECTORY', 'white', 'on_blue'))
          sys.exit()
          
        else:
          print(colored('[-] File Not Found !!!', 'red', attrs=["blink"]))
          print(colored('[-] MAKE SURE YOU PASTE THE CSV FILE CONTAINING EMAILS TO BE VALIDATED IN THE INPUT FOLDER', 'red'))
          print(colored('[-] Terminating!!..,','red'))
          sys.exit()
          
      except FileNotFoundError:
        print(colored('[-] File Not Found !!!', 'red', attrs=["blink"]))
        print(colored('[-] MAKE SURE YOU PASTE THE CSV FILE CONTAINING EMAILS TO BE VALIDATED IN THE INPUT FOLDER', 'red'))
        print(colored('[-] Terminating!!..,', 'red'))
        sys.exit()
      

    except KeyboardInterrupt:

      state = False
      print(colored('[+] Bye \n', 'yellow'))
      print(colored('*' * NUM, BANNER_COLOR))
      invalid_file.close()
      valid_file.close()
      sys.exit()
