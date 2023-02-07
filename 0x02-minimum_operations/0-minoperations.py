#!/usr/bin/env python3
'''Interview Challenge module
'''


def minOperations(n):
    '''finds no of time opertion is performed
    '''
    var = 'H'
    count = 0
    dup = ''
    while len(var) < n:
        if n % len(var) != 0:
            var += dup
            count += 1
        else:
            dup = var
            var += dup
            count += 2
    return (count if len(var) == n else 0)
