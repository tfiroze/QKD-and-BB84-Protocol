import polarizer
import random_binary_generator

basis=polarizer.polar(8)
alicebin=random_binary_generator.bin_str(8)
alicephot=[0]*len(alicebin)

for i in range(0,8):
    if(alicebin[i]=='0' and basis[i]=='p'):
        alicephot[i]='v'
    elif(alicebin[i]=='0' and basis[i]=='x'):
        alicephot[i]='r'
    elif(alicebin[i]=='1' and basis[i]=='x'):
        alicephot[i]='l'
    elif(alicebin[i]=='1' and basis[i]=='p'):
        alicephot[i]='h'
    else:
        print('error')
print(alicebin)                  #binary key stream
print(basis)                     #random basis chosen by alice
print(alicephot)                 #photons sent by alice through polarizer to bob