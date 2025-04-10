def group_by(xs, key_function):
    result={} #empty dict, the result is asked to be a dict
    #key_function gives us the key that we want to group by
    for element in xs:
        #getting key for each object in xs
        key_of_element= key_function(element) #ie if the element is Card(value=2, suit='hearts') and we want to group by suit, card_suit(of this obj) will return obj.suit so it will give us the key
        if key_of_element not in result:
            result[key_of_element]=[] #to add elements of same key in it
        result[key_of_element].append(element) #adding each element to its corresponding existing key(updatiing)
    return result


        
