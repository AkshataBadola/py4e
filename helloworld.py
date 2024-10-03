#variables
print ("Hello, world!")
n = 43
print(n)

#functions
def HelloWorld():
    print("Hello,                                    world!")

HelloWorld()

def HelloName(name):
    return 'Hello, {}!'.format(name)  # string formatting
print(HelloName('Akshata')) 


#objects
def twice(x,y):
    """ apply f twice"""
    return f(f(x))

#scope
#1. global
a = 2
b= 3
c= a-b
print(c)

def add(a,b):
    x = a+b  #All these are local variables for the function add
    return x

c = add(4,6)
print(c)

#nested functions
def greeting(first, last):
    def FullName():
        return first + " "+last
    print("Hi "+ FullName())

greeting('Akshata', 'Badola')


def mult(a,b):
    def add():
        return a*b
    print(add())

mult(2,3)


#closure
def mult(a):
    def add(b):
        return a*b
    return add

print(mult(2)(3))

#lambda i.e anonymous functions
y = lambda a, b : a*b
print(y(2,5))