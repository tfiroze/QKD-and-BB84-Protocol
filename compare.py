import aliice
import bob
arr=bob.keyarfun()
bin=aliice.alicebin
key=[0]

for i in range(0,32):
    if(bob.bobpolar[i]==aliice.basis[i]):
        if(arr[i]==bin[i]):
            key.append(bin[i])
print(key)
print(len(key))