import random

def roll_dice(n, d):
    if n < 1: raise ValueError('Attempting to throw 0 or less dice')
    if d < 1: raise ValueError('Attempting to throw dice with 0 or less faces')
    return [ random.randint(1, d) for i in range(n) ]
