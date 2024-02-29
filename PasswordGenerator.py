#Password generator - Wilder Edwards
#This script simulates an 'app' that measures the strength of user passwords, as well as improving user inputted passwords or generating strong passwords upon user request. 
#Currently working on export to GUI interface with react.js


#The random library is what is used in this program, though I found it important to mention the "re" library, as it allows for more complex functionalities that built-in python string methods cannot accomplish, though i found them ultimately unecessary for this code.
import re
import random

password = True


#this function checks the strength of the user inputted password by using built-in python string methods (islower(), is upper(), isdigit() to check for digits, uppercase letters, #lowercase letters, and special symbols, while also considering the length of the password.

def check_strength(password):
  strength=0
#creating string database to call while checking for special symbols in password
  special="!/#%^&*)@('_:;][|\~`"
#Checking for weaknesses and strengths typically found in passwords.
  if password == ("password","Password","PASSWORD"):
    strength -=1
  if 1<= len(password)<= 7:
    strength -= 1
  if len(password)>= 7:
    strength += 1
  if any(char.isdigit() for char in password):
    strength += 1
    if len([char for char in password if char.isdigit()])>=2:
      strength += 1
  if any(char.isupper() for char in password):
    strength += 1
  if any(char.islower() for char in password):
    strength += 1
  if any(char in special for char in password):
    strength += 1
#This variable will determine whether the user is told if their password is weak or not.
  return strength
    
def generate_password(password,attempts):
  letters = [chr(i) for i in range(65,123)]
  special="!/#%^&*)@('_:;][|\~`"
    # Replace specific characters with symbols and numbers from the user inputted password
  new_password = password.replace('i', '1')
  new_password = new_password.replace('a', '@')
  new_password = new_password.replace('m', 'M')
  new_password = new_password.replace('B', '8')
  new_password = new_password.replace('s', '$')
  #Adding random numbers, letters, and symbols to password
  new_password = new_password + str(random.randint(1,9))
  new_password = new_password + random.choice(letters)
  new_password = new_password + random.choice(special)
  #recursive function that repeats these arguments up to 4 times to make password longer and more complex
  if attempts >=4: 
    return new_password
  else:
    return generate_password(password, attempts = attempts + 1)

#function used to create a completely new and random password based on user input
def generate_random_password(attempts):
  #Letters and symbols used to create a complex password are added to the random generator
  letters= [chr(i) for i in range (65,123)]
  special="!/#%^&*)@'_~`"
  #assigns variable new_password as a string
  new_password=""
  for i in range(random.randint(7,12)):
    #this function uses the random library to make a completely random arrangement of the previously assigned letters and symbols, as well as numbers 0-9.
    new_password += random.choice(str(letters)+str(special)+"0123456789")
  if attempts >= 6:
    return new_password.replace(" ","")
  else:
    return generate_random_password(attempts=attempts+1)



#The main function, calls the previously arranged functions, requests multiple user inputs; asks the user if they want to create a new random password or if they want to improve one they already use
def main():
    strength = 0
    print("Welcome to password generator!")
    print()
    print("This program will check the strength of your password, and produce a new one depending on that strength!")
    print()
    print("Would you like to improve a password, or have a entirely new one made?")
    print()
    user_input0 = input("Type 'U' to enter your own password, or type 'N' to create a new one: ")
    print()
    if user_input0 == "U":
        password = input("Enter a password you'd like to use: ")
        strength = check_strength(password)
        if strength < 3:
            print("Password is weak. Would you like a new password to be created?")
            user_input1 = input("Y or N: ")
            if user_input1 == "Y":
                new_password = generate_password(password, attempts=0)
                print("Your new password is: " + new_password)
            else:
                print("Program is complete.")
        else:
            print("Nice password. You don't need a new one... unless you want it to be even stronger? Y or N: ")
            user_input2 = input()
            print()
            if user_input2 == "Y":
                new_password = generate_password(password, attempts=0)
                print("Your new password is: " + new_password)
            elif user_input2 == "N":
                print("Program is complete.")
    elif user_input0 == "N":
        print("Would you like a completely random password to be created or would you like to be involved?")
        user_input1 = input("Type 'R' for a random password or 'C' to choose your own characters: ")
        print()
        if user_input1 == "R":
            new_password = generate_random_password(attempts=0)
            print("Your new password is: " + new_password)
        elif user_input1 == "C":
            password = input("Please enter the characters you'd like in your password: ")
            new_password = generate_password(password, attempts=0)
            print("Your new password is: " + new_password)
    else:
        print("Invalid input. Program is complete.")

main()
