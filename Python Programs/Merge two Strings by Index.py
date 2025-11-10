#Merge Two Strings by Index
a=input()
b=input()
if (len(a)<len(b)):
	c=len(a)
else:
	c=len(b)
for x in range(0,c):
	print(a[x]+b[x], end='')
	y=x+1
if (len(a)<len(b)):
	print(b[y:len(b)])
else:
	print(a[y:len(a)])