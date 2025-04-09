class CircularBuffer:
    def __init__(self, n):
        self.__n=n
        #emptylist useful to set a max size in the loop
        self.__buffer=[]

    @property
    def n(self):
        return self.__n
    
    def add(self, item):
        self.__buffer.append(item)
        if len(self.__buffer) == (self.__n+1):
            return self.__buffer.pop(0) #we pop the firstv element if the max length is reached
        return self.__buffer
    
    def __len__(self):
    #len(obj) will actually call obj.__len__() behind the scenes
        return len(self.__buffer)
    
    def __getitem__(self, index): 
    #You can have your own classes respond to [] by defining the __getitem__ dunder method:
        return self.__buffer[index]
