from tkinter import *

class MyFrame(Frame):
        def __init__(self, root):
                Frame.__init__(self,root)
                self.items = [['egg', 'dairy', 1.99, '12/12/2023'], ['milk', 'dairy', 2.99, '1/2/2024'], \
                              ['salmon', 'seafood', 4.99, '12/10/2024']] #2d List, each small list contains item info
                
                self.data=StringVar(self,'Subtotal: $0.00')#Initialize StringVar and set current subtotal to be 0.0
                self.welcome() #call welcome method to start the code
                

        def init_container(self):
                self.quantity_entries = [] #qunatity entry list, i-th entry has i-th quantity
                self.states = [] #holds state if selected/not, i-th item holds i-th state
                
        def clear_frame(self): #clears the previous frame
                for widget in self.winfo_children():
                        widget.destroy()
                
        def welcome(self):
                self.clear_frame()
                
                l1=Label(self,text='Welcome to the grocery store!')
                b1=Button(self,text='Start Ordering',command=self.start)#start ordering button: command = self.start
                l1.pack()#layout button
                b1.pack()
                

        def start(self):
                self.clear_frame()
                self.init_container()
                
                for row, item in enumerate(self.items):
                        self.states.append(IntVar()) #creating the check buttons
                        c = Checkbutton(self, text = item[0],variable = self.states[row])
                        c.grid(row=row,column=0) #formatting the check button
                       
                        price_label=Label(self,text=f'${item[2]:.2f}')#create and layout a price_label where text set to price of an item
                        price_label.grid(row=row,column=1)

                        quantity_entry=Entry(self)#create and layout an qunatity_entry - user enter quantity
                        quantity_entry.grid(row=row,column=2)
                        self.quantity_entries.append(quantity_entry)#append to quantity_entries list - see init_container method

                        expiration_label=Label(self,text=item[3])#create and layout expiration_label, set text to exipration date of an item
                        expiration_label.grid(row=row,column=3)

                subtotal_label=Label(self,textvariable=self.data) #create subtotal label
                #create and layout subtotal_label and set textvariable to StringVar created in __init__
                subtotal_label.grid(row=len(self.items)+1,column=0) #layout goes one below the other items 

                add_to_cart_button=Button(self,text='Add to cart',command=self.add_to_cart)#create and layout add_to_cart_button and set command = add_to_cart method
                add_to_cart_button.grid(row=len(self.items)+1,column=2)
                

        def add_to_cart(self):
                '''Displays subtotal after user adds item to cart'''
                current_subtotal = 0 #initialize current subtotal
                
                for i in range(len(self.items)):
                        
                        if (self.states[i].get() == 1): #check if item selected using get()
                
                                product_quantity = int(self.quantity_entries[i].get())  #get the quantity user selected
                                #obtain item name from self.items using index notation

                                        
                                item_price=self.items[i][2]#obtain item price from self.items using index notation
                                current_subtotal += item_price * product_quantity#calculate current subtotalmultiplying  item price with quantity
                                

                #set the self.data to current_subtotal 
                self.data.set(f'subtotal: ${current_subtotal:.2f}')
                
        
                
#main driver code
root=Tk()#create root window
root.title('Grocery Cart')
app=MyFrame(root)#object of MyFrame class
app.pack()
root.mainloop()#layout and call mainloop()
                     

