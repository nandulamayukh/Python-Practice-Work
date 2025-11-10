#Sorting Given input Alphabetically and numerically
a=input()
b=list(a)
c=[]
d=[]
for x in range(0,len(b)):
	if(b[x].isalpha()==True):
		c.append(b[x])
	else:
		d.append(b[x])
print(''.join(sorted(c)+sorted(d)))
