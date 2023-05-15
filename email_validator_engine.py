"""
#  Simple Email Validator
#  Checks if email adress is valid or not
#  github: www.github.com/anomalous254
#  code by: am_request
"""

# loading imports
import dns.resolver 


class EmailValidatorEngine:
    
    def __init__(self, email: str):
        
        # checking and making sure the input i.e the email address is a string
        assert email == '', f'Email adress: {email} is not a string'
        
        self.email = email
        
        # slipting the email address to get the domain name of mail service provider
        self.parts = email.split('@')
        
    def is_valid(self):
        
        # checking if the splited email address list >> (parts not eual to two) 
        if len(self.parts) != 2:
            return False

        # getting and assigning the email service provider domain name to the domain variable 
        domain = self.parts[1]
        
        # checking the MX record i.e Mail Exchanger record of the domain
        # N/B MX stands for Mail Exchanger record, which is a resource record that specifies the mail server which is responsible for accepting emails on behalf of the domain. I
        try:
            answers = dns.resolver.query(domain, 'MX')
        except dns.exception.DNSException:
            return False

        return True

        

