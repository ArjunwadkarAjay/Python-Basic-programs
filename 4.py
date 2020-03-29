x1=input("Enter the first string ")
x1=x1.upper()
#x2=input("Enter the second string ")
str1=""
str2=""
l1=[chr(i) for i in range(65,91)]
l2=[i for i in x1 if l1.index(i)==x1.index(i)]
print("The count is ",len(l2))
#print("1st string {} 2nd string {}".format(str1.join(set(l1)),str2.join(set(l2))))

