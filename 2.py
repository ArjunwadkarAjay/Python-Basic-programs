x1=input("Enter the first string ")
x2=input("Enter the second string ")
str1=""
str2=""
l1=[i for i in x1 if(i not in x2)]
l1.extend(i for i in x2 if(i not in x1))
#l2=[i for i in x1 if(x1.count(i)==1)]

print("the string is {} ".format(str1.join(set(l1))))

