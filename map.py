#
#   @author      : SRvSaha
#   Filename     : map.py
#   Timestamp    : 20:03 13-December-2016 (Tuesday)
#


"""
This script is to use the inbuilt map() in Python 3.x.

Requirement : Python3

Note : map() returns an iterator in Python 3.x and not a list as in Python 2.
"""

items = [1, 2, 3, 4, 5, 6]


def sqr(x):
    """The method returns the square of any number that is passed as input."""
    return x**2

'''
The map method takes in function_name and a sequence as parameter
and returns the iterator to the output list.
It works like -> One by one an item is fetched from the sequence and
passed to the function. The result is then stored in a list. This process
goes on until the iterator to the sequence reaches the last element.
'''

print(map(sqr, items))

'''
Using loop we can print all elements in the list which is formed by map.
Though map() doesn't return a list, the iterator to the list is return
which helps in getting all the elements in the list it's pointing.
'''

for item in map(sqr, items):
    print(item)

'''
This is a more pythonic way of working with map.
'''
print(list(map(sqr, items)))
