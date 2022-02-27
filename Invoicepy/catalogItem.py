import string

class catalogItem():

    item_id: int
    name: string
    price: float
    discount: float
    category: string
    tax_rate: float
    amount: float

    def __init__(self, params):
        '''
            Initiates the catalogItem class object from the params provided to it.
            The params ought to be fetched from the DB before calling the constructor.
        '''

        self.item_id=params[0]
        self.name=params[1]
        self.price=params[2]
        self.discount=params[3]
        self.category=params[4]
        self.tax_rate=params[6]
        self.amount = round((self.price * (1-(self.discount/100))) * (1+(self.tax_rate)/100), 2)
    
    def print(self):
        '''
            Prints the information about the catalogItem
            Only the information necessary for catalog display is printed
        '''
        
        print('‣', self.item_id, self.name, ', price: ₹', self.price, ', discount: ', self.discount, '%')
        print()

    def printVerbose(self):
        '''
            Prints the information about the catalogItem
            The information necessary for Invoice printed;
        '''

        print('‣', self.name)
        print('price: ₹', self.price, ',',
        ' discount: ', self.discount, '%,',
        ' tax rate: ', self.tax_rate, '%,',
        ' amount: ₹', self.amount
        )
