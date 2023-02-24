def sequential_search_itr(xs, y):
    '''
    Check whether y is contained in the list xs

    >>> sequential_search_itr([1, 3, 5, 4, 2, 0], 2)
    True
    >>> sequential_search_itr([1, 3, 5, 4, 2, 0], 6)
    False
    '''
    for x in xs:
        if x == y:
            return True
    return False


def binary_search(xs, y):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Return True if y is in the list xs.

    >>> binary_search([1, 3, 5, 7, 9, 11], 9)
    True
    >>> binary_search([1, 3, 5, 7, 9, 11], 8)
    False
    >>> binary_search(list(range(-1001, 1001, 2)), 9)
    True
    >>> binary_search(list(range(-1000, 1000, 2)), 9)
    False
    '''
    if len(xs) == 0:
        return False

    mid = len(xs) // 2
    if xs[mid] > y:
        return binary_search(xs[:mid], y)
    if xs[mid] < y:
        return binary_search(xs[mid+1:], y)
    if xs[mid] == y:
        return True


def trinary_search(xs, y):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Return True if y is in the list xs.

    >>> trinary_search([1, 3, 5, 7, 9, 11], 9)
    True
    >>> trinary_search([1, 3, 5, 7, 9, 11], 8)
    False
    >>> trinary_search(list(range(-1001, 1001, 2)), 9)
    True
    >>> trinary_search(list(range(-1000, 1000, 2)), 9)
    False
    '''
    if len(xs) == 0:
        return False
    if len(xs) == 1:
        return xs[0] == y

    mid1 = len(xs) // 3
    mid2 = 2 * len(xs) // 3
    if y == xs[mid1] or y == xs[mid2]:
        return True
    if y < xs[mid1]:
        return trinary_search(xs[:mid1], y)
    if xs[mid1] < y < xs[mid2]:
        return trinary_search(xs[mid1:mid2], y)
    if xs[mid2] < y:
        return trinary_search(xs[mid2:], y)
