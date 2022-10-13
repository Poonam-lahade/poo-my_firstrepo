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
class Son(Father,Mother):
    def _init_(self):
        print('son class constructor')
        Mother._init_(self)
        Father._init_(self)
    def showS(self):
        print("Son Class Method")
s =Son()
s.showF()
s.showM()
s.showS()



print('#############################################')
class Father:
    def _init_(self):
        
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")
class Mother:
	def _init_(self):
         super()._init_()
         print("Mother Class Constructor")
        def showM(self):
	    print("Mother Class Method")
class Son(Mother,Father):
    def _init_(self):
        super()._init_()
        print('son class constructor')
        
    def showS(self):
        print("Son Class Method")
s =Son()
s.showF()
s.showM()
s.showS()