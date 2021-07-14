'''
Code to filter all letters in the dictionary 
starting with 'Q', via loops.
'''
from timeit import default_timer as timer

with open('dictionary.txt', 'r') as inFile:
    dict = [word[:-1] for word in inFile]

startTime = timer()
Qs = []
# make a sublist of only words that start with 'Q'
for word in dict:
    if word[:1] == 'Q':
        Qs.append(word)
stopTime = timer()

print(stopTime - startTime)