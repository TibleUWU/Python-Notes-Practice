# Python uses blocks for stuff

# blockHead:
#     code line 1
#     code line 2
#     ...

#functions are declared by 'def'
def myFunc():
    print("bogos binted")

#functions can also recieve arguments, be them variables or built in functions
def funcWithArgs(username, greeting):
    print("Hello, %s. This is printed from a function. Have a great %s!" % (username, greeting))

#functions can also return values inside the function
def sumTwoNumbers(a, b):
    return a + b

#function call
myFunc()

funcWithArgs('John Doe', 'a great year')

x = sumTwoNumbers(1,2)
print(x)