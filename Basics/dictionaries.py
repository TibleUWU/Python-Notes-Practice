# Dictionaries work similar to arrays, but instead of indexes, it works with keys and values
# Each value in a dictionary is accessed and assigned by keys, which can be any object (strings, numbers, lists, etc)

phonebook = {
    "The Hookup" : 6054756959,
    "Santa" : 16034134124,
    "Epic" : 18884475594
}
print(phonebook)

#  ______________________________________________________
# |_So_apparently_you_can_do_it_like_this?_______|-|[]|X|
# |                                                     |
# | phonebook = {}                                      |
# | phonebook["Name"] = bunchanumbers                   |
# | phonebook["More"] = 111111111                       |
# | print(phonebook)                                    |
# |_____________________________________________________|
# | But VSCode (with Python 3.10.6 64bit) complained    |
# |_ALOT!_______________________________________________|

# Dictionary Iteration.
# Similar to iterating over a list, but instead of iterating over the order of the values in the list, we can iterate over key, value pairs

dictionary = {"Perhaps" : 12, "Eat Eggs" : 27}
for name, number, in dictionary.items():
    print("Value of %s is %d" % (name, number))

# You can remove values with 'del'

addressBook = {
    'Home':123,
    'Home2':456
}
print(addressBook)
del addressBook["Home2"]
print(addressBook)
# or
# addressBook.pop["Home2"]
