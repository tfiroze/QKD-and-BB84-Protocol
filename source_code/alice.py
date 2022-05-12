import polarizer
import random_binary_generator

basis=polarizer.polar(100)
alicebin=random_binary_generator.binfun(100)
alicephot=[0]*len(alicebin)
def basfun():
    for i in range(0,100):
        if(alicebin[i]==0 and basis[i]=='p'):
            alicephot[i]='v'
        elif(alicebin[i]==0 and basis[i]=='x'):
            alicephot[i]='r'
        elif(alicebin[i]==1 and basis[i]=='x'):
            alicephot[i]='l'
        elif(alicebin[i]==1 and basis[i]=='p'):
            alicephot[i]='h'
        else:
            print('error')
    return alicephot
#print("\nThis is the stream of binary data\n",alicebin)
#print("\nThese are the basis used by alice\n",basis)
#print("\nThis is the stream of photons sent by alice\n",basfun())