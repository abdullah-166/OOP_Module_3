#key value pair 
#dictonary
#onject
#overlap with set
#object
#structure = {key:vaue}
numbers = [12,56,98,78,56,12,26,98]
person = {'name':'abdullah', 'address':'uttara', 'age': '23', 'profession':'student'}

# print(person) #all the items
print(person['profession'])
print(person.keys())
print(person.values())
person['language'] = 'python'
print(person)
person['name'] = 'Arif' #same thing can be updated
# del person['age']
print(person)

#using loop
#special dictonary looping
for key, value in person.items():
    print(key, value)




