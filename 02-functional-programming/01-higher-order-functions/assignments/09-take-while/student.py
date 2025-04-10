#
def take_while(xs, condition):
    index=0
    for element in xs:
        if not condition(element):
            return (xs[:index], xs[index:])
        index+=1
    return xs, [] #if all of them satsify the condition
        




