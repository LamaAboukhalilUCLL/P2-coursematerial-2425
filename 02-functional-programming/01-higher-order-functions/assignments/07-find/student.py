#find function that takes a list of any kind of object, together with condition function such that it returns the first object in the list that satisfies the condition.
def find(listOfObjs, condition):
    for element in listOfObjs:
        if condition(element):
            return element
        
        