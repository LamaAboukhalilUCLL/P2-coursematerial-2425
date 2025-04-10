#

'''
def count_older_than(people, min_age):
    result= set()
    count=0
    for person in people: #for element in collection
        if not person.age>min_age: #if not condition(element)
            count+=1
        else:
            result.add(count)
            count+=1
    return len(result) 
'''
'''
def indices_of_cards_with_suit(cards, suit):
    result= set()
    index_count=0
    for card in cards: #for element in collection
        if not card.suit==suit: #if not condition(element)
            index_count+=1
        else:
            result.add(index_count)
            index_count+=1
    return result
'''

#-------------------my code, is correct but not for the test---------
'''
def count(collection, condition):
    result=[]
    count=0
    for element in collection:
        if condition(element):
            result.append(count)
        count+=1
    return result

def count_older_than(people, min_age):
    def is_min_age(person):
        return person.age>=min_age
    return len(count(people, is_min_age))

def indices_of_cards_with_suit(cards, suit):
    def is_suit(card):
        return card.suit== suit
    return count(cards, is_suit)
'''

#---------------code matching the requirements of the test class, use 2 fcts insteadof 1 general--
def count(collection, condition):
    count = 0
    for element in collection:
        if condition(element):
            count += 1
    return count

def indices_of(collection, condition):
    result = []
    index = 0
    for element in collection:
        if condition(element):
            result.append(index)
        index += 1
    return result

def count_older_than(people, min_age):
    def is_min_age(person):
        return person.age >= min_age  # Note: >= not >
    return count(people, is_min_age)

def indices_of_cards_with_suit(cards, suit):
    def is_suit(card):
        return card.suit == suit
    return indices_of(cards, is_suit)

            






