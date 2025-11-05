

#create dictionary
def create_dict(filename):
    '''parameter is name of txt file, need to add into application file!
    returns dictionary, key=item, value=dict w/______
    convert file into & store in dictionary'''
    grocery_dict = {}
    with open(filename, 'r') as fin:
        for line in fin:
            itemID, name, department, quantity, price = line.split(':')
            #store in dict -> grocery_dict[ID/name] = {dict of values here}
            grocery_dict[itemID] = {'name' : name, 'department' : department, 'quantity' : quantity, 'price' : price}
    return grocery_dict

#price list function
price list (using dictionary) function
def print_dict(grocery_dict):
    for k, v in grocery_dict.items():
        line = '{} | {}\n.'.format(k, '|'.join(v.values()))
        print(line)
        #another way -> print(k, '-'.join(v))

#show items on sale function
def sale_items(grocery_dict):
    sale_items={}
    for item in grocery_dict:
        if price=={2f.97}:
            sale_dict.append(item)
         print(sale_dict)   
        
#purchase by name function
def purchase_by_name(grocery_dict, cart):
    for item in items:
        itemID, name, department, quantity, price = line.split(':')
        if name == user_name:
            cart.append(item)
            print(f'{user_name} was added to cart!')
            
#purchase by price function
def purchase_by_price(grocery_dict, cart):
    for item in items:
        itemID, name, department, quantity, price = line.split(':')
        if price == user_price:
            cart.append(item)
            print(f'{user_price} was added to cart!')

#purchase by category function
def purchase_by_category(grocery_dict, cart):
    for item in items:
        itemID, name, department, quantity, price = line.split(':')
        if category == user_category:
            cart.append(item)
            print(f'{user_category} was added to cart!')

#view inventory function
def view_inventory(grocery_dict):
    for item in grocery_dict:
        itemID, name, department, quantity, price = line.split(':')
        return(item_name, quantity)
    

#checkout function

def checkout(grocery_dict, cart):
    total = 0
    for item in cart:
        itemID, name, department, quantity, price = line.split(':') #may have to change based on v dict
        price = float(price)
        total += price
    print(f'Total Purchase Items: $(total:.2f)')
    return Total
#discount function
def apply_discount(cart,new_total):
    new_total=0
    total=0
    for item in cart:
        itemID, name, department, quantity, price = line.split(':') #may have to change based on v dict
        price = float(price)
        total += price
        if total>=20.00:
            new_total=total*0.8
            print(f'Your discounted total is${new_total}.')
            return True
        else:
            return False 

#exit function
def exit():
    print('You have exited Wegmans Grocery. Thank you for shopping with us.')
