#Exercise 2: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

solution = []

for i in range(0,len(list1)):
    newWord = list1[i] + list2[i]
    solution.append(newWord)

print(solution)



#list1 = ["M", "na", "i", "Ke"] 
#list2 = ["y", "me", "s", "lly"]
#list3 = [i + j for i, j in zip(list1, list2)]
#print(list3)
