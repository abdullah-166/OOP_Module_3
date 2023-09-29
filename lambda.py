# def doubled(x):
#     return x*2
doubled = lambda num: num*2 #this is another format of function
squared = lambda num: num ** 2 
result = doubled(12)
result1 = squared(12)
# print(result,result1)

add = lambda x, y : x+y
sum = add(12,11)
# print(sum)

numbers = [12,14,16,12,78,45,14,89]
# print(numbers)
doubled_nums = map(doubled,numbers)
squared_nums = map(squared,numbers)
# print(list(doubled_nums))
# print(list(squared_nums))

actors = [
    {'name': 'A','age': 45},
    {'name': 'B','age': 40},
    {'name': 'C','age': 39},
    {'name': 'D','age': 30},
]
juniors = filter(lambda actor : actor['age'] < 40,actors)
fivers = filter(lambda actor : actor['age'] %5 == 0, actors)
# print(list(juniors))
print(list(fivers))

