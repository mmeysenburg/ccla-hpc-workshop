'''
calculate speedup for the function aggregate examples.
'''

orig = []
with open('fa01.txt', 'r') as inFile:
    for line in inFile:
        tokens = line.split(',')
        orig.append((int(tokens[0]), float(tokens[1])))

spedup = []
with open('fa02.txt', 'r') as inFile:
    for line in inFile:
        tokens = line.split(',')
        spedup.append((int(tokens[0]), float(tokens[1])))

for o, s in zip(orig[1:], spedup[1:]):
    speedup = o[1] / s[1]
    print('{0:d},{1:f}'.format(o[0],speedup))
