x1=input("Enter the first string ")
#x2=input("Enter the second string ")
str1=""
str2=""
l1=[i for i in x1 if((65<=ord(i)<=90) or (97<=ord(i)<=122) or ord(i)==32)]
#print(l1)
print("1st string {}".format(str1.join(l1)))

