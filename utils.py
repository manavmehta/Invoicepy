import Invoicepy as ip
import os
import loggerUtil

logger = loggerUtil.getLogger()


def printCatalog(cursor, DB):
    '''
        Prints the catalog available
    '''

    try:
        cursor.execute("select * from " + DB + " left join tax_rates on catalog.category = tax_rates.category;")
        logger.debug("Catalog printed successfully")
    except:
        logger.error("Print catalog execution failed")

    for item in cursor:
        ci = ip.catalogItem(item)
        ci.print()


def addToCart(item_id, cart, cursor, DB):
    '''
        Adds the item corresponding to item_id into the cart.
        Accepts, item_id from the user,
        searches the mysql DB, if found, adds to cart.

        Return value:
            0 -> operation successful
            Other value -> operation failed
    '''

    try:
        cursor.execute("select * from catalog left join tax_rates on catalog.category = tax_rates.category where id=" + item_id + ';')
        logger.debug("successful addToCart DB execution with item_id=%s", item_id)
    except:
        logger.error("unsuccessful addToCart DB execution with item_id=%s", item_id)
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
        Deletes the item corresponding to item_id from the cart.
        Accepts, item_id from the user,
        searches the cart, if found, performs deletion.

        Return value:
            0 -> operation successful
            Other value -> operation failed
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
        Executes a checkout operation using the cart.
        Generates invoice item, commits transaction
        into ORDERSDB.
        cart must be a list of catalogItems.
    '''

    try:
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
        logger.debug("Checkout successful")
    
    except:
        logger.log("Checkout Failed!")
    
    exit()


helloMessage = "Hello user\nWelcome to ShopPy powered by InvoicePy :)\n"
