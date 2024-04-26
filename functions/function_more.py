def greet_user_by_fullname(firstname, lastname, age, middlename='', country='usa'):
    #greets user by name, name should be provided
    print("Pay attention to order of arguments...")
    print(f'Hello Mr/Mrs/Ms {lastname.title()}, {firstname.title()}!')
    print(f"you are {age} years young.")

greet_user_by_fullname('john', 'doe', 25) #motly used, positional
greet_user_by_fullname(lastname='doe', age='26', firstname='jane') #keyword arguments, position does not matter
greet_user_by_fullname('john', 'doe', 25, 'brown''')
greet_user_by_fullname('jackie', 'chan', 60, "lee", 'china')
#Note: if arguments (values) provided/passed to optional parameters then default values is used

print('testing print function-------')
print('hello', 'world', 'this is Sparta!', 2344, sep=' | ', end='\n\n\t')
filepath= '/Users/salimam0712/dev/pythonBasics2/data/print_file.sample.csv'
with open(filepath, 'w') as report:
    print('companyName', 'city', 'Country', 'Phone', sep=',', file=report)
    print('level up academy', 'brooklyn', 'usa', 3434375737, sep=',', file=report)
    print("-----")