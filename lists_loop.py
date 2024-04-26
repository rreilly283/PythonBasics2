#Looping

magicians =['elice', 'david', 'carolina']

for magician in magicians:
    print(magician)
    print("*** this is repeatable line***")
print("*** this is not repeatable line***")

nums = [3, 5, 1, 8]
#print list os square of these numbers
squares = [] #mutable: can be changed
coordinates = (10, 30) #tuple: immutable: you can not change it

for num in nums:
    print("calculating the square of:", num)
    #print(i**2)
    squares.append(num**2)
print(num) #out of scope, i variable does not exist here
print("Input list: ", nums)
print("Generated list: ", squares)
    #print(i)

cars =['tesla', 'merc', 'toyota', 'rols']
for car in cars:
    print(f"I love my {car}!")
print("end of the dream***")

print("*** Exercise 4-1**** not pizza but kebab ******")
kebabs = ['chicken', 'shish', 'adana', 'lamb']

for kebab in kebabs:
    print(f"I like {kebab} kebab, :p")
print("I love having kebabs for lunch from Greece restaurant.")

