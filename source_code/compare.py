import alice
import bob
arr=bob.keyarfun()
key=[0]*16
i=0
while(i!=16):
    #print(i)
    if(bob.bobpolar[i]==alice.basis[i]):
        if(arr[i]==alice.alicebin[i]):
            key[i]=alice.alicebin[i]            
    i=i+1
print("\nThis is the 16 digit key\n",key)