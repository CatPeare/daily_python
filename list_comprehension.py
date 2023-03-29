# find the even numbers inside a list
# instead of using this tedious way
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_but_tedious = []
for num in numbers:
    if num % 2 == 0:
        even_numbers_but_tedious.append(num)
print(even_numbers_but_tedious)


# you can use list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)