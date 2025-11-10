#Printing Odd And Even indexes
a=input()
b=list(a)
c=[]
d=[]
for x in range(0,len(b)):
	if(x%2==0):
		c.append(b[x])
	else:
		d.append(b[x])
print(''.join(c))
print(''.join(d))