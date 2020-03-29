x1=input("Enter the first string ")
#x2=input("Enter the second string ")
str1=""
str2=""
l1=[i for i in x1 if(x1.count(i)>1)]
l2=[i for i in x1 if(x1.count(i)==1)]

print("1st string {} 2nd string {}".format(str1.join(set(l1)),str2.join(set(l2))))

