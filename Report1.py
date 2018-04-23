print 'This is a program for Report1'
sp = [103,97,106,104,107,101,100,106,103,99,102,111]
mip = sp[1] - sp[0] #provent the "0" bug
msf = sp[0] #buying price
for i in range(1,11):
	d = sp[i] - msf #profit function
	if d < mip: #if the new profit is less
		mip = d #keep the new profit
	if sp[i] > msf: #if the new price is higher
		msf = sp[i] #renew the price for buying
print "==============================="
print mip, 'in data1'
print "==============================="
# reload new data in the same program
sp = [92,95,97,99,99,100,103,106,110,112,118,121]
mip = sp[1] - sp[0]
msf = sp[0]
for i in range(1,11):
	d = sp[i] - msf
	if d < mip:
		mip = d
	if sp[i] > msf: 
		msf = sp[i]
print "==============================="
print mip, 'in data2'
print "==============================="
raw_input("Press enter to exit")