'''
A generator function in Python is a special type of function
that generates a sequence of values, one at a time, using the yield statement instead of return.
When a generator function is called, it returns an iterator object,
which can be used to iterate over the values produced by the generator.
'''
def squares(n):
    for i in range(1, n+1):
        yield i**2

for sq in squares(3):
    print(sq)


print("###############################")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))

'''
Fibonacci numbers are a sequence of numbers in which each number is the sum of the two preceding numbers, starting from 0 and 1.
The sequence is named after Leonardo Fibonacci, an Italian mathematician who introduced it to the Western world in his book "Liber Abaci", published in 1202.

The first few numbers in the Fibonacci sequence are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

To obtain the next number in the sequence, you simply add the two previous numbers. For example, 2 + 3 = 5, 3 + 5 = 8, and so on.

Fibonacci numbers have many interesting mathematical properties and appear in various areas of science, such as biology, physics, and finance.
For instance, they describe the growth of rabbit populations, the branching of trees, and the structure of spiral galaxies.

In programming, Fibonacci numbers are often used as a simple example to demonstrate various concepts, such as recursion, iteration, and dynamic programming.
They can also be generated efficiently using loops or generators in Python, as shown in my previous answer.'''