
# generator to print even numbers
def print_even(test_list):
	for i in test_list:
		if i % 2 == 0:
			yield i

# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
	print(j, end=" ")





# initializing list
numbers = [1, 2, 3, 4, 5]

# converting the list to iterator
iterator_list = iter(numbers)

# setting default value as -1
default = -1

next_element_1 = next(iterator_list, default)
print(next_element_1)

next_element_2 = next(iterator_list, default)
print(next_element_2)

next_element_3 = next(iterator_list, default)
print(next_element_3)

next_element_4 = next(iterator_list, default)
print(next_element_4)

next_element_5 = next(iterator_list, default)
print(next_element_5)

next_element_default = next(iterator_list, default)
print(next_element_default)

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

l = [1, 2, 3]
l.extend([4, 5, 6])
print(l)

lis = ['POOJA', 'POORVA']
lis.insert(1, "For")
print(lis)



