import Invoicepy as ip
import os

def printCatalog(cursor, DB):
    '''
        helper function responsible to print the catalog available
    '''

    cursor.execute("select * from " + DB + " left join tax_rates on catalog.category = tax_rates.category;")
    for item in cursor:
        ci = ip.catalogItem(item)
        ci.print()

def printCart(cursor, DB):
    '''
        helper function responsible to print the cart of the user
    '''

    cursor.execute("select * from catalog left join tax_rates on catalog.category = tax_rates.category;")
    for item in cursor:
        cartItem = ip.catalogItem(item)
        cartItem.print()

def addToCart(item_id, cart, cursor, DB):
    '''
        helper function responsible to add an item into the cart
        accepts, item_id from the user,
        searches the mysql DB, if found, adds to cart.
    '''

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
    '''
        helper function responsible to delete an item from the cart
        accepts, item_id from the user,
        searches the cart, if found, adds to cart.
    '''

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

def checkout(cart, cursor, DB, dbName, customer_id=1, customer_address='dummy'):
    '''
        helper function responsible to make a checkout operation
        using the cart. Generates invoice item, commits transaction
        into ORDERSDB
    '''

    invoice = ip.Invoice(cart, customer_id, customer_address)
    os.system('clear')
    invoice.print()

    cursor.execute("insert into " + dbName +
            " values(" +
            str(invoice.order_id) + ", " + 
            str(invoice.customer_id) + ", " +
            str(invoice.checkout_amount) + ", \"" + 
            invoice.address+ "\", \"" + 
            invoice.timestamp + "\");")
    DB.commit()
    exit()
    

helloMessage = "Hello user\nWelcome to ShopPy powered by InvoicePy :)\n"
