# Using example in the textbook to see how it works
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1   
# Using a for loop to do the same thing
fruit = 'banana'
for letter in fruit:
    print(letter)
# Using a for loop with the range function to get the index
fruit = 'banana'
for index in range(len(fruit)):     
    letter = fruit[index]
    print(index, letter)
# Using the break statement to exit a loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    if letter == 'a':
        break
    print(index, letter)
    index = index + 1                   