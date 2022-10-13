#pillers of oops
'''
inheritance
type of inheritance
single
multiple 
multilevel
hybrid

abstaction-ABC class abstrction,interface
incaptulation-clas is a best example for incapsulation.binding data memeber and method incapsulation
polymorphism
'''

# Python program to demonstrate
# single inheritance

# Base class/parentclass/
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class


class Child(Parent):
	def func2(self):
		print("This function is in child class.")


# Driver's code
object = Child()
object.func1()   #inherite parent
object.func2()



########################################################################
#single inheritance
class Company:   #parent class/base class
    name1='MTSS'  #parent class class variable
    def _init_(self):
        print('calling from parent constructor')
        self.city='pune'  #data member instance variable
        self.address='hadpsar'
    def show_company_detail(self):   #method/action
        print(self.city,self.address)    

class Employee(Company):  #child class
    def _init_(self):
        super()._init_()   #calling parent class constructor
        print('calling from child constructor')
        self.name='rahul'
        self.age=28
    def show(self):
        print(self.name)    
e=Employee()
e.show()
print(e.name1)  #parent class variable name 1 access by inheritance


#why we use parent class constructor inside child using super
#################################################################################


# Python program to demonstrate
# multiple inheritance
# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)
# Base class
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)
# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


############################################################################

class Design:
    def _init_(self):
        self.name1='mechanical design'
    def show1(self):
        print(self.name1)
class web_Design:
    def _init_(self):
        self.name2='web design'
    def show2(self):
        print(self.name2)

class courses(web_Design,Design):
    def _init_(self):
        super()._init_()
        # super()._init_()
        self.name3='we offered'
    def show3(self):
        print(self.name3)
c=courses()
print(c.name1)
print(c.name2)


###############################################################################################################
class Tokenizer:
    """Tokenize text"""
    def _init_(self, text):
        print('Start Tokenizer._init_()')
        self.tokens = text.split()
        print('End Tokenizer._init_()')
class WordCounter(Tokenizer):
    """Count words in text"""
    def _init_(self, text):
        print('Start WordCounter._init_()')
        super()._init_(text)
        self.word_count = len(self.tokens)
        print('End WordCounter._init_()')
class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def _init_(self, text):
        print('Start init Vocabulary._init_()')
        super()._init_(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary._init_()')
class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def _init_(self, text):
        print('Start init TextDescriber._init_()')
        super()._init_(text)
        print('End init TextDescriber._init_()')
td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)


########################################################################################
print('##########################################################')
# Multiple Inheritance
class Father:
	def _init_(self):
		print("Father Class Constructor")
	def showF(self):
		print("Father Class Method")
class Mother:
	def _init_(self):
		print("Mother Class Constructor")
	def showM(self):
		print("Mother Class Method")
class Son(Mother,Father):
	def _init_(self):
         print("Son Class Constructor")
        Mother._init_()
	def showS(self):
		print("Son Class Method")
s = Son()
s.showF()
s.showM()
s.showS()



class TeamMember():
    def _init_(self, name, uid):
        print('team member constructor')
        self.name = name
        self.uid = uid
# Parent class 2
class Worker():
    def _init_(self, pay, jobtitle):
        print('workser constrctoe')
        self.pay = pay
        self.jobtitle = jobtitle
# Deriving a child class from the two parent classes
class TeamLeader(Worker,TeamMember):
    def _init_(self, name, uid, pay, jobtitle, exp):
        print('teamleader class constructor')
        self.exp = exp
        Worker._init_(self, pay, jobtitle)
        TeamMember._init_(self, name, uid)
        
        print("Name: {}, Pay: {}, Exp: {}".format(
            self.name, self.pay, self.exp))
TL = TeamLeader('Michael', 10001, 250000, 'Scrum Master', 5)