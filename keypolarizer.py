import compare
key=compare.key

newpol=[0]*16
for i in range(0,16):
    if(key[i]==0):
        newpol[i]='p'
    if(key[i]==1):
        newpol[i]='x'
for i in range(0,20):
    newpol.extend(newpol)    
#print(len(newpol))
