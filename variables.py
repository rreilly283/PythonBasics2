#comment line
#Variables - storage with reference, so we can use the value with reference
#variables can hold various data types
#variables names and filenames:
#lower case, no spaces (new_message), dont start with number
#SQL< Java: CustomerID, newMessage(java)
msg ='hello python'
message = "wow I am coDiNg" #string data type
num = 123
a = 34
b =88.99 #float
c =1 #integer
status = True #boolean

print(a+b)
print(message)
print(msg, message)
print("python world")

print ("*******Data types*******")
#primitive data type: numbers(integer, double, float), strings, boolean
#data structure: list, dictionary ..

print(type(b)) #print(), type() is the buil-in functions
print(type(c))
print(type(message))
print(type(status))

print("***Built in functions ********")
print(message.upper())
print(message.lower())
print(message.title())

city = "  brooklyn   "
country = 'USA'
print(city, country)
print(city.strip(), country)
print("***** concatenation *********")
print("My location is " + city.strip().title() + ", " + country.upper())
print(f"My location is {city.strip().title()} , {country.upper()}.")

print(" ------- special characters tab, new line (enter")
print("******\n********\t\t*******\n\t*****")

print("**** Reassigning the value for the variable*******")
print("old value: ", msg)
msg='good morning'
print("new value: ", msg)

#print(language)
language = 'python'
print("Favorite language: ", language)

x=45
y=55
print("1. sum of x and y: ", x+y)
x=145
print("2. sum of x and y: ", x+y)

print("******Working with Numbers**********")
num1=5
num2=3
print("result", 5**3) #5*5*5
print("modulo:", num1 % num2)
# when you divide number at 'a", modulo returns a remainder (c) --> remainder 5= 3*1 +2 | x=a*b + c(C<a)
#10 = 3*3 +1
#when you divide number at 'a", floor division returns a 'b' --> remainder 5= 3*1 +2 | x=a*b + c(C<a)
print("Floor division", num1//num2) #remainder (b) 5=3*1 +2 | x =a*b +c (c<a)

#odd numbers: 1, 3, 5
#even numbers: 2,4,6

num3=50
print("if modulo returns 0 then given number is dividable by 2, so it is even number")
print("Remainder:", num3 %2)


print("********* useful functions while working with numbers ********")
print("regular division:", 100/3) #
print("converting division result to integer:", int(100/3))
print("converting division result to integer:", 100)
print("converting division result to a float", float(100))

print("*******useful function while working with mix data types******")
age=25
msg1="I am " + str(age) + " years old." #converting integer to a string with str function
print(msg1)
age=26
msg1= f"I am {age+3} years old." #converting integer to a string with str function
print(msg1)

age=25
msg1="I am " + str(age+2) + " years old." #converting integer to a string with str function
print(msg1)

print(25+30) #55, we are adding numbers
print('25' + '30') #2530, we are just combining text


#int(45.5), str(n), float(a)

for i in range(4):
    num = None
    num_str = input('enter the number: '). strip() #input returns a string data type
    if num_str == '':
        num=-1
    else:
    num =int(num_str) #convert to num

    if num <=0:
        print('invalid entry')
    elif num % 15 ==0: # bug, reprot in JIRA
        print('fizzbuzz')
    if num % 3 ==0:
        print('fizz')
    elif num % 5 ==0:
        print('buzz')
    else:
        print('not dividable')
#is returning error, which I don't understand when I pass 'a' as input
# test data: 3, 5, 15, 17, a, 0, string, any number divdiable by 15, 34.55, ###, '   ' , '\n'



