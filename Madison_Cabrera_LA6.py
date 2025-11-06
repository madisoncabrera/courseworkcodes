# define two exception class: InvalidLength and InvalidFirstChar
class InvalidLength(Exception):
    def __init__(self,key): 
        self.key=key 

    def __str__(self):
        return f'Invalid length. Must be 5 characters.' #return error string
    
class InvalidFirstChar(Exception):
    def __init__(self,key):
        self.key=key

    def __str__(self):
        return f'Must start with the letter G' #return error string

class SpecialDict(dict):
    def setdefault(self, key, value):
        # define a try and except block
        # to add a key value pair to the dict
        # check the conditions on the key
        # if conditions are not met
        # raise specific exceptions
        # else call super class's setdefault method
        # super().setdefault(key, value)
        try:
            if len(key)!=5: #if len not equal to 5
                raise InvalidLength(key) #raise error 
            if not key.startswith('g'):#if not start w g
                raise InvalidFirstChar(key) #raise error
        except (InvalidLength,InvalidFirstChar) as e: 
            print(e) #print error

        else:
            super().setdefault(key,value) #add to roster
            print(f'{key} was added to the roster.') #print success
        

class Department(object):
    
    roster = SpecialDict()
    
    def add_student(self):
        # user input for GMU ID(key) and full name(value)
        # call setdefault to add a student to roster dict.
        key=input('Enter the GMU ID: ').lower() #user input
        value=input('Enter the students full name: ') #user input
        self.roster.setdefault(key,value) #call fxn
        
        

    def print_roster(self):
        # your code here
        # print the roster dict using a for loop
        for key,value in self.roster.items():
            print(f'{key}-{value}') #print roster 

# keep adding a student as long as user selects 'y'
choice = ''
while choice != 'n':
    d = Department() #fxn call
    d.add_student() #fxn call
    choice = input('Continue adding? (y/n): ')

print('Student Roster')
d.print_roster() #fxn call
            
        



