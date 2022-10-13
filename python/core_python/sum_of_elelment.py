total = 0
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# and add them in variable total
for element in range(0, len(list1)):
    total = total + list1[element]
 
# printing total value
print("Sum of all elements in given list: ", total)

########################### OR ############################

list1 = [11, 5, 67, 18, 23]
 
# using sum() function
total = sum(list1)
 
# printing total value
print("Sum of all elements in given list: ", total)