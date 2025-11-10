#Search for an Element in List
a=eval(input("Input List"))
b=eval(input("Which Element would you like to search? "))
for i in range(0,len(a)):
	if(b==a[i]):
		print(b,"is found at index",i+1)
		break;
	else:
		print(b,"is not found in given list");

