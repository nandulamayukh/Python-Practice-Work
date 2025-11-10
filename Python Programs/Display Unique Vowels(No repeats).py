#Display Unique Vowels(No repeats)
a=input()
e=list(a)
b='aeiou'
c=[]
for x in range(0,len(e)):
	if(e[x] in b):
		if(e[x] in c):
			print(c)
		else:
			c.append(e[x])
print(c)
