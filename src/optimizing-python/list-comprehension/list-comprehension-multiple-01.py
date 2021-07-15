letters = ['a', 'b', 'c', 'd']
digits = [1, 2, 3]

values = []
for x in letters:
    for y in digits:
        values.append((x, y))

print(values)