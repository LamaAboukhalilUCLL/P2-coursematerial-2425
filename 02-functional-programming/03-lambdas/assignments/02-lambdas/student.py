
#to visualise:
#'''
def group_by(xs, key_function):
    result = {}
    for x in xs:
        key = key_function(x)
        if key not in result:
            result[key] = []
        result[key].append(x)
    return result
#'''
#the key_function is a getter method of suit value, hence we will use lambda for it since its simple instead of using a nested fct.
#key_function here is def anonymous(card): return card.suit
def group_by_suit(cards):
    return group_by(cards,lambda card: card.suit)

#key_function here is def anonymous(card): return card.value
def group_by_value(cards):
    return group_by(cards,lambda card: card.value)
#-------------------------------------------------------------
#'''
def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)
#'''
#condition(xs) is the lambda, first list is black cards, which suit is spades and clubs
#anynymous(cards): return ["spades", "clubs"].contains(card.suit)
def partition_by_color(cards):
    return partition(cards, lambda card: card.suit in ['clubs', 'spades'] )





    