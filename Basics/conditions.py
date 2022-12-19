x = 2
print(x == 2) # True
print(x == 3) # False
print(x < 3) # True

# = assigns value 
# == compares values positively "equal"
# != compares values negatively "not equal"

name = 'John'
age = 23

if name == 'John' and age == 23:
    print("Your name is %s, and you're %d years old." % (name, age))
if name == 'John' or name == 'Rick':
    print("Your name is either %s, or Rick" % name)

if name in ['John', 'Rick']:
    print("Your name is either %s, or Rick" % name)

statement = False
anotherStatement = True

if statement is True:
    # code
    pass
elif anotherStatement is True: # else if
    # more code
    pass
else:
    # even more code
    pass

if x == 2:
    print("x equals two")
else:
    print("x does not equal two")

a = [1,2,3]
b = [1,2,3]
print(a == b) # Print True
print(a is b) # Print False

print(not False) # Print True
print((not False) == (False)) # Print False