import sys

'''
usage: python3 makeBat.py <start> <stop> <increment> <filename.py>
'''

begin = int(sys.argv[1])
end = int(sys.argv[2]) + 1
increment = int(sys.argv[3])
filename = sys.argv[4]

for n in range(begin, end, increment):
    print('python3 {0:s} {1:d}'.format(filename, n))