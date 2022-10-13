from turtle import clear

#conditional satatement
if 5>2:
    print('five is grater than two!')
    if 5>3:
        print("five is grater than three!")

print("##############################****************##############")        
                                            
num= 5
if(num<10): 
 print('num is smaller than 10')
 print("this statement will always be executed")

 print("##############################****************##############")        

a=7
b=0
if(a>=b):
    print("a is grater than b")

    print("##############################****************##############")        

a=7
b=10
if(a):
    print("true")

    
print("##############################******USING IF_ELSE STATEMENT **********##############")        
                                            
num= 5
if(num<10): 
 print('num is grater than 10')
else:
 print('num is smaller than 10')

 print("this statement will always be executed")
 print("######################################################")

 a= 15
 b=10
if(a<b): 
 print('a is grater than b')
else:
 print('a is smaller than b')

 print("this statement will always be executed")

#######################
 print('##############################******USING ELIF STATEMENT **********##############')                    
num= 10
if(num==0): 
 print('number is 0')
elif(num>5):
 print("number is grater than 5")
else:
 print('num is smaller than 5')

 print("this statement will always be executed")


a= 10
b=2
if(a==b): 
 print('a and b are same')
elif(a>5):
 print("a is grater than 5")

else:
 print('a is smaller than 5')

a= -10
#b=2
if(a>0): 
 print('a is positive')
elif(a<0):
 print("a is negative")

else:
 print('a is 0')
 
print("##############################******USING NESTED IF_ELSE STATEMENT **********##############")                                                  
 
num=5
if(num>5):
    print("number is positive")
if(num<10):
     print("num is less than 10")

list1=[1,2,44444,5,6,7,'amol']
for i in list1:
        print("list1")
for i in range(10):
    print(i)

print("###########################################")

list1=[1,2,44444,5,6,7,55,66,77]
for i in list1:
        if i%2==0:
         print(i)
        else:
            pass

print("######################################")

list=[1,2,3,4,5,6,7,8,999999]
for i in list:
    if type(i)==str:
        break
    print(i)

print("######################################")

list=[1,2,3,4,5,6,7,8,999999]
for i in list:
    if i==999999:
        continue
    print(i)

print("######################################")

list=[1,2,3,4,5,6,7,8,999999]
for i in list:
    if i==999999:
        pass
    print(i)

