cars = ['ferrari', 'maybach', 'lambo', 'tesla', 'audi']
nums = [4,6,2,11,2,3,-55]

print("**** permanent sorting *****")
copy_cars = cars.sort()
print("copy cars: ", copy_cars) #doesn't generate the value
cars.sort() #sorting the original list in asc order
nums.sort() #sorting the original list in asc order
print("Permanent sorted cars:", cars)
print("Permanent sorted cars:", nums)

cars1 = ['ferrari', 'maybach', 'lambo', 'tesla', 'audi']
nums1 = [14,16,12,111,12,13,-155]

cars1.sort(reverse=True) #sorting the original list in desc order
nums1.sort(reverse=True) #sorting the original list in desc order
print("Permanent sorted cars:", cars1)
print("Permanent sorted cars:", nums1)

print("**** temporary sorting *****")
cars2 =['ferrari2', 'maybach2', 'lambo2', 'tesla2', 'audi2']
print("sorted copy", sorted(cars2))
sorted_cars2 =sorted(cars2) #returns the new copy of the list
print("original car2:", cars2)
print("sorted copy of cars2, asc", sorted_cars2)

sorted_cars3 =sorted(cars2, reverse=True) #returns the new copy of the list
print("original car2:", cars2)
print("sorted copy of cars2, asc", sorted_cars2)
print("sorted copy of cars2, desc", sorted_cars3)

print("number of element in the list:", len(cars1))
print("number of element in the list:", len(cars2))
print("number of element in the list:", len(nums))

print("permanently reversing the list without sorting")
print("original: ", cars2)
cars2.reverse()
print("reversed cars2, this is not sorted", cars2)

print(sorted_cars2)

#all lists and variabloes die here, ie. removed from the memory after excecution complete