from datetime import datetime
import random
import string

from Invoicepy import catalogItem

class Invoice():
    
    order_id: int
    customer_id: int
    checkout_amount: int
    address: string
    timestamp: str
    cartItems = []

    def __init__(self, cart, customer_id, address):
        '''
            Initialize an Invoice object using the cart provided to the constructor.
            The customer_id and address are needed for commiting transaction into ORDERSDB
        '''
        
        self.order_id=random.randint(1, 100000)
        self.customer_id=customer_id
        self.address=address
        self.checkout_amount=0
        self.timestamp = str(datetime.now())
        self.cartItems = cart
        
        for item in cart:
            self.checkout_amount += item.amount

        self.checkout_amount = round(self.checkout_amount, 2)
    
    
    def print(self):
        '''
            Prints the transaction Invoice for the customer.
        '''
        
        print("********** INVOICE **********\n")
        print("Order Number: ", self.order_id)
        print("Customer ID:", self.customer_id)
        print("Customer Address:", self.address)
        print("Order Date and Time:", self.timestamp)
        print()

        print("Checkout items: ")
        for cartItem in self.cartItems:
            cartItem.printVerbose()
            print()
        
        print("Final amount: ₹", self.checkout_amount)
        print(100*'_')
