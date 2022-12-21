# Objects are an encapsulation of vars and functions into one unholy creature. They get their values from classes. Classes are like the character creation screen but you create something not even God has the capacity to love.

class MyClass:
    variable = 'blah'

    def function(self):
        print("This is inside a class")

# to assign the class to an object you'd

myobjectx = MyClass()

# Access ObjVars
# To access the stuff inside of this demon creature, you'd
myobjectx.variable
# to print this
print(myobjectx.variable)

# You can make many objects with the same class
myobjecty = MyClass()

myobjecty.variable = "yackity"
# print those mfs
print(myobjecty.variable)

# Access ObjFuncs
myobjectx.function()
# Would print out the function inside the Class

#init()
# The __init__() function, is a special function that is called when the clss is being initiated. It assigns values in a class

class NumberHolder:

    def __init__(self, number):
        return self.number

var = NumberHolder(7)
print(var.returnNumber()) #prints 7