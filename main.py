# Import the random library
import random

# Initialize the counts and lists to required values
j = 0
passwords = []
keys = ['@', "1", "23", "456",  "$", "#", "7890", "X"]
index = 0
key_count = 6


# A "Blank" line function
def blank():
    print("")


# Prompt keys from the user
for h in range(6):
    key = input(f"Please enter keys that are easy to remember, {key_count} remaining: ")

    # Inset the key into the keys_list
    keys.insert(index, key)
    index += 1

    # Count how many keys left
    key_count -= 1

# Blank line
blank()

# GPassword generation
while j < 5:

    # Initialize the password to a blank string
    password = ""

    # loop over 3 keys from the keys list
    for i in range(3):

        # Generate the password from the three randomly picked keys
        password += random.choice(keys)

        # Check whether the password has been generated before or not to avoid repetition
        if password in passwords is True:
            print('password has been used')

    # Password length validation
    while len(password) < 8:
        password += random.choice(keys)

    else:
        while len(password) > 12:
            password = password[0:13]
        # add the generated password to the passwords list
        passwords.append(password)

    # Increment the generated_password count
    j += 1

# Prompt the user to pick from the generated passwords
print("Please pick a password from the following suggestions:")

# Blank line
blank()

# Initialise the number to 0
n = 0

password_file = open("passwords.txt", "w")

# Loop over the generated passwords and display them to the user
for k in passwords:
    n += 1
    password_file.write(f'{n}. {k}\n')

    print(f'{n}. {k}')

password_file.close()
