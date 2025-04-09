class Money:
    def __init__(self, amount, currency):
        self.amount= amount
        self.currency= currency
    #getter and setter for amount
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            raise ValueError ("amount is a digit number")
        self.__amount=value
    #getter and setter for currency
    @property
    def currency (self):
        return self.__currency
    @currency.setter
    def currency(self,value):
        if not value.isalpha():
            raise ValueError ("currency is a string ")
        self.__currency= value
    #to add 2 objects together we need the dunder __add__ 
    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("other should be also a type of Money")
        else:
            if other.currency== self.currency:
                return Money(self.amount+other.amount, self.currency)
            else:
                raise RuntimeError("Mismatched currencies!")
    #to substract 2 objects from each other we use the __sub__
    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError("other should be also a type of Money")
        else:
            if other.currency== self.currency:
                return Money(self.amount-other.amount, self.currency)
            else:
                raise RuntimeError("Mismatched currencies!")
    #to multiply two objects together we use the __mul__
    def __mul__(self,number):
        if not isinstance(number, int):
            raise TypeError("other should be a number")
        else:
            return Money(self.amount*number, self.currency)


        


    



            

