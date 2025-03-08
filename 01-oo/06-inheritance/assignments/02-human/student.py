class Human:
    def __init__(self, name):
        self.__name = name #mangled private name if we want to access it we do obj._class__prv_var

    def get_name(self):
        return self.__name


class Archer(Human): #inherits fromm human class
    def __init__(self, name, num_arrows):
        super().__init__(name) #calling super constructor  
        self.__num_arrows= num_arrows #priv 

    def get_num_arrows(self):
        return self.__num_arrows #priv 
    


