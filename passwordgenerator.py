# This program will generate a password, write it to a txt file and encrypt the file

# Import modules
import random
import string
from datetime import date
import sqlite3

def read_database(account:str):
    """
    Returns the password for the given account from the database.
    """
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords(account text, password text, date text)")
    c.execute("SELECT * FROM passwords WHERE account=:account", {"account":account})
    result = c.fetchall()
    conn.close()

    if len(result) == 0:
        return f"Found no password for {account} in the database."

    data = f"Account: {result[0][0]} \nPassword: {result[0][1]} \nDate created: {result[0][2]}"
    return data

# Welcome message for user
print("Welcome to Password Generator.")

# asking the user for the task
task = int(input("What to do?\n 1. Read password \n 2. Generate password \n"))
if task == 1:
    account = input("Which account's password do you want to know? ")
    print(read_database(account))
    quit()

# Variable to store username
username = input("How should I call you? ")
# Store the category/where the password is going to be used
pwID = input("Where are you going to use this password? ")


def add_to_database(account:str, password:str):
    """
    Stores passwords into the database.
    """
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords(account text, password text, date text)")
    c.execute("INSERT INTO passwords VALUES(:account, :password, :date)", {"account":account, "password":password, "date":date.today()})
    conn.commit()
    conn.close()
    print(f"Password for {account} added successfully into the database.")


# Function to prompt user to enter length of password
def pwlength():
    while True:
        # Error handling
        # Try statement to ensure that user enters length in digits
        # Converts the input to an int
        try:
            password_length = int(input(f"Okay {username.capitalize()}, How many characters do you want in you "
                                        f"password? "
                                        f"\nEnter password length: "))
        # If user enter password length in words e.g. Six or Ten
        except:
            print("Please enter number of characters in digits!")
            password_length = int(input("Enter password length: "))
            print("Generating password with", password_length, "characters...")
            break
        else:
            break
    return password_length


# Store password length in a variable inside function
password_length = pwlength()

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
def genpw(password_length):
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
    # Adding the password to the database
    add_to_database(pwID, password)


# Only print password if password_length is less than 32 characters
if 8 <= password_length <= 32:
    genpw(password_length)
    # If password_length is more than 32 do not print password
    # Print error message instead
else:
    # If password is not within range
    # Print error message
    error_msg()
    # Re ask for new password
    new_password_length = int(input("Enter password length: "))
    genpw(new_password_length)
