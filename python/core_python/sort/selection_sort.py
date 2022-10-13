list1=[1,22,3,4]
z=sorted(list1)
print(z)

#selection sort
#selction sort
s=[56,3,2,78,6,2,0]
print(s)
for i in range(len(s)):
    min_val=min(s[i:])
    min_ind=s.index(min_val)
    s[i],s[min_ind]=s[min_ind],s[i]
print(s)