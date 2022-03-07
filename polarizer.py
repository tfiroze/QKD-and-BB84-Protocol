#function to make random polarizers 
import random
def polar(temp):
    #two possible polarizers + or x defined as p and x respectively
    mylist = ['p', 'x']
    return random.choices(mylist, weights = [1, 1], k = temp)

