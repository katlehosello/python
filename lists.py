fruits = ["apple", "banana", "cherry"]

print(fruits[2])

fruits[1] = "blueberry"
 
print(fruits)  # This is to replace something on the list

#Using lists


fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)  #This is to add something to the list

fruits.insert(1, "orange")
print(fruits) #This is used to add a to a specific position

fruits.remove("kiwi")
print(fruits) #This is used to remove from the list, but only the one that appears first not all if there is more

fruits.sort()
print(fruits) #This arranges the list in assending order

fruits.sort(reverse=True)
print(fruits) #this arranges the list in decending order