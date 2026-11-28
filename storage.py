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
    global inventory
    id=int(input("Enter id of product: "))
    if inventory['id'].isin([id]).any():  
        print("This id is already exist..try with another id")
    else:
        name=str(input("Enter name of product: "))
        quantity=int(input("Enter the quantity: "))
        price=int(input("Enter the price: "))
        reorder_level=int(input("Enter the reorder number: "))

        df1= pd.DataFrame({'id':[id],'name':[name],'quantity':[quantity],'price':[price],'reorder_level':[reorder_level]})
        inventory=pd.concat([inventory,df1],ignore_index=True)
        inventory.to_csv('data/inventory.csv',index=False)
        print(inventory)

def view_inventory():
    if inventory.empty==True:
        print("Inventory is empty")
    else:
        print(inventory)


def search_product():
    Name = str(input("Search with name: "))
    if (inventory['name']==Name).any():
       print( inventory[inventory['name']==Name])
    else:
        print("This product is not available")


def low_stock():
    low=inventory[inventory['quantity']<= inventory['reorder_level']]
    if low.empty:
        print("Product quantity is fine")
    else:
        print("This product should be ordered")
        print(low)

def  total_inventory_value():
    total=(inventory ['quantity']* inventory['price']).sum()
    print("Total inventory value is :",total)

def sell_product():
    global inventory, transaction
    product_id=int(input("Enter the product id "))
    product =inventory[inventory['id']==product_id]
    if product.empty:
        print("product isnot avalilable")
    else:
        need=int(input("How many units customer want :"))
        if need<=0:
            print("Enter a valid quantity")
        else:
            avilable=product['quantity'].iloc[0]
            if need<=avilable:
                print("You can sell this product")
                inventory.loc[inventory['id']==product_id,'quantity']=avilable-need
                inventory.to_csv('data/inventory.csv',index=False)
                if transaction.empty:
                    new_id=1
                else:
                    new_id=int(transaction['transaction_id'].max())+1
                new_transaction=pd.DataFrame({'transaction_id':[new_id],'product_id':[product_id],'transaction_type':['sale'],'quantity':[need],'price_per_unit':[product['price'].iloc[0]]})
                transaction=pd.concat([transaction,new_transaction],ignore_index=True)
                transaction.to_csv('data/transaction.csv',index=False)     
            else:
                print("Not have enough product")

def load_transaction():
    os.makedirs('data', exist_ok=True)
    if(os.path.exists('data/transaction.csv')):
        df=pd.read_csv('data/transaction.csv')
        return(df)
    else:
        df2=pd.DataFrame(columns=['transaction_id','product_id','transaction_type','quantity','price_per_unit'])
        df2.to_csv('data/transaction.csv',index=False)
        return (df2)
transaction=load_transaction()

def view_transaction():
    if transaction.empty==True:
        print("No transaction history found")
    else:
        print(transaction)

def restock_product():
    product_id=int(input("Enter the product id: "))
    product=inventory[inventory['id']==product_id]
    if product.empty:
        print("Product isnot available")
    else:
        arrive=int(input("How many arrived"))
        if arrive<=0:
            print("Invalide number")
        else:
            available = product['quantity'].iloc[0]
            inventory.loc[inventory['id']==product_id,'quantity']=available+arrive
            inventory.to_csv('data/inventory.csv',index=False)

def main_menu():
    while True:
        print("===== INVENTORY MANAGER =====")
        print("1. Add product")
        print("2. View inventory")
        print("3. Search product")
        print("4. Low stock alart")
        print("5. Total inventory value")
        print("6. Sell product")
        print("7. Restock product")
        print("8. View transaction history")
        print("9. Exit")

        choose=int(input("Enter your choose"))
        if choose==1:
            add_product()
        elif choose==2:
            view_inventory()
        elif choose==3:
            search_product()
        elif choose==4:
            low_stock()
        elif choose==5:
            total_inventory_value()
        elif choose==6:
            sell_product()
        elif choose==7:
            restock_product()
        elif choose==8:
            view_transaction()
        elif choose==9:
            print("Thank you for using")
            break
        else:
            print("Invalid choose...try another")

main_menu()