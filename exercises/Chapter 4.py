#4-5
nums = []  #Preferred way
for num in range(1, 1000001):
    print(num)
    nums.append(num)

#list comprehension
nums = [num for num in range(1, 1000001)]

print("min of one to one million: ", min(nums))
print("max of one to one million: ", max(nums))
print("sum of one to one million: ", sum(nums))

