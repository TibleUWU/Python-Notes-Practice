x = object()
y = object()

#change this code
xList = [x] * 10
yList = [y] * 10
bigList = xList + yList

print("xList contains %d objects" % len(xList))
print("yList contains %d objects" % len(yList))
print("bigList contains %d objects" % len(bigList))

#testing code
if xList.count(x) == 10 and yList.count(y) == 10:
    print("Almost there...")
if bigList.count(x) == 10 and bigList.count(y) == 10:
    print("Great!")