#
def indices_of(xs, condition):
    """
    Returns the indices of all elements in xs that satisfy the condition.
    
    Args:
        xs: A list of elements
        condition: A function that takes an element and returns a boolean
        
    Returns:
        A list of indices where the condition is True
    """
    indices = []
    for index, element in enumerate(xs):
        if condition(element):
            indices.append(index)
    return indices

def is_palindrome(string):
    """
    Determines whether a given string is a palindrome 
    (reads the same forwards and backwards).
    
    Args:
        string: The string to check
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    return string == string[::-1]

