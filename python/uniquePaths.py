import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def uniquePaths(m, n):
    """
    Let's build a table, where each cell in the table represents the number of ways to get to 
    that point. Instead of starting from our last cell, we build from the foundation up. This way
    we can cache results we already calculated. The recurrence relation remains the same. Namely 
    
    table[i][j] = table[i - 1][j] + table[i][j - 1]
    
    Keep in mind the base cases: The first row and first column only have 1 way, since we have no 
    choice but to walk straight from (0, 0) in either direction.
    
    An even more optimized solution would only keep 2 rows, since a whole table is not necessary to 
    find the # of rows for the last cell. 
    :type m: int
    :type n: int
    :rtype: int
    """
    
    ### Check for valid arguments here ###
    if m <= 0 or n <= 0: return 0 
    
    table = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n): 
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[-1][-1]     

    # table = [[1 for _ in range(n)] for _ in range(2)]
    # for i in range(1, m): 
    #     for j in range(1, n): 
    #         table[1][j] = table[0][j] + table[1][j - 1]
    #     table[0], table[1] = table[1], table[0]
    # return table[0][-1]

def recursiveUniquePaths(m, n): 
    """
    A top-down solution would go something like this: 
    How many ways do we have to get to our last cell (m, n)? Sum of
        -> number of ways we got to cell (m - 1, n)
            -> number of ways we got to cell (m - 2, n)
            -> number of ways we got to cell (m - 1, n - 1)
        -> number of ways we got to cell (m, n - 1)
            ... 
    
    We can recognize that the number of ways to get to anywhere on the leftmost column
    and topmost row is 1, since all we can do is move horizontally. Therefore, our 
    base cases are m == 0 and n == 0 
    """
    if m == 1 or n == 1: 
        return 1
    sum = recursiveUniquePaths(m - 1, n) + recursiveUniquePaths(m, n - 1)
    return sum

wrapped = wrapper(recursiveUniquePaths, 11, 11)
print(timeit.timeit(wrapped, number=10))
print(recursiveUniquePaths(3, 3))

wrapped = wrapper(uniquePaths, 11, 11)
print(timeit.timeit(wrapped, number=10))
print(uniquePaths(3, 3))