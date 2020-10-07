"""
Author: Elijah Morishita
elmorishi  ta@dmacc.edu
10/5/2020
This program gathers numeric input from a user, and places it into a list as a string
"""
def get_input():
    """
    This function gathers numeric user input and converts it to a string, then returns it
    :return: user_input
    """

    end_loop = True  # Used to stop the loop for user input
    while end_loop:
        try:
            user_input = str(float(input("Please enter a number: ")))
            end_loop = False  # The loop breaks once the user has entered valid input
        except:
            print("Invalid input, please try again.")
    
    return user_input


def make_list():
    """
    This function places the return of get_input() into a list, then returns the list
    :return: user_input
    """
    user_input = [0, 0, 0]  # initialized a list

    for x in range(0, 3):
        user_input[x] = get_input()

    return user_input


if __name__ == '__main__':
    print(make_list())
