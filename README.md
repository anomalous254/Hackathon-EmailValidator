# Email Validator 
### About This Project

In this script, we define an EmailValidatorEngine class that takes an email address as input and has a is_valid() method that checks if the email domain has a valid MX record. If an exception is raised when querying the MX record, we consider the email to be invalid.

We then define a list of email addresses and loop through them, creating an instance of EmailValidator for each email and outputting the validity of the email.


