# class Queue:
#     index=0
#     #an initial queue is usually empty
#     def __init__(self):
#         self._items=[] #empty list called items and it is private

#     #adds a new item to the queue
#     def add(self, item):
#         self._items.append(item) #append is adding an item at the end
    
#     #removes and returns the next item from the queue
#     def next(self):
#         if self.is_empty():   #if the list is empty (.is_empty() method used down) we return an error 
#             raise IndexError("the queue is empty")
#         return self._items.pop(0)   #else we remove the first person from the list and return it (pop speciality)

#     def is_empty(self):
#         return len(self._items) == 0 #True if the list is empty 


# #okay so the next method pops the first value, by taking it out of the list and returning it as the output value,
# #  so when we first removed alice, we took it out of the list and returned it since it is a pop fucntion. and 
# # then Bob becomes rthe first one in the list so when we pop again bob was at index 0 and same thibg happened

#-------------------------------------------------------------------------
class Queue:
    def __init__(self):
        self.__queue= [] #new queue is empty
    @property
    def queue(self):
        return self.__queue #reading the queue
    def add(self,item):
        self.__queue.append(item) #add new customer to the end 
    def next(self):
        if not self.is_empty(): #iif the queue isnt empty
            return self.__queue.pop(0) #remove first one, who gets served
        else:
            raise IndexError("the list is empty")
    def is_empty(self):
        return self.__queue== [] #true if it is empty, false if it isnt
 
    

    

