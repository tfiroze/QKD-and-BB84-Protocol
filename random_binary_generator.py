#function to make random polarizers 
import random
def polar(temp):
    #two possible polarizers + or x defined as p and x respectively
    mylist = [0, 1]
    return random.choices(mylist, weights = [1, 1], k = temp)
#   example
#   n=8
#   out = bin_str(n)
#   print(out)
