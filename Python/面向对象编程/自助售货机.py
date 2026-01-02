class VendingMachine:
    def __init__(self,product,price):
        self.product=product
        self.price=price
        self.fund=0
        self.amount=0
    def vend(self):
        if self.amount==0:
            print('Nothing left to vend. Please restock')
        elif self.fund<self.price:
            gap=self.price-self.fund
            print('Please add $'+str(gap)+' more funds')
        else:
            change=self.fund-self.price
            print('Here is your '+str(self.product)+' and $'+str(change)+' change')
            self.fund=self.fund-self.price
            self.amount=self.amount-1
    def restock(self,new_product):
        self.amount=self.amount+new_product
        print('Current '+str(self.product)+' stock: '+str(self.amount))
    def add_funds(self,new_fund):
        self.fund=self.fund+new_fund
        print('Current balance: $'+str(self.fund))