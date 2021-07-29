'''
Aggregate function exercise. 
'''

import random

def buildData(n, defectRate):
    '''
    Build a list of sample data in the range [0, 1).
    A certain percentage of the elements will be outside
    the range; these represent invalid data points.

    parameters
    ----------
        n - number of list elements
        defectRate - percent of elements that are invalid

    returns
    -------
        List of sample data with some invalid values. 
    '''
    values = []
    rand = random.random
    for i in range(n):
        if rand() <= defectRate:
            if rand() <= 0.5:
                values.append(-rand())
            else:
                values.append(1.0 + rand())
        else:
            values.append(rand())
    return values

# TODO: replace this with a function that operates on
# the aggregate instead of individual elements
def validateElement(element):
    '''
    Determine if a single data point is valid.

    parameter
    ---------
        element - number supposed to be in [0, 1)

    returns 
    -------
        True if element is valid, False if it is not
        in the specified range
    '''
    return element >= 0.0 and element < 1.0

# main program
n = 10_000_000
defectRate = 0.01

# build sample data
originals = buildData(n, defectRate)

# TODO: replace this with a call to your new function
# filter data
filteredData = [x for x in originals if validateElement(x)]