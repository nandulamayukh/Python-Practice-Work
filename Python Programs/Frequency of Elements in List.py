#Frequency of Elements in List
a=eval(input("Input List"))
n=0
c=0
b=eval(input("Which Element would you like to search? "))
for i in range(0,len(a)):
	if(b==a[i]):
		n=n+1
		c=i
		print(b,"is found at index", i+1)
if (n==0):
		print(b,"is not found in given list")
else:
	print(b, "appears",n,"times")


