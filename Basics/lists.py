myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[0]) #prints 1
print(myList[1]) #prints 2
print(myList[2]) #prints 3
# or
for x in myList:
    print(x)

#  _________________________________
# |_Will not Work___________|_|[]|X|
# | myListOne = [1,2,3]            |
# | print(myListOne[10])           |
# |                                |
# |________________________________|
# | Index Error: List Index out of |
# | range                          |
# |________________________________|