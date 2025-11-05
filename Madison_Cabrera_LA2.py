#-------------------------------------------------------------------------------
# LA2.py
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

class AbsVal:
    
    def __init__(self,x,y):
        self.x=float(x) #float so that numbers can be manipulated in case a decimal is added
        self.y=float(y)

    def solve(self):
        start= self.x**2 + self.y**2 #square per equation
        av= start**0.5 #sqrt per equation
        return av

    def __str__(self):
        return f' The absolute value of {x}-i{y} is {av}.'
    

while True: #making a loop to ask the choice
    
    x=input('Enter x: ') #user input
    y=input('Enter y: ')

    z=AbsVal(x,y) #new variable to call to be able to run the solve on
    av=z.solve() #run solve on the user input variables put into z
    print(z) 

    choice=input('Do you want to continue? y/n : ') #ask if continue

    if choice != 'y':
        print('DONE.') #if no print done and get out of function
        break
        

