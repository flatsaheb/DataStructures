'''
Decorators can be defined in one file and can be re-used in another program
'''
from MainDecorator import dfHelloWorld

@dfHelloWorld
def say_helloworld():
    print ('Re-use Hello World of Decorators')

say_helloworld()