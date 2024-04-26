cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car =='bmw':
        print("This is the real beast:", car.upper())
    else:
        print(car.title())

#car == 'bmw' -> checking the value, expression returns true or false
#car = 'bmw' #assigning the value to car variable

#Expression
#True, False
# 2 <3 (True)
#num <5, num >= 10
#'tesla' in cars

nums=[3,6,1,10,6]
#print "I got the number" whenever you find the number 6 in the list
# if you don't find number 6 then just print 'next'
for num in nums:
    if num==6:
        print('I got the number:', num)
    else:
        print('next')

