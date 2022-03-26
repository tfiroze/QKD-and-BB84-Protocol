import alicenew
import keypolarizer
import compare
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
#print(asd)
flag=asd
print(len(flag))
for i in range(0,16):
    flag.pop(i)
print(len(flag))
for num in range(len(flag)-1,len(flag)-17, -1) :
    flag.pop(num)
    #print(num)
print(len(flag))
print(len(alicenew.temp))
asd=flag
temp=[0]*len(asd)
for i in range(0,len(asd)):
    temp[i]=str(asd[i])
str1 = "" 
# traverse in the string  
for ele in temp: 
    str1 += ele
cat=int(str1)
#print(compare.key)
#print(cat)
# Python3 code to demonstrate working of
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()


# Defining BinarytoDecimal() function
def BinaryToDecimal(binary):
		
	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return (decimal)

# Driver's code
# initializing binary data
bin_data =str1

# print binary data
print("The binary value is:", bin_data)

# initializing a empty string for
# storing the string data
str_data =' '

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
	
	# slicing the bin_data from index range [0, 6]
	# and storing it as integer in temp_data
	temp_data = int(bin_data[i:i + 7])
	
	# passing temp_data in BinarytoDecimal() function
	# to get decimal value of corresponding temp_data
	decimal_data = BinaryToDecimal(temp_data)
	
	# Decoding the decimal value returned by
	# BinarytoDecimal() function, using chr()
	# function which return the string corresponding
	# character for given ASCII value, and store it
	# in str_data
	str_data = str_data + chr(decimal_data)

# printing the result
print("The Binary value after string conversion is:",
	str_data)
