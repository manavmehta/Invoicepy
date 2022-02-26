import string

class catalogItem():
    '''
    catalogItem class
    '''

    item_id: int
    name: string
    price: float
    discount: float
    category: string
    tax_rate: float
    amount: float

    def __init__(self, params):
        self.item_id=params[0]
        self.name=params[1]
        self.price=params[2]
        self.discount=params[3]
        self.category=params[4]
        self.tax_rate=params[6]
        self.amount = round((self.price * (1-(self.discount/100))) * (1+(self.tax_rate)/100), 2)
    
    def print(self):
        print('‣', self.item_id, self.name, ', price: ₹', self.price, ', discount: ', self.discount, '%')
        print()

    def printVerbose(self):
        print('‣', self.name)
        print('price: ₹', self.price, ',',
        ' discount: ', self.discount, '%,',
        ' tax rate: ', self.tax_rate, '%,',
        ' amount: ₹', self.amount
        )
    