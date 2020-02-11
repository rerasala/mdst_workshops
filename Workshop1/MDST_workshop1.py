"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """

    #num = input("Enter a number\n");

    if int(num) % 2 == 0:
        print("even")
    else:
        print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    integer = random.randint(1,10)

    input_num = input("Guess: ")

    while input_num != "exit":
        
        if int(input_num) > integer:
            print("too high\n")
        elif int(input_num)  < integer:
            print("too low\n")
        elif int(input_num) == integer:
            print("you got it!\n")
            integer = random.randint(1,10)
                
        input_num = input("Guess: ")
    


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """

    #input_str = input("input a string\n")
    input_str2 = string[::-1]


    if string == input_str2:
        print("True")
    else:
        print("False")

    


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    
    user64 = username.encode("utf-8")
    pw64 = password.encode("utf-8")

    user_bytes = base64.b64encode(user64)
    pass_bytes = base64.b64encode(pw64)

    user_str = str(user_bytes, "utf-8")
    pw_str = str(pass_bytes, "utf-8")

    print(user_str)
    print(pw_str)
    

    f = open(filename,"w")
    f.write(user_str)
    f.write('\n')
    f.write(pw_str)
    f.close()
    

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """

    f = open(filename,"r")

    with open(filename, 'r') as file:
        data = file.readlines()


    if password != None:
        data[1] = password


    base64_message = data[0]
    base64_message = base64_message + "==="
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    user = message_bytes.decode('ascii')
    print(user)

    base64_message = data[1]
    base64_message = base64_message + "==="
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    pw = message_bytes.decode('ascii')
    print(pw)

    with open(filename, 'w') as file:
        file.write(user)
        file.write('\n')
        file.write(pw)


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
