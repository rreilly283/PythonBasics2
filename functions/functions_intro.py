#Note: each function has a purpose, keep it simple, it has a name, input/output, execution (call the function)
#Name: lower case, should not start with number, use _do seperate the words, give meaningful names(summary) according to purpose of fucntion

#defining the function/method
def greet_user():
    print('Hello User!')
    print("this function just for general greeting")


def greet_user_by_name(username):
    ##Display a simple greeting ## This line is called docstring
    print(f'Hello {username.upper()}!')
    print("we want to greet any user by their name")

def greet_user_by_fullname(firstname, lastname, age):
    ##greets user by name, name should be provided
    print("Pay attention to the order of arugments...")
    print(f'Hello Mr/Mrs/Ms {lastname}, {firstname}!')
    print(f"you are {age} years young.")

def add_numbers(num1, num2):
    print("----This function add and given 2 numbers----")
    print(f"Addition of '{num1}' and '{num2}' is : {num1 + num2}")

print("*****Execution of functions *****")
# calling the method/function(execution)
greet_user()
greet_user()
greet_user_by_name('jane') #jane is the agrument for the function
greet_user_by_name('mehmet')
greet_user_by_name('john')
greet_user_by_name('123')

add_numbers(50,30)
add_numbers(-20, 30)
add_numbers(440, 55.55)

friends = ['mehmet', 'palina', 'stela']
for friend in friends:
    greet_user_by_name(friend)

print("following the right order in passing the argument")
greet_user_by_fullname('john', 'doe', 30)
print("NOT following the right order in passing the argument")
greet_user_by_fullname('doe', 'jane', 25)

#HW 8-1, 8-2
