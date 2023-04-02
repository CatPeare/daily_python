# Lambda functions are useful when you need (or want :P) to define a function quickly
# lambda arguments: expression

add = lambda x, y: x + y # this code creates a lambda function that takes two arguments x and y, and returns their sum (:
print (add(2,6)) # outputs 8

another_example = lambda a, q: a ** q
print(another_example(3, 3))

another_example_2 = lambda f: f * 5 # this code takes one arguments and multiply it with 5
print(another_example_2(6))

# you can check the map().py file for info related to map() function, then you may understand code below! :)
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]
