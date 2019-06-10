import random

''' Figure out the overlap in two lists using the random.sample 
method to generate the initial two list of different lengths. '''

''' createList function used to create random list of different lenghts '''
def createList():
    newList = random.sample(range(1,200), random.randint(7,20))
    return newList

# Function to compare the two list and put elements in common in a
# third list
def listCompare(first, second, empty):
    pass

# Program Flow
'''
Create List one (random length)
Create list two (random lenght)
Init empty list
Compare lists "Method" overLapList = listCompare(fist, second, empty)
Print overlap list
'''

