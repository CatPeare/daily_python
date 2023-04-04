# itertools is a Python module that provides a collection of functions for working with iterable objects
# more example https://docs.python.org/3/library/itertools.html
import itertools

# The chain() function takes several iterable objects as arguments and returns a single iterable object that concatenates them all together.
list1_chain = [3, 5, 7, 8]
list2_chain = [12, 14, 16, 19]
list_chain_empty = [item for item in itertools.chain(list1_chain, list2_chain)] # list comprehension
print(list_chain_empty)

string_example = [i for i in itertools.chain("abc", "def")]
print(string_example)

# Use itertools.product() to generate Cartesian product of multiple lists in Python.
# here I wanted to create every combination of 2 lists as str into a list.
list1_pro = [1, 2, 3]
list2_pro = ['a', 'b', 'c']
paired_list = []
for pair in itertools.product(list1_pro, list2_pro):
    paired_list.append(str(pair[0])+ str(pair[1]))

print(paired_list)

