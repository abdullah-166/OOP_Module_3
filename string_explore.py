name = 'sakib'
name2 = 'rakib'
name3 = 'jabel'
print(name2, name, name3)

#"\"escape related 
name4 = 'Abdullah Al Arif\'s book'
print(name4)

#multi line
name5 = """
        IUBAT
        NSU
        AIUB 
"""
print(name5)

#mutable means changeable
#immutable means you can not change it
#string is a sequence of character
for char in name2:
    print(char)

#index finding
print('Index number:',name3[3])
print(name[1:5])
print(name[-3])
print(name[::-1]) #reberser finding

#find particular string using condition
if 'Arif' in name4:
    print('yes')

#upper & loower case
print(name.upper())
print(name.lower())
c =  name.count('a')
print(c)




