'''
The map() function in Python applies a given function to each item of an iterable (such as a list, tuple, or string)
and returns an iterator of the results. The syntax for map() is as follows:
map(function, iterable)
btw variable named in german :D they may be incorrect, I don't know german for sure! at least yet ^^
'''
nummern = [5, 10, 15, 20]
verdoppelt_nummern = map(lambda x: x + 10, nummern)
print(list(verdoppelt_nummern))

# I asked myself if I could make this work with dict values, I mean why notttt?
nummern_dict = {
    "erster": 5,
    "zweite": 10,
    "dritte": 15,
}
verdoppelt_nummern_d_values = map(lambda x: x + 10, nummern_dict.values())
print(list(verdoppelt_nummern_d_values))

# different example
words = ["this", "time", "english"]
def to_uppercase(word):
    return word.upper()
uppercase_words = map(to_uppercase, words)
print(list(uppercase_words))  # Output: ['THIS', 'TIME', 'ENGLISH']
