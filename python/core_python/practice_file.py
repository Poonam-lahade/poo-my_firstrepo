# leap year program


year=int(input("Enter a year:->"))

if(year%4==0)and(year%100==0)or(year%400==0):
    print("The year is leap year")
else:
    print("The year is not a leap year")

##################################

year=int(input("Enter a year to check a leap year:->"))
if(year%4==0):
    print("{0}The year is leap year".format(year))
else:
 if(year%100==0):
    print("{0}The year is not a leap year".format(year))
 else:
  if(year%400==0):
    print("{0}The year is leap year".format(year))
  else:
    print("{0}The year is not a leap year".format(year))

##########################################################
###########################################################

#program to check if the number is an armstrang no or not

num=int(input("Enter a number to check armstrang no or not"))
sum=0
X=num
while X>0:
    A=X%10
    sum+=A**3
    X//=10

    if num==sum:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstron number")    

#################################################################
#################################################################

# program to print multiplication table of given number

num = int(input("Enter a number to show a table "))
count=1


while count<=10:
    num=num*1
    print(num,"X",count,'=',num*count)
    count+=1


###################################################################################
######################################
#Write a program  that display sum of series - 1,1/2,1/3,........1/n

N=int(input("Enter of number of tearms:"))
sum=0
for i in range (1,n=1):
    sum=sum=(1/i)
    print("the sum of series is ",round(sum,2))

    
######################################################################
##########################################

#write a program to display sum of series -1,1/2**2.....,1/n**2
N=int(input("Enter of number of tearms:"))
sum=0
for i in range (1,n=1):
    sum=sum=(1/i**2)
    print("the sum of series is ",round(sum,2))
    
##############################################################
####################################################

#write a program to calculate sum of cubes of no's from 1-n




















