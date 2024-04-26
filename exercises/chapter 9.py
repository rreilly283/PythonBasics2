class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.cuisine_type = cuisine_type
        self.restaurant_name = restaurant_name

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name.title()}! we are fine {self.cuisine_type} restaurant! ")

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}! We aer now Open!")
        for i in range(5):
            print(f"Welcome to {self.restaurant_name.title()}! We are now Open!")


restaurant1 = Restaurant("Bella Napoli", "italian")
restaurant2 = Restaurant("Uncle Hulio", "mexican")
restaurant3 = Restaurant("Avacado Queen", "european")
restaurant4 = Restaurant("Egg Harbor", "american")

restaurant1.open_restaurant()
restaurant1.describe_restaurant()
print(restaurant1.restaurant_name) #accessing the class attributes
print(restaurant1.cuisine_type)

restaurant2.open_restaurant()
restaurant2.describe_restaurant()
print(restaurant2.restaurant_name) #accessing the class attributes
print(restaurant2.cuisine_type)

restaurant3.open_restaurant()
restaurant3.describe_restaurant()
print(restaurant3.restaurant_name) #accessing the class attributes
print(restaurant3.cuisine_type)

restaurant4.open_restaurant()
restaurant4.describe_restaurant()
print(restaurant4.restaurant_name) #accessing the class attributes
print(restaurant4.cuisine_type)

#h/w 9-3

