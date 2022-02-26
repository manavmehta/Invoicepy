import Invoicepy as ip
import os

def printCatalog(cursor):
    cursor.execute("select * from catalog left join tax_rates on catalog.category = tax_rates.category;")
    for item in cursor:
        ci = ip.catalogItem(item)
        ci.print()

def printCart(cursor):
    cursor.execute("select * from catalog left join tax_rates on catalog.category = tax_rates.category;")
    for item in cursor:
        cartItem = ip.catalogItem(item)
        cartItem.print()

def addToCart(item_id, cart, cursor):
    cursor.execute("select * from catalog left join tax_rates on catalog.category = tax_rates.category where id=" + item_id + ';')
    found=0
    
    for item in cursor:
        found=1
        cartItem=ip.catalogItem(item)
        cartItem.print()

    if found:
        cart.append(cartItem)
        return 0
    else:
        return 1
        # can be further used for other error codes

def deleteFromCart(item_id, cart):
    found=0
    index=0
    for item in cart:
        if item.item_id == item_id:
            found=1
            break
        else:
            index+=1
    
    if found:
        cart.pop(index)
        return 0
    else:
        return 1

def checkout(cart, customer_id=1, customer_address='dummy'):
    invoice = ip.Invoice(cart, customer_id, customer_address)
    os.system('clear')
    invoice.print()