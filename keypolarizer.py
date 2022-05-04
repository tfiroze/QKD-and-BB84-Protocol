import compare
keypol=compare.key
newpol=[0]*16
for i in range(0,16):
    if(keypol[i]==0):
        newpol[i]='p'
    if(keypol[i]==1):
        newpol[i]='x'
for i in range(0,20):
    newpol.extend(newpol)    