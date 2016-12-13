#
#   @author      : SRvSaha
#   Filename     : lambda.py
#   Timestamp    : 20:44 13-December-2016 (Tuesday)
#

"""
This script is to explore the inbuilt lambda expressions.

Small functions are to used the lambda statement instead of def func everytime.
lambda takes a number of parameters and an expression combining these parameter
and creates an anonymous function that returns the value of the expression.

NOTE : lambda expressions has limitations so are not widely used.
TROLL :
Fredrik Lundh once suggested the following set of rules for refactoring
uses of lambda:

    Write a lambda function.
    Write a comment explaining what the heck that lambda does.
    Study the comment for a while, and think of a name that captures the
    essence of the comment.
    Convert the lambda to a def statement, using that name.
    Remove the comment.

I really like these rules, but you’re free to disagree about whether this
lambda-free style is better.

"""

'''
The lambda expression takes two parameters and then returns the value
obtained by doing x raised to the power y.
my_lambda works as the name for the lambda expression.
This is similar to doing this ->
def my_lambda(x,y):
    return x ** y
'''
my_lambda = lambda x, y: x ** y

'''
This is similar to calling the function my_labda with 4,5 as parameters.
'''
print(my_lambda(4, 5))

'''
This is pythonic way of doing the same thing. One Liner.
The body of the lambda expression is x*2 so x is the bound variable here.
The parameter that is passed to the expression or technically argument in
lambda calculus terms, it replace all x with the arg and returns the result
after computing.
'''
print((lambda x: x * 2)(10))
