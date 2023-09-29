# .csv comma seperated value
# .txt text file

#for write operation
# with open('message.txt', 'w') as file:
#     file.write('I Love You, Python')

#for append operation
# with open('message.txt', 'a') as file:
#     file.write('I Love You, Python')

#for read operation
with open('message.txt', 'r') as file:
    text = file.read()
    print(text)