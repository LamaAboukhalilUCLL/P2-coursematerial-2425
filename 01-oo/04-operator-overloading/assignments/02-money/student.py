class Money:
    # constructor init
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

        #add method for obj
    def __add__ (self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money (self.amount + other.amount, self.currency) #only adding the amount
            else:
                raise RuntimeError("Mismatched currencies!")
        else:
            raise TypeError("Unsupported operand type for +: " + str(type(other)))
        
    def __sub__ (self, other):
        if isinstance(other, Money):
            if self.currency== other.currency:
                return Money (self.amount - other.amount, self.currency) #only - the amount
            else:
                raise RuntimeError("Mismatched currencies!")
        else:
            raise TypeError("Unsupported operand type for -: " + str(type(other)))
        
    def __mul__(self, number):
        return Money(self.amount * number, self.currency)
    
    #use of repr method to printout the results instead of assigning a print value above
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"



            

