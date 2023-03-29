'''enumerate is a built-in function in Python that allows you to iterate over a sequence (e.g. a list, tuple, or string) 
while keeping track of the index of each item in the sequence.'''
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n")

# you can add second argument to change starting index

fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits, 5):
    print(index, fruit)