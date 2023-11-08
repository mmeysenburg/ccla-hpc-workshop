'''
Code to filter all letters in the dictionary 
starting with 'Q', via list comprehension.
'''
from timeit import default_timer as timer

with open('dictionary.txt', 'r') as inFile:
    dict = [word[:-1] for word in inFile]

startTime = timer()
# make a sublist of only words that start with 'Q'
Qs = [word for word in dict if word[0] == 'Q']
stopTime = timer()

print(stopTime - startTime)
