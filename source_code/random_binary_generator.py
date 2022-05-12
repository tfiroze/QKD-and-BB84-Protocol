#function to make random polarizers 
import random
def binfun(temp):
    mylist = [0, 1]
    return random.choices(mylist, weights = [1, 2], k = temp)
