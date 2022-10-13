from operator import le
from pickletools import string1


str1 = "welcome"
str2 = 'wellcome'
str3 = '''hello guys am poonam'''
str4 = '''hello guys '''
str5=str4

print("str1=", str1,id(str1))
print("str2=", str2,id(str2))
print("str3=", str3,id(str3))
print("str4=", str4,id(str4))
print("str5=", str5,id(str5))

str = 'hello'
n = len(str)
print(n)

str = "hi guys am poonam , am from latur"
n= len(str)
print(n)

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])
print(str[7])
print(str[8])
print(str[9])
print(str[10])
print(str[11])
print(str[12])
print(str[13])
print(str[14])
print(str[15])
print(str[16])


for c in str:
    print(c)

    for i in range(len(str)):
        print(str[i],'=',i)



