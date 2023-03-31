import re # import built-in regular expression module to use regular expressions in Python

'''
Special Characters: Regular expressions also have special characters that allow you to match more complex patterns. 
Here are a few common special characters:
. (dot): Matches any character except for a newline character
* (asterisk): Matches zero or more occurrences of the preceding character or group
+ (plus): Matches one or more occurrences of the preceding character or group
? (question mark): Matches zero or one occurrence of the preceding character or group
[] (brackets): Matches any character inside the brackets
^ (caret): Matches the beginning of a string
$ (dollar sign): Matches the end of a string
'''
text = "I want to say hello world, but which world is this; I should stop speaking out loud."
text_2 = "Hello my friend, if you are my friend of course!"
# example 1
pattern = "hello"
result = re.search(pattern, text) # the 'search' method will search for the pattern "hello" in the 'text' string.
print(result)

# example 2
pattern = "h.*r"
result = re.search(pattern, text)
print(result)

# example 2
pattern = "^hello"
result = re.search(pattern, text)
print(result) # returns None because text doesn't start with "hello"

result = re.search(pattern, text_2)
print(result) # returns None because text_2 starts with upper case, the caret is case-sensitive by default!

result = re.search(pattern, text_2, re.IGNORECASE) # using re.IGNORECASE parameter we changed its behaviour
print(result) # this should print something rather than None :)
