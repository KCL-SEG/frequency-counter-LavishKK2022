def count(items, searchTerm):
    iterator = 0

    for item in items:
        if item == searchTerm:
            iterator = iterator + 1
    
    return iterator
        

def frequencies(items):

    strlist = [str(item) for item in items]
    keyset = set(strlist)

    frequencies = {}

    for key in keyset:
        frequencies[key] = count(strlist, key)

    return frequencies
