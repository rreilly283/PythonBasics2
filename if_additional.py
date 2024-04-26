#if expression1:
 #   code to execute when expreassion1 returns True
#elif expression2:
#    code to execute in case expression1 returns False and expression2 returns True
#elif ..
 #   ...
#else:
 #   code to execute when all above expressions return false

 #NESTED FOR LOOP: loop inside the loop
meals = ['hamburger', 'kebab', 'pizza', 'plov']
drinks =['water', 'milk', 'coffee', 'tea']

for meal in meals:
    for drink in drinks:
        print(f"Customer's order: {meal} and {drink}. ")
print("==================")


print("******Multiplication************")
for i in range (1,11):
    print() #adds newline, hits enter with every 'i'
    for j in range(1,11):
        # "5*3=15"
        print(f"{i} * {j} = {i * j}", end="\t\t")
print("\n*******")

age=30
if age >10:
    if age <20:
        print("more than 10 but less than 20")
    else:
        print("more than 20")
else:
    print("less or equal to 10")

print("$$$$Welcome to the Pizza Restaurant!$$$$")
#for i in range(3): if you want to repeat this below process 3 times
wish_to continue = 'yes': # we will start with default value to begin While loop
while wish_to_continue.lower() =='yes':
    print("$$$$Welcome to the Pizza Restaurant!$$$$")
    print('You have a choice of 3 toppings')
    topping1 = input('Please enter your first choice of pizza topping: ')
    topping2 = input('Please enter your second choice of pizza topping: ')
    topping3 = input('Please enter your third choice of pizza topping: ')
    print(f"you have entered: '{topping1}'")
    print(f"you have entered: '{topping2}'")
    print(f"you have entered: '{topping3}'")
    print("-----we started making your pizza------")
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = [topping1, topping2, topping3]

    for requested_toppings in requested_toppings:
        if requested_toppings in available_toppings: #scans the available_toppings list for requested_topping
            print("Adding " + requested_toppings + ".")
        else:
            print("Sorry, we don't have " + requested_toppings + ".")
    print("\nFinished making your pizza!")
    wish_to_continue = input('Do you wish to continue? enter yes/no: ')
print("**** we are done for this session, thank you ****")
