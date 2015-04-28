"""
    This account class represents bank accounts that stores money for an owner.
"""

class Account(object):

    def __init__(self, name):
        self.balance = 0
        self.owner = name

    def deposit(self, amount):
        """
            Deposits 'amount' into account
        """
        self.balance = self.balance + amount

    def withdraw(self, amount):
        """
            Deposits 'amount' into account
        """
        self.balance = self.balance - amount

    def getBalance(self):
        """
            Returns balance of the account
        """
        return self.balance

    def getOwner(self):
        """
            Returns owner of the account
        """
        return self.owner

    def transferTo(self, amount, receiving_account):
        if (self.balance < amount):
            return False #not enough money
        self.withdraw(amount)
        self.deposit(amount)
        return True
