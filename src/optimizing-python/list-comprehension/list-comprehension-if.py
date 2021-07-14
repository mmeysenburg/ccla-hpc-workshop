with open('dictionary.txt', 'r') as inFile:
    dict = [word[:-1] for word in inFile]

# make a sublist of only words that start with 'Q'
Qs = [word for word in dict if word[:1] == 'Q']

print(Qs)