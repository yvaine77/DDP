word="winter"
letter=word[4]
print(letter)

word="simultaneously"
sub_word=word[5:11]
print(sub_word)

text= "I love Python"
upper_text= text.upper()
print(upper_text)
lower_text= text.lower()
print(lower_text)


# String with leading and trailing whitespace
whitespace_string = " I love Python! "
# Removing whitespace
stripped_string = whitespace_string.strip()
print(stripped_string) 

sentence="Winter is my favorite kpop idol."
#finding a substring
index=sentence.find("favorite")
print(index)
#replace a substring
new_sentence=sentence.replace("my","her")
print(new_sentence)

data="apple,peach,orange"
fruits=data.split(",")
print(fruits)
sentence=" ".join(fruits)
print(sentence)

#formatting strings
name="Alice"
age=25
message= f"Hello, {name}. You are {age} years old." 
print(message)

#escape characters
text="hello\nworld"
print(text)
text="hello\tworld"
print(text)
text="hello world\n"
print(text)

path = "C:\\Users\\Username"
print(path)
# Output: C:\Users\Username
raw_path=r"C:\Users\Username"
print(raw_path)

quote="She said, \"You jump I jump!\""
print(quote)

round_number=round(3.1415926)
print(round_number)
round_number=round(5.253412,3)
print(round_number)
integer_number=int(7.8)
print(integer_number)

import math
square_root=math.sqrt(16)
print(square_root)

soft_drink=["bubble tea","tea","coffee"]
print(soft_drink[0])
print(soft_drink[-1])

# Generate a random integer within a specified range.
import random
random_integer = random.randint(1, 10)  # Random integer between 1 and 10
print(random_integer)

#input function
user_name= input("Enter your name:")
print("Hello,", user_name)

age=input("Enter your age:")
age=int(age)
print("Your are", age, "years old." )

first_name= input("Enter your first name:")
last_name= input("Enter your last name:")
print("Your full name is:", first_name, last_name)

