
l=[1,2,3,'myshow',2,33,3,44,4]
print(l)
print(type(l))

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
print(l[6])
print(l[7])
print(l[8])

l[0]=1000
print(1)

print('################### without index ##########################')
#without index
l=[1,2,3,'myshow',2,33,3,44,4]
for i in l:
    print(i)

print('################### with index ##########################')


#with index
for i in range(len(l)):
    print('index->',i,'element',l[i])

    print("#with while loop")

l1=[1,2,3,'myshow',2,33,3,44,4]
i1=0
while i1<len(l1):
    print(l1[i1])
    #i=i+2
    i1=i1+4
print("#####################################################")
l=[1,2,3,33,3,44,4]
print(len(l))

print("####################### count ##############################")
print(l.count(4))

print("####################### index ##############################")
print(l.index(4))

print("######################## append #############################")
print(l)
print(l.append(5555555555555))
print(l)

print("########################## insert ###########################")
l=[1,2,3,43,5,6,7]
print(l.insert(5,1000))
print(l)

print("######################## extend #############################")
l1=[11,22,33,43,53,63,73]
print(l.extend(l1))
print(l)


print("######################### remove ############################")
l=[10,20,30,40,50,60,70]
print(l.remove(10))
print(l)

print("######################### pop ############################")

print(l.pop())
print(l)
l=[]

print("######################## reverse #############################")
l=[10,20,30,40,50,60,70]
print(l.reverse())
print(l)

print('################### sort ##########################')

print(l.sort(reverse=False))
print(l)



print("######################## nasted list ################")

l=[1,2,3,4,[1,2,3,4]]

for i in range(len(l)):
    if type(l[i])==list:
        for j in range(len(l[i])):
            print('outer_index->',i,'inner_index->',j,'element->',l[i][j])
        else:
            print('index->',i,'element->',l[i])

            print=("****************************************************")
            
l1=[[1,2,3,4],[1,2,3,4]]

for i in range(len(l1)):
    if type(l1[i])==list:
        for j in range(len(l1[i])):
            print('outer_index->',i,'inner_index->',j,'element->',l1[i][j])
        else:
            print('index->',i,'element->',l1[i])






