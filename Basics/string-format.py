name = 'John'
age = 23
print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))

myList = [1,2,3]
print("A list: %s" % myList)

#  ____________________________________________________
# |_Basic Argument Modifiers___________________|_|[]|X|
# | $ touch BArgMods.txt                              |
# | $ nano BArgMods.txt                               |
# |___________________________________________________|
# | %s String (or any object that represents a string)|
# | %d Integer                                        |
# | %f Floating point                                 |
# | %.<number of digits>f Floating point with a fixed |
# | amount of digits right of the dot                 |
# | $x/%X Integers in hexadecimal representation      |
# |_(upper or lowercase)______________________________|
