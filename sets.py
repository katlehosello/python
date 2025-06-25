#Sets
'''
my_set ={1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
''' #these 3 dots cancels out the info, remeber to open and close

set1 = {1, 2, 3}

set2 = {3, 4, 5}

#union
union_set = set1.union(set2)
print(union_set) #This joins 2 sets and removes the duplicates

#Intersection
inter_set = set1.intersection(set2)
print(inter_set)

#Difference
diff_set = set1.difference(set2)
print(diff_set)
