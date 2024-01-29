number=34
converted_to_string=str(number)
print(f"Number {converted_to_string} is now a string.")
print(type(converted_to_string))

float_number=4.5
converted_to_int=int(float_number)
print(f"Float {float_number} is now converted to integer {converted_to_int}.")
print(type(converted_to_int))

x=15
print(x==15) #"=" give numbers，“==” check if equals.
print(x<5)
print(x>20)
print(x!=5) #!= means not equial to

x,y= 20,15
print(x>15 and y<20)
print(x>15 and y>20)
print(x>15 or y>20)
print(not x== 10)

fruits=["apple", "pear", "banana"]
print("mango" in fruits)
print("peach" not in fruits)

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)    # True
print(a is c)    # False！！！
print(a is not c)  # True


#if condition1:
    # code to execute if condition1 is True
#elif condition2:
    # code to execute if condition1 is False but condition2 is True
#else:
    # code to execute if both condition1 and condition2 are False

import random
random_integer=random.randint(1,6)
print(random_integer)
if random_integer > 5:
    print("random number is greater than 5.")
elif random_integer >4:
        print("random number is greater than 4.")
else:
    print("random number is 4 or less.")

score=random.randint(30,100)
print(score)
if score >= 70:
    grade="Distinction"
elif score >= 60:
    grade="Merit"
elif score >= 50:
    grade="Pass"
else:
    grade="Fail"
print(f"Your grade is {grade}.")

#while loops
#code to execute repeatedly

number = random.randint(0,5)
while number<5:
    print("Number is:", number)
    number += 1 #number = number + 1

count=0
while True:
    print(count)
    count += 1
    if count >= 4:
        break
print("Loop ended!")

count=0
while count<=5:
    print(count)
    count += 1
print("Loop ended!!!")

#continue:
#If we want to print a list of numbers except those are multiples of 5:
numbers=[5,6,7,8,9,10,11,12,13,14,15]
index=0
while index<len(numbers):
    if numbers[index] % 5 ==0: #care about the "=="!!
        index += 1 
        continue
    print(numbers[index])
    index += 1

#for loops:
idols = ["Winter", "Yoona", "Nayeon"]
for idol in idols:
    print(idol)  # This line is part of the for loop
    print("She is beautiful!")  # This line is also part of the for loop

