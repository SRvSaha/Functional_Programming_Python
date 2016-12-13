#
#   @author      : SRvSaha
#   Filename     : map_wrapper.py
#   Timestamp    : 02:48 14-December-2016 (Wednesday)
#

"""
This is a wrapper of map() in Python 3.x.

It's created so that the map() works like it used to do in Python 2.x.
Basically, with this wrapper, the map() function returns list instead
of iterator to the list.
"""


def sqr(x):
    """Return the square of the number passed as argument."""
    return x**2


def map_wrapper(function, sequence):
    """Wrapper over map in Python 3.x to return list as result."""
    result = []
    for item in sequence:
        result.append(function(item))
    return result

if __name__ == '__main__':
    # Using our own wrapper of map()
    print(map_wrapper(sqr, [1, 2, 3]))
    # Using the original map() in Python 3.x + list()
    print(list(map(sqr, [1, 2, 3])))
