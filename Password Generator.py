import random
import string
import itertools

#asking a user for length of password
def password_length():
    while True: 
        length = input("How many characters should the password be: (Very strong/Strong/Weak/Custom)").strip().lower()
        if length == "very strong":
            return 12
        elif length == "strong":
            return 9
        elif length == "weak":
          return 6
        elif length == "custom":
            while True:
                try:
                    custom_length = int(input("How many characters would you like: "))
                    if custom_length > 0: 
                        return custom_length 
                    else: 
                        print("Password must have positive number of characters")
                except ValueError:
                    print("Must be an integar")                




length = password_length() 

def char_type(length):
    letter = random.choice(string.ascii_letters)
    number = random.choice(string.digits)
    punctuation = random.choice(string.punctuation)
    while True: 
        char_type = input("would you like special characters (Yes/No)").strip().lower()       
        if char_type == "yes":
            return list(letter) + list(number) + list(punctuation) + random.choices(string.ascii_letters + string.digits + string.punctuation, k=(length-3))
        elif char_type == "no":
            return list(letter) + list(number) + random.choices(string.ascii_letters + string.digits, k=(length-2))
        else:
            print("Answer must be Yes or No")
            



passwordlist = char_type(length)
# print("before ", passwordlist) - testing before and after of shuffle
random.shuffle(passwordlist)
# print("After", passwordlist) - testing before and after of shuffle

# print("passwordlist is", passwordlist)# - testing half way through


stringpassword = []

for element in passwordlist:
    stringpassword.append(str(element))


# print("stringpassword is ", stringpassword) - testing half way through

password = "".join(stringpassword)

print("Your password is ", password)


