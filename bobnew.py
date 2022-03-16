import alicenew
import keypolarizer
bindata=[0]*len(alicenew.alicenewphot)
def finalar():
    for i in range(0,len(alicenew.alicenewphot)):
        if(keypolarizer.newpol[i]=='p' and alicenew.alicenewphot[i]=='v'):
            bindata[i]=0
        elif(keypolarizer.newpol[i]=='p' and alicenew.alicenewphot[i]=='h'):
            bindata[i]=1
        elif(keypolarizer.newpol[i]=='x' and alicenew.alicenewphot[i]=='r'):
            bindata[i]=0
        elif(keypolarizer.newpol[i]=='x' and alicenew.alicenewphot[i]=='l'):
            bindata[i]=1
        else:
            print("Error in transmission")
    #print("Quantum key distribution key is ",bindata)
    return bindata
asd=finalar()
temp=[0]*len(asd)
for i in range(0,len(asd)):
    temp[i]=str(asd[i])
str1 = "" 
# traverse in the string  
for ele in temp: 
    str1 += ele
cat=int(str1)

print(cat)