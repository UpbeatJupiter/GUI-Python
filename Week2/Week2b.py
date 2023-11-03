#List

list1 = ["A", "B", "C", "D"]
print(list1) #list[1] = B
print(f"list1 has {len(list1)} items.")

list2 = ["Red", 17, False, "Python"]
print(list2[0:2]) #['Red', 17] starts from index 0 to 2 (2 is not included)
print(list2[-1]) #['Python'] will be the output

list2[3] = 6
print(list2) #python variable will be changed to 6

list2.append("Apple")
list2.insert(3,True)
list2.remove("Red")

#for loop to return every element
for i in list2:
    print(i)

if 20 in list2:
    print("Found")
else:
    print("Not Found")


list3 = list2.copy()
print(list3)