def build_dict(filename):
    store={}
    with open(filename, 'r') as f: #open file
        for line in f:
            app, price= line.strip('\n').split(',') #break down line
            store[app]=price #store in dict
        return store

def add_app(app,price,store):
    if app in store.keys(): #check to see if present
        print('App already exists.')

    else:
        store[app]=price #if not present- add to dict
        print(store)

def del_app(app,price,store):
    if app in store.keys(): #check to see if its present
        del store[app] #delete
        print(f' App: {app} has been deleted.') #alert user
def update_file(app,price,store):
     with open('new_playstore.txt','w') as fout: #create new txt file
        for k,v in store.items():
               line=k+'-'+str(v)+'\n' #concatenate components
               fout.write(line) #write to file
               
    
def main():
    filename= 'playstore.txt'
    store=build_dict(filename) #saving this as universal dict to be used for all fxns
    #call build_dict function and return store
    build=build_dict(filename)
    print(store) #show the store 
    app = input('Enter an app name: ')
    price = float(input('Enter price:'))
    #call add_app function
    add=add_app(app,price,store)
    app = input('Enter an app name to delete: ')
    #call del_app function
    delete=del_app(app,price,store)
    #call update_file function
    update=update_file(app,price,store)
    
main()
