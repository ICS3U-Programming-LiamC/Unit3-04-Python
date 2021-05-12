#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 11, 2021
# This program determines whether the number the user inputed was
# positive, negative, or 0


# this is the fucntion that does everything
def what_is_the_num():
    # get the users number
    user_num = input("\nPick a number, positive, negative or otherwise: ")

    # got this from a website while I was trying to
    # figure out how to make it so that if an error
    # arose I could just print it to the user like so
    # https://docs.python.org/3/tutorial/errors.html
    try:
        user_num = int(user_num)

    except ValueError:
        # If an error arrises this gets printed to the user
        print("Your number is not a number")

    else:

        # if num is greater than 0
        if (int(user_num) > 0):
            print("Your number is positive!")

        # if num is less than 0
        elif (int(user_num) < 0):
            print("Your number is negative!")

        # if num is 0
        elif (int(user_num) == 0):
            print("Your number is 0!")
    what_is_the_num()


# initial bootup of the program
if __name__ == "__main__":
    what_is_the_num()
