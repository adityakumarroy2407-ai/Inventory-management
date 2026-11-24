import pandas as pd
import os

def load_inventory():
    os.makedirs('data', exist_ok=True)
    if(os.path.exists('data/inventory.csv')):
        df = pd.read_csv('data/inventory.csv')
        return(df)
    else:
        df=pd.DataFrame(columns=['id','name','quantity','price','reorder_level'])
        df.to_csv('data/inventory.csv',index=False)
        return df
inventory =load_inventory()

def add_product():
    id=int(input("Enter id of product: "))
    if inventory['id'].isin([id]).any():  
        print("This id is already exist..try with another id")
    else:
        name=str(input("Enter name of product: "))
        quantity=int(input("Enter the quantity: "))
        price=int(input("Enter the price: "))
        reorder_level=int(input("Enter the reorder number: "))

        df1= pd.DataFrame({'id':[id],'name':[name],'quantity':[quantity],'price':[price],'reorder_level':[reorder_level]})
        global inventory
        inventory=pd.concat([inventory,df1],ignore_index=True)
        inventory.to_csv('data/inventory.csv',index=False)
        print(inventory)

add_product()
add_product()

