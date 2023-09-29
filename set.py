# set: collection of items
# list --> []
# tuple --> ()
# set -- {}
numbers = [12,14,16,12,78,45,14,89]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)

#add new 
numbers_set.add(23)
print(numbers_set)

#remove any item
numbers_set.remove(12)
print(numbers_set)

#using loop
for item in numbers_set:
    print(item)

#using condition
if 89 in numbers_set:
    print('yes')

#set declare
#unique item no duplicte value
a = {1,3,5,7}
b = {1,2,3,4,5,7}
c = {1,2,3,4,5,6,7,8}
print(a & b & c) #it will provide the most common value
print(a | b | c) #it will provide all the value

