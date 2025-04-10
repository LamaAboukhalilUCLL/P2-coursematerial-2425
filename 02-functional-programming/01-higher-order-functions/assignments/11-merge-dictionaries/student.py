def merge_dictionaries(d1, d2, merge_function):
    """
    Merges two dictionaries according to the provided merge function.
    
    Args:
        d1: First dictionary
        d2: Second dictionary
        merge_function: Function that takes two values and returns a combined result
        
    Returns:
        A new dictionary with all keys from both dictionaries and merged values
    """
    result = {}
    
    # Copy all keys from d1
    for key, value in d1.items():
        result[key] = value
    
    # Process keys from d2
    for key, value in d2.items():
        if key in result:
            # Key exists in both dictionaries, apply merge function
            result[key] = merge_function(result[key], value)
        else:
            # Key only in d2, just copy it
            result[key] = value
    
    return result


