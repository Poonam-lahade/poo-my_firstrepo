'''
in python everyting is object. to craete a class we required some blue print or plan which is nothing but
 a classs
python class is group of attributes and method.



attribute/properties-class varieble-attributes are represented by varianble which content data.
methods/actions-metjod perform ac action or task ,it is similar to fucntipon


#define class

class ClassName:
    constructor
    variablle
    methods
'''




class employee:   #classss
    def _init_(self):    #constructor,self
        self.name='lalit'    # insatnce variabels
        self.age=30
        self.salary=80000
    def emp_details(self):    #action/method
        print(f'my name is {self.name} and my age is {self.age} and i got {self.salary}')
e=employee()   # object cretae
print('instance variable ################################')
print(e.name) #accesss instancce vriable
print(e.salary)
print(e.age)
e.emp_details()

##############################################################
'''
#constructor and self keyword.
python suppport special type of method called constructor  for  intilize instance avriable  of calss.\
a class constructor is called when we create a object for that  perticular class   
if two instacne are created for a class , the constrtor will called once for each.
#we can create a multiple object from a class because it a blueprint.


#self define object referance
'''
print("##########################################")
#withou argument
class Student:
    def _init_(rd):  #consttrctor have by default self as first argument
        rd.name='lalit'    #initilize /declare insatcne variabel
        rd.age=28
    def show_data(self):     #instance method define with self as first argument
        print(self.name,self.age)    
s=Student()     #object crete
print(s.name )    #access insatce variabel
r=Student()       #second object created
r.show_data()    #access instance method


#passing argument ouside of class
print('#####################################################################')
class Student:
    def _init_(self,name,age,salary):   #constructor
        print('constructor calling for student class thats mean object is created for studemnt class')
        self.name=name    #insatcne variable
        self.age=age
        self.salary=salary
    def show_data(self):  #defince instacne method
        print(self.name,self.salary,self.age)   
s=Student('abhay',30,80000)#referacnce variabel/object of class/class level variable
print(s.name)  #acceessing instacne variable outside of classs
print(s.age)
print(s.salary)
s.show_data()   #accessing instance method outside of class

###########################################################################################
#class
#object
#constructor
#self
# types of variable-insatcne ,class, local
#types of methods-instacne method,class method ,static method
#why oops(object orinted programming)

#####################################################################################
class Student:
    def _init_(self,name,age,salary):   #constructor
        print('constructor calling for student class thats mean object is created for studemnt class')
        self.name=name    #insatcne variable
        self.age=age
        self.salary=salary
    def show_data(self):  #defince instacne method
        print(self.name,self.salary,self.age)   
s=Student('abhay',30,80000)#referacnce variabel/object of class/class level variable
print(s.name)  #acceessing instacne variable outside of classs
print(s.age)
print(s.salary)
s.show_data()   #accessing instance method outside of class




##########################################################

class Employee:  #self define cuerrent class instance/object  referance
    company='Radhe engineering'   #class level variable
    def _init_(self,salary):  #constructor are used to intilize  insatnce variable
        self.name='rahul'    #instance variable
        self.age=28
        self.salary=salary
    def show_details(self):  #instacne method
        x=2   #local variable
        y=3
        print(x+y)
        print('Employee name:-',self.name,'\n','Employee age:-',self.age,'\n','Employee saalry:-',self.salary,y)

e=Employee(800000)  #referance variable/instance of class/object/class level variable
e.show_details()

#constructor class-
'''
when we create a instance for class,1)memory allowcate acoording to varaibele and method inside a class.

2)and costructor(a special method used in a class to initilize insatcen variable) will 
call automatically and load the variable data inside a referance variable
'''       

#method vs constructor
'''
we can define a name for method but we can not define for constuctor.
method will execute when we call but constuctor will calll automatically.
method can call any numbeer of times but constructor will calll onces for each object.
method can write business logic but constrctor used for initilizing insatcne variable.
'''
#types of avriable
'''
1)insatnce variable-

instance variable are  variable whose seperate copy is created for each object.
insactne var are define and initilize using constaructoor and self key word.
'''

class Mobile:
    def _init_(self):
        self.name='Real me 1212312'
    def show_model(self):
        print(self.name)
Realme=Mobile()      #1 object
iPhone=Mobile()       #2 object
Realme.name='realme'  #set name for first object
iPhone.name='iphone'   #set name foe second onbject
print(Realme.name)
print(iPhone.name)
#where we can declare instacnce variabele
#1)inside constrcor by using self keyword
#2)inside insatcne method using self keyword
#3)outside of class by using object referance
class Test:
    def _init_(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=20
t=Test()
t.a=100  #access outside of class using object name


#static variable/class variable
'''
if the value of a variable is not varied form object to objecct such type of variable we have to 
declare with in the class directly but outside of metthod such type of variable are called static 
variable.
we can access class/ static variable either by class name or by object referance. but recommanded 
to use class name
'''

class Student:
    college='D.Y.Patil college of engineering and technology'   #class
    def _init_(self):
        self.name='rahul'
        self.age=28
        self.marks=80

    def show_details(self):   
        x=3
        print(x)
        print(Student.college)   #access class level variable using class name
        print('Enter a name:-',self.name)
        print('Enter a age:- ',self.age)
        print('Enter a marks:-',self.marks) 
s=Student()
t=Student()
Student.college='raddhe'  #access it using class name
print(s.college)  
s.college='radhe'
print(t.college)     
print(s.college)
s.show_details()

#local variable-=define locally and has local scope can not acces outside of class