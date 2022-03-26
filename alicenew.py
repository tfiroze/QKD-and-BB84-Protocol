import keypolarizer
data="hey there how are you what is the time"
res = ''.join(format(ord(i), '08b') for i in data)
temp=[0]*len(res)
for i in range(0,len(res)):
    temp[i]=int(res[i])
print(temp)
send=keypolarizer.keypol.copy()
send.extend(temp)
send.extend(keypolarizer.keypol)
#print(send)
#print(keypolarizer.newpol)
alicenewphot=[0]*len(send)
def newsend():
    for i in range(0,len(send)):
        if(send[i]==0 and keypolarizer.newpol[i]=='p'):
            alicenewphot[i]='v'
        elif(send[i]==0 and keypolarizer.newpol[i]=='x'):
            alicenewphot[i]='r'
        elif(send[i]==1 and keypolarizer.newpol[i]=='x'):
            alicenewphot[i]='l'
        elif(send[i]==1 and keypolarizer.newpol[i]=='p'):
            alicenewphot[i]='h'
        else:
            print(send[i])
    return(alicenewphot)
newsend()
#print(len(send))
#print(len(alicenewphot))
