#Loops

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(fruit)

numbers = [1,2,3,7,15]

for number in numbers:
    print(number)


#While loops

count = 5

while count <= 10:
    print(count)
    count +=1 # Increments the count by 1

#Loop control statements

fruits = ["apple", "banana","peach", "grape", "cherry", "date"]

for fruit in fruits:
    if fruit== "cherry":
        break #Exit the loop if cherry is found
    print(fruit)

print()
for fruit in fruits:
    if fruit== "peach":
        continue #Skip cherry and move to the iteration
    print(fruit)


count = 0

while count <5:
    print(count)
    count +=1
    if count == 3:
        break #Exit loop when the count is reached = 3
    