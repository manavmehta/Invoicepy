import mysql.connector
import os
from dotenv import load_dotenv
import utils
import time

load_dotenv()

USER, PASSWORD = os.getenv('USER'), os.getenv('PASSWORD')

DB = mysql.connector.connect(user=USER, password=PASSWORD,
    host='127.0.0.1', database='catalog', auth_plugin='mysql_native_password')

cursor = DB.cursor()

cart = []

while(True):
    # os.system('clear')
    menuChoice = input(
        '1. Browse Catalog \n'
        '2. Check Cart\n'
        '3. Checkout\n'
        '~> '
    )

    if(menuChoice=='1'):
        while(True):
            utils.printCatalog(cursor)
        
            catalogChoice = input(
                '• To add item to cart, type \'Add <item_id>\' \n'
                '• To delete item from cart, type \'Delete <item_id>\' \n'
                '• To checkout, type \'Checkout\'\n'
                '• To return to main menu, type \'Return\'\n'
                '~> '
            ).split(' ')

            if(catalogChoice[0].lower()=='add'):
                add_status = utils.addToCart(catalogChoice[1], cart, cursor)
                if(add_status==0):
                    print("Added to the cart")
                else:
                    print("Item not found in the catalog. Please check the item number")
                time.sleep(2)
            
            elif(catalogChoice[0].lower()=='delete'):
                delete_status = utils.deleteFromCart(int(catalogChoice[1]), cart)
                if delete_status == 0:
                    print("Deleted")
                else:
                    print("Item not found in cart")
                time.sleep(2)
        
            elif(catalogChoice[0].lower()=='checkout'):
                utils.checkout(cart)
                break
        
            elif(catalogChoice[0].lower()=='return'):
                break

            elif(catalogChoice[0].lower()=='clear'):
                os.system('clear')
        
            else:
                print("Invalid choice. Please choose from the options above1. \n")
                time.sleep(2)
        

    elif(menuChoice=='2'):
        if len(cart)>0:
            for item in cart:
                item.print()
        else:
            print("Cart is empty")
        time.sleep(2)

    elif(menuChoice=='3'):
            utils.checkout(cart)
            break
    
    else:
        print("Invalid choice. Please choose from the options above. \n")
        time.sleep(2)
    