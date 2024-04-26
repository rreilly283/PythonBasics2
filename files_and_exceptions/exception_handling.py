print("***Exception handling file started****")
try:
    a= int(input('enter the first number: '))
    b= int(input('enter the second number: '))
    print(a/b)
except ZeroDivisionError as err:
    print("000Ps error happened, Go back to Algebra: ")
    print(err, 'Nothing can be divided by zero')
except ValueError as err:
    print('Enter valid number not a character')
    print(err)
print("***Exception handling file competed****")