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