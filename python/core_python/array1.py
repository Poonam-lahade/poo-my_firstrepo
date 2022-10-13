'''
array is an object that provide a mechanism for storing data with only one
identifier that simpify
task of data management.
array is benificial if you need to store same type of items.
array can increase and decrease their size dynamically.
array uses less memory than list.
array type :-
one d arry
multi d array
a=[1,2,3,4,5]
a=[1,2,3,4],[1,2,3,4]
'''
#import array module
'''
import array-entire array module will import
from array import*-this will import all class , object , varianble from
array module.
import array
array1 =array.array('type code',[elements])
arrayobject=modulename.classname('int',[elemet])
'''
import array
from inspect import ismethoddescriptor
from re import L, T
import re
matplotlib.pyplot
from matplotlib.pyplot import prism
stu=array.array('i',[1,2,3,4,5,6])
print(stu)
print(type(stu))
import array
stu=array.array('f',[1,2,3,4,5,6])
print(stu)
print(type(stu))
from array import*
stu=array('i',[12,3,4,56,1924,4,56,67])
print(stu)
print(type((stu)))
#indexing
print(stu[0])
print(stu[1])
print(stu[2])
print(stu[3])
print('##############################################################')
#access using for loop
#witout index
for ele in stu:
 print(ele)
print('##############################################################')
#with index
for ele in range(len(stu)):
 print(ele,stu[ele])
print('##############################################################')
#using while loop
n=len(stu)
i=0
while i<n:
  print(stu[i])
i+=1
print('##############################################################')
#getting user input as array
# from array import*
# stu1=array('i',[]) #empty array
# n=int(input('how many ele you want to insert'))
# for i in range(n):
# stu1.append(int(input('enter element:-')))
# print(stu1)
print('##############################################################')
#methods in array
'''
append(element),insert(element),pop(),pop(position),remove(element),index(element
),reverse,extend,
'''
print('##############################################################################')
#third party packages install using pip only and predefinded module you have to import inside your perticular module.
#numpy,pandas,matplotlib.
#numpy
'''
numpy is a packge which conatian classes, function, variable, large math function
etc to work
with scintific calculastion .
numpy can be used to creqate n-D arayy where n is any integer. we can create 1-d
,2-d,3-d array \
and so on.
numpy array class is called ndaray.
'''
'''
#import numpy
import numpy-this is will import entire numpy module.
from numpy import*-this will import all classes ,object,variable,etc from numpy
package.
#hetrodata allowed
#mutable
#indexing
'''
''''
ways of creating array in numpy
#array()
#linespace()
#logspace()
#arrange()
#zeroes()
#ones()
'''
#1)array() function
'''
import numpy
array_name=numpy.array([element])
'''
import numpy
stu=numpy.array([1,2,3,54,6567])
print(stu)
print(type(stu))
a=numpy.array([1.2,3.3,5.6,2.4],float)
print(a)
str1=numpy.array(['sakshi','lalit','poonam'],dtype=str)
print(str1)
str2=numpy.array(['sakshi','lalit','poonam',34])
print(str2)
#indexing
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[2])
#modify
str1[0]='rahul'
print(str1)
#2)linespace() function
'''
linespece function is used to create an array with evenly apacd number between
startpoint annd end point.
syntax:-
numpy.linespace(start,stop,num=50,endpoint=true)
start-to represett starting element
stop-to represent ending element.
num-to represent number of parts the element should be divided defautl=50,it must
be non negative.
end-point=if true stopis the last elemtn if false stop is not included.
'''
#creating array using linespace function
from numpy import*
a=linspace(1,8)
print(a)
print(type(a))
print('################################################')
from numpy import*
a=linspace(1,8,num=5)
print(a)
print(type(a))
print('################################################')
from numpy import*
a=linspace(1,8,5,endpoint=False)
print(a)
print(type(a))
#indexig
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#access using for loop
for i in a:
 print(i)
#logspace() function
'''
this function is used to create array with evenly apaced number.
syntax:-
numpy.logspace(start,stop,num=50,base=10)
#ask me how it devide
'''
print('##########################################################')
from numpy import*

array_name=logspace(1,1)
print(array_name)
print('##########################################################')
a=logspace(1,3,5)
print(a)
b=logspace(1.0, 3.0, num=5, dtype = int)
print(b)
c=logspace(3,4,5)
print(c)
print('##########################################################')
print(c[0])
print(c[1])
print('##########################################################')
n=len(c)
i=0
while i<n:
 print(c[i])
i+=1
print('##########################################################')
#arrange() functyion
#syntax:-
'''
numpy.arrange(start,stop,stepsize,stype)
'''
from numpy import*
a=arange(5)
print(a)
b=arange(5,10,1,dtype=float)
print(b)
#access
print(b[0])
print('#############################################################')
#zeroes () function
'''
syntax:-
aname=zeres(shape,dtype=)
'''
from numpy import*
a=zeros(5,dtype=int)
print(a)
#ones() functipon
a=ones(5)
print(a)
##################################################################
#math operation on array
a=array([101,102,103,104])
a=a+5
print(a)
b=array([10,20,30,40])
print(a+b)
#array alaising
b=c
print(c)
c[0]=2222
print(c)
print(b)
#################################################################################
##
#view() method
'''
this method is used to construct a new view of array with same data of existing
array.
existing array and new array share differnt memory location.
if the new array get modified the existing will also be modified as the element.
'''
print('#############################################')
a=array([10,20,30,405])
b=a.view()
a[0]=100000
print(b)
print(id(b))
print(a)
print(id(a))
#copy() funcytion
'''
this function is used to create a copy of an existing array . iuf new array get
modified ,
the existing array will not be affected or vice vercsa
both the array are independent.
'''
print('#############################################')
a=array([10,20,30,405])
b=a.copy()
a[0]=100000
print(b)
print(id(b))
print(a)
print(id(a))
#################################################################################
########
#################################################################################
######3
#multi-d array
'''
2-d array 3-d array are called multi d array
'''
#2-array
print('##########################################################')
'''
if an arrya contain more than 1 row and 1 column that is know as 2-d array.
it also known as array of array
'''
a=array([[1,2,3,4],[4,2,4,5,67]])
b=array([[1,2,3,4],[4,2,4,5,67],[112,224,4456,777]])
print(a)
print(b)
print(type(a))
#ways of creating multi-d array
'''
array()
zeroes()
ones()
reshape()
syntax:-
'''
print('#####################################3')
#1)array:-
#numpy.array(object,dtype)
#arname=numpy.array([element],[elemenmt])
a=numpy.array([[10,20,40,50],[10,20304,5405]])
print(a)
a=numpy.array([['rahul','sanika','raj'],['lalit','sakshi','ra1']],dtype=str)
print(a)
#access using indexing
print(a[1][0])
print(a[1][1])
print(a[1][2])
#modified multi d
a[1][0]='vikrant'
print(a)
print('#########################################################')
#access using for loop
#without index
for i in a:
 for j in i:
  print(j)
print('###########################################################')
#with index
for i in range(len(a)):
 for j in range(len(a[i])):
  print(i,j,a[i][j])
#using while loop
print('#######################################################')
n=len(a)
i=0
while i<n:
 j=0
while j<len(a[i]):
  print(i,j,a[i][j])
j+=1
i+=1
print('############################################################')
#zeroes() function
a=zeros((3,2))
print(a)
#ones() function
a=ones((3,4))
print(a)
#reshape( ) function
'''
this function is used to change the shape of array .we can convert 1-d array to
2-d or 3-d array .
the new array should have the same number of element as the original
'''
print('################################################')
#convert 1-d array into 2-D array
a=array([11,22,33,44,55,66,22,33])
b=reshape(a,[2,4])
print(b)
print('################################################')
#convert 1-d array into 3-D array
a=array([11,22,33,44,55,66,22,33,11,11,22,33,11,22,33,44,11,223])
b=reshape(a,[2,3,3])
print(b)
#convert 2-d into 1-d array
print('################################################')
a=array([[1,2,34],[12,3,4]])
f=reshape(a,(6))
print(f)
#convert 3-d into 1-d array
print('################################################')
a=array([[1,2,34],[12,3,4],[1,2,3]])
f=reshape(a,(9))
print(f)
#################################################################################
##########
#copy() function-memory location different but not reflect change
print('#########################################################')
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=43
print(arr)
print(id(arr))
print(x)
print(id(x))
print('#########################################################')
#view() function -memory location differnt but change refflect on other
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=43
print(arr)
print(id(arr))
print(x)
print(id(x))
print('#####################################################################')
#shape-the number of each element in each dimention
import numpy as np
arr=np.array([[1,2,3,4],[1,2,3,4],[12,23,4,5]])
print(arr.shape)
print('#####################################################################')
import numpy as np
arr=np.array([[1,'rahul','dhokane',9130904439],[2,'mayuri','idknow',236402153],[3
,'sakshi','chidrawar',164098]])
print(arr.shape)
print('#####################################################################')
#reshape()
#1-d 2-d
import numpy as np
arr=np.array([1,2,34,4,5,6,7,8,12,3,4,2])
newarr=arr.reshape(3,4)
print(newarr)
print('#1-d 3-d####################################################################')
#1-d 3-d
import numpy as np
arr=np.array([1,2,34,4,5,6,7,8,12,3,4,2,1,2,3,4,5,6])
newarr=arr.reshape(2,3,3)
print(newarr)
#flattening the array
#flattening array means converting a multidimensional array into a 1-2 array
arr=np.array([[1,'rahul','dhokane',9130904439],[2,'mayuri','idknow',236402153],[3
,'sakshi','chidrawar',164098]])
newarr=arr.reshape(-1)
print(newarr)
###########################################################################
#########################################################################
################################################################################
#joining arrays
#join 1 -d array
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)
#join 2-d array
print('#########################################################')
import numpy as np
arr1=np.array([[1,2],[3,4]])
# arr12=arr1.reshape(-1)
# print(arr12)
arr2=np.array([[5,6],[7,8]])
# arr123=arr2.reshape(-1)
arr=np.concatenate((arr1,arr2))
print(arr)
# newarr=arr1.reshape(-1)
# print(newarr)
#################################################################################
########
#joining array using stack function.
'''
stacking is same as concatenation , the only fifferance is that stacking is done
only along a new axis
'''
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([1,2,34,4])
arr=np.stack((arr1,arr2))
print(arr)
print('###############################################')
#stacking along rows
#nupmy provide a helper function hstack() to stack along rows
import numpy as np
arr1=np.array([1,2,34])
arr2=np.array([4,5,6])
arr=np.hstack((arr1,arr2))
print(arr)
print('###############################################')
#stacking along columns
#vstack()
import numpy as np
arr1=np.array([1,2,34])
arr2=np.array([4,5,6])
arr=np.vstack((arr1,arr2))
print(arr)
#################################################################################
##############
#################################################################################
######
#split() function
import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,5)
print(newarr)
print('###################################################')
#splitting 2-d array
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr=np.array_split(arr,2)
print(newarr)
#################################################################################
#######
#searching arrays
print('searching array#####################')
import numpy as np
arr=np.array([1,2,3,4,'54',5,67,78,4])
x=np.where(arr=='54')
print(x)
####################################
import numpy as np
arr=np.array([1,2,3,4,54,5,67,78,4])
x=np.where(arr%2==0)
print(x)
#############################################
import numpy as np
arr=np.array([1,2,3,4,54,5,67,78,4])
x=np.where(arr%2==1)
print(x)
############################################
#array sorting-putting element in an ordered sequence
print('####################################################')
import numpy as np
arr=np.array([1,2,3,4,54,5,67,78,4])
x=np.sort(arr)
print(id(arr))
print(id(x))
##############################################################
#sorting technique
#searching technique
#filter technique
###########################################################################
#data structure-what is datastrucre
#stack
#queue
#search-binary,liner search
#sort-bubble sort,insertion sort,merge sort