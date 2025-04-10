#sort by increasing age
def sort_by_age(people):
    people.sort(key= lambda person: person.age)
    return people

#sort by decreasing age
def sort_by_decreasing_age(people):
    people.sort(key=lambda person: person.age, reverse=True)
    return people
#or we can do people.sort(key=lambda person: -person.age)

#sort by name
def sort_by_name(people):
    people.sort(key= lambda person: person.name)
    return people

#by name then age- tuple use
def sort_by_name_then_age(people):
    people.sort(key= lambda person: (person.name, person.age))
    return people

#by name then decreasing age- tuple use
def sort_by_name_then_decreasing_age(people):
    people.sort(key= lambda person: (person.name, -person.age ))
    return people
