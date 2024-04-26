#Data Structures: List(Array), Dictionary(HashMap), Set, Tuple
#what do I need to know about data structures:
#create
#Access (Read)
#Update
#Delete
#CRUD operations: create, update, read, delete
#Loop: repeatetive actions on the DS (data structure)

#List: [elem1, elem2, ..., elemN]
#indexing starting with 0,1,2 ...
#Indexing with negative numbers: -1(elemN), -2(elemN-1) ...
#Creating a list:
print("****** Creating a list: ********")
numbers=[]
students=["alex", "ali", "ali", "john", "anna", "elvin","ali", "malika"]
fruits =('orange', 'apple')
cities = list(fruits) #creates and converts iterative objects (sets, dictionary, range() , ...)
print(students)
print(cities)

print("****** Accessing the list: ********")
print('Second student in the list:', students[1])
print(f'Second student in the list: "{students[1]}".')
print(f'Last student in the list: "{students[3]}".')
print(f'Last student in the list: "{students[-1]}".')

print("****** Update the list element values: ********")
#Alex to Alexandr
students[0] ='alexandr'
print(f"whole list: {students}")
print(f"first students name: {students[0]}")

print("****** Update: Modifying the list: ********")
print("****** Adding a value to the end of the list (mostly done) ********")
students.append("stela")
print(f"whole list: {students}")
print(f"updated list, added 'stela' to the list: {students}")

print("****** Adding a value to any position (index) of the list  ********")
students.insert(1, 'mansur')
print(f"updated list, added 'mansur' to the list: {students}")

print("****** Deleting the list: ********")
print("----deleting the element with del function------")
del students[4]
print(f"updated list, removed student5 from the list: {students}")

print("----deleting the element with pop() function------")
students.pop() #deletes the last element by default, when no arguments passed
print(f"updated list, pop() default: {students}")

students.pop(3) #deletes the last element at index3 ('anna')

print(f"updated list, removed student3 from the list: {students}")

print("----deleting the element with remove()------")
students.remove('ali') #removes only first occurence of the value
print(f"updated list, deleted by value 'ali' from the list: {students}")
#students.remove('jane') #removes only first occurence of the value
#print(f"updated list, deleted by value 'jane' from the list: {students}")

###HW #3-1, 3-2, 3-3, 3-4, 3-5, 3-6
print(f"Hi {students[0].title()}, Welcome to Level Up Academy!")

