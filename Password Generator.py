import random
import string
import itertools

#asking a user for length of password
def password_length():
    while True: 
        try: 
          length = int(input("How many characters should the password be: "))
          if length > 0: 
              return length 
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
        char_type = input("would you like special characters (Yes/No)")        
        if char_type == "Yes":
            return list(letter) + list(number) + list(punctuation) + random.choices(string.ascii_letters + string.digits + string.punctuation, k=(length-3))
        elif char_type == "No":
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


