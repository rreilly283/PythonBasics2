class Car:
    #""" A simple attempt to model a car"""
    #odometer =0 A# option 1 create optional variables
    #odometer=0
    def __init__(self, model, color, made):
        #Constructor method for car class
        self.model = model
        self.color = color
        self.made = made
        #option 2: create otpion variables
        self.__odometer=10

    def drive(self, miles):
        if miles > 0:
            print(f"Car is driving...")
            self.__odometer +=miles
        else:
            print(f"Error: incorrect input. Don't cheat")
        print(f"my odometer is showing: {self.__odometer}")

    def car_description(self):
        print(f"description of the car: {self.model} made by {self.made}")
        print("gas is full. Ignite and Drive!")

    def fill_the_gas(self):
        print(f"{self.model.title()}: filling the gas tank...")
        print("gas is full. Ignite the engine and Drive!")
class ElectricCar():
    pass
# modeling the Electric Car and using all what regular car has

    #Parent does not have access to child data and fuctions
    #if we have something different in a child class constructior, weneed to redefine the constructor in child class
    #we want to add a battery_size instance variable
    def __init__(self, model, color, made, battery_size)
        super().__init__(model, color, made) #calling the constructor of parent class
        self.battery_size = battery_size
    def accelerate(self):
        print('reaching 100 miles in 1..2...3 seconds')
