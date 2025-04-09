class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if (self.__num_arrows>=num):
            self.__num_arrows-=num
        else:
            raise Exception ("Not enough arrows")

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3) #this decreases number of arrows by 3 (using arrows)
        # Handle both string targets and Human objects
        if isinstance(target, str):
            target_name = target
        else:
            target_name = target.get_name()
            
        return f"{target_name} was shot by 3 crossbow bolts"
    
