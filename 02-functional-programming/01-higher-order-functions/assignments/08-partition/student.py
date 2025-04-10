#can take a list of any kind of object, together with a function that for each object determines whether it should be in the first or second list.
def partition(lst, condition):
    first_list=[]
    second_list=[]
    for element in lst:
        if condition(element):
            first_list.append(element)
        else:
            second_list.append(element)
    return (first_list, second_list)

def children_and_adults(people):
    children, adults= partition(people, SmallAge)
    return (children, adults)

def SmallAge(person):
    return person.age<18
      
 










