t=True
x=input("Enter the string")
print(x)
l1=list(x)
#l=[x[i] for i in range(0,len(x)) if(x[i]!=x[len(x)-i]) ]
print(l)
for i in range(0,len(x)):
	for j in range(len(x),0):
		if(x[i]!=x[j]):
			t=False

if(l1==l):
	print("The string is palindrome")
else:
	print("The string is not palindrome")
