class Bookstore:
    # REQUIRED ATTRIBUTES:
    #   name (str), location (str), catalog (dict: title -> price)
    # REQUIRED METHODS:
    def __init__(self, name, location):
        # initialize name, location and catalog dictionary
        # YOUR CODE HERE
        self.catalog = {} #initialize the dict
        self.name=name 
        self.location=location
    def add_to_catalog(self, title, price):
        if title in self.catalog: #check to see if in catalog
            print(f'ERROR: {title} was found.')
        else:
            self.catalog[title]=price #add to dict
            print(f'{title} has been added.')
            
        # if the title in the catalog
        #   return an informational message
        # else:
        #   add the title and price to self.catalog
        #   return an informational message

    def update(self, title, new_price):
        self.catalog[title]=float(new_price) #update the new price- as a float not string
        if title in self.catalog:
            self.catalog[title]=new_price
            print(f'{title} has the updated price {new_price}.')
        else:
            print(f'ERROR: {title} was not found.') #error message
            
        # if title in the catalog:
        #   update the price with new_price
        #   return an informational message
        # else return an informational message 

    def __str__(self):
       return f'{self.name} Location: {self.location}'
    



# Example usage (students can follow the spec steps):
store1 = Bookstore("PageTurner Books", "Fairfax")
store2 = Bookstore("DataDives", "Washington DC")
print(f'Welcome to {store1}') #print title/loc
print(f'Welcome to {store2}')


#PageTurner Books - store1
store1.add_to_catalog("The Ocean at the End", 9.50)
store1.add_to_catalog("Python Tales", 12.99)
store1.add_to_catalog("Mystery Bites", 8.00)
#DataDives Books - store2
store2.add_to_catalog("AI 101", 5.00)
store2.add_to_catalog("AI 101", 5.00)#to test repeat
store2.add_to_catalog("Data Structures", 10.50)
store2.add_to_catalog("IT 200", 7.00)
store1.update('Intro to Prog', 20.00) # for store 1
store1.update('Python Tales', 25.99) #for store 1
store1.update('The Ocean at the End', 10.50) # store1
store2.update('Fix-It Friends', 2.99)#store2
    


