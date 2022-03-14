import aliice
import bob
arr=bob.keyarfun()
bin=aliice.alicebin
key=[0]*16
i=0
while(i!=16):
    #print(i)
    if(bob.bobpolar[i]==aliice.basis[i]):
        if(arr[i]==bin[i]):
            key[i]=bin[i]
            
    i=i+1
print(key)
print(len(key))