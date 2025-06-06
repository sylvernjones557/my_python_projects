import random
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# List of all numbers from 0 to 9
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of common special characters
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~'
]
print("WELCOME TO MY PASSWORD GENERATOR APP ....")
print("YOU CAN CREATE YOUR PASSWORDS MORE STRONGER THAN YOUR LIFE...")
total = int(input("What is the total number of characters should be in your password ...."))
no_letters = int(input("How many letters do you want in your password  ...."))
no_numbers = int(input("How many numbers do you want in your password..."))
no_characters = int(input("How many characters do you need in your password"))
if total == no_letters + no_numbers + no_characters:
    password = ""
    for i in range(0,no_letters):
        password += alphabets[random.randint(0,len(alphabets)-1)]
    for j in range(0,no_numbers):
        password += digits[random.randint(0,len(digits)-1)]
    for k in range(0,no_characters):
        password += special_characters[random.randint(0, len(special_characters) - 1)]
    print(password)

else:
    print("password length and your customization choices were not same try again...")






