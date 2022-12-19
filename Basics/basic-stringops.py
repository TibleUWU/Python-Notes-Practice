aString = "Hello world!"
bString = 'Hello world!' # Can use either single or double quotes when declaring the value of string variables

print("Single quotes are ' '")
print(len(aString)) # len is length. "Hello World" is 12 chars long, so it prints 12

print(bString.index("o")) # Will print 4 because the letter o rests in index 4 (counting from 0)

print(aString.count("l")) # Will print 3

print(bString[3:7]) # Printing the characters from index 3 to 6. "lo w"

print(aString[3:7:2]) # Prints index 3 to 6, skipping one. [start:stop:step] Will print "l"
print(bString[3:7:1]) # Prints the same as [3:7]

print(aString[::-1]) # Reverses aString

print(bString.upper()) # Makes bString Uppercase
print(aString.lower()) # Makes aString Lowercase

print(bString.startswith("Hello")) # Boolean Value. Prints "True"
print(aString.endswith("asdfasdfasdf")) # Boolean Value. Prints "False"

aFewWords = bString.split(" ")
# Splits the string at " " and divides the items up into a list.

