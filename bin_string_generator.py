import random


def bin_str(n):
    bin = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        bin += temp
    return bin
#   example
#   n=8
#   out = bin_str(n)
#   print(out)
