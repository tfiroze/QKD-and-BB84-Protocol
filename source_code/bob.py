from alice import basfun
import polarizer
import random
import alice
bobpolar=polarizer.polar(100)
alicephot=alice.basfun()
keyarray=[0]*len(alicephot)
def keyarfun():
    for i in range(0,100):
        if(bobpolar[i]=='p' and alicephot[i]=='v'):
            keyarray[i]=0
        elif(bobpolar[i]=='p' and alicephot[i]=='h'):
            keyarray[i]=1
        elif(bobpolar[i]=='p' and alicephot[i]=='r'):
            keyarray[i]=random.randint(0,1)
        elif(bobpolar[i]=='p' and alicephot[i]=='l'):
            keyarray[i]=random.randint(0,1)
        elif(bobpolar[i]=='x' and alicephot[i]=='h'):
            keyarray[i]=random.randint(0,1)
        elif(bobpolar[i]=='x' and alicephot[i]=='v'):
            keyarray[i]=random.randint(0,1)
        elif(bobpolar[i]=='x' and alicephot[i]=='r'):
            keyarray[i]=0
        elif(bobpolar[i]=='x' and alicephot[i]=='l'):
            keyarray[i]=1
        else:
            print("Error in transmission")
    return keyarray
#print("\nThis are the basis used by bob\n",bobpolar)
#print("\nThis is the stream of binary data recieved by bob\n",keyarfun())


        
