#Adding Two Unequal Lists
a=eval(input("input a "))
b=eval(input("input b "))
c=[]
if len(a)<len(b):
	d=len(a)
else:
	d=len(b)
for i in range(0,d):
	c.append((a[i])+(b[i]))
print(c)