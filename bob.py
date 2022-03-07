import polarizer
import random
bobpolar=polarizer.polar(8)
alicephot=['h','v','l','r','r','l','h','v'] #test list alicephot
keyarray=[0]*len(alicephot)
for i in range(0,8):
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
print("Quantum key distribution key is ",keyarray)
#for i in range(0,8):
#    print(keyarray[i])


        
