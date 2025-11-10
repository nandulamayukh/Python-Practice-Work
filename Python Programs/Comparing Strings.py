#Comparing Strings
import sys
a=b=c=d=e=f=g=0
m=input('Enter String')
for i in range(0, len(m)):
	if(m[i].isalpha()):
		a=a+1
	else if (m[i].isdigit()):
		b=b+1
	else if (m[i].isspace()):
		c=c+1
	else:
		d=d+1

print("Number Of Alphabets:", a)
print("Number Of Digits:", b)
print("Number Of Spaces:", c)
print("Number Of Special Characters:", a)

