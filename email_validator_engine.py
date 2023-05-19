"""
#  Simple Email Validator
#  Checks if email adress is valid or not
#  github: www.github.com/anomalous254
#  code by: Nyando | am_request | anomalous254
"""

# loading importsl
from termcolor import colored
import dns.resolver 
import re
import smtplib
import sys


class EmailValidatorEngine:
    
    def __init__(self, email: str):
        
        ''' # checking and making sure the input i.e the email address is a string
        assert email == '', f'Email adress: {email} is not a string' '''
        
        self.email = email
        
        
        # slipting the email address to get the domain name of mail service provider
        self.parts = self.email.split('@')
        
    def is_valid(self):
        
        try:
        
            # Simple Regex for syntax checking
            regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

            # Syntax check
            match = re.match(regex, self.email)
            if match == None:
                return False

            # Get domain for DNS lookup
            domain = self.parts[1]
            print(f'\n[+] Domain: {domain}')

            # MX record lookup
            records = dns.resolver.query(domain, 'MX')
            mxRecord = str(records[0].exchange).rstrip('.')
            mxRecord = str(mxRecord)
            print(f'[+] MX: {mxRecord}')


            # SMTP lib setup (use debug level for full output)
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            # SMTP Conversation
            server.connect(mxRecord, port=25)
            # server.local_hostname(Get local server hostname)
            server.helo(server.local_hostname)
            server.mail(self.email)
            code, message = server.rcpt(str(self.email))
            server.quit()


            # Assume SMTP response 250 is success
            if code == 250:
                return True
            else:
                return False
        except Exception as e:
            print(colored(f'[-] {e}!!!'.upper(), 'white', 'on_red'))
            sys.exit()
        
            

        
        