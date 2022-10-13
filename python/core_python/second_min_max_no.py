list1 = [10, 20, 20, 4, 45, 55, 45, 99, 99]
 
# Removing duplicates from the list
list2 = list(set(list1))
 
# Sorting the  list
list2.sort()
 
# Printing the second last element
print("Second largest element is:", list2[-2])

print("########################################################")

list2 = [10, 20, 4, 45, 99]
 
# new_list is a set of list1
new_list = set(list2)
 
# Removing the largest element from temp list
new_list.remove(max(new_list))
 
# Elements in original list are not changed
# print(list1)
print(max(new_list))




list12=[12, 45, 2, 41, 31, 10, 8, 6, 4]

def find_len(list12):
    length = len(list12)
    list12.sort()
   
    print("Second Smallest element is:", list12[1])
 
# Driver Code
Largest = find_len(list12)

########################### OR ################################

list2 = [10, 20, 4, 45, 99]
 
# new_list is a set of list1
new_list = set(list2)
 
# Removing the largest element from temp list
new_list.remove(min(new_list))
 
# Elements in original list are not changed
# print(list1)
print(min(new_list))