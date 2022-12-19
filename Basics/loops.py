# For Loops

primes = [2,3,5,7]
for prime in primes:
    print(prime)

# For Loop
# Loops over a sequence of numbers in a range.

for x in range(5):
    print(x) # print 0 to 5
# Python counts from 0 so it goes 0,1,2,3,4,5

for y in range(3, 6):
    print(y) # print 3 to 5
# Loops through a confined range, this case - 3,4,5

for z in range(3,8,2):
    print(z) # print 3, 5, 7
# [Start:Stop:Step] like in Basic String Ops 'basic-stringops.py'

# While Loops

count = 0
while count < 5: # while count is less than 5
    print(count) # print count value
    count += 1 # then add 1 to the value to count
# Loop will loop until count equals 5.

# Break & Continue

countNew = 0
while True:
    print(countNew)
    countNew += 1
    if countNew >= 5:
        break
# while True, continue to print the value of countNew. Once printed, move to next line. Add 1 to countNew. If countNew is greater than or equal to 5, break out of the loop. Repeat until conditions fulfilled

#Odd Number printer go brr
for a in range(10):
    if a % 2 == 0:
        continue
    print(a)
# Doing constant mod division on a (1-10), if the value of a is divisable by 2 and has a remainder of 0, it continues/skips to the next number that does not have a remainder of 0

# Using Else

countCount = 0
while(countCount<5):
    print(countCount)
    countCount += 1
else:
    print("count value is %d" %(countCount))
# Counts from 0 to 4, then prints "count value is 5" once it reaches 5

