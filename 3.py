x1=input("Enter the first string ")
#x2=input("Enter the second string ")
str1=""
str2=""
c,d,e=0,0,0
for i in x1:
	if i.islower():
		c=c+1
	if i.isupper():
		d=d+1
	if i.isidentifier():
		e=e+1
#l1=[i for i in x1 if((65<=ord(i)<=90) or (97<=ord(i)<=122) or ord(i)==32)]
#print(l1)
print("count of upper is {}, lower is {}, specialcharacter is {}".format(c,d,len(x1)-c+d))

