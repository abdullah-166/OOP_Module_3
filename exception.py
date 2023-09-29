try:
    # result = 45/0 [this statement is wrong so it will print except]
    result = 45/5
except:
    print('error happen')
finally:
    print('finally here')
print('yes')