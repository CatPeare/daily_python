'''
The iter() function returns an iterator object for the given sequence. 
An iterator is an object that can be iterated (looped) upon, 
meaning that you can get the next value from the sequence using the next() function.
'''
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)  # Create an iterator object
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3

'''
In the example above, we created an iterator object called my_iter using the iter() function 
and then used the next() function to get the first three values from the list
The next() function returns the next item from the iterator. 
If there are no more items, it raises a StopIteration exception.

Note that you can also use a for loop to iterate over an iterator.
The for loop automatically calls iter() on the sequence and creates an iterator for you.
'''
for item in my_list:
    print(item)

