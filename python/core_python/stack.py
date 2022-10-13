#satck work on FILO  or LIFO
#using list
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print((stack))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())



#stack implemewntatuion using collections.deque

from collections import deque

stack=deque()
print(type(stack))

print('stack implementation using collections.deque')
#append() functions to  push
stack.append(11)
stack.append(22)
stack.append(33)
stack.append(44)
#pop() pop out element

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


######################################################################################
print('###########################################################')
def push(l,val):
    l.append(val)
def popitem(l):    
    x=l.pop()
    print('pop item is:>',x)
l=[]
while True:
    choice=int(input('1-> push\n2->pop\n3->display\n4->exit\nenter your choise->'))
    if choice==1:
        val=int(input('enter number to insert:-'))
        push(l,val)
        print(l)
    elif choice==2:
        if len(l)==0:
            print('stack is empty')
        else:
            popitem(l)       
    elif choice==3:
        print(l)   
    else:
        break    


# data strcuture devide
# built in data types-list,tuple,set,dict
# user-defined data structure-array,satck,queue,tree,