#
#   @author      : SRvSaha
#   Filename     : list_comprehension.py
#   Timestamp    : 23:47 13-December-2016 (Tuesday)
#

"""
This script depicts how list comprehensions can make like easier.

List Comprehensions are one liner pythonic way over traditional looping.
A list comprehension consists of the following parts:

    -An Input Sequence.
    -A Variable representing members of the input sequence.
    -An Optional Predicate expression.
    -An Output Expression producing elements of the output list from members of
     the Input Sequence that satisfy the predicate.
NOTE : All the list comprehension works like the traditional code in comments.
"""

'''
Suppose we have to find out a list of all the integers in a sequence
and then square each of them.
_list_ = ['a',1,'2',0.2,4,9,0,'Z']
A traditional way of doing this would be :
answer = []
for item in _list_:
    if type(item) == int:
        answer.append(item**2)
print(answer)

But, the magic of python is list compression can do it in 1 line.
'''
_list_ = ['a', 1, '2', 0.2, 4, 9, 0, 'Z']

print([item**2 for item in _list_ if type(item) == int])

'''

    -The iterator part iterates through each member item of the
     input sequence _list_. (for item in _list_)
    -The predicate (if type(item) == int) checks if the member is an integer.
    -If the member is an integer then it is passed to the output expression,
     squared, to become a member of the output list. (item**2)

Terminology :
    output expression : item**2
    input sequence with iterable : for item in _list_
    optional predicate : if type(item) == int
'''

'''
Suppose we have 2 lists and from where we need to take only those tuples whose
sum is even and return a list of such tuples.
Traditional way of doing it :
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 0]
answer = []
for i in list1:
    for j in list2:
        if (i+j) % 2 == 0 :
            answer.append((i,j))
print(answer)

BUT again, list comprehensions can do it a single line :)
This is called Nested Comprehension.
'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 0]

print([(i, j) for i in list1 for j in list2 if (i + j) % 2 == 0])

'''
Suppose when we need the output part dependent on some condition like so
if the condition is true it prints something otherwise print some other thing,
at that time, the predicate constructs can(must) be applied before iterable.

Suppose for the above lists, we need the tuple for which sum is even, else we
need (0,0) to be returned, so traditional way of doing it is :
answer=[]
for i in list1:
    for j in list2:
        if (i + j) % 2 == 0:
            answer.append((i, j))
        else:
            answer.append((0, 0))
print(answer)

Yet, list comprehension come handy here : Pythonic Way
'''

print([(i, j) if (i + j) % 2 == 0 else (0, 0) for i in list1 for j in list2])

'''
Crux of Nested List Comprehesion : The initial expression in a list
comprehension can be any arbitrary expression, including another
list comprehension.
'''

'''
Suppose we need to do transpose of a given matrix :
matrix = [
            [1,2,3,4]
            [5,6,7,8]
            [9,10,11,12]
        ]
Tradition Way :
transpose = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transpose.append(transposed_row)
print(transpose)

List comprehension can again do the magic in one line :
'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])

'''
Suppose we want to square all values in a list :
List comprehension can come to aid.
'''

to_be_squared = [1, 2, 3, 4, 5, 6, 7]
print([x**2 for x in to_be_squared])
