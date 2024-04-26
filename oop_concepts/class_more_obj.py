from oop_concepts.classes_more import *

my_car= Car('Huracan', 'Orange', 'Lamborghini') #init method is called
##my_car.odometer =20
#print("odometer value: ", my_car.odometer) #directly updating the variable
my_car.drive(15)
my_car.car_description()

#to prevent incorrect or accidental modification you can hide some data/variables/methods from the object, but hidden data is still available in the class -Encapsulation


#H-W 9-4,  9-5

#Inheritance, Polymorphism()
print("***Inheritance Polymorphism (method overriding")
car2=ElectricCar('model X', 'red', 'tesla', 100)
car2.accelerate()
car2.drive(20)
car2.car_description()
car2.fill_the_gas()


