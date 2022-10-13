#dictionary from two lists i.e. key_list and value_list
key_list = [1,2,3,4]
value_list = ['python','java','c#','c']
new_dict = dict([k,v] for k in key_list for v in value_list if key_list.index(k)==value_list.index(v))
print(new_dict)



set3={i if i%2==0 else i*1000 for i in range(10)}
print(set3)


lst=[i if i%3==0 else i*2000 for i in range(10)]
print(lst)

list=[1,2,3,'a','b','c',33,33.4]
lst2=[i for i in list if type(i)==str]
print(lst2)

dict={i:i for i in range(10)}
print(dict)

dict2={n:n*2 for n in range(10)}
print(dict2)

dict3={n:n*2 for n in range(11) if n%2==0}
print(dict3)