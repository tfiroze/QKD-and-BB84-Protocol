import polarizer
import random
import alice

alicephot = alice.basfun()
evebasis = polarizer.polar(100)

evepol = [0]*len(alicephot)
evebin=[0]*len(alicephot)

def eveint():
    for i in range(0,100):
        if(evebasis[i]=='p' and alicephot[i]=='v'):
            evepol[i]='v'
        elif(evebasis[i]=='p' and alicephot[i]=='h'):
            evepol[i]='h'
        elif(evebasis[i]=='p' and alicephot[i]=='r'):
            evepol[i]=random.choice(['h','v'])
        elif(evebasis[i]=='p' and alicephot[i]=='l'):
            evepol[i]=random.choice(['h','v'])
        elif(evebasis[i]=='x' and alicephot[i]=='h'):
            evepol[i]=random.choice(['r','l'])
        elif(evebasis[i]=='x' and alicephot[i]=='v'):
            evepol[i]=random.choice(['r','l'])
        elif(evebasis[i]=='x' and alicephot[i]=='r'):
            evepol[i]='r'
        elif(evebasis[i]=='x' and alicephot[i]=='l'):
            evepol[i]='l'
        else:
            print("Error in transmission")
    return evepol
eveint()
def evestr():
    for i in range(0,100):
        if evepol[i]=='v':
            evebin[i]=0
        elif evepol[i]=='h':
            evebin[i]=1
        elif evepol[i]=='r':
            evebin[i]=0
        elif evepol[i]=='l':
            evebin[i]=1
        else:
            print("error")
evestr()        
print("\nThese are the photons intercepted by eve\n",evepol)
print("\nThis is the binary stream intercepted by eve\n ",evebin)