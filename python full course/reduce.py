import functools

letters = ["G","O","A"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)