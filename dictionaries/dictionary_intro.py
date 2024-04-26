#Dictionaries, data structures with key-value pair elements
#remember: keys are unique
student1 = {'name': 'john', 'city': 'brooklyn'}
student2 = {}

print("accessing values")
print(student1)
print(student1['name'])
print(student1['city'])

print('update or assign a new value, adding new key-value pair')
student1['city'] = 'manhattan'
print('updated city: ', student1['city'].title())
student1['country'] = 'USA'
print(student1)
student1['classes'] = ['sql', 'linux']
print(student1['classes'][0])
print('****Removing the key-value pair from the dictionary*****')
del student1['country']
print(student1)

#age =30
print("---aditional on input")
#age_text = input("enter your age" ) # input returns string data type
# age = int(age_text)
age = int(input ("enter your age: ")) # input retunrs string data type

if age >10:
    if age < 20:
        print("more than 10 but less than 20")
    else:
        print("more than 20")
else:
    print("less or equalt to 10")
