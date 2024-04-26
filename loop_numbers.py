print("*****range (1,5) *****")
for num in range(1,5): #generate number starting from 1, up to 5, incrementing bby 1
    print(num, end="\t")

print("\n*****range (10) *****")
for num in range(10): #starting from 0 up to 10, incrementing by 1
    print(num, end="\t")

print("\n*****range (5,30,3 ) *****")
for num in range(5,30,3): #starting from 5 up to 30, incrementing by 3
    print(num, end="\t")

print("\n print odd numbers from 10 to 20")
print("odd numbers: ", end ="\t")
for num in range (11, 20, 2):
    print(num, end="\t")

print("\n print squares of even numbers from 10 to 20")
print("even numbers: ", end ="\t")
squares=[]
for num in range (10, 20, 2):
    print(num**2, end="\t")
    squares.append(num**2)
print("\nsquares of even numbers from 10 to 20:", squares)

print("****** Find min and max from the given unsorted list without using min or max functions ********")
nums =[4, -22, 2005, 104, 44]
nums. sort()
print(f"min {nums[0]} and max: {nums[-1]}")

#H/W 4-3 -- 4-8