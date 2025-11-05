import project_utility as u
def main():
    filename='WEGMANS_ITEMS.txt'
    user_choice=''
    while user_choice!=9:
        print('1.Show price list.')
        print('2.Show sale items.')
        print('3.Purchase from name list.')
        print('4.Purchase from price list.')
        print('5.Purchase from category list.')
        print('6.View Inventory')
        print('7.Apply discount, if over $20 purchase.')
        print('8.Checkout.')
        print('9.Exit.')
        user_choice=input('Enter your selection for how you choose to shop.')

        if user_choice=='1': #show price list
            grocery_dict=u.create_dict(filename)
            price_list=u.print_dict(grocery_dict)
            
        elif user_choice=='2': #show sale items
            items on sale=u.sale_items(grocery_dict)
            
        elif user_choice=='3': #purchase from name
            user_name=input('Enter the name of the item you want to search: ')
            purchase=u.purchase_by_name(grocery_dict,cart)
            
        elif user_choice=='4': #purchase by price
            user_price=input('Enter the price you are searching for: ')
            p_by_price=u.purchase_by_price(grocery_dict,cart)
            
        elif user_choice=='5': #purchase by category
            user_category=input('Enter the category that you are looking for: ')
            p_by_cat=u.purchase_by_category(grocery_dict,cart)
        
            
        elif user_choice=='6': #view inventory
            view=u.view_inventory(grocery_dict)
                        
        elif user_choice=='7': #apply discount
            discount=u.apply_discount(cart,new_total)
            
        elif user_choice=='8': #checkout
            checking_out=u.checkout(grocery_dict,cart)
            
        elif user_choice=='9': #exit
            exiting=u.exit()
            
        else:
            print('Invalid option.')

main()
