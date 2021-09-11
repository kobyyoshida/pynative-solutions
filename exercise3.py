#Exercise 3: Given a Python list of numbers. Turn every item of a list into its square

aList = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(aList)):
    aList[i] = aList[i]**2

print(aList)

'''aList = [1, 2, 3, 4, 5, 6, 7]
aList =  [x * x for x in aList]
print(aList)'''