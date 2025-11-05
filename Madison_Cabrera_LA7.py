#-------------------------------------------------------------------------------
# Name: FirstName LastName
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Comments to grader:
#-------------------------------------------------------------------------------
# Code: Tkinter GUI — Library Book Checkout (writes to checkouts.txt)
#-------------------------------------------------------------------------------
import os
os.chdir("/Users/mcabre1")

from tkinter import *
from datetime import datetime

class LibraryCheckout(Frame):
    def __init__(self, root):
        Frame.__init__(self,root)
        self.status=StringVar(self,'Please enter your details')
        self.create_widgets()

    def create_widgets(self):
        self.name= Label(self,text= 'Student Name')
        self.gnum= Label(self,text= 'G Number')
        self.btitle= Label(self,text= 'Book Title')
        self.date= Label(self,text= 'Due Date (MM/DD/YYYY')
        self.name_entry= Entry(self)
        self.gnum_entry=Entry(self)
        self.btitle_entry=Entry(self)
        self.date_entry= Entry(self)

        self.name.grid(row=0,column=0)
        self.gnum.grid(row=1,column=0)
        self.btitle.grid(row=2,column=0)
        self.date.grid(row=3,column=0)
        self.name_entry.grid(row=0,column=1)
        self.gnum_entry.grid(row=1,column=1)
        self.btitle_entry.grid(row=2,column=1)
        self.date_entry.grid(row=3,column=1)

        self.b=Button(self,text='Add',command=self.add)
        self.b.grid(row=4,column=0,columnspan=2)

        self.status_label=Label(self,textvariable=self.status)
        self.status_label.grid(row=5,column=0,columnspan=2)
        
        

        # Status StringVar

        # -----------------------------
        # a) Create widgets + layout
        # -----------------------------
        # Labels and entries

        # Button


        # Status label and associate with textvariable to connect to status stringVar

    # -----------------------------------------------------------------------
    # b) add(): validate and append a line to checkouts.txt, update status
    # -----------------------------------------------------------------------
    def add(self):
        # Read values
        # Validation — non-empty
        # Validation — date format MM/DD/YYYY
        name_entry= self.name_entry.get().strip()
        gnum_entry=self.gnum_entry.get().strip()
        btitle_entry=self.btitle_entry.get().strip()
        date_entry= self.date_entry.get().strip()

        if len(name_entry)==0:
             self.status.set('Error. Cannot be empty.')
             return
        if len(gnum_entry)==0:
             self.status.set('Error. Cannot be empty.')
             return
        if len(btitle_entry)==0:
             self.status.set('Error. Cannot be empty.')
             return
        if len(date_entry)==0:
             self.status.set('Error. Cannot be empty.')
             return
        
        
        try:
           due_date=datetime.strptime(date_entry, '%m/%d/%Y').date()
        except ValueError:
            self.status.set('Invalid date. Use MM/DD/YYYY.')

        

        # Append to tab-separated text file
        with open('checkouts.txt','a') as f:
            f.write(f'{name_entry}, {gnum_entry}, {btitle_entry}, {date_entry}\n')
            
            

        # d/e) Status messaging (success)

        self.status.set('Added Successfully!.')

# your code here
# create root window and object, then call mainloop
if __name__ == "__main__":
    root = Tk()
    app = LibraryCheckout(root)
    app.grid() # IH: since app is a frame, needs layout manager
    root.mainloop()

