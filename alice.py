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
#print(alicebin)                  #binary key stream
#print(len(alicebin))
#print(basis)                     #random basis chosen by alice
#print(len(basis))
#basfun()
#print(alicephot)                 #photons sent by alice through polarizer to bob
#print(len(alicephot))                 #photons sent by alice through polarizer to bob