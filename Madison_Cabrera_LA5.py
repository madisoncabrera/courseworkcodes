#-------------------------------------------------------------------------------
# LA5.py
# Name: Madison Cabrera
# Python Version: 2.XX or 3.XX
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments to grader: 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------


#define exceptions classes InsufficientLength, NoDigit, NoEdu and NoAtSymbol
class InvalidAddress(Exception):
    def __init__(self,email):
        self.email=email

    def __str__(self):
        return f' Invalid email: {self.email}' #return the false message and bad email
    
class InsufficientLength(InvalidAddress):
    def __str__(self):
        return 'Address must contain at least 12 characters.' #print error message
    
    
class NoDigit(InvalidAddress):
    def __str__(self):
        return 'Address must contain at least one digit 0-9.'#print error message

class NoEdu(InvalidAddress):
    def __str__(self):
        return 'Address must contain .edu suffix.'#print error message
    
class NoAtSymbol(InvalidAddress):
    def __str__(self):
        return 'Address must contain the @ symbol.'#print error message
    
# sample code can be Number Guessing Game
#helper functions
def has_digit(address):
    '''
    Checks if an address string has at least one digit.
    Returns True if at least one digit is present, False otherwise
    '''
    for e in address:
        if e.isdigit(): #looking for if a digit is present 
            return True #if digit found
    return False # if no digit 
        
        
def check_email(email):
    try:
        if len(email) <12:
            raise InsufficientLength(email) #raises correct error
        if '@' not in email:
            raise NoAtSymbol(email)#raises correct error
        if not has_digit(email):
            raise NoDigit(email)#raises correct error
        if not email.endswith('.edu'):
            raise NoEdu(email)#raises correct error
    except InvalidAddress as e:
        print(f'{e}')
        return False #allows loop to continue
    else:
        print(f'{email} is valid!') 
        return True # has loop0 end 
        

while True:
    user_email=input('Enter an email address: ') #takes user input 
    #check=check_email(user_email)
    if check_email(user_email): #runs check
        break 
    


