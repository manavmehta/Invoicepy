import random
import string

from Invoicepy import catalogItem

class Invoice():
    '''
    Invoice class
    '''

    order_id: int
    customer_id: int
    checkout_amount: int
    address: string
    cartItems = []

    def __init__(self, cart, customer_id, address):
        self.order_id=random.randint(1, 100000)
        self.customer_id=customer_id
        self.address=address
        self.checkout_amount=0
        self.cartItems = cart
        for item in cart:
            self.checkout_amount += item.amount
        
        for cartItem in self.cartItems:
            cartItem.print()
    
    def print(self):
        print("INVOICE")
        print("Order Number : ", self.order_id)

        print("Checkout items: ")
        for cartItem in self.cartItems:
            cartItem.printVerbose()
        
        print("Final amount: ", self.checkout_amount)
        print(50*'_')
