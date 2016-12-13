#
#   @author      : SRvSaha
#   Filename     : lambda_map.py
#   Timestamp    : 01:45 14-December-2016 (Wednesday)
#

"""
This script describes the use of lambda statements inside map functions.

Requirements : Python 3
The map method takes in function_name and a sequence as parameter
and returns the iterator to the output list.
This is where we can use lambda statements instead of defining a new function.
The lambda statement can actually serve the need of function in map().
Note : map() returns an iterator in Python 3.x and not a list as in Python 2.
Since it returns iterator, we are doing like list(map((arg1, arg2))) to get the
output from map in a list format as in Python 2.
"""

'''
Suppose we want to find the squares of all the numbers in a list.
Tradition way for doing this is :
def sqr(x):
    """Return the square of a number."""
    return x * x
answer = []
to_be_squared = [1, 2, 3, 4, 5]
for item in to_be_squared:
    answer.append(sqr(item))
print(answer)

Using MAP without lambda it can be done as :
print(list(map(sqr, to_be_squared)))

But there's still overhead of writing the sqr function. So, a more pythonic
way of doing it is using lambda statements instead of sqr function which works
as function and get the job done is just ONE LINE.
'''
to_be_squared = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, to_be_squared)))

'''
x*x is the body of the lambda expression where x is the bound variable.
It takes argument one by one from the to_be_squared sequence and computes
the square of the item and store it in a list.
'''

'''
Lambda Functions come handy when we need to take compute a list of functions
on our sequence.
lambda statement takes the name of the function one-by-one from funcs and call
it using x(i) and result is stored in a list. This is a perfect mixture of
functions and lambda and give intuition how powerful lambda functions are.
'''
data = [1, 4, 2, 5, 7, 3, 9]


def sqr(x):
    """Return square of a number."""
    return x ** 2


def cube(x):
    """Return cube of a number."""
    return x ** 3

funcs = [sqr, cube]  # list of name of the functions

for i in range(5):
    print(list(map(lambda x: x(i), funcs)))
