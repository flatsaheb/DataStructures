'''
Decorator function with return value
'''

import functools

def dfMath(func):
    functools.wraps(func)
    def wInnerAdd(*args, **kwargs):
        print ('Output of two numbers {} and {}'.format(*args, **kwargs))
        return func(*args, **kwargs)
    return wInnerAdd

@dfMath
def df_AddTwoNumber(num1, num2):
    print ("Addition of two number {} and {}".format(num1, num2))
    num3 = num1+num2
    return num3
print('Addtion of two number is {}'.format(df_AddTwoNumber(4,5)))

# Below is the advantage of decorators. I have created new multiplication function and can easily re-use
# it for multiplication. If decorators had not been in place I have to type Output of two numbers {} and {}
# again for multiplication numbers
@dfMath
def df_Multiply(num1, num2):
    num3 = num1*num2
    return num3
print ('Multiplication of two numbers is {}'.format(df_Multiply(3,4)))