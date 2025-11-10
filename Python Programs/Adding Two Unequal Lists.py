#Adding Two Unequal Lists
a=list(input("input a "))
b=list(input("input b "))
c=[]
if len(a)<len(b):
	d=len(a)
else:
	d=len(b)
for i in range(0,d):
	c[i]=a[i]+b[i]
print(c)