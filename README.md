# Email Validator 
### About This Project

In this script, we define an EmailValidatorEngine class that takes an email address as input and has a is_valid() method that checks if the email domain has a valid MX record. If an exception is raised when querying the MX record, we consider the email to be invalid.

We then define a list of email addresses and loop through them, creating an instance of EmailValidator for each email and outputting the validity of the email.

Note that this approach is not foolproof and some email providers may have different DNS configurations that make this check less reliable. Additionally, some email providers may have spam filters that block email addresses even if they are technically valid. Nonetheless, this should give a reasonable indication of the validity of the email addresses provided.
