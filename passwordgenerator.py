# This program will generate a password, write it to a txt file and encrypt the file

# Import modules
import random
import string
import datetime

# Welcome message for user
print("Welcome to Password Generator.")


# Ask user for password
def master_pw():
    master_password = input("Please enter the password: ")
    return master_password


master_password = master_pw()

# Number of chances user have to enter the right password
chances = 3
# The master password to access file
pwd = 'hello'
# Loop to check password
# and tell user how many chances at guessing the pw user have left
if master_password == pwd:
    pass
else:
    while chances > 1:
        print("Wrong password!")
        chances -= 1
        print(f"You have {chances} chance(s) left.")
        new_master_password = input("Please enter the password: ")
        if new_master_password == pwd:
            break
    else:
        print("INTRUDER ALERT! CLOSE PROGRAM!")
        exit()

# Variable to store username
username = input("How should I call you? ")
# Store the category/where the password is going to be used
pwID = input("Where are you going to use this password? ")


# Function to prompt user to enter length of password
def pw_length():
    while True:
        # Error handling
        # Try statement to ensure that user enters length in digits
        # Converts the input to an int
        try:
            password_length = int(input(f"Okay {username.capitalize()}, How many characters do you want in you "
                                        f"password? "
                                        f"\nEnter password length: "))
        # If user enters password length in words e.g. Six or Ten
        except:
            print("Please enter number of characters in digits!")
            password_length = int(input("Enter password length: "))
            print("Generating password with", password_length, "characters...")
            break
        else:
            break
    return password_length


# Store password length in a variable inside function
password_length = pw_length()

# Empty list to store password
passwordList = []
# Message to display password
message = "This is your password: "


# Error message if password_length is more than 32 characters
def error_msg():
    print(f"Please choose a password between 8 and 32 characters!")


# Types of characters for password
# String module used
password_characters = string.hexdigits + "!@$"


# Function to generate the password and write to file
def gen_pw(password_length):
    # For loop to append number of times in password_length
    # i.e. if password_length == 8 append 8 times
    for characters in range(password_length):
        # Add characters randomly from password_characters variable
        passwordList.append(random.choice(password_characters))
    # Converts password from a list to a string
    password = ''.join(passwordList)
    # Print message and password as string
    print(message + "".join(password))
    # Create txt file to store password
    with open('passwords.txt', 'a') as f:
        f.write(f'{pwID.capitalize()}: {password}\n')
        f.write(f'Password generated on {datetime.date.today()}.')
        f.write('\n\n')
        f.close()


# Only print password if password_length is less than 32 characters
if 8 <= password_length <= 32:
    gen_pw(password_length)
    # If password_length is more than 32 do not print password
    # Print error message instead
else:
    # If password is not within range
    # Print error message
    error_msg()
    # Re ask for new password
    new_password_length = int(input("Enter password length: "))
    gen_pw(new_password_length)
