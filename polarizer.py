#function to make random polarizers 
import random
def polarizer(temp):
    #two possible polarizers + or x defined as p and x respectively
    mylist = ['p', 'x']
    print(random.choices(mylist, weights = [1, 1], k = temp))

