#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 31th, 2025

# Dating age range response program


def main():

    # Get user input, no casting yet
    user_age = input("Enter your age: ")
    try:

        # Try casting incase user entered string to prevent error
        user_age = int(user_age)

        # Check the users age, declare if they are too young, too old or within the permitted range
        if user_age >= 20 and user_age <= 40:
            print("You may date our granddaughter")
        elif user_age < 20:
            print("Sorry, you're too young")
        elif user_age > 40:
            print("Sorry, you're too old")
    except:

        # Correct any errors that the user might have entered
        print("Please enter a valid age! You entered ", user_age)
    finally:

        # Thank the user for playing and terminate the program
        print("Thanks for playing")


if __name__ == "__main__":
    main()
