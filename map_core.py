#
#   @author      : SRvSaha
#   Filename     : map_core.py
#   Timestamp    : 02:37 14-December-2016 (Wednesday)
#

"""
This script is for understanding how map() function works at it's core.

NOTE : Though map() doesn't return the list in Python 3.x but the iterator
to the list, here for understanding the core, we assume it returns list
as in Python 2.x
"""

'''
Suppose this is the original map(). We want to write core implementation of it.
def sqr(x):
    return x*x
print(list(map(sqr,to_be_squared)))
'''


def sqr(x):
    """Return the square of the number."""
    return x**2

to_be_squared = [1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = []
for item in to_be_squared:
    result = sqr(item)
    answer.append(result)
print(answer)

'''
This is the core implementation of the map function using loops.
So, basically map functions takes one item from the iterable
sequence and then calls the function with that item as argument.
The returned result is stored in a list (result list).
After all items are done the same process, map function returns the
result list (in Python 2.x) and returns the iterator to the list(in Python 3.x)
So, this is what goes on behind the scene when we use map().
A lot of function calls are involved so generally list comprehension is
preferred over map. But it's optimized to use with inbuilt functions,
so may come handy at that time. Also, code becomes really small
due to functional language paradigm.
'''
