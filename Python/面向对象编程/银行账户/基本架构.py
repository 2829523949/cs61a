class Account:
    max_withdrawal=10
    interest=0.02

    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance

    def withdral(self,amount):
        if self.balance<amount:
            return "Insufficient funds"
        elif amount>Account.max_withdrawal:
            return "Can't withdraw that amount"
        else:
            self.balance=self.balance-amount
            return self.balance     
    
    def time_to_retire(self,amount):
        assert self.balance>0 and amount>0 and self.interest>0
        year=0
        copy=self.balance 
        while copy<amount:
            copy=copy*(1+self.interest)
            year=year+1
        return year
class Freechecking(Account):
    withdraw_fee=1

    def __init__(self,holder):
        self.balace=0
        self.holder=holder
        self.free_withdrawals=2

    def withdral(self,amount):
        if amount>self.max_withdrawal:
            return "Can't withdraw that amount"
        else:
            if self.free_withdrawals>0:
                self.free_withdrawals=self.free_withdrawals-1
                return Account.withdral(self,amount)
            else:
                return Account.withdral(self,amount+self.withdraw_fee)